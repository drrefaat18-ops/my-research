"""Citation check for review drafts (rules ported from Imbad0202/academic-research-skills:
citation_compliance_agent, _claim_audit_constants, claim_registry_coverage, temporal_integrity_audit,
check_acronyms). Tags look like [Kang2013] / [vanBoheemen2021]; each must have papers/<Tag>.md.

Usage (from the review folder):
    PYTHONIOENCODING=utf-8 python ../scripts/cite_check.py drafts/Day1.md [more files]
    python ../scripts/cite_check.py --demo
Acronyms are checked across ALL drafts/*.md (a term defined on Day 1 counts on Day 3).
"""
import glob, os, re, sys

TAG = re.compile(r"\[([A-Za-z]+\d{4}[a-z]?)\]")
YEAR = re.compile(r"(?<![\d.])(19|20)\d{2}(?![\d.])")
MAX_TAGS = 5            # tags per sentence (citation dump)
RECENT_YEARS = 5        # share of refs from the last 5 years
MIN_RECENT_PCT = 40     # ponytail: ODR-era target; raise if the chosen journal stresses recency
# a sentence reporting data needs a tag in it or later in the same paragraph
DATA = re.compile(r"\d+(\.\d+)?\s*%|\b[Nn]\s*=\s*\d|\b(HR|OR|RR|aHR|aOR|CI|SMD|MD)\b\s*[\d(=:,]|"
                  r"\bp\s*[<=>]\s*0?\.\d|\d+(\.\d+)?\s*(mg|µg|μg|g)(/kg)?\b|\b\d+\s+(patients|participants|"
                  r"mice|rats|subjects|adults|women|men)\b|\b(fold|odds|hazard) ratio|\d+-fold")
VAGUE = re.compile(r"\b(many|several|some|numerous|most) (studies|reports|researchers|authors|trials)\b|"
                   r"\bit is (well )?(known|established)\b|\bin recent years\b", re.I)
STALE = re.compile(r"\b(currently|recently(?! (diagnosed|treated|developed))|nowadays|at present|"
                   r"presently|the latest|newest|this year|last year)\b", re.I)
ACRO = re.compile(r"(?<![\w-])([A-Z][A-Za-z]*[A-Z][A-Za-z0-9]*)(?:-[0-9A-Za-zα-ωΑ-Ω]+)*(?![\w])")
DEF_SPAN = re.compile(r"[^.()]{0,60}\(([^()]{1,20})\)")  # long form + '(ABC)'
ACRO_OK = {"RA", "DNA", "RNA", "mRNA", "CI", "HR", "OR", "RR", "SD", "SEM", "II", "III", "IV", "VI",
           "USA", "UK", "US", "NF", "Th", "Treg", "TH", "IgG", "IgM"}


def blocks(md):
    """(section, paragraph) pairs; skips frontmatter, headings, '>' marker lines."""
    md = re.sub(r"(?s)^---.*?---", "", md)
    out, sec = [], ""
    for ln in md.splitlines():
        if ln.startswith("#"):
            sec = ln.lstrip("# ").strip()
        elif ln.strip() and not ln.lstrip().startswith(">"):
            out.append((sec, ln.strip()))
    return out


def sentences(p):
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", p) if s]


def acros(text):
    """Acronym tokens; plural 's' dropped; skips names (TriNetX) and compound codes (WY14643)."""
    out = set()
    for a in ACRO.findall(text):
        a = a[:-1] if a.endswith("s") and len(a) > 2 else a
        if sum(c.islower() for c in a) <= 1 and sum(c.isdigit() for c in a) < 3:
            out.add(a)
    return out


def acronyms(texts):
    """Acronyms used but never defined '(ABC)' in any draft, and ones defined twice."""
    defined, used = {}, set()
    for t in texts:
        for _, p in blocks(t):
            p = TAG.sub("", p)
            for m in DEF_SPAN.finditer(p):
                for a in acros(m.group(1)):
                    defined[a] = defined.get(a, 0) + 1
            used |= acros(DEF_SPAN.sub("", p))  # drop long forms: 'AMP-activated … (AMPK)'
    undefined = sorted(a for a in used if a not in defined and a not in ACRO_OK)
    twice = [a for a, n in defined.items() if n > 1]
    return undefined, twice


def check(md, papers, all_drafts=()):
    issues, tags = [], []
    for sec, p in blocks(md):
        sents = sentences(p)
        ptags = TAG.findall(p)
        tags += ptags
        if len(sents) > 2 and not ptags:
            issues.append((sec, "paragraph with no citation", p[:70]))
        for i, s in enumerate(sents):
            st = TAG.findall(s)
            later = any(TAG.search(x) for x in sents[i:])
            plain = TAG.sub("", s)
            if len(st) > MAX_TAGS:
                issues.append((sec, f"{len(st)} tags in one sentence (max {MAX_TAGS})", plain[:70]))
            if DATA.search(plain) and not later:
                issues.append((sec, "data/number with no citation in this or a later sentence", plain[:70]))
            if VAGUE.search(plain) and not st:
                issues.append((sec, f"vague '{VAGUE.search(plain).group(0)}' → cite or name the studies", plain[:70]))
            if STALE.search(plain) and not st and not YEAR.search(plain):
                issues.append((sec, f"time word '{STALE.search(plain).group(0)}' with no year or citation", plain[:70]))
    for t in sorted(set(tags)):
        if t not in papers:
            issues.append(("refs", f"[{t}] has no papers/{t}.md (orphan citation)", t))
    uniq = set(tags)
    if len(uniq) >= 10:
        this_year = 2026  # ponytail: fixed to the manuscript year; bump at resubmission
        recent = 100 * sum(int(re.search(r"\d{4}", t).group()) >= this_year - RECENT_YEARS for t in uniq) / len(uniq)
        if recent < MIN_RECENT_PCT:
            issues.append(("refs", f"only {recent:.0f}% of refs from the last {RECENT_YEARS} years (min {MIN_RECENT_PCT}%)", "whole file"))
    if all_drafts:
        undefined, twice = acronyms(all_drafts)
        mine = {}
        for sec, p in blocks(md):
            for a in acros(DEF_SPAN.sub("", TAG.sub("", p))):
                mine.setdefault(a, (sec, p[:70]))
        for a in undefined:
            if a in mine:
                issues.append((mine[a][0], f"'{a}' used but never defined as 'long form ({a})'", mine[a][1]))
        for a in twice:
            if f"({a})" in md:
                issues.append(("acronyms", f"'{a}' defined more than once across drafts", a))
    return issues


def papers_in(folder):
    return {os.path.basename(p)[:-3] for p in glob.glob(os.path.join(folder, "*.md"))}


def demo():
    md = ("## X\nTumour necrosis factor (TNF) rose. Metformin cut CRP by 30% in 66 patients. "
          "It worked [Gharib2021].\n\n"
          "Many studies show benefit. Recently, a trial failed. A B C D [A2001][B2002][C2003][D2004][E2005][F2006].\n\n"
          "One. Two. Three. TNF fell and CRP was 5 mg [Nope2020].\n")
    kinds = " ".join(i[1] for i in check(md, {"Gharib2021"}, [md]))
    for k in ("vague 'Many studies'", "time word 'Recently'", "6 tags", "[Nope2020] has no papers",
              "'CRP' used but never defined"):
        assert k in kinds, (k, kinds)
    assert "data/number" not in kinds, kinds  # 30% sentence is covered by the later [Gharib2021]
    assert "'TNF'" not in kinds, kinds
    bad = check("## Y\nA. B. It fell by 40%.\n", set())
    assert any("data/number" in i[1] for i in bad) and any("no citation" in i[1] for i in bad), bad
    print("demo ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--demo"]:
        demo(); sys.exit()
    total = 0
    for path in sys.argv[1:]:
        d = os.path.dirname(os.path.abspath(path))
        papers = papers_in(os.path.join(d, "..", "papers"))
        drafts = [open(p, encoding="utf-8").read() for p in sorted(glob.glob(os.path.join(d, "*.md")))]
        found = check(open(path, encoding="utf-8").read(), papers, drafts)
        total += len(found)
        print(f"\n== {path}: {len(found)} citation issue(s)")
        for sec, what, where in found:
            print(f"  [{sec}] {what}\n      → {where}")
    print("\n✅ citations clean" if total == 0 else f"\n⚠️ {total} citation issue(s)")
    sys.exit(1 if total else 0)
