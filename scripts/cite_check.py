"""Citation check for review drafts (rules ported from Imbad0202/academic-research-skills:
citation_compliance_agent, _claim_audit_constants, claim_registry_coverage, temporal_integrity_audit,
check_acronyms). Tags look like [Kang2013] / [vanBoheemen2021]; each must have papers/<Tag>.md.

Usage (from the review folder):
    PYTHONIOENCODING=utf-8 python ../scripts/cite_check.py drafts/Day1.md [more files]
    python ../scripts/cite_check.py --demo
Acronyms are checked across ALL drafts/*.md (a term defined on Day 1 counts on Day 3).
"""
import glob, os, re, sys

_T = r"[A-Za-z]+\d{4}[a-z]?"
TAG = re.compile(rf"\[({_T}(?:\s*[;,]\s*{_T})*)\]")  # [Kang2013] and [Zhou2001; Gwinn2008]
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
DEF_SPAN = re.compile(r"[^.()]{0,60}\(([^()]{1,20})\)")  # up to 60 chars + '(ABC)'; long form = long_form()
ACRO_OK = {"RA", "DNA", "RNA", "mRNA", "CI", "HR", "OR", "RR", "SD", "SEM", "II", "III", "IV", "VI",
           "USA", "UK", "US", "NF", "Th", "Treg", "TH", "IgG", "IgM", "CD4", "CD8",
           "DBA"}  # DBA/1J = mouse strain name, never spelled out


def tags(s):
    """Every tag in s, one per citation: '[Zhou2001; Gwinn2008]' -> both."""
    return [t for g in TAG.findall(s) for t in re.split(r"\s*[;,]\s*", g)]


def long_form_start(m):
    """Offset in m.group(0) where the long form starts: only the words that spell the acronym, not
    all 60 characters before '(ABC)'. The window can start mid-word: 'SGLT|2 inhibitor use …
    urinary tract infection (UTI)' left 'SGLT' as an undefined acronym (step 18)."""
    letters = [c for c in re.split(r"[;,\s]", m.group(1).strip())[0] if c.isupper()]
    ws = list(re.finditer(r"\S+", m.group(0)[:m.group(0).rindex("(")]))
    if not letters or not ws:
        return 0
    window = ws[-(len(letters) + 1):]  # one spare word: 'an AMP-activated protein kinase (AMPK)'
    hit = [w for w in window if w.group(0)[:1].upper() == letters[0]]
    return (hit[0] if hit else ws[-min(len(letters), len(ws))]).start()


def strip_defs(p):
    """p without each 'long form (ABC)'; the words before the long form stay."""
    out, pos = [], 0
    for m in DEF_SPAN.finditer(p):
        out.append(p[pos:m.start() + long_form_start(m)])
        pos = m.end()
    return "".join(out) + p[pos:]


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
                # only the first token defines: '(DALYs; 95% UI …)' → DALY; '(95% CI 1.1–2.0)' and
                # '(HR 0.91)' are data, not definitions
                span = m.group(1).strip()
                if re.match(r"\S+\s+[<>=≤≥−-]?\d", span):
                    continue
                for a in acros(re.split(r"[;,\s]", span)[0]):
                    defined[a] = defined.get(a, 0) + 1
            used |= acros(strip_defs(p))  # drop long forms: 'AMP-activated … (AMPK)'
    # an isoform of a defined family is defined: 'JAK1/2' once 'Janus kinase (JAK)' exists
    undefined = sorted(a for a in used if a not in defined and a not in ACRO_OK
                       and re.sub(r"\d+$", "", a) not in defined)
    twice = [a for a, n in defined.items() if n > 1]
    return undefined, twice


def check(md, papers, all_drafts=()):
    issues, cited = [], []
    for sec, p in blocks(md):
        sents = sentences(p)
        ptags = tags(p)
        cited += ptags
        own = "methods" in sec.lower()  # ponytail: Methods describe our own search; numbers come from search-log.md, not papers
        if len(sents) > 2 and not ptags and not own:
            issues.append((sec, "paragraph with no citation", p[:70]))
        for i, s in enumerate(sents):
            st = tags(s)
            later = any(TAG.search(x) for x in sents[i:])
            plain = TAG.sub("", s)
            if len(st) > MAX_TAGS:
                issues.append((sec, f"{len(st)} tags in one sentence (max {MAX_TAGS})", plain[:70]))
            if DATA.search(plain) and not later and not own:
                issues.append((sec, "data/number with no citation in this or a later sentence", plain[:70]))
            if VAGUE.search(plain) and not st:
                issues.append((sec, f"vague '{VAGUE.search(plain).group(0)}' → cite or name the studies", plain[:70]))
            if STALE.search(plain) and not st and not YEAR.search(plain):
                issues.append((sec, f"time word '{STALE.search(plain).group(0)}' with no year or citation", plain[:70]))
    for t in sorted(set(cited)):
        if t not in papers:
            issues.append(("refs", f"[{t}] has no papers/{t}.md (orphan citation)", t))
    uniq = set(cited)
    if len(uniq) >= 10:
        this_year = 2026  # ponytail: fixed to the manuscript year; bump at resubmission
        recent = 100 * sum(int(re.search(r"\d{4}", t).group()) >= this_year - RECENT_YEARS for t in uniq) / len(uniq)
        if recent < MIN_RECENT_PCT:
            issues.append(("refs", f"only {recent:.0f}% of refs from the last {RECENT_YEARS} years (min {MIN_RECENT_PCT}%)", "whole file"))
    if all_drafts:
        undefined, twice = acronyms(all_drafts)
        mine = {}
        for sec, p in blocks(md):
            for a in acros(strip_defs(TAG.sub("", p))):
                mine.setdefault(a, (sec, p[:70]))
        for a in undefined:
            if a in mine:
                issues.append((mine[a][0], f"'{a}' used but never defined as 'long form ({a})'", mine[a][1]))
        for a in twice:
            if re.search(rf"\({re.escape(a)}s?\)", md):  # plural '(DMARDs)' defines DMARD too
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
    assert tags("x [Zhou2001; Gwinn2008] y [Kang2013]") == ["Zhou2001", "Gwinn2008", "Kang2013"]
    tail = "2 inhibitor use was linked to more urinary tract infection "  # 60-char window starts mid-'SGLT2'
    lf = "Sodium-glucose cotransporter 2 (SGLT2) is new. Use of SGLT" + tail + "(UTI)."
    assert acronyms([lf]) == ([], []), acronyms([lf])  # window began mid-'SGLT2' and left 'SGLT'
    assert strip_defs("then AMP-activated protein kinase (AMPK) rose") == "then  rose"
    assert acronyms(["Janus kinase (JAK) signals. A JAK1/2 inhibitor. STAT3 rose."])[0] == ["STAT3"]
    bad = check("## Y\nA. B. It fell by 40%.\n", set())
    assert any("data/number" in i[1] for i in bad) and any("no citation" in i[1] for i in bad), bad
    assert not check("## 2. Methods\nA. B. It found 628 records.\n", set()), "Methods own-search text needs no tag"
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
