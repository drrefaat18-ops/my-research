import io, re, os
from fpdf import FPDF

R = r"d:/vault/my research/08 - RA Repurposing Review"
sections = {}
for d in (1, 2, 3):
    cur = None
    for ln in io.open(f"{R}/drafts/Day{d}.md", encoding="utf-8"):
        ln = ln.rstrip("\n")
        if ln.startswith("## "):
            cur = ln[3:].strip(); sections[cur] = []
        elif cur and ln.strip() and not ln.startswith(">"):
            sections[cur].append(ln.strip())

key = lambda h: [int(x) for x in re.match(r"([\d.]+)", h).group(1).strip(".").split(".")]
groups = {}

F = r"C:\Windows\Fonts"
pdf = FPDF(unit="mm", format=(110, 190))  # phone-sized page
pdf.set_margins(8, 10, 8); pdf.set_auto_page_break(True, 12)
pdf.add_font("T", "", os.path.join(F, "times.ttf")); pdf.add_font("T", "B", os.path.join(F, "timesbd.ttf"))
pdf.add_font("T", "I", os.path.join(F, "timesi.ttf"))
pdf.add_page()
pdf.set_font("T", "B", 15); pdf.multi_cell(0, 7, "Drug Repurposing in Rheumatoid Arthritis", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("T", "I", 10); pdf.set_text_color(110); pdf.multi_cell(0, 5, "Section 4 — working draft (Days 1–3)", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(4)
seen = set()
for h in sorted(sections, key=key):
    g = ".".join(str(x) for x in key(h)[:2])
    if g in groups and g not in seen:
        seen.add(g); pdf.set_text_color(20, 40, 80); pdf.set_font("T", "B", 13)
        pdf.ln(3); pdf.multi_cell(0, 6, groups[g], new_x="LMARGIN", new_y="NEXT"); pdf.ln(1)
    pdf.set_text_color(20, 40, 80); pdf.set_font("T", "B", 12)
    pdf.ln(2); pdf.multi_cell(0, 6, h, new_x="LMARGIN", new_y="NEXT"); pdf.ln(1)
    pdf.set_text_color(25); pdf.set_font("T", "", 11.5)
    for p in sections[h]:
        pdf.multi_cell(0, 5.6, p, align="J", new_x="LMARGIN", new_y="NEXT"); pdf.ln(2.5)
out = f"{R}/Section-4-Drafts-Day1-3.pdf"
pdf.output(out); print(out, pdf.pages_count)
