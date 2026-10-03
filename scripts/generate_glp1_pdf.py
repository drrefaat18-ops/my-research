import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class GLP1PDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_margins(22, 20, 22)
        self.set_auto_page_break(auto=True, margin=20)
        
        # Load system Unicode fonts
        font_dir = r"C:\Windows\Fonts"
        self.add_font("Calibri", "", os.path.join(font_dir, "calibri.ttf"))
        self.add_font("Calibri", "B", os.path.join(font_dir, "calibrib.ttf"))
        self.add_font("Calibri", "I", os.path.join(font_dir, "calibrii.ttf"))
        self.add_font("TimesNewRoman", "", os.path.join(font_dir, "times.ttf"))
        self.add_font("TimesNewRoman", "B", os.path.join(font_dir, "timesbd.ttf"))
        self.add_font("TimesNewRoman", "I", os.path.join(font_dir, "timesi.ttf"))

    def header(self):
        self.set_font("Calibri", "I", 8.5)
        self.set_text_color(115, 125, 140)
        self.cell(0, 5, "Rheumatoid Arthritis Drug Repurposing Review — Section 4.1.3", 
                  new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font("Calibri", "B", 8.5)
        self.cell(0, 5, "GLP-1 Receptor Agonists", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(210, 220, 230)
        self.set_line_width(0.3)
        self.line(22, 16.5, 188, 16.5)
        self.ln(5)

    def footer(self):
        self.set_y(-14)
        self.set_draw_color(210, 220, 230)
        self.set_line_width(0.3)
        self.line(22, 283, 188, 283)
        self.set_y(-12)
        self.set_font("Calibri", "", 8)
        self.set_text_color(125, 135, 145)
        self.cell(0, 5, "Faculty of Pharmacy, Port Said University  •  Pharmacology Department", 
                  align="L", new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font("Calibri", "B", 8)
        self.cell(0, 5, f"Page {self.page_no()} of {{nb}}", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

def extract_section_text(source_path):
    with open(source_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_section = False
    paragraphs = []
    
    for line in lines:
        s = line.strip()
        if s == "## 4.1.3. GLP-1 Receptor Agonists":
            in_section = True
            continue
        if s == "## 4.1.4. SGLT2 Inhibitors":
            in_section = False
            break
        if in_section:
            if s.startswith(">") or not s:
                continue
            paragraphs.append(s)
            
    return paragraphs

def build_pdf(source_path, output_pdf_path):
    paragraphs = extract_section_text(source_path)
    
    pdf = GLP1PDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    # Title on page 1
    pdf.set_font("Calibri", "B", 15.5)
    pdf.set_text_color(26, 54, 93) # Academic Navy
    pdf.cell(0, 7, "4.1.3. GLP-1 Receptor Agonists", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Accent underline
    pdf.set_draw_color(43, 108, 176)
    pdf.set_line_width(0.7)
    y_title = pdf.get_y()
    pdf.line(22, y_title, 88, y_title)
    pdf.ln(5.5)

    # Body: Times New Roman 11.5 pt, justified, 1.5 line spacing, blank space between paragraphs
    pdf.set_font("TimesNewRoman", "", 11.5)
    pdf.set_text_color(35, 40, 50)
    line_height = 11.5 * 1.5 * 25.4 / 72 # 1.5 line spacing in mm

    for p in paragraphs:
        # Render _P_ as italic P via markdown support (__P__ in fpdf2)
        p_md = p.replace("_P_", "__P__")
        pdf.multi_cell(0, line_height, p_md, markdown=True, align="J")
        pdf.ln(4.0)

    pdf.output(output_pdf_path)
    print(f"PDF generated successfully at: {output_pdf_path}")

if __name__ == "__main__":
    source_file = r"D:\vault\my research\08 - RA Repurposing Review\drafts\Day3.md"
    output_pdf = r"D:\vault\my research\08 - RA Repurposing Review\Section-4.1.3-GLP1-RA-Review.pdf"
    build_pdf(source_file, output_pdf)
