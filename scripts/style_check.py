"""Style check for review drafts: flags the patterns that made AI detectors fire.

Usage (from the review folder):
    PYTHONIOENCODING=utf-8 python ../scripts/style_check.py drafts/Day1.md [more files]
    python ../scripts/style_check.py --demo
Rules validated 2026-10-04: Day1-3 scored 0-1% AI on several detectors after these fixes.
"""
import re, sys

MAX_WORDS = 40  # validated text had sentences up to 38 words; split above this

FANCY = {  # flagged word -> plain swap
    "cornerstone": "widely used in", "pleiotropic": "other effects", "potent": "strong / drop it",
    "possess": "have", "attenuate": "reduce", "attenuates": "reduces", "attenuated": "reduced",
    "thereby": "and this", "subsequently": "then", "which in turn": "and this",
    "plays an integral role": "regulates", "plays a key role": "drives", "plays a crucial role": "drives",
    "growing evidence": "some studies", "counterbalance": "work against", "meaningful": "drop it",
    "warrant": "be studied", "warrants": "should be studied", "robust": "clear", "novel": "new",
    "promising": "drop it", "underscore": "show", "underscores": "shows", "highlight": "show",
    "highlights": "shows", "crucial": "important", "pivotal": "main", "delve": "look at",
    "intricate": "complex", "comprehensive": "drop it", "in the context of": "in",
    "a total of": "drop it", "well-known": "common", "well-designed": "better",
    "primarily": "mainly", "modulates": "changes", "notably": "drop it",
    "concentration-dependent manner": "more as the dose rose",
    "corresponding to": "a fall of", "failed to produce": "did not",
}
CONNECTORS = ["Moreover", "Furthermore", "In addition", "Additionally", "Likewise", "Importantly",
              "Notably", "Mechanistically", "Nevertheless", "Overall", "However", "Further evidence",
              "At the clinical level", "Regarding", "Thus"]
PARTICIPLE = re.compile(r",\s+(suggesting|indicating|providing|leading|resulting|highlighting|"
                        r"making|thereby|triggering|producing|demonstrating|reflecting)\b", re.I)
ENDING = re.compile(r"\b(are|is) needed\b|\bneed (more|well|further)\b|\bfurther (studies|research)\b", re.I)
TAG = re.compile(r"\s*\[[A-Za-z]+\d{4}[a-z]?\]")


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
    issues, endings = [], []
    for sec, p in paragraphs(md):
        sents = sentences(p)
        conn = [s for s in sents for c in CONNECTORS if s.startswith(c)]
        if len(conn) > 1:
            issues.append((sec, f"{len(conn)} sentence-opening connectors in one paragraph (max 1)", conn[1][:70]))
        if len(sents) > 2 and re.match(r"(In|A|An) (a |an |the )?\S*\s?(rats?|mice|study|trial|cohort|preclinical|patients)\b", sents[0]):
            issues.append((sec, "paragraph opens with study details — add a short topic sentence first", sents[0][:70]))
        for s in sents:
            low = s.lower()
            for w, fix in FANCY.items():
                if re.search(r"\b" + re.escape(w) + r"\b", low):
                    issues.append((sec, f"fancy word '{w}' → {fix}", s[:70]))
            if PARTICIPLE.search(s):
                issues.append((sec, "trailing participle clause → split or use 'and this / so'", s[:70]))
            n = len(s.split())
            if n > MAX_WORDS:
                issues.append((sec, f"{n} words → split (design | result)", s[:70]))
        if sents and ENDING.search(sents[-1]):
            endings.append((sec, sents[-1][:70]))
    if len(endings) > 2:
        for sec, s in endings[2:]:
            issues.append((sec, "repeated 'trials are needed' ending → vary the closing", s))
    return issues


def demo():
    bad = ("## X\nIn rats, drug A, a potent agent, reduced swelling, suggesting a benefit. Moreover, it worked. "
           "However, B failed. Trials are needed.\n\nC is known. Further studies are needed.\n\nD. More trials are needed.\n")
    kinds = " ".join(i[1] for i in check(bad))
    assert "potent" in kinds and "participle" in kinds and "connectors" in kinds and "repeated" in kinds, kinds
    assert check("## Y\nAnimal data are mixed. In rats, drug A reduced swelling.\n") == []
    print("demo ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--demo"]:
        demo(); sys.exit()
    total = 0
    for path in sys.argv[1:]:
        found = check(open(path, encoding="utf-8").read())
        total += len(found)
        print(f"\n== {path}: {len(found)} issue(s)")
        for sec, what, where in found:
            print(f"  [{sec}] {what}\n      → {where}")
    print("\n✅ style clean" if total == 0 else f"\n⚠️ {total} style issue(s)")
    sys.exit(1 if total else 0)
