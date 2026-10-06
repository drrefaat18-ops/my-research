"""Find missing primary studies per drug via the free Europe PMC REST API (covers PubMed/MEDLINE,
no key). Idea from Imbad0202/academic-research-skills deep-research (source_quality_hierarchy:
SR/MA > RCT > trial > cohort/case-control > animal > in vitro); the search itself is ours.

Usage (from the review folder):
    python ../scripts/find_sources.py metformin statins        # or: all
    python ../scripts/find_sources.py --demo                    # offline self-check
Writes search/<drug>.md (ranked candidates, ✅ already in papers/ or ⬜ missing, OA vs EKB) and
appends database/date/query/hit count to search/search-log.md -> raw material for 2. Methods.
It only FINDS papers; reading them and taking numbers stays manual (rule G: own paper, own result).
"""
import datetime, glob, json, os, re, sys, urllib.parse, urllib.request

API = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
DISEASE = ['rheumatoid arthritis', 'collagen-induced arthritis', 'adjuvant-induced arthritis',
           'inflammatory arthritis']
DRUGS = {
    "metformin": ["metformin"],
    "statins": ["statin", "statins", "atorvastatin", "simvastatin", "rosuvastatin"],
    "fenofibrate": ["fenofibrate", "fibrate", "PPAR-alpha agonist"],
    "pioglitazone": ["pioglitazone", "rosiglitazone", "thiazolidinedione"],
    "arbs": ["losartan", "telmisartan", "candesartan", "valsartan", "angiotensin receptor blocker"],
    "glp1": ["liraglutide", "semaglutide", "exenatide", "dulaglutide", "GLP-1 receptor agonist"],
    "sglt2": ["dapagliflozin", "empagliflozin", "canagliflozin", "SGLT2 inhibitor"],
    "dpp4": ["sitagliptin", "vildagliptin", "linagliptin", "DPP-4 inhibitor"],
}
RANK = {"meta-analysis": 6, "RCT": 5, "clinical trial": 4, "observational": 3, "animal": 2,
        "in vitro": 1, "other": 0}
PER_DESIGN = 10   # ponytail: top 10 per design is enough to spot gaps; raise for the Methods count


def query(terms):
    f = lambda xs: " OR ".join(f'TITLE_ABS:"{x}"' for x in xs)
    return f'({f(terms)}) AND ({f(DISEASE)}) AND NOT PUB_TYPE:"Review"'


def fetch(q, size=300):
    url = API + "?" + urllib.parse.urlencode({"query": q, "format": "json", "pageSize": size,
                                              "resultType": "core"})
    with urllib.request.urlopen(url, timeout=60) as r:
        d = json.load(r)
    return d["hitCount"], d["resultList"]["result"]


def design(r):
    t = (r.get("title") or "") + " " + (r.get("abstractText") or "")[:1500]
    pt = " ".join(r.get("pubTypeList", {}).get("pubType", []))
    mesh = {m["descriptorName"] for m in r.get("meshHeadingList", {}).get("meshHeading", [])}
    if re.search(r"Meta-Analysis|Systematic Review", pt) or re.search(r"meta-analy", t, re.I):
        return "meta-analysis"
    if "Randomized Controlled Trial" in pt or re.search(r"\brandomi[sz]ed\b|placebo-controlled", t, re.I):
        return "RCT"
    if "Clinical Trial" in pt or re.search(r"\bopen-label\b|\bpilot (study|trial)\b", t, re.I):
        return "clinical trial"
    if re.search(r"cohort|case-control|population-based|registry|retrospective|mendelian|nested", t, re.I):
        return "observational"
    if ("Animals" in mesh and "Humans" not in mesh) or re.search(
            r"\b(rats?|mice|murine|mouse)\b|collagen-induced|adjuvant-induced", t, re.I):
        return "animal"
    if re.search(r"synoviocyte|\bFLS\b|in vitro|cell line|macrophages?\b", t, re.I):
        return "in vitro"
    return "other"


def have(papers_dir):
    """DOIs and 'Surname+Year' keys of papers already saved in papers/*.md."""
    dois, keys = set(), set()
    for p in glob.glob(os.path.join(papers_dir, "*.md")):
        keys.add(os.path.basename(p)[:-3].lower())
        m = re.search(r"\*\*DOI:\*\*\s*(\S+)", open(p, encoding="utf-8").read(3000))
        if m:
            dois.add(m.group(1).lower().rstrip("."))
    return dois, keys


def key(r):
    first = re.split(r"[ ,]", (r.get("authorString") or "x").strip())[0]
    return (re.sub(r"[^A-Za-z]", "", first) + str(r.get("pubYear", ""))).lower()


def rows(results, dois, keys):
    out = []
    for r in results:
        d = design(r)
        got = (r.get("doi") or "").lower() in dois or key(r) in keys
        oa = "OA" if r.get("isOpenAccess") == "Y" or r.get("pmcid") else "EKB"
        out.append((RANK[d], r.get("citedByCount", 0), d, got, oa, r))
    out.sort(key=lambda x: (-x[0], -x[1]))
    return out


def report(drug, q, hits, ranked, today):
    lines = [f"# Candidates: {drug}", "", f"Europe PMC, {today}, {hits} hits (title/abstract, reviews excluded)",
             "", "```", q, "```", "", "✅ = already in papers/ · ⬜ = missing · OA = free full text · "
             "EKB = download from the Egyptian Knowledge Bank", ""]
    for d in RANK:
        group = [x for x in ranked if x[2] == d][:PER_DESIGN]
        if not group:
            continue
        lines += [f"## {d} ({sum(1 for x in ranked if x[2] == d)} found)", "",
                  "| | Year | First author | Title | Cited | Access | Link |", "|---|---|---|---|---|---|---|"]
        for _, cites, _, got, oa, r in group:
            link = f"https://doi.org/{r['doi']}" if r.get("doi") else f"https://europepmc.org/abstract/MED/{r.get('pmid')}"
            title = (r.get("title") or "").replace("|", "/")[:110]
            author = (r.get("authorString") or "").split(",")[0]
            lines.append(f"| {'✅' if got else '⬜'} | {r.get('pubYear')} | {author} | {title} | {cites} | {oa} | {link} |")
        lines.append("")
    return "\n".join(lines)


def demo():
    rec = lambda **k: {"title": k.get("t", ""), "pubTypeList": {"pubType": k.get("pt", [])},
                       "meshHeadingList": {"meshHeading": [{"descriptorName": m} for m in k.get("mesh", [])]}}
    assert design(rec(t="Metformin in RA: a randomized trial")) == "RCT"
    assert design(rec(t="Statins and RA onset: a population-based cohort")) == "observational"
    assert design(rec(t="Losartan attenuates collagen-induced arthritis in rats")) == "animal"
    assert design(rec(t="x", pt=["Meta-Analysis"])) == "meta-analysis"
    assert design(rec(t="Metformin inhibits RA synoviocyte migration")) == "in vitro"
    r = {"authorString": "Chodick G, Amital H.", "pubYear": "2010", "doi": "10.1/X", "isOpenAccess": "N"}
    (_, _, _, got, oa, _), = rows([dict(r, title="cohort")], set(), {"chodick2010"})
    assert got and oa == "EKB"
    assert 'TITLE_ABS:"metformin"' in query(["metformin"]) and "NOT PUB_TYPE" in query(["x"])
    print("demo ok")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--demo"] or not args:
        demo(); sys.exit()
    names = list(DRUGS) if args == ["all"] else args
    bad = [n for n in names if n not in DRUGS]
    if bad:
        sys.exit(f"unknown drug(s) {bad}; choose from {list(DRUGS)}")
    os.makedirs("search", exist_ok=True)
    dois, keys = have("papers")
    today = datetime.date.today().isoformat()
    for n in names:
        q = query(DRUGS[n])
        try:
            hits, res = fetch(q)
        except OSError as e:
            sys.exit(f"Europe PMC unreachable ({e}); nothing written for {n}")
        ranked = rows(res, dois, keys)
        open(f"search/{n}.md", "w", encoding="utf-8").write(report(n, q, hits, ranked, today))
        with open("search/search-log.md", "a", encoding="utf-8") as log:
            log.write(f"| {today} | Europe PMC | {n} | {hits} | `{q}` |\n")
        missing = sum(1 for x in ranked if not x[3] and x[2] in ("meta-analysis", "RCT", "clinical trial", "observational"))
        print(f"{n}: {hits} hits, {len(res)} ranked, {missing} human studies missing → search/{n}.md")
