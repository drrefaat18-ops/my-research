"""Whole-manuscript structure check for a narrative review. Rules from
Master-cai/Research-Paper-Writing-Skills (abstract roles, intro gap, conclusion) and
Imbad0202/academic-research-skills (paper_structure_patterns: thematic review, failure_paths F3/F4,
EQUATOR items a narrative review should still report). Run at assembly, not per paragraph.

Usage (from the review folder):
    PYTHONIOENCODING=utf-8 python ../scripts/structure_check.py drafts/Day*.md
    python ../scripts/structure_check.py --demo
"""
import re, sys

TOTAL = (6000, 7500)       # journal-neutral target (START-HERE: 6-7k words)
ABSTRACT_MAX = 250
SECTIONS = {               # number -> (name regex, share of body words lo-hi %) ; ponytail: rough bands
    "1": (r"introduction", (6, 15)), "2": (r"methods?", (2, 8)), "3": (r"patho", (8, 20)),
    "4": (r"", (40, 65)), "5": (r"challenges|perspectives", (6, 15)), "6": (r"conclusion", (2, 8)),
}
GAP = re.compile(r"\b(however|remains?|lack\w*|limited|unclear|unknown|few|gap)\b", re.I)
AIM = re.compile(r"\b(this review|we (review|summari[sz]e|discuss|examine)|here,? we|the aim)\b", re.I)
LIMIT = re.compile(r"\blimitation", re.I)
FUTURE = re.compile(r"\b(future|further|trials? (are|is) (needed|required)|should (be|now))\b", re.I)
METHOD_ITEMS = {"database": r"PubMed|MEDLINE|Scopus|Web of Science|Embase|Google Scholar|Europe PMC",
                "date range": r"\b(19|20)\d{2}\b.{0,40}\b(19|20)\d{2}\b|\buntil\b|\bup to\b",
                "search terms": r"search (terms|string|strategy)|keywords|\bAND\b|\bOR\b",
                "inclusion criteria": r"inclu\w+|exclu\w+|eligib\w+"}
TAG = re.compile(r"\[[A-Za-z]+\d{4}[a-z]?\]")


def sections(texts):
    """{heading: [paragraphs]} over all drafts; '>' markers and frontmatter skipped."""
    out, head = {}, None
    for md in texts:
        md = re.sub(r"(?s)^---.*?---", "", md)
        for ln in md.splitlines():
            if ln.startswith("## "):
                head = ln[3:].strip()
                out.setdefault(head, [])
            elif ln.startswith("#"):
                head = None
            elif head and ln.strip() and not ln.lstrip().startswith(">"):
                out[head].append(ln.strip())
    return out


def words(paras):
    return sum(len(TAG.sub("", p).split()) for p in paras)


def find(secs, num, rx):
    for h, ps in secs.items():
        if h.startswith(num + ".") and re.search(rx, h, re.I):
            return h, ps
    return None, []


def check(texts):
    secs, issues = sections(texts), []
    body = {h: ps for h, ps in secs.items() if re.match(r"\d", h)}
    total = words([p for ps in body.values() for p in ps])
    if not TOTAL[0] <= total <= TOTAL[1]:
        issues.append(("length", f"body = {total} words (target {TOTAL[0]}–{TOTAL[1]})"))
    for num, (rx, (lo, hi)) in SECTIONS.items():
        parts = {h: ps for h, ps in body.items() if h.split(".")[0] == num}
        n = words([p for ps in parts.values() for p in ps])
        if not n:
            issues.append((f"section {num}", "missing or empty"))
        elif total and not lo <= 100 * n / total <= hi:
            issues.append((f"section {num}", f"{n} words = {100 * n / total:.0f}% of body (band {lo}–{hi}%)"))
    ab = next((ps for h, ps in secs.items() if h.lower().startswith("abstract")), [])
    if ab:
        text = " ".join(ab)
        n, s = len(text.split()), len(re.split(r"(?<=[.!?])\s+", text))
        if n > ABSTRACT_MAX:
            issues.append(("abstract", f"{n} words (max {ABSTRACT_MAX})"))
        if not 5 <= s <= 10:
            issues.append(("abstract", f"{s} sentences (expected 5–10: background, gap, aim, themes, implication)"))
        if TAG.search(text):
            issues.append(("abstract", "contains citation tags"))
        for name, rx in (("gap", GAP), ("aim", AIM)):
            if not rx.search(text):
                issues.append(("abstract", f"no {name} sentence"))
    else:
        issues.append(("abstract", "missing"))
    kw = next((ps for h, ps in secs.items() if h.lower().startswith("keyword")), [])
    k = len([x for x in re.split(r"[;,]", " ".join(kw)) if x.strip()])
    if not 3 <= k <= 7:
        issues.append(("keywords", f"{k} keywords (expected 3–7)"))
    h, intro = find(secs, "1", "introduction")
    if intro and not (GAP.search(intro[-1]) and AIM.search(intro[-1])):
        issues.append(("introduction", "last paragraph should state the gap and this review's aim"))
    h, meth = find(secs, "2", "method")
    for item, rx in METHOD_ITEMS.items():
        if meth and not re.search(rx, " ".join(meth)):
            issues.append(("methods", f"no {item}"))
    allp = " ".join(p for ps in body.values() for p in ps)
    if body and not LIMIT.search(allp):
        issues.append(("limitations", "no paragraph names the review's or the evidence's limitations"))
    h, concl = find(secs, "6", "conclusion")
    if concl and not FUTURE.search(concl[-1]):
        issues.append(("conclusion", "last paragraph should give a concrete future direction"))
    return issues


def demo():
    good = ("## Abstract\nRA is common. Many patients fail DMARDs. Drug repurposing is cheap. However, evidence "
            "remains scattered. This review summarizes cardiometabolic drugs. Metformin and statins show the "
            "most data. Trials should now test them.\n## Keywords\nRA; metformin; statins; repurposing\n"
            "## 1. Introduction\nx " * 1 + "\nHowever, data remain scattered, and this review examines them.\n"
            "## 2. Methods\nWe searched PubMed and Scopus from 2000 to 2026 using search terms; inclusion was English.\n"
            "## 6. Conclusions\nFuture trials should test metformin. A limitation is bias.\n")
    kinds = " ".join(f"{a} {b}" for a, b in check([good]))
    assert "abstract" not in kinds and "methods" not in kinds and "introduction" not in kinds, kinds
    assert "section 3 missing" in kinds and "body =" in kinds, kinds
    bad = check(["## Abstract\nRA is bad [Kang2013].\n## 2. Methods\nWe read papers.\n"])
    kinds = " ".join(f"{a} {b}" for a, b in bad)
    for k in ("contains citation", "no gap", "no aim", "no database", "keywords"):
        assert k in kinds, (k, kinds)
    print("demo ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--demo"]:
        demo(); sys.exit()
    found = check([open(p, encoding="utf-8").read() for p in sys.argv[1:]])
    for where, what in found:
        print(f"  [{where}] {what}")
    print("\n✅ structure clean" if not found else f"\n⚠️ {len(found)} structure issue(s)")
    sys.exit(1 if found else 0)
