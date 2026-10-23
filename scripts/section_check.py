"""Check a scratch section (writer output + orchestrator rewording) against its evidence cards
and its word budget, before it is inserted into a draft (agent pipeline, phases 5-8).

1. Numbers: every number in a cited sentence must appear in a card quote of a tag that sentence
   cites (a sentence with no tag takes the tags of the next cited sentence in its paragraph).
2. Wording: statistic or certainty words (mean, median, significant, adjusted, randomised,
   prevented ...) must appear in a card quote of a cited tag. "mean" slipped in at step 18.
3. Tags: a cited tag with no card in the cards file = writer went outside the evidence.
4. Budget: words (tags removed) above the step budget = ask the user before exceeding it.
   Section 5 part 1 grew from 349 to 557 words at step 18.

Cards file: `Tag | line | quote` lines (verify_quotes.py format). Budget: --budget 300-350, or
a budget.txt next to the cards file holding "300-350". review_hook.py runs this on every edit
of .claude/state/step*/section*.txt. Exit 1 on any finding.

Usage:
    python scripts/section_check.py .claude/state/step19/section.txt .claude/state/step19/cards.txt [--budget 300-350]
    python scripts/section_check.py --demo
"""
import os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cite_check import TAG, sentences, tags  # noqa: E402

NUM = re.compile(r"(?<![\w.])\d{1,3}(?:,\d{3})+(?!\d)|(?<![\w.,])\d+(?:\.\d+)?")  # 100,000 = one number
NOT_DATA = re.compile(r"\b(type|phase|grade|class|step|day)\s+\d+\b|\b(19|20)\d{2}\b|"
                      r"\b(sections?|tables?|figures?|fig\.)\s+\d+(\.\d+)*|"  # 'Section 4.2' = cross-ref
                      r"\b95\s*%\s*(CI|UI|confidence|uncertainty)", re.I)
# word in a sentence -> what must appear in a cited card quote to support it
WORDS = {
    r"\bmean\b": r"\bmean\b", r"\bmedian\b": r"\bmedian\b", r"\baverage\b": r"\baverage|\bmean\b",
    r"\bsignificant(ly)?\b": r"significan|\bp\s*[<=>≤]|\bci\b|confidence interval",
    r"\badjusted\b": r"adjust|\ba(hr|or|irr|rr)\b|multivariable",
    r"\bindependent(ly)?\b": r"independent|adjust|multivariable",
    r"\brandomi[sz]ed\b": r"randomi[sz]|\brcts?\b", r"\bdouble-blind\b": r"double-blind|double blind",
    r"\bplacebo\b": r"placebo", r"\bdose-dependent(ly)?\b": r"dose-dependent|dose dependent",
    r"\bcaus(al|ally|ed|es)\b": r"caus", r"\bprevent(ed|s)?\b": r"prevent",
    r"\brevers(ed|es|al)\b": r"revers",
}  # ponytail: 'all'/'every' dropped, too often plain wording ('all conducted in Egypt or India')


def load_cards(path):
    cards = defaultdict(list)
    for raw in open(path, encoding="utf-8").read().splitlines():
        if raw.strip() and not raw.lstrip().startswith("#") and raw.count("|") >= 2:
            tag, _, quote = (p.strip() for p in raw.split("|", 2))
            cards[tag].append(quote)
    return cards


def words(text):
    return len(TAG.sub("", text).split())


def check(text, cards, budget=None):
    out, nocard = [], set()
    for para in [p for p in re.split(r"\n\s*\n", text) if p.strip() and not p.lstrip().startswith(">")]:
        sents = sentences(" ".join(para.split()))
        for i, s in enumerate(sents):
            cited = next((tags(x) for x in sents[i:] if tags(x)), [])
            if not cited:
                continue
            plain = TAG.sub("", s)
            for t in sorted(set(tags(s)) - set(cards) - nocard):
                nocard.add(t)
                out.append(("tag", f"[{t}] cited but has no card (its numbers and wording unchecked)", plain[:80]))
            cited = [t for t in cited if t in cards]
            if not cited:
                continue
            quotes = " ".join(q for t in cited for q in cards[t]).replace("−", "-")
            # quote numbers may sit inside names: 'DAS28' supports '28-joint'
            have = {n.replace(",", "") for n in re.findall(r"\d{1,3}(?:,\d{3})+(?!\d)|\d+(?:\.\d+)?", quotes)}
            for n in NUM.findall(NOT_DATA.sub("", plain)):
                if n.replace(",", "") not in have:
                    out.append(("number", f"{n} not in cards of {'/'.join(cited)}", plain[:80]))
            low = quotes.lower()
            for w, need in WORDS.items():
                m = re.search(w, plain, re.I)
                if m and not re.search(need, low):
                    out.append(("wording", f"'{m.group(0)}' not in cards of {'/'.join(cited)}", plain[:80]))
    if budget:
        lo, hi = budget
        n = words(text)
        if n > hi:
            out.append(("budget", f"{n} words, budget {lo}-{hi}: cut, or ask the user before exceeding it", "whole text"))
    return out


def parse_budget(s):
    m = re.fullmatch(r"\s*(\d+)\s*[-–]\s*(\d+)\s*", s or "")
    return (int(m.group(1)), int(m.group(2))) if m else None


def demo():
    cards = {"Kitas2019": ["CK and ALT levels were 12% and 15% higher with atorvastatin (P < 0.001)."]}
    ok = "CK and ALT levels were 12–15% higher with atorvastatin, significantly so [Kitas2019]."
    assert check(ok, cards) == [], check(ok, cards)
    bad = ("Mean CK levels were 12–15% higher in all patients with type 2 diabetes [Kitas2019]. "
           "It fell by 9% [Ghost2020].\n\nA tagless lead-in of 40 cases. It rose [Kitas2019].")
    kinds = [(k, w.split(" ")[0]) for k, w, _ in check(bad, cards)]
    for k in [("wording", "'Mean'"), ("tag", "[Ghost2020]"), ("number", "40")]:
        assert k in kinds, (k, kinds)
    assert ("number", "2") not in kinds, kinds  # 'type 2 diabetes' is not data
    assert check("It fell 9% (95% CI 1 to 20) in 100,000 people [A2020]. Again [A2020].",
                 {"A2020": ["fell 9% (CI 1-20) among 100,000"]}) == []
    assert [k for k, *_ in check("x 5 [B2020]. y 6 [B2020].", {})] == ["tag"]  # once; numbers skipped
    assert check("one two three four [Kitas2019]", {"Kitas2019": ["x"]}, (1, 3))[-1][0] == "budget"
    assert parse_budget("300–350") == (300, 350) and parse_budget("") is None
    print("demo ok")


def main(args):
    if args == ["--demo"]:
        return demo()
    budget = None
    if "--budget" in args:
        i = args.index("--budget")
        budget = parse_budget(args[i + 1])
        args = args[:i] + args[i + 2:]
    if len(args) != 2:
        sys.exit(__doc__)
    text_path, cards_path = args
    bfile = os.path.join(os.path.dirname(os.path.abspath(cards_path)), "budget.txt")
    if budget is None and os.path.exists(bfile):
        budget = parse_budget(open(bfile, encoding="utf-8").read())
    text = open(text_path, encoding="utf-8").read()
    found = check(text, load_cards(cards_path), budget)
    print(f"== {text_path}: {words(text)} words" + (f" (budget {budget[0]}-{budget[1]})" if budget else ""))
    for kind, what, where in found:
        print(f"  [{kind}] {what}\n      → {where}")
    print("\n✅ section matches cards" if not found else f"\n⚠️ {len(found)} finding(s): confirm against the paper, or drop")
    return 1 if found else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
