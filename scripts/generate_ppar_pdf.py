import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PPARExactPDF(FPDF):
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
        self.cell(0, 5, "Rheumatoid Arthritis Drug Repurposing Review — Section 4.1.2", 
                  new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font('Calibri', 'B', 8.5)
        self.cell(0, 5, "PPAR Agonists: Pioglitazone & Fenofibrate", align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
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
        self.cell(0, 5, f"Page {self.page_no()} of {{nb}}", align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

def build_ppar_pdf(output_pdf_path):
    pdf = PPARExactPDF()
    pdf.alias_nb_pages()
    
    # ==================== PAGE 1 ====================
    pdf.add_page()
    
    # Title Block
    pdf.set_font('Calibri', 'B', 15.5)
    pdf.set_text_color(26, 54, 93) # Academic Navy
    pdf.cell(0, 7, "4.1.2. PPAR Agonists: Pioglitazone and Fenofibrate", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    # Accent underline
    pdf.set_draw_color(43, 108, 176)
    pdf.set_line_width(0.7)
    y_title = pdf.get_y()
    pdf.line(22, y_title, 110, y_title)
    pdf.ln(5.5)

    # Paragraphs for Page 1
    p1 = (
        "Pioglitazone, a thiazolidinedione, is a potent ligand of the nuclear receptor PPAR-γ "
        "(peroxisome proliferator-activated receptor-gamma). Although primarily employed as an antidiabetic "
        "agent, it may also possess anti-inflammatory properties. Mechanistically, PPAR-γ activation attenuates "
        "the expression of pro-inflammatory genes, thereby reducing the production of inflammatory cytokines, "
        "matrix metalloproteinases (MMPs), and reactive oxygen species (ROS) [Shahin2011]. A further rationale "
        "is the bidirectional relationship between insulin resistance and inflammation, whereby each process "
        "reinforces the other [Ormseth2013]."
    )
    
    p2 = (
        "In the adjuvant-induced arthritis (AIA) rat model, oral pioglitazone reduced disease severity, but only "
        "at the top dose of 30 mg/kg/day [Koufany2008]. It reduced bone erosions and inflammation-associated "
        "bone loss but failed to prevent cartilage lesions [Koufany2008]. Importantly, these anti-arthritic "
        "doses exceeded those needed to restore insulin sensitivity and were accompanied by increased "
        "adiposity [Koufany2008]. In a later study using the same model, pioglitazone monotherapy (1.35 mg/kg/day) "
        "had no significant effect on disease activity, whereas its combination with methotrexate (MTX; "
        "0.225 mg/kg/day) suppressed disease activity more than either agent alone (P < 0.05) [Roy2017]."
    )
    
    p3 = (
        "At the clinical level, an Egyptian non-randomized, single-blind trial enrolled 49 patients with rheumatoid "
        "arthritis (RA) and type 2 diabetes mellitus, all maintained on MTX 15 mg/week [Shahin2011]. The 28 patients "
        "with more active disease added oral pioglitazone 30 mg/day for 12 weeks, while the other 21 took placebo "
        "[Shahin2011]. Compared with placebo, pioglitazone produced significantly larger reductions in the DAS28 "
        "disease activity score (P = 0.001) and in C-reactive protein (CRP; P < 0.0001), although weight gain was "
        "reported in 25% of treated patients [Shahin2011]."
    )
    
    p4 = (
        "Further evidence came from a US crossover trial that was randomized, double-blind and placebo-controlled, "
        "in which 34 patients with RA on stable therapy received pioglitazone 45 mg/day and placebo for 8 weeks "
        "each [Ormseth2013]. Pioglitazone produced a modest 9.3% reduction in CRP-based DAS28 (P = 0.046) but no "
        "improvement in DAS28 based on the erythrocyte sedimentation rate (ESR) (P = 0.92) [Ormseth2013]. "
        "Lower-extremity edema occurred in 16% of participants while on pioglitazone but in none while on "
        "placebo [Ormseth2013]."
    )

    pdf.set_font('TimesNewRoman', '', 10.5)
    pdf.set_text_color(35, 40, 50)
    
    for p in [p1, p2, p3, p4]:
        pdf.multi_cell(0, 5.3, p)
        pdf.ln(3.5)

    # ==================== PAGE 2 ====================
    pdf.add_page()

    p5 = (
        "A larger crossover trial with the same design and dose enrolled 143 non-diabetic patients with RA, "
        "with 3 months per treatment arm [Marder2013]. DAS28-CRP decreased by a mean of 0.31 on pioglitazone "
        "compared with 0.15 on placebo (P = 0.02) [Marder2013]. Nevertheless, the authors concluded that these "
        "findings did not, at that stage, support adding PPAR-γ agonists to the standard treatment of RA "
        "[Marder2013]. Overall, the observed therapeutic effect was modest and appeared to be driven primarily "
        "by improvements in CRP-based measures rather than by consistent reductions in joint counts. When "
        "weighed against the risks of fluid retention and weight gain, these findings do not support the "
        "routine use of pioglitazone in RA; however, it may warrant further investigation as a selective "
        "adjunctive therapy for patients with coexisting insulin resistance or type 2 diabetes mellitus."
    )
    
    p6 = (
        "Fenofibrate is a widely used PPAR-α agonist prescribed primarily for the treatment of "
        "hypertriglyceridemia [Zhou2012]. In vitro, fenofibrate inhibited Th17-cell differentiation in murine "
        "T cells in a concentration-dependent manner over the range of 5–20 μM, producing a 74% reduction at "
        "20 μM [Zhou2012]. However, other PPAR-α agonists, including WY14643, GW7647, and bezafibrate, had no "
        "effect on Th17-cell differentiation, suggesting that the inhibitory effect of fenofibrate may be "
        "independent of PPAR-α activation [Zhou2012]. In rats with adjuvant-induced arthritis, 12 days of "
        "fenofibrate treatment (300 mg/kg/day) reduced the arthritis score from 11.0 to 5.83, corresponding to "
        "an approximately 47% reduction in the external signs of inflammation (P < 0.01) [Castillero2012]. In "
        "patients with RA, the only clinical data come from one randomized trial in which fenofibrate performed "
        "similarly to a statin on ESR, CRP, and DAS28 [Xing2015]. Placebo-controlled trials are therefore "
        "needed to determine whether these preclinical anti-inflammatory effects translate into meaningful "
        "therapeutic benefits in RA."
    )

    for p in [p5, p6]:
        pdf.multi_cell(0, 5.3, p)
        pdf.ln(3.5)

    # References Block
    pdf.ln(2)
    y_ref = pdf.get_y()
    pdf.set_draw_color(200, 210, 225)
    pdf.set_line_width(0.3)
    pdf.line(22, y_ref, 188, y_ref)
    pdf.ln(3)

    pdf.set_font('Calibri', 'B', 8.5)
    pdf.set_text_color(26, 54, 93)
    pdf.cell(0, 4.5, "References", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    refs = [
        "[Shahin2011] Shahin D, El Toraby E, Abdel-Malek H, et al. Effect of peroxisome proliferator-activated receptor gamma agonist (pioglitazone) and methotrexate on disease activity in rheumatoid arthritis (experimental and clinical study). Clin Med Insights Arthritis Musculoskelet Disord. 2011;4:1-10.",
        "[Ormseth2013] Ormseth MJ, Oeser AM, Cunningham A, et al. Peroxisome proliferator-activated receptor γ agonist effect on rheumatoid arthritis: a randomized controlled trial. Arthritis Res Ther. 2013;15(5):R110.",
        "[Koufany2008] Koufany M, Moulin D, Bianchi A, et al. Anti-inflammatory effect of antidiabetic thiazolidinediones prevents bone resorption rather than cartilage changes in experimental polyarthritis. Arthritis Res Ther. 2008;10(1):R6.",
        "[Roy2017] Roy T, Banerjee I, Ghosh S, et al. Effects of co-treatment with pioglitazone and methotrexate on experimentally induced rheumatoid arthritis in Wistar albino rats. Indian J Pharmacol. 2017;49(2):180-186.",
        "[Marder2013] Marder W, Khalatbari S, Myles JD, et al. The peroxisome proliferator activated receptor-γ pioglitazone improves vascular function and decreases disease activity in patients with rheumatoid arthritis. J Am Heart Assoc. 2013;2(6):e000441.",
        "[Zhou2012] Zhou Z, Sun W, Liang Y, et al. Fenofibrate inhibited the differentiation of T helper 17 cells in vitro. PPAR Res. 2012;2012:145654.",
        "[Castillero2012] Castillero E, Martín AI, Nieto-Bona MP, et al. Fenofibrate administration to arthritic rats increases adiponectin and leptin and prevents oxidative muscle wasting. Endocr Connect. 2012;1(2):77-87.",
        "[Xing2015] Xing B, Yin YF, Zhao LD, et al. Effect of 3-hydroxy-3-methylglutaryl-coenzyme A reductase inhibitor on disease activity in patients with rheumatoid arthritis. Medicine (Baltimore). 2015;94(8):e572."
    ]

    pdf.set_font('TimesNewRoman', '', 7.5)
    pdf.set_text_color(70, 75, 85)
    for r in refs:
        pdf.multi_cell(0, 3.5, r)
        pdf.ln(0.7)

    pdf.output(output_pdf_path)
    print(f"PPAR Agonists exact PDF generated successfully at: {output_pdf_path}")

if __name__ == '__main__':
    pdf_path = r"D:\vault\my research\08 - RA Repurposing Review\Section-4.1.2-PPAR-Agonists-Review.pdf"
    build_ppar_pdf(pdf_path)
