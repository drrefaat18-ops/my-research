"""A4 PDF of selected Day-draft sections, with [Tag] citations numbered and a reference list
built from papers/<Tag>.md metadata (# title, **Authors:**, **Journal:** Name (Year), **DOI:**).

Usage: python scripts/make_section_pdf.py
Edit JOBS below to add sections. Fails loudly if a cited tag has no metadata.
"""
import io, os, re
from fpdf import FPDF
from fpdf.enums import XPos, YPos

R = r"d:/vault/my research/08 - RA Repurposing Review"
OUT = f"{R}/to-Dr-Ahmed-Morad"
DATE = "9 October 2026"
JOBS = [  # (draft, headings, short title, output file)
    ("Day1", ["4.1. Antidiabetic Drugs", "4.1.1. Metformin"], "Section 4.1.1 — Metformin", "Section-4.1.1-Metformin.pdf"),
    ("Day1", ["4.2. Lipid-Lowering Drugs", "4.2.1. Statins"], "Section 4.2.1 — Statins", "Section-4.2.1-Statins.pdf"),
    ("Day1", ["4.1. Antidiabetic Drugs", "4.1.1. Metformin", "4.2. Lipid-Lowering Drugs", "4.2.1. Statins",
              "4.2.2. Fenofibrate"], "Day 1 — Metformin, Statins, Fenofibrate", "Day1-Metformin-Statins-Fenofibrate.pdf"),
]
TAG = re.compile(r"((?:\[[A-Za-z]+\d{4}[a-z]?(?:\s*[;,]\s*[A-Za-z]+\d{4}[a-z]?)*\])+)")  # [A2001][B2002] and [A2001; B2002]
PARTICLES = {"van", "de", "von", "der", "den", "da", "di", "le", "la", "el"}


def sections(day):
    out, cur = {}, None
    for ln in io.open(f"{R}/drafts/{day}.md", encoding="utf-8"):
        ln = ln.strip()
        if ln.startswith("## "):
            cur = ln[3:].strip(); out[cur] = []
        elif cur and ln and not ln.startswith((">", "#")):
            out[cur].append(ln)
    return out


def meta(tag):
    t = io.open(f"{R}/papers/{tag}.md", encoding="utf-8").read()
    title = re.search(r"^# (.+)$", t, re.M).group(1).strip().rstrip(".☆★*†")  # journal footnote marks
    authors = re.search(r"\*\*Authors:\*\*\s*(.+)", t).group(1).strip()
    jy = re.search(r"\*\*Journal:\*\*\s*(.+?)\s*\((\d{4})\)\s*$", t, re.M)
    doi = re.search(r"\*\*DOI:\*\*\s*(\S+)", t)
    return title, authors, jy.group(1), jy.group(2), doi.group(1) if doi else ""


def vancouver_name(full):
    """'van Boheemen Laurette' -> 'van Boheemen L'; 'Son Hye-Jin' -> 'Son HJ'."""
    w = full.split()
    i = 1
    while i < len(w) - 1 and w[i - 1].lower() in PARTICLES:
        i += 1
    given = re.split(r"[\s\-.]+", " ".join(w[i:]))
    return " ".join(w[:i]) + " " + "".join(g[0] for g in given if g)


def reference(n, tag):
    title, authors, journal, year, doi = meta(tag)
    names = []
    for a in (x.strip() for x in authors.split(",")):
        if a and vancouver_name(a) not in names:  # source lists have duplicates (Kitas2019)
            names.append(vancouver_name(a))
    au = ", ".join(names[:3]) + (", et al." if len(names) > 3 else ".")
    journal = re.sub(r"\s*\(.*?\)", "", journal)
    return f"{n}. {au} {title}. {journal}. {year}." + (f" doi:{doi}" if doi else "")


def number(paras):
    order = []
    def repl(m):
        nums = []
        for tag in re.split(r"\s*[;,]\s*|\]\s*\[", m.group(1).strip("[]")):
            if tag not in order:
                order.append(tag)
            nums.append(str(order.index(tag) + 1))
        return "[" + ", ".join(dict.fromkeys(nums)) + "]"
    return [TAG.sub(repl, p) for p in paras], order


class PDF(FPDF):
    def footer(self):  # plain Word-style page number only
        self.set_y(-10); self.set_font("T", "", 10)
        self.cell(0, 5, str(self.page_no()), align="C")


def build(day, heads, short, fname):
    secs = sections(day)
    blocks = [(h, secs[h]) for h in heads]
    flat, order = number([p for _, ps in blocks for p in ps])
    words = sum(len(TAG.sub("", p).split()) for _, ps in blocks for p in ps)
    pdf = PDF(format=(105, 180))  # phone-width page; plain Word-like styling
    F = r"C:\Windows\Fonts"
    for st, f in (("", "times.ttf"), ("B", "timesbd.ttf"), ("I", "timesi.ttf")):
        pdf.add_font("T", st, os.path.join(F, f))
    pdf.set_margins(8, 10, 8); pdf.set_auto_page_break(True, 14); pdf.add_page()
    LH = 5.8  # 12 pt, ~1.4 line spacing
    i = 0
    for h, ps in blocks:
        pdf.set_font("T", "B", 12)
        pdf.multi_cell(0, LH, h, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("T", "", 12)
        for _ in ps:
            pdf.multi_cell(0, LH, flat[i], align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT); pdf.ln(LH / 2); i += 1
    pdf.set_font("T", "B", 12)
    pdf.multi_cell(0, LH, "References", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("T", "", 12)
    for n, tag in enumerate(order, 1):
        pdf.multi_cell(0, LH, reference(n, tag), align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    os.makedirs(OUT, exist_ok=True)
    pdf.output(f"{OUT}/{fname}")
    return fname, pdf.pages_count, words, len(order)


if __name__ == "__main__":
    assert vancouver_name("van Boheemen Laurette") == "van Boheemen L"
    assert vancouver_name("Son Hye-Jin") == "Son HJ" and vancouver_name("Belch Jill J. F.") == "Belch JJF"
    assert number(["a [X2001][Y2002]. b [X2001]."])[0] == ["a [1, 2]. b [1]."]
    for job in JOBS:
        print(*build(*job))
