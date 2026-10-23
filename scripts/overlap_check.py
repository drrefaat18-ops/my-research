"""Local plagiarism check: flags sentences in a draft that share long word runs
with the downloaded source papers.

Usage: python overlap_check.py <draft.md> <papers_dir>
"""
import glob
import os
import re
import sys

N = 7  # ponytail: 7-word shingles, same idea as iThenticate's "exact match"; not a web-wide check
# Proper names that must be quoted verbatim (instrument/guideline titles); removed from draft before matching.
NAMES = ["Scale for the Assessment of Narrative Review Articles",
         "European Alliance of Associations for Rheumatology"]


def words(text):
    return re.findall(r"[a-z0-9α-ω]+", text.lower())


def shingles(ws):
    return {" ".join(ws[i:i + N]) for i in range(len(ws) - N + 1)}


def draft_sentences(md):
    # skip headings, Claude's '>' marker lines, and frontmatter
    body = re.sub(r"(?s)^---.*?---", "", md)
    lines = [l for l in body.splitlines() if l.strip() and not l.lstrip().startswith(("#", ">"))]
    text = re.sub(r"\[[A-Za-z]+\d{4}[a-z]?(?:\s*[;,]\s*[A-Za-z]+\d{4}[a-z]?)*\]", "", " ".join(lines))  # drop ref tags, also [A2001; B2002]
    for name in NAMES:
        text = re.sub(re.escape(name), "", text, flags=re.I)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(words(s)) >= N]


def check(draft_md, sources):
    index = {}
    for name, text in sources.items():
        for sh in shingles(words(text)):
            index.setdefault(sh, set()).add(name)
    report, flagged_words, total_words = [], 0, 0
    for s in draft_sentences(draft_md):
        sh = shingles(words(s))
        total_words += len(words(s))
        hits = {}
        for x in sh:
            for name in index.get(x, ()):
                hits[name] = hits.get(name, 0) + 1
        if hits:
            src, n = max(hits.items(), key=lambda kv: kv[1])
            flagged_words += len(words(s))
            report.append((n, src, s))
    pct = 100 * flagged_words / total_words if total_words else 0
    return pct, sorted(report, reverse=True)


def demo():
    src = {"A": "Metformin attenuates experimental autoimmune arthritis through reciprocal regulation of Th17 and Treg balance."}
    draft = "# h\n> note\nMetformin attenuates experimental autoimmune arthritis through reciprocal regulation of Th17 cells [Son2014]. Our own wording about AMPK and joints here is fine."
    pct, rep = check(draft, src)
    assert len(rep) == 1 and rep[0][1] == "A", rep
    assert 0 < pct < 100
    src = {"B": "we developed SANRA, the Scale for the Assessment of Narrative Review Articles, as a tool"}
    assert not check("Its search follows the Scale for the Assessment of Narrative Review Articles (SANRA) closely here.", src)[1]


if __name__ == "__main__":
    if len(sys.argv) < 3:
        demo()
        print("self-check ok")
        sys.exit()
    sys.stdout.reconfigure(encoding="utf-8")  # Windows console default cp1252 crashes on '←'
    draft = open(sys.argv[1], encoding="utf-8").read()
    sources = {os.path.basename(p)[:-3]: open(p, encoding="utf-8").read()
               for p in glob.glob(os.path.join(sys.argv[2], "*.md"))}
    pct, rep = check(draft, sources)
    print(f"Overlap: {pct:.1f}% of draft words are in sentences that copy {N}+ words in a row from a source\n")
    for n, src, s in rep:
        print(f"[{n} matches ← {src}] {s}\n")
    print("✅ clean" if not rep else "⚠️ rewrite the sentences above in your own words")
