import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class LosartanExactPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_margins(22, 20, 22)
        self.set_auto_page_break(auto=False)
        
        # Load system Unicode fonts
        font_dir = r"C:\Windows\Fonts"
        self.add_font("Calibri", "", os.path.join(font_dir, "calibri.ttf"))
        self.add_font("Calibri", "B", os.path.join(font_dir, "calibrib.ttf"))
        self.add_font("Calibri", "I", os.path.join(font_dir, "calibrii.ttf"))
        self.add_font("TimesNewRoman", "", os.path.join(font_dir, "times.ttf"))
        self.add_font("TimesNewRoman", "B", os.path.join(font_dir, "timesbd.ttf"))
        self.add_font("TimesNewRoman", "I", os.path.join(font_dir, "timesi.ttf"))
        
    def header(self):
        self.set_font('Calibri', 'I', 8.5)
        self.set_text_color(115, 125, 140)
        self.cell(0, 5, "Rheumatoid Arthritis Drug Repurposing Review — Section 4.3", 
                  new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font('Calibri', 'B', 8.5)
        self.cell(0, 5, "ARBs & Losartan", align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
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
        self.set_font('Calibri', '', 8)
        self.set_text_color(125, 135, 145)
        self.cell(0, 5, "Faculty of Pharmacy, Port Said University  •  Pharmacology Department", 
                  align='L', new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font('Calibri', 'B', 8)
        self.cell(0, 5, "Page 1 of 1", align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

def build_exact_pdf(output_pdf_path):
    pdf = LosartanExactPDF()
    pdf.add_page()
    
    # ------------------ TITLE BLOCK ------------------
    pdf.set_font('Calibri', 'B', 15.5)
    pdf.set_text_color(26, 54, 93) # Academic Navy
    pdf.cell(0, 7, "4.3. Angiotensin II Receptor Blockers", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    # Accent underline
    pdf.set_draw_color(43, 108, 176)
    pdf.set_line_width(0.7)
    y_title = pdf.get_y()
    pdf.line(22, y_title, 82, y_title)
    pdf.ln(5)

    # ------------------ EXACT 5 PARAGRAPHS ------------------
    paragraphs = [
        "The renin–angiotensin system (RAS) plays an integral role in blood pressure regulation and fluid homeostasis, and its hyperactivity has been classically linked to hypertension. However, growing evidence suggests a pathological role of RAS in RA, particularly through angiotensin-converting enzyme (ACE), which is overexpressed in the peripheral blood and synovium of RA patients [Wang2013].",
        
        "Angiotensin II stimulates angiotensin II type 1 receptors (AT1R), triggering the generation of reactive oxygen species (ROS) and activation of nuclear factor kappa B (NF-κB), which subsequently promotes the release of multiple pro-inflammatory cytokines [Mostafa2020]. In contrast, angiotensin II type 2 receptors (AT2R) counterbalance AT1R, and their stimulation has been linked to anti-inflammatory and tissue-protective effects [Wang2013].",
        
        "In a preclinical study, adjuvant-induced arthritis (AIA) rats treated with losartan at doses of 10 and 15 mg/kg had a significant reduction in their polyarthritis index compared with vehicle-treated rats, although this improvement was smaller than that seen with methotrexate (MTX) [Wang2013]. Losartan also shifted the balance between the two receptors, with less AT1R and more AT2R in the spleen and synovium, and this shift tracked the fall in the polyarthritis index [Wang2013]. Another study on AIA rats found that losartan lowered serum IL-6 and TNF-α compared with the untreated arthritic group, together with a rise in serum glutathione (GSH) and a fall in serum malondialdehyde (MDA) [AbdelElGaphar2018]. An in vitro study tested losartan, valsartan, and enalapril on peripheral blood mononuclear cells (PBMCs) collected from 16 RA patients. Only losartan clearly lowered four cytokines (IL-6, IL-17F, IL-22, and IFN-γ), while valsartan and enalapril did little, which points to an effect of losartan itself rather than of the whole class [Cardoso2018].",
        
        "The main clinical evidence for this class in RA comes from a trial of another ARB, candesartan. In this Egyptian single-blind, randomized, placebo-controlled trial, 45 patients with RA (15 per group) were treated for 3 months with add-on candesartan (8 mg/day), atorvastatin (20 mg/day), or placebo [Mostafa2020]. Candesartan significantly lowered serum IL-1β, TNF-α, CRP, and erythrocyte sedimentation rate (ESR), and it improved DAS28 and HAQ-DI disability scores compared with both baseline and the control group [Mostafa2020]. However, unlike the antioxidant effect of losartan in rats, candesartan failed to produce significant changes in MDA and rheumatoid factor (RF), whereas atorvastatin significantly lowered both markers [Mostafa2020]. The interpretation of these findings is further limited by baseline imbalances between the groups in several clinical variables and by the small sample size [Mostafa2020].",
        
        "ARBs, particularly losartan, may represent a reasonable antihypertensive option for patients with RA and hypertension; however, larger and longer-term randomized controlled trials, especially those evaluating losartan, are needed to confirm these findings."
    ]

    pdf.set_font('TimesNewRoman', '', 10.5)
    pdf.set_text_color(35, 40, 50)
    
    for p in paragraphs:
        pdf.multi_cell(0, 5.3, p)
        pdf.ln(3.2)

    # ------------------ REFERENCES BLOCK ------------------
    pdf.ln(1)
    y_ref = pdf.get_y()
    pdf.set_draw_color(200, 210, 225)
    pdf.set_line_width(0.3)
    pdf.line(22, y_ref, 188, y_ref)
    pdf.ln(2.5)

    pdf.set_font('Calibri', 'B', 8.5)
    pdf.set_text_color(26, 54, 93)
    pdf.cell(0, 4.5, "References", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    refs = [
        "[Wang2013] Wang D, Hu S, Zhu J, et al. Angiotensin II type 2 receptor correlates with therapeutic effects of losartan in rats with adjuvant-induced arthritis. J Cell Mol Med. 2013;17(11):1459-1469.",
        "[AbdelElGaphar2018] Abdel El-Gaphar OAM, Abo-Youssef AM, Abo-Saif AA. Effect of losartan in complete Freund's adjuvant-induced arthritis in rats. Iran J Pharm Res. 2018;17(4):1395-1408.",
        "[Cardoso2018] Cardoso PRG, Matias KA, Dantas AT, et al. Losartan, but not enalapril and valsartan, inhibits the expression of IFN-γ, IL-6, IL-17F and IL-22 in PBMCs from rheumatoid arthritis patients. Open Rheumatol J. 2018;12:160-170.",
        "[Mostafa2020] Mostafa TM, Hegazy SK, Elshebini EM, et al. A comparative study on the anti-inflammatory effect of angiotensin-receptor blockers & statins on rheumatoid arthritis disease activity. Indian J Med Res. 2020;151(6):538-546."
    ]

    pdf.set_font('TimesNewRoman', '', 7.6)
    pdf.set_text_color(70, 75, 85)
    for r in refs:
        pdf.multi_cell(0, 3.6, r)
        pdf.ln(0.8)

    pdf.output(output_pdf_path)
    print(f"Exact text PDF generated successfully at: {output_pdf_path}")

if __name__ == '__main__':
    pdf_path = r"D:\vault\my research\08 - RA Repurposing Review\Section-4.3-Losartan-Review.pdf"
    build_exact_pdf(pdf_path)
