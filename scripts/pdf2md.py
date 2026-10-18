"""Convert downloaded PDFs (papers/pdf/<Key>.pdf) to papers/<Key>.md + papers/text/<Key>.txt.
Header and abstract come from Europe PMC (by DOI); body text from the PDF, one paragraph per text block.

Usage (from the review folder):
    python ../scripts/pdf2md.py Kwak2000 10.1038/82219 [Key DOI ...]
    python ../scripts/pdf2md.py --demo
Then highlight key sentences with highlight.py (it warns on second-hand claims).
"""
import html, json, os, re, sys, urllib.parse, urllib.request

API = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
HEAD = re.compile(r"^(\d+\.?\s*)?(abstract|introduction|background|(materials and |patients and )?methods|"
                  r"results|discussion|conclusions?|references)$", re.I)


def clean(block):
    """Join PDF lines into one paragraph: undo end-of-line hyphenation, collapse whitespace."""
    t = re.sub(r"(\w)-\n(?=[a-z])", r"\1", block)
    t = re.sub(r"-\n(?=[A-Z0-9])", "-", t)  # IL-\n6 -> IL-6
    return re.sub(r"\s+", " ", t).strip()


def meta(doi):
    url = API + "?" + urllib.parse.urlencode({"query": f'DOI:"{doi}"', "format": "json", "resultType": "core"})
    with urllib.request.urlopen(url, timeout=60) as r:
        res = json.load(r)["resultList"]["result"]
    return res[0] if res else {}


def convert(key, doi, folder="papers"):
    import fitz  # PyMuPDF, already used by extract_pdf_papers.py
    doc = fitz.open(os.path.join(folder, "pdf", key + ".pdf"))
    paras = []
    for page in doc:
        for b in page.get_text("blocks"):
            p = clean(b[4])
            # some layouts glue an ALL-CAPS heading to its first sentence: "RESULTS PPAR-γ ..."
            glued = re.match(r"(INTRODUCTION|BACKGROUND|MATERIALS AND METHODS|METHODS|RESULTS|DISCUSSION|CONCLUSIONS?) (?=[A-Z])", p)
            if glued:
                paras.append("## " + glued.group(1))
                p = p[glued.end():]
            if HEAD.match(p):  # keep section headings so secondary_check knows Intro/Discussion
                paras.append("## " + p)
            elif len(p) > 40:  # ponytail: drops running heads/page numbers
                paras.append(p)
    with open(os.path.join(folder, "text", key + ".txt"), "w", encoding="utf-8") as f:
        f.write("\n\n".join(page.get_text() for page in doc))
    m = meta(doi)
    ab = re.sub(r"<h4>(.*?)</h4>", r"\n\n**\1:** ", m.get("abstractText") or "")
    ab = html.unescape(re.sub(r"<(?!/?(sub|sup))[^>]+>", "", ab)).strip()
    authors = ", ".join(f'{a.get("lastName", "")} {a.get("initials", "")}'.strip()
                        for a in m.get("authorList", {}).get("author", []))
    journal = m.get("journalInfo", {}).get("journal", {}).get("title", "")
    md = (f'# {m.get("title", key).rstrip(".")}\n\n**Authors:** {authors}  \n'
          f'**Journal:** {journal} ({m.get("pubYear", "")})  \n**DOI:** {doi}  \n**PDF:** pdf/{key}.pdf\n\n'
          f'## Abstract\n\n{ab}\n\n## Full text (PDF extraction)\n\n' + "\n\n".join(paras) + "\n")
    with open(os.path.join(folder, key + ".md"), "w", encoding="utf-8") as f:
        f.write(md)
    return len(paras)


if __name__ == "__main__":
    if sys.argv[1:] == ["--demo"]:
        assert clean("statins de-\ncrease  iso-\nprenylation\nof Ras") == "statins decrease isoprenylation of Ras"
        assert clean("IL-\n6 and TNF") == "IL-6 and TNF"  # capital after hyphen is kept
        assert HEAD.match("2. Materials and methods") and HEAD.match("DISCUSSION") and not HEAD.match("Results show X")
        print("demo ok")
        sys.exit()
    a = sys.argv[1:]
    for key, doi in zip(a[::2], a[1::2]):
        print(key, convert(key, doi), "paragraphs")
