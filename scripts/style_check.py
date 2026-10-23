"""Style check for review drafts: academic register without AI-writing tells.

Usage (from the review folder):
    PYTHONIOENCODING=utf-8 python ../scripts/style_check.py drafts/Day1.md [more files]
    python ../scripts/style_check.py --demo
v1 (2026-10-04) pushed plain words -> spoken English. v2 (2026-10-05) keeps the structural
rules but swaps spoken words for short academic ones. Validated on the ARBs section:
original 12% Grammarly / 3% HumanizeAI; spoken->academic swaps + fewer contrast openers 12% / 3%;
a full-section rewrite scored 34% / 71% -> fix sentence by sentence, never regenerate.
v3 (2026-10-05): file-level profile vs 3 human reviews (PROFILE) replaces the per-paragraph
mean and the per-sentence participle ban.
v4 (2026-10-06): hidden-Unicode watermark check + extra stock phrases + sentence-length CV,
ported from guillaumemeyer/watermarks-remover (text_unicode.py, score_stylometry.py).
Its humanize pass is NOT ported: it turns en dashes into commas ("drug–drug", "Phase I–II").
    python ../scripts/style_check.py --fix drafts/Day1.md   # strip hidden chars in place
"""
import re, sys, unicodedata

MAX_WORDS = 45       # hard cap per sentence (split: design | result)
MAX_CONTRAST = 3     # contrast openers per section
# File-level profile targets from 3 pre-ChatGPT reviews (Salvatore 2020 Pharmaceuticals,
# statins Front Med 2018, Bu 2021 Front Pharmacol; all 0% on HumanizeAI). Mean kept below
# their 24-28 to stay clear of the AI average (~29 words). (label, low, high)
PROFILE = {
    "mean sentence length": (22, 25), "sentence length sd": (10, 99),
    # sd/mean; watermarks-remover scores <0.35 as high-risk AI uniformity. Benchmarks ~0.45,
    # calibrated ARBs 0.39 scored 1% HumanizeAI -> 0.35 floor, not higher.
    "sentence length CV": (0.35, 99),
    "% sentences <12 words": (0, 12), "% sentences >35 words": (5, 18),
    "% opener connectors": (5, 15), "% passive": (20, 99), "% hedged": (12, 99),
    "% ', and this/, so'": (0, 1), "% ', -ing' tails": (0, 5),
}

AI_CLICHES = {  # stock phrases detectors and reviewers associate with AI -> swap
    "cornerstone": "widely used in", "delve": "examine", "pivotal": "main", "crucial": "important",
    "intricate": "complex", "comprehensive": "drop it", "underscore": "show", "underscores": "shows",
    "highlight": "show", "highlights": "shows", "plays an integral role": "regulates",
    "plays a key role": "drives", "plays a crucial role": "drives", "growing evidence": "several studies",
    "growing body of evidence": "several studies", "shed light": "clarify", "pave the way": "allow",
    "holds promise": "may be useful", "promising": "drop it", "landscape": "field", "robust": "clear",
    "meaningful": "drop it", "warrant": "require", "warrants": "requires", "in the context of": "in",
    "a total of": "drop it", "well-known": "established", "well-designed": "adequately designed",
    "which in turn": "split the sentence", "possess": "have",
    # watermarks-remover / academic-research-skills stock-phrase lists (not already above)
    "tapestry": "drop it", "foster": "promote", "fosters": "promotes", "showcase": "show",
    "testament": "drop it", "leverage": "use", "utilize": "use", "utilise": "use", "realm": "field",
    "embark": "begin", "multifaceted": "complex", "synergy": "combined effect", "holistic": "drop it",
    "streamline": "simplify", "cutting-edge": "new", "groundbreaking": "drop it",
    "it is important to note": "drop it", "it is worth mentioning": "drop it",
    "it should be noted": "drop it", "in order to": "to", "due to the fact that": "because",
    "a large number of": "many", "has the ability to": "can", "when it comes to": "for",
    "this section will": "drop the signpost", "the following paragraph": "drop the signpost",
    "it is well known": "cite it instead", "it goes without saying": "drop it", "in today's": "drop it",
}
SPOKEN = {  # conversational words -> short academic swap (keep words short: long words read as AI)
    "cheap": "inexpensive / low-cost", "switches on": "activates", "switch on": "activate",
    "work against": "oppose", "works against": "opposes", "point in the same direction": "are consistent",
    "point to": "indicate", "make each other worse": "are mutually reinforcing",
    "goes back into": "is reabsorbed into", "behave": "function / differentiate", "helped": "was effective",
    "so far": "to date", "do not have to": "are not necessarily", "does not have to": "is not necessarily",
    "doubted": "questioned whether", "more as the dose rose": "in a dose-dependent manner",
    "make less": "reduce the synthesis of", "a lot": "drop it", "big": "large", "tracked": "paralleled",
    "comes from two sides": "has two lines of support", "for example": "drop it or use 'such as'",
}
CONNECTORS = ["Moreover", "Furthermore", "In addition", "Additionally", "Likewise", "Importantly",
              "Notably", "Mechanistically", "Nevertheless", "Overall", "However", "Further evidence",
              "At the clinical level", "Regarding", "Thus"]
CONTRAST = re.compile(r"^(However|In contrast|Unlike|While|Whereas|Conversely|On the other hand)\b")
PARTICIPLE = re.compile(r",\s+(suggesting|indicating|providing|leading|resulting|highlighting|"
                        r"making|thereby|triggering|producing|demonstrating|reflecting)\b", re.I)
CHAIN = re.compile(r",\s+(and this|so)\s", re.I)   # v1's own fixes; spoken when repeated
# a superlative about the literature ("the largest trial") reads as a claim about ALL trials → hedge with "we found"
ABSOLUTE = re.compile(r"\b(the only|never|always|no (study|trial|data|evidence)|first to"
                      r"|the (largest|biggest|longest|first|earliest) (\w+ ){0,2}(trials?|stud(y|ies)|cohorts?|meta-analys[ie]s|RCTs?))\b", re.I)
HEDGED = re.compile(r"\b(to our knowledge|we found|we are aware)\b", re.I)
ENDING = re.compile(r"\b(are|is) (needed|required)\b|\bneed (more|well|further)\b|\bfurther (studies|research)\b", re.I)
TAG = re.compile(r"\s*\[[A-Za-z]+\d{4}[a-z]?(?:\s*[;,]\s*[A-Za-z]+\d{4}[a-z]?)*\]")  # also [Zhou2001; Gwinn2008]


# Hidden Unicode (watermarks-remover STRIP_CODEPOINTS + ranges). Stripped by --fix.
STRIP = ({0xAD, 0x34F, 0x61C, 0x115F, 0x1160, 0x17B4, 0x17B5, 0x3164, 0xFEFF, 0xFFA0}
         | set(range(0x180B, 0x1810)) | set(range(0x200B, 0x2010)) | set(range(0x202A, 0x202F))
         | set(range(0x2060, 0x2070)) | set(range(0xFE00, 0xFE10)) | set(range(0xFFF0, 0xFFFC)))
# Reported only, never auto-replaced: odd spaces (thin space in "5 mg" can be intended),
# Cyrillic / fullwidth look-alikes of Latin letters. Greek, µ, ±, ≥, dashes are never touched.
ODD_SPACE = {0xA0, 0x1680, 0x202F, 0x205F, 0x3000} | set(range(0x2000, 0x200B))


def is_hidden(cp):
    return (cp in STRIP or 0xE0000 <= cp <= 0xE0FFF or 0xE000 <= cp <= 0xF8FF or cp >= 0xF0000
            or 0xFDD0 <= cp <= 0xFDEF or cp & 0xFFFE == 0xFFFE or unicodedata.category(chr(cp)) == "Cf")


def body_line(ln):  # headings / '>' markers carry emoji (✍️ = U+270D U+FE0F) -> skip them
    return ln.strip() and not ln.lstrip().startswith(("#", ">"))


def unicode_issues(md):
    issues = []
    for i, ln in enumerate(md.splitlines(), 1):
        if not body_line(ln):
            continue
        for ch in sorted(set(ln)):
            cp = ord(ch)
            if is_hidden(cp):
                kind = "hidden char (watermark risk) → run --fix"
            elif cp in ODD_SPACE:
                kind = "non-standard space → retype as normal space"
            elif 0x400 <= cp <= 0x4FF or 0xFF01 <= cp <= 0xFF5E:
                kind = "Cyrillic/fullwidth look-alike letter → retype"
            else:
                continue
            name = unicodedata.name(ch, "?")
            issues.append(("unicode", f"{kind}: U+{cp:04X} {name} ×{ln.count(ch)}", f"line {i}"))
    return issues


def strip_hidden(md):
    out = [ln if not body_line(ln) else "".join(c for c in ln if not is_hidden(ord(c)))
           for ln in md.split("\n")]
    return "\n".join(out)


def paragraphs(md):
    md = re.sub(r"(?s)^---.*?---", "", md)
    out, sec = [], ""
    for ln in md.splitlines():
        if ln.startswith("#"):
            sec = ln.lstrip("# ").strip()
        elif ln.strip() and not ln.startswith(">"):
            out.append((sec, TAG.sub("", ln.strip())))
    return out


def sentences(p):
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", p) if s]


def check(md):
    issues, endings, contrast = unicode_issues(md), [], {}
    for sec, p in paragraphs(md):
        sents = sentences(p)
        conn = [s for s in sents for c in CONNECTORS if s.startswith(c)]
        if len(conn) > 1:
            issues.append((sec, f"{len(conn)} sentence-opening connectors in one paragraph (max 1)", conn[1][:70]))
        if len(sents) > 2 and re.match(r"(In|A|An) (a |an |the )?\S*\s?(rats?|mice|study|trial|cohort|preclinical|patients)\b", sents[0]):
            issues.append((sec, "paragraph opens with study details — add a short topic sentence first", sents[0][:70]))
        chains = [s for s in sents if CHAIN.search(s)]
        if len(chains) > 1:
            issues.append((sec, f"{len(chains)} ', and this' / ', so' clauses in one paragraph (max 1) → use ', which …' or split", chains[1][:70]))
        for s in sents:
            low = s.lower()
            if CONTRAST.match(s):
                contrast.setdefault(sec, []).append(s)
            for table, kind in ((AI_CLICHES, "AI cliché"), (SPOKEN, "spoken")):
                for w, fix in table.items():
                    if re.search(r"\b" + re.escape(w) + r"\b", low):
                        issues.append((sec, f"{kind} '{w}' → {fix}", s[:70]))
            if ABSOLUTE.search(s) and not HEDGED.search(s):
                issues.append((sec, "absolute claim → hedge ('to our knowledge', 'few studies')", s[:70]))
            n = len(s.split())
            if n > MAX_WORDS:
                issues.append((sec, f"{n} words → split (design | result)", s[:70]))
        if sents and ENDING.search(sents[-1]):
            endings.append((sec, sents[-1][:70]))
    for sec, ss in contrast.items():
        if len(ss) > MAX_CONTRAST:
            issues.append((sec, f"{len(ss)} contrast openers in section (max {MAX_CONTRAST}) → move contrast mid-sentence ('…, but …')", ss[MAX_CONTRAST][:70]))
    if len(endings) > 2:
        for sec, s in endings[2:]:
            issues.append((sec, "repeated 'trials are needed' ending → vary the closing", s))
    for label, val, (lo, hi) in profile(md):
        if not lo <= val <= hi:
            issues.append(("profile", f"{label} = {val:.1f} (benchmark {lo}–{hi if hi < 99 else '…'})", "whole file"))
    return issues


CONN_RX = re.compile(r"^(" + "|".join(CONNECTORS + ["Indeed", "Interestingly", "Therefore", "Conversely",
                                                    "Similarly", "In particular", "Consistently"]) + r")\b")
PASSIVE = re.compile(r"\b(was|were|is|are|been|be)\s+\w+(ed|en)\b")
HEDGE = re.compile(r"\b(may|might|could|suggest\w*|appear\w*|likely|possibl\w*|potential\w*)\b", re.I)


def profile(md):
    sents = [s for _, p in paragraphs(md) for s in sentences(p) if len(s.split()) > 2]
    if len(sents) < 20:  # too short to profile
        return []
    L = [len(s.split()) for s in sents]
    n, mean = len(L), sum(L) / len(L)
    pct = lambda f: 100 * sum(1 for s in sents if f(s)) / n
    vals = {
        "mean sentence length": mean, "sentence length sd": (sd := (sum((x - mean) ** 2 for x in L) / n) ** 0.5),
        "sentence length CV": sd / mean,
        "% sentences <12 words": 100 * sum(x < 12 for x in L) / n,
        "% sentences >35 words": 100 * sum(x > 35 for x in L) / n,
        "% opener connectors": pct(CONN_RX.match), "% passive": pct(PASSIVE.search),
        "% hedged": pct(HEDGE.search), "% ', and this/, so'": pct(CHAIN.search),
        "% ', -ing' tails": pct(PARTICIPLE.search),
    }
    return [(k, vals[k], PROFILE[k]) for k in PROFILE]


def demo():
    bad = ("## X\nIn rats, drug A, a pivotal agent, reduced swelling, suggesting a benefit. Moreover, it worked. "
           "However, B failed, and this matters. It is cheap, so it is used. Trials are needed.\n\n"
           "C is the only study. However, x. Further studies are needed.\n\nUnlike y, z. Whereas q, r. More trials are needed.\n")
    kinds = " ".join(i[1] for i in check(bad))
    for k in ("pivotal", "connectors", "repeated", "spoken 'cheap'", "', so'", "absolute", "contrast openers"):
        assert k in kinds, (k, kinds)
    assert check("## Y\nAnimal data are mixed. In rats, drug A attenuated swelling in a dose-dependent manner.\n") == []
    assert check("## Z\nTo our knowledge, this is the only study.\n") == []
    assert "absolute" in " ".join(i[1] for i in check("## S\nThe drug failed in the largest trial, TRACE RA.\n"))
    assert check("## S\nThe drug failed in the largest trial we found, TRACE RA.\n") == []
    assert check("## S\nMice were dosed after the first immunization.\n") == []
    choppy = "## C\n" + " ".join(["The drug lowered the score in rats."] * 25) + "\n"
    kinds = " ".join(i[1] for i in check(choppy))
    assert "% sentences <12 words" in kinds and "mean sentence length" in kinds, kinds
    marked = "# ✍️ Head\nAMPK​–mTOR in 5 mg TNF-α аnd µM ±.\n"
    kinds = " ".join(i[1] for i in check(marked))
    assert "U+200B" in kinds and "U+2009" in kinds and "U+0430" in kinds and "FE0F" not in kinds, kinds
    assert strip_hidden(marked) == marked.replace("​", ""), "strip must only drop hidden chars"
    print("demo ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--demo"]:
        demo(); sys.exit()
    if sys.argv[1:2] == ["--fix"]:
        for path in sys.argv[2:]:
            md = open(path, encoding="utf-8", newline="").read()  # keep CRLF as is
            new = strip_hidden(md)
            if new != md:
                open(path, "w", encoding="utf-8", newline="").write(new)
            print(f"{path}: removed {len(md) - len(new)} hidden char(s)")
        sys.exit()
    total = 0
    for path in sys.argv[1:]:
        found = check(open(path, encoding="utf-8").read())
        total += len(found)
        print(f"\n== {path}: {len(found)} issue(s)")
        for sec, what, where in found:
            print(f"  [{sec}] {what}\n      → {where}")
    print("\n✅ style clean" if total == 0 else f"\n⚠️ {total} style issue(s)")
    sys.exit(1 if total else 0)
