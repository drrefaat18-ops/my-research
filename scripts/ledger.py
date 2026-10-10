"""Claim ledger across review drafts: which [Tag] backs which sentence in which Day file.

Flags (1) the same tag + same number reported in two drafts = likely repeated claim,
(2) tags cited once only (check the paper earns its place), (3) tags with no papers/<Tag>.md.

Usage (from the review folder):
    PYTHONIOENCODING=utf-8 python ../scripts/ledger.py            # all drafts/Day*.md
    python ../scripts/ledger.py --demo
"""
import glob, os, re, sys
from collections import defaultdict

TAG = re.compile(r"\[([A-Za-z]+\d{4}[a-z]?)\]")
NUM = re.compile(r"(?<![\w.])\d+(?:\.\d+)?(?:\s*%)?")
SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")


def build(texts):
    """texts: {draft_name: text} -> {tag: [(draft, sentence, numbers)]}"""
    led = defaultdict(list)
    for name, text in texts.items():
        for para in text.split("\n"):
            if para.lstrip().startswith((">", "#", "---")):
                continue
            for s in SENT.split(para):
                nums = {n.replace(" ", "") for n in NUM.findall(TAG.sub("", s))}
                for t in set(TAG.findall(s)):
                    led[t].append((name, s.strip(), nums))
    return led


def repeats(led):
    """(tag, number, drafts) where one tag carries the same number in more than one draft."""
    out = []
    for t, uses in led.items():
        by_num = defaultdict(set)
        for d, _, nums in uses:
            for n in nums:
                by_num[n].add(d)
        out += [(t, n, sorted(ds)) for n, ds in by_num.items() if len(ds) > 1 and not re.fullmatch(r"\d", n)]
    return out


def demo():
    led = build({"Day1.md": "Statins cut CRP by 23% [Kang2013]. Metformin acts on AMPK [Zhou2001].",
                 "Day3.md": "> note [Kang2013] 23%\nAs noted, CRP fell 23% [Kang2013]."})
    assert set(led) == {"Kang2013", "Zhou2001"}, led
    assert len(led["Kang2013"]) == 2  # blockquote line skipped
    assert repeats(led) == [("Kang2013", "23%", ["Day1.md", "Day3.md"])], repeats(led)
    print("demo ok")


def main():
    if "--demo" in sys.argv:
        return demo()
    texts = {os.path.basename(p): open(p, encoding="utf-8").read() for p in sorted(glob.glob("drafts/Day*.md"))}
    if not texts:
        sys.exit("no drafts/Day*.md here — run from the review folder")
    led = build(texts)
    print(f"Ledger: {len(led)} tags across {len(texts)} drafts")
    for t in sorted(led):
        print(f"  {t}: " + ", ".join(f"{d}×{n}" for d, n in sorted(
            {d: sum(1 for x in led[t] if x[0] == d) for d, *_ in led[t]}.items())))
    rep = repeats(led)
    print(f"\nSame tag + same number in 2+ drafts (likely repeated claim): {len(rep)}")
    for t, n, ds in rep:
        print(f"  [{t}] {n} in {', '.join(ds)}")
    once = [t for t, u in led.items() if len(u) == 1]
    print(f"\nCited once only ({len(once)}): " + ", ".join(sorted(once)))
    missing = [t for t in led if not os.path.exists(f"papers/{t}.md")]
    print(f"No papers/<Tag>.md ({len(missing)}): " + (", ".join(sorted(missing)) or "none"))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
