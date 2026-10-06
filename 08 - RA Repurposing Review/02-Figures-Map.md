---
tags: [review-article, figures]
status: mapped — drawing pending (plan 2026-10-06: all original, Q2)
---

# 🖼️ Figures Map — من الأبحاث للريفيو

> **قاعدة الحقوق (مهمة):**
> - **CC BY** ← مسموح ننقل الـ figure زي ما هي بشرط نكتب تحتها: *"Reproduced from [Author, Year] under CC BY 4.0."*
> - **CC BY-NC / NC-ND / NC-SA** ← مجلة الكلية غالبًا non-commercial، بس الأأمن: **نرسم من جديد** ونكتب *"Adapted from [ref]"* (ND = ممنوع تعديل → ممنوع نقل معدَّل؛ نرسم فكرتنا بس).
> - **الأفضل للمحكّم:** figures **أصلية** (احنا بنرسمها) مبنية على الأبحاث ← ده اللي هنعمله.
>
> **قرار 2026-10-06 (Q2):** الأربعة أصليين، مفيش ولا شكل منقول أو "adapted". الأشكال اللي في الأبحاث مرجع للمعلومة بس.
> **الأداة:** بايثون (matplotlib، موجود) ← PNG/TIFF 600 dpi + SVG/PDF. أيقونات الخلايا من Servier Medical Art (CC BY 4.0) وتحت الشكل: *"Parts of the figure were drawn using Servier Medical Art (smart.servier.com), licensed under CC BY 4.0."* ممنوع BioRender المجاني.
> **المواعيد (START-HERE):** Fig 2 ← 15/10 · Fig 4 ← 17/10 · Fig 1 ← 19/10 · Fig 3 + النسخ النهائية ← 26/10 · الملخص المرسوم ← بعد اختيار المجلة.

---

## Figure 1 — RA pathogenesis & druggable pathways (قسم 3)
**أصلي** (كان adapted) — Ding2023 مرجع للمعلومة بس؛ بيتذكر في النص مش تحت الشكل كـ"Adapted from".

| المصدر | فيه ايه | الرخصة | هناخد منه |
|---|---|---|---|
| Ding2023 Fig 4 (`figs/Ding2023/p5_Im6.jpg`) | الخلايا جوه المفصل: T/B cells، macrophage، FLS، osteoclast + cytokines (IL-1، TNF، IL-6، IL-17، RANKL) + أدوية الـ biologics | CC BY 4.0 | **الهيكل الأساسي** للـ Figure (الخلايا والـ cytokines) |
| Ding2023 Fig 5 (`figs/Ding2023/p6_Im7.jpg`) | الـ signaling pathways: JAK/STAT، PI3K/AKT/mTOR، NF-κB، MAPK، Wnt، Notch + inhibitors | CC BY 4.0 | الـ pathways اللي أدويتنا بتأثر عليها بس: **mTOR، STAT3، NF-κB** |
| Ding2023 Fig 2 (`figs/Ding2023/p3_Im4.jpg`) | RA كمرض systemic (قلب، كلى، ...) + risk factors | CC BY 4.0 | اختياري للـ Intro: فكرة إن RA مرتبط بالـ **cardiometabolic comorbidity** (ده مبرر إعادة توظيف أدوية القلب والسكر) |

**Caption plan:** "Key cellular players and signaling pathways in RA synovium targeted by repurposed drugs." + سطر Servier.

---

## Figure 2 — ⭐ الشكل المركزي: الأدوية المعاد توظيفها بتتقابل على نفس الـ pathways (قسم 4)
**أصلي 100% — ده اللي هيميز الريفيو.** Claude يرسمه من الكروت.

| الدوا | المسار اللي هيترسم | مصدر الفكرة (figure في البحث) |
|---|---|---|
| Metformin | AMPK ↑ → mTOR ↓ → STAT3 ↓ → Th17 ↓ / Treg ↑؛ TRAF6 ↓ → osteoclast ↓ | Son2014 **Fig 6** (schematic، CC BY) · Chen2020 **graphical abstract** (`fx1.jpg`: AMPK → IL-6/IL-1β/TNF ↓، RAPTOR ↓، HAPLN1 ↑؛ CC BY-NC-ND → نرسم بس) |
| Pioglitazone | PPARγ → NF-κB ↓ → cytokines ↓؛ bone resorption ↓ | Koufany2008 Fig 7 (PPAR target genes) |
| Fenofibrate | STAT3 ↓ + IL-21 ↓ → Th17 ↓ (⚠️ ممكن مش عن طريق PPARα) | Zhou2012 **Fig 3–5** |
| Statins | HMG-CoA reductase ↓ → isoprenoids ↓ → Rho/Rac ↓ → NF-κB ↓ | discussion Chodick2010 / ElBarbary2010 (مفيش schematic) |
| ARBs | Ang II → AT1R ⊣ (losartan)؛ AT2R ↑ | Wang2013 Fig 1–6 |
| Dapagliflozin | AMPK ↑ → autophagy ↑ + Hedgehog (Shh/Gli-1) ↓ + apoptosis of synovial cells | ElDemerdash2025 Fig 1 (study design) + Fig 2–9 (data) |
| GLP-1 RA | GLP-1R → ? (mechanism غير مؤكد في أبحاثنا) — **خط منقط** | Israel2026 discussion |

**Caption plan:** "Convergence of repurposed cardiometabolic drugs on shared inflammatory pathways in RA. Solid lines: preclinical evidence in arthritis models; dashed lines: proposed/indirect evidence."

---

## Figure 3 — Evidence map (قسم 5 Challenges)
**أصلي** — heat-map/bubble: الدوا × مستوى الدليل (in vitro · animal · observational · RCT)، واللون = الاتجاه (✅ إيجابي · ⚪ محايد · ❌ سلبي/متضارب). البيانات من "Table 1 rows" في كل ملف قسم.

> مثال: Statins → RCT ⚪ (TRACE RA: CRP ↓ بس DAS28 ماتغيرش) · cohort ⚪/❌ متضارب · animal ❌ (Vandebriel2012)

---

## Figure 4 — Literature search and selection (قسم 2 Methods)
**أصلي** — مخطط بسيط: عدد النتايج لكل قاعدة بيانات ← بعد حذف التكرار ← بعد الفرز ← الدراسات المذكورة في الريفيو، لكل دوا. الأعداد من `search/search-log.md` + `papers/`.

## Graphical abstract (بعد اختيار المجلة)
نسخة مبسطة من Figure 2 على مقاس المجلة.

---

## Data figures (مش هننقلها — بس مفيدة ليك)
الـ bar charts والـ histology في الأبحاث (مثلًا ElDemerdash2025 Fig 9: caspase-3/9، p53، Bax/Bcl2) **ماتنقلهاش** — ريفيو مش بيعيد رسم نتايج. استخدمها بس عشان **تفهم** الرقم اللي في الإملاء.

---

## 📋 Inventory — كل الـ figures (من الـ XML)
| Paper | Fig | File | License | Caption (short) |
|---|---|---|---|---|
| AbdelElGaphar2018 | Figure 1 | `figs/AbdelElGaphar2018/ijpr-17-1420-g001.jpg` |  | Photomicrographs for joint sections stained with H& E |
| AbdelElGaphar2018 | Figure 2 | `figs/AbdelElGaphar2018/ijpr-17-1420-g002.jpg` |  | Photographs of joints demonstrating macroscopical changes |
| Cardoso2018 | Fig. (1) | `figs/Cardoso2018/TORJ-12-160_F1.jpg` | CC BY |  |
| Cardoso2018 | Fig. (2) | `figs/Cardoso2018/TORJ-12-160_F2.jpg` | CC BY |  |
| Castillero2012 | Figure 1 | `figs/Castillero2012/ec-01-01-g001.jpg` | CC BY | Serum concentrations of adiponectin (A), leptin (B), resistin (C), and insulin (D) in control (C), arthritic ( |
| Castillero2012 | Figure 2 | `figs/Castillero2012/ec-01-01-g002.jpg` | CC BY | Effect of arthritis and fenofibrate (300 mg/kg) on soleus weight (A), mean fiber area (B), and cross-sectional |
| Castillero2012 | Figure 3 | `figs/Castillero2012/ec-01-01-g003.jpg` | CC BY | Effect of arthritis and fenofibrate (300 mg/kg) on Pparα (A) and Tnf (B) mRNA in soleus. AA, arthritic rats; P |
| Castillero2012 | Figure 4 | `figs/Castillero2012/ec-01-01-g004.jpg` | CC BY | Effect of arthritis and fenofibrate (300 mg/kg) on Murf1 (A) and ATROGIN1 (B) mRNA in soleus. AA, arthritic ra |
| Castillero2012 | Figure 5 | `figs/Castillero2012/ec-01-01-g005.jpg` | CC BY | Effect of arthritis and fenofibrate (300 mg/kg) on myostatin mRNA (A) and protein (B) in soleus. AA, arthritic |
| Castillero2012 | Figure 6 | `figs/Castillero2012/ec-01-01-g006.jpg` | CC BY | Effect of arthritis and fenofibrate treatment (300 mg/kg) on soleus MyoD (A and B) and myogenin (C and D) mRNA |
| Chen2020 |  | `figs/Chen2020/fx1.jpg` | CC BY-NC-ND |  |
| Chen2020 | Figure 1 | `figs/Chen2020/gr1.jpg` | CC BY-NC-ND | Expression of Serum AMPK-α1 and p-AMPK-α1 Levels in RA and OA Patients(A) AMPK-α1 levels between RA (n = 61) a |
| Chen2020 | Figure 2 | `figs/Chen2020/gr2.jpg` | CC BY-NC-ND | Changes in the Metabolic Pathway in RA Compared to OA Synovium(A) In total, 119 DEGs between RA and OA patient |
| Chen2020 | Figure 3 | `figs/Chen2020/gr3.jpg` | CC BY-NC-ND | DEGs in FLSs Identified by mRNA High-Throughput Sequencing Method(A) In total, 111 DEGs were identified in RA- |
| Chen2020 | Figure 4 | `figs/Chen2020/gr4.jpg` | CC BY-NC-ND | Effect of AMPK Modulators on RA-FLS Proliferation(A) An MTT assay was used to determine the effects of metform |
| Chen2020 | Figure 5 | `figs/Chen2020/gr5.jpg` | CC BY-NC-ND | AMPK Modulators Inhibited Migration of RA-FLSs(A) A scratch test was performed to evaluate the effects of metf |
| Chen2020 | Figure 6 | `figs/Chen2020/gr6.jpg` | CC BY-NC-ND | Metformin Inhibited Inflammatory Cytokines by Promoting AMPKExpression levels of inflammatory cytokines were m |
| Chen2020 | Figure 7 | `figs/Chen2020/gr7.jpg` | CC BY-NC-ND | Metformin Promoted HAPLN1 in the PKA-α1/RUNX1/RUNX2 PathwayRelative HAPLN1 expression levels were measured aft |
| Chodick2010 | Figure 1 | `figs/Chodick2010/pmed.1000336.g001.jpg` | CC BY | Incidence density rate (per 1,000 person-years) of RA and OA in study cohort, by age and sex, 1998–2006. |
| Chodick2010 | Figure 2 | `figs/Chodick2010/pmed.1000336.g002.jpg` | CC BY | Adjusted HR and 95% CI for RA and OA, according to PDC with statins in patients with at least 5 y of follow-up |
| Chodick2010 | Figure 3 | `figs/Chodick2010/pmed.1000336.g003.jpg` | CC BY | Proportional effects of persistence with statins on reduction of risk for RA per 10% of follow-up days covered |
| ElDemerdash2025 | Fig. 1 | `figs/ElDemerdash2025/10787_2025_1750_Fig1_HTML.jpg` | CC BY | Experimental design summary showing the timeline for induction and drug administration of phase II |
| ElDemerdash2025 | Fig. 2 | `figs/ElDemerdash2025/10787_2025_1750_Fig2_HTML.jpg` | CC BY | Effect of different doses of DAPA (1, 5, 10mg/kg/day) in CFA-induced arthritic rats. A Photographs of rats’ hi |
| ElDemerdash2025 | Fig. 3 | `figs/ElDemerdash2025/10787_2025_1750_Fig3_HTML.jpg` | CC BY | Photomicrographs of H&E-stained hind paw sections showing the effect of different doses of DAPA (1, 5, 10 mg/k |
| ElDemerdash2025 | Fig. 4 | `figs/ElDemerdash2025/10787_2025_1750_Fig4_HTML.jpg` | CC BY | Effect of MTX and/or DAPA (10 mg/kg/day) in CFA-induced arthritic rats. A Photographs of the rat’s hind paws.  |
| ElDemerdash2025 | Fig. 5 | `figs/ElDemerdash2025/10787_2025_1750_Fig5_HTML.jpg` | CC BY | Photomicrographs of hind paw sections of arthritic rats treated with MTX and/or DAPA (10 mg/kg/day) stained by |
| ElDemerdash2025 | Fig. 6 | `figs/ElDemerdash2025/10787_2025_1750_Fig6_HTML.jpg` | CC BY | Effect of MTX and/or DAPA (10 mg/kg/day) on inflammatory markers in CFA-induced arthritic rats. A NF-κB p65 se |
| ElDemerdash2025 | Fig. 7 | `figs/ElDemerdash2025/10787_2025_1750_Fig7_HTML.jpg` | CC BY | Effect of MTX and/or DAPA (10 mg/kg/day) on articular gene expression of autophagic markers in CFA-induced art |
| ElDemerdash2025 | Fig. 8 | `figs/ElDemerdash2025/10787_2025_1750_Fig8_HTML.jpg` | CC BY | Effect of MTX and/or DAPA (10 mg/kg/day) on articular gene expression of Hedgehog signaling pathway markers in |
| ElDemerdash2025 | Fig. 9 | `figs/ElDemerdash2025/10787_2025_1750_Fig9_HTML.jpg` | CC BY | Effect of MTX and/or DAPA (10 mg/kg/day) on apoptotic markers and articular gene expression of p53 in CFA-indu |
| Fan2020 | Figure 1 | `figs/Fan2020/atm-08-23-1565-f1.jpg` | CC BY-NC-ND | Protective effect of MF on CIA rats. (A) Representative images of paw swelling in the normal, CIA, and MF grou |
| Fan2020 | Figure 2 | `figs/Fan2020/atm-08-23-1565-f2.jpg` | CC BY-NC-ND | Effects of MF on arthritis and systemic inflammation in CIA rats. Representative knee joint sections stained w |
| Fan2020 | Figure 3 | `figs/Fan2020/atm-08-23-1565-f3.jpg` | CC BY-NC-ND | Effects of MF on joint bone erosion in CIA rats. Reconstructed 3D micro-CT images of knee joints of the normal |
| Fan2020 | Figure 4 | `figs/Fan2020/atm-08-23-1565-f4.jpg` | CC BY-NC-ND | Effect of MF on osteoblasts in joints of CIA rats. Representative knee joint sections stained with hematoxylin |
| Fan2020 | Figure 5 | `figs/Fan2020/atm-08-23-1565-f5.jpg` | CC BY-NC-ND | Effect of MF on osteoclasts in joints of CIA rats. Representative knee joint sections stained with TRAP. Compa |
| Fan2020 | Figure 6 | `figs/Fan2020/atm-08-23-1565-f6.jpg` | CC BY-NC-ND | Effect of MF on cartilage in joints of CIA rats. Representative knee joint sections stained with Alcian blue ( |
| Fan2020 | Figure 7 | `figs/Fan2020/atm-08-23-1565-f7.jpg` | CC BY-NC-ND | Effects of MF on ADAMTS-5 (A), MMP-9 (B) in cartilage of the knee joints in CIA rats. Representative knee join |
| Gharib2021 | FIGURE 1 | `figs/Gharib2021/fphar-12-726490-g001.jpg` | OA (see paper) | The study flow chart. *DMARDs: disease modifying anti-rheumatic drugs. |
| Gharib2021 | FIGURE 2 | `figs/Gharib2021/fphar-12-726490-g002.jpg` | OA (see paper) | Boxplot of serum adiponectin levels of control group (n = 30), and metformin group (n = 30) at baseline, and a |
| Israel2026 | Figure 1. | `figs/Israel2026/10.1177_1759720X261425441-fig1.jpg` | CC BY-NC | Physiological role of GLP-1 and its impact on body weight.GI, gastrointestinal; GLP-1, glucagon-like peptide 1 |
| Israel2026 | Figure 2. | `figs/Israel2026/10.1177_1759720X261425441-fig2.jpg` | CC BY-NC | Study population.csDMARD, conventional synthetic disease-modifying antirheumatic drug; GI, gastrointestinal; G |
| Israel2026 | Figure 3. | `figs/Israel2026/10.1177_1759720X261425441-fig3.jpg` | CC BY-NC | Multivariate analysis of GLP-1RA use up to 10 years prior to RA diagnosis. Forest plots displaying multivariab |
| Israel2026 | Figure 4. | `figs/Israel2026/10.1177_1759720X261425441-fig4.jpg` | CC BY-NC | Pro- and anti-inflammatory properties of GLP-1 receptor agonists.APC, antigen-presenting cell; CD, cluster of  |
| Kitas2019 | Figure 1 | `figs/Kitas2019/ART-71-1437-g001.jpg` | CC BY | Trial profile. A total of 3,002 patients from 102 UK rheumatology centers were randomized in the Trial of Ator |
| Kitas2019 | Figure 2 | `figs/Kitas2019/ART-71-1437-g002.jpg` | CC BY | Kaplan‐Meier plots of time to first cardiovascular event (CVE) for patients in the atorvastatin and placebo gr |
| Kitas2019 | Figure 3 | `figs/Kitas2019/ART-71-1437-g003.jpg` | CC BY | Cumulative incidence of first cardiovascular event (CVE) for patients in the atorvastatin and placebo groups.  |
| Koufany2008 | Figure 1 | `figs/Koufany2008/ar2354-1.jpg` | CC BY | Modulation of body weight gain by rosiglitazone and pioglitazone in the course of adjuvant-induced arthritis.  |
| Koufany2008 | Figure 2 | `figs/Koufany2008/ar2354-2.jpg` | CC BY | Modulation of body temperature and locomotive activity by rosiglitazone and pioglitazone treatment during adju |
| Koufany2008 | Figure 3 | `figs/Koufany2008/ar2354-3.jpg` | CC BY | Modulation of disease severity by rosiglitazone and pioglitazone treatment during adjuvant-induced arthritis.  |
| Koufany2008 | Figure 4 | `figs/Koufany2008/ar2354-4.jpg` | CC BY | Effect of rosiglitazone and pioglitazone treatment on cartilage changes in arthritic knees. Animals were treat |
| Koufany2008 | Figure 5 | `figs/Koufany2008/ar2354-5.jpg` | CC BY | Effect of rosiglitazone and pioglitazone treatment on histological grading of ankle lesions during adjuvant-in |
| Koufany2008 | Figure 6 | `figs/Koufany2008/ar2354-6.jpg` | CC BY | Effect of rosiglitazone and pioglitazone treatment on dual-energy X-ray absorptiometry changes during adjuvant |
| Koufany2008 | Figure 7 | `figs/Koufany2008/ar2354-7.jpg` | CC BY | Effect of rosiglitazone and pioglitazone treatment on expression of PPAR target genes during adjuvant-induced  |
| Liang2023 | Figure 1 | `figs/Liang2023/jcm-12-02461-g001.jpg` | CC BY | Workflow of the study. GWAS, genome-wide association study; IVs, instrumental variables; IVW, inverse variance |
| Liang2023 | Figure 2 | `figs/Liang2023/jcm-12-02461-g002.jpg` | CC BY | Diagram for Mendelian randomization (MR). MR is based on three hypotheses. First of all, SNPs identified as IV |
| Liang2023 | Figure 3 | `figs/Liang2023/jcm-12-02461-g003.jpg` | CC BY | (A) Scatter plot of the effects of genetic variants on the metformin treatment and RA. The slopes of the solid |
| Marder2013 | Figure 1. | `figs/Marder2013/jah3-2-e000441-g1.jpg` | OA (see paper) | Study population recruitment summary. |
| Marder2013 | Figure 2. | `figs/Marder2013/jah3-2-e000441-g2.jpg` | OA (see paper) | Change in various CV measures and inflammatory markers during study. Mean change is plotted over time between  |
| Mostafa2020 | Figure | `figs/Mostafa2020/IJMR-152-393-g001.jpg` | CC BY-NC-SA | Flowchart showing study design. |
| Ormseth2013 | Figure 1 | `figs/Ormseth2013/ar4290-1.jpg` | CC BY | Randomized, placebo-controlled, crossover trial design. Patients were screened for eligibility. Those meeting  |
| Ormseth2013 | Figure 2 | `figs/Ormseth2013/ar4290-2.jpg` | CC BY | Randomization and follow-up of study participants. A total of 34 patients with rheumatoid arthritis (RA) were  |
| Ormseth2013 | Figure 3 | `figs/Ormseth2013/ar4290-3.jpg` | CC BY | Rheumatoid arthritis disease activity measured by Disease Activity Score in 28 joints score is decreased by pi |
| Peterson2021 | Fig. 1 | `figs/Peterson2021/13075_2021_2617_Fig1_HTML.jpg` | CC BY | Study design for RA case and control selection. RA rheumatoid arthritis, DMARD disease-modifying antirheumatic |
| Peterson2021 | Fig. 2 | `figs/Peterson2021/13075_2021_2617_Fig2_HTML.jpg` | CC BY | Study population flow diagram. E&M evaluation and management, RA rheumatoid arthritis, MTX methotrexate, DMARD |
| Ren2023 | Figure 1. | `figs/Ren2023/medi-102-e35088-g001.jpg` | OA (see paper) | Flow diagraph of identification process for eligible studies. |
| Ren2023 | Figure 2. | `figs/Ren2023/medi-102-e35088-g002.jpg` | OA (see paper) | The risk of bias and quality of RCT. RCT = randomized clinical trial. |
| Ren2023 | Figure 3. | `figs/Ren2023/medi-102-e35088-g003.jpg` | OA (see paper) | The forest graph of DAS28 in statins versus placebo. The total standardized mean difference was −0.78, 95% CI  |
| Ren2023 | Figure 4. | `figs/Ren2023/medi-102-e35088-g004.jpg` | OA (see paper) | Subgroup analysis according to the type of statins (A), continent (B) and DAS28 baseline (C). (A) showed that  |
| Ren2023 | Figure 5. | `figs/Ren2023/medi-102-e35088-g005.jpg` | OA (see paper) | Sensitivity analysis on the effect of statins on DAS28 in RA patients. It indicated the overall effect has not |
| Roy2017 | Figure 1 | `figs/Roy2017/IJPharm-49-168-g004.jpg` | CC BY-NC-SA | Radiological images of (a) hind paw of normal rat (b) hind paw of arthritis rat (c) X-ray of hind paw of norma |
| Roy2017 | Figure 2 | `figs/Roy2017/IJPharm-49-168-g005.jpg` | CC BY-NC-SA | Histopathology of joint of rat belonging to (a) normal control group (b) arthritis control group (c) pioglitaz |
| Sarabi2016 | Figure 1 | `figs/Sarabi2016/EPJ-08-2700-g001.jpg` | OA (see paper) | CONSORT flow diagram of the trial |
| Sarabi2016 | Figure 2 | `figs/Sarabi2016/EPJ-08-2700-g002.jpg` | OA (see paper) | Serologic findings (inflammatory markers) |
| Shahin2011 | Figure 1. | `figs/Shahin2011/cmamd-2011-001f1.jpg` | OA (see paper) | Effect of methotrexate (0.1 mg/kg) and pioglitazone (30 mg/kg) combination on the arthritic index of CIA rats. |
| Son2014 | Figure 1 | `figs/Son2014/MI2014-973986.001.jpg` | CC BY | Therapeutic effects of metformin in CIA model. CIA was induced in C57BL/6 mice. Metformin 5 mg/mice (n = 10) o |
| Son2014 | Figure 2 | `figs/Son2014/MI2014-973986.002.jpg` | CC BY | Regulation of Th17 cells and Foxp3+ regulatory T cells in CIA spleen. Spleen tissue was obtained from metformi |
| Son2014 | Figure 3 | `figs/Son2014/MI2014-973986.003.jpg` | CC BY | Treatment with metformin Treg cells and decreases Th17 cells in CIA mice and in vitro Th17 polarizing conditio |
| Son2014 | Figure 4 | `figs/Son2014/MI2014-973986.004.jpg` | CC BY | Metformin inhibits osteoclast formation in CIA mice. (a) Joint tissues of CIA control mice (n = 5) and metform |
| Son2014 | Figure 5 | `figs/Son2014/MI2014-973986.005.jpg` | CC BY | Metformin suppresses osteoclastogenesis in vitro. C57BL/6 mice preosteoclasts were cultured in the presence of |
| Son2014 | Figure 6 | `figs/Son2014/MI2014-973986.006.jpg` | CC BY | The signaling pathway that metformin uses to regulate T cell and osteoclasts in autoimmune arthritis. |
| TejeraSegura2017 | Fig. 1 | `figs/TejeraSegura2017/13075_2017_1431_Fig1_HTML.jpg` | CC BY | Meal test curves of glucose, insulin, C-peptide, gastric inhibitory polypeptide, and glucagon-like peptide 1 c |
| Vandebriel2012 | Figure 1 | `figs/Vandebriel2012/ar3814-1.jpg` | CC BY | Scheme of collagen-induced arthritis induction and statin administration. Mice were immunized at day 0 (IMM) a |
| Vandebriel2012 | Figure 2 | `figs/Vandebriel2012/ar3814-2.jpg` | CC BY | Effect of collagen-induced arthritis induction and statin treatment on body weight. Mice were immunized at day |
| Vandebriel2012 | Figure 3 | `figs/Vandebriel2012/ar3814-3.jpg` | CC BY | Effect of statin treatment on arthritis incidence and score. (A) Number of arthritic animals per group versus  |
| Vandebriel2012 | Figure 4 | `figs/Vandebriel2012/ar3814-4.jpg` | CC BY | Statin administration accelerates arthritis onset (fraction of arthritic animals versus time). Mice were immun |
| Vandebriel2012 | Figure 5 | `figs/Vandebriel2012/ar3814-5.jpg` | CC BY | Anti-collagen type II IgG levels. Mice were immunized at day 0 and challenged at day 21. Atorvastatin (A) or p |
| Vandebriel2012 | Figure 6 | `figs/Vandebriel2012/ar3814-6.jpg` | CC BY | Cytokine production by lymph node and spleen cells. (A) IL-2 production by Concanavalin-A (Con A)-stimulated i |
| Wang2013 | Figure 1 | `figs/Wang2013/jcmm0017-1577-f1.jpg` | CC BY | Losartan ameliorated the polyarthritis index in adjuvant-induced arthritis (AIA) rats. The secondary polyarthr |
| Wang2013 | Figure 2 | `figs/Wang2013/jcmm0017-1577-f2.jpg` | CC BY | Losartan ameliorated the histological manifestation of arthritis in adjuvant-induced arthritis (AIA) rats. Nor |
| Wang2013 | Figure 3 | `figs/Wang2013/jcmm0017-1577-f3.jpg` | CC BY | Losartan decreased the production of tumour necrosis factor-α (TNF-α), VEGF and angiotensin II. Treatment with |
| Wang2013 | Figure 4 | `figs/Wang2013/jcmm0017-1577-f4.jpg` | CC BY | Losartan decreased angiotensin II type 1 receptor (AT1R) expression and up-regulated AT2R expression. AT1R and |
| Wang2013 | Figure 5 | `figs/Wang2013/jcmm0017-1577-f5.jpg` | CC BY | Angiotensin II type 1 receptor (AT1R) and AT2R expression in monocytes cultured in vitro. The western blot res |
| Wang2013 | Figure 6 | `figs/Wang2013/jcmm0017-1577-f6.jpg` | CC BY | The effects of CGP42112 on monocytes cultured in vitro. The IC50 value of CGP42112 was 5.21 × 10−6 M (A). Trea |
| Wang2013 | Figure 7 | `figs/Wang2013/jcmm0017-1577-f7.jpg` | CC BY | The therapeutic effects of CGP42112 on adjuvant-induced arthritis (AIA) rats in vivo. Intra-articular injectio |
| Xing2015 | FIGURE 1 | `figs/Xing2015/medi-94-e572-g001.jpg` | CC BY-NC-ND | Flowchart of the study selection.∗3 of them have only abstracts available. |
| Xing2015 | FIGURE 2 | `figs/Xing2015/medi-94-e572-g003.jpg` | CC BY-NC-ND | Forest graph of the meta-analysis of the effect of statins versus placebo on DAS28 in RA patients. The pooled  |
| Xing2015 | FIGURE 3 | `figs/Xing2015/medi-94-e572-g004.jpg` | CC BY-NC-ND | Subgroup analysis based on type of statin (A) and disease activity (B). A. Atorvastatin produced a greater red |
| Xing2015 | FIGURE 4 | `figs/Xing2015/medi-94-e572-g006.jpg` | CC BY-NC-ND | Sensitivity analysis on the effect of statins versus placebo on DAS28 in RA patients. The results show that om |
| Xing2015 | FIGURE 5 | `figs/Xing2015/medi-94-e572-g007.jpg` | CC BY-NC-ND | Overall analysis of publication bias on the effect of statins versus placebo on DAS28 in RA patients. Egger li |
| Yen2026 | Figure 1 | `figs/Yen2026/fimmu-17-1867117-g001.jpg` | OA (see paper) | Selection process (SGLT2i vs. sulfonylureas). T2DM, type 2 diabetes mellitus; SGLT2i: Sodium-glucose Cotranspo |
| Yen2026 | Figure 2 | `figs/Yen2026/fimmu-17-1867117-g002.jpg` | OA (see paper) | Kaplan-Meier curve for rheumatoid arthritis. |
| Yen2026 | Figure 3 | `figs/Yen2026/fimmu-17-1867117-g003.jpg` | OA (see paper) | Forest plot of the subgroup analyses. SGLT2i, Sodium-glucose Cotransporter-2 Inhibitors; HbA1c, hemoglobin A1C |
| Zemedikun2021 |  | `figs/Zemedikun2021/keab148f1.jpg` | CC BY | Forest plot summarizing aHRs of glycaemic control and associated therapies on the risk of RA using time-depend |
| Zhang2023 | Fig. 1 | `figs/Zhang2023/40001_2023_1476_Fig1_HTML.jpg` | CC BY | Expression of HMGB1, inflammatory factors and T cell subtypes in RA patients |
| Zhang2023 | Fig. 2 | `figs/Zhang2023/40001_2023_1476_Fig2_HTML.jpg` | CC BY | Comparisons of HMGB1 and inflammatory factors between two groups. *P < 0.05 compared between metformin group a |
| Zhang2023 | Fig. 3 | `figs/Zhang2023/40001_2023_1476_Fig3_HTML.jpg` | CC BY | VAS scores and the expression of T cell subtypes in RA patients after metformin treatment |
| Zhang2023 | Fig. 4 | `figs/Zhang2023/40001_2023_1476_Fig4_HTML.jpg` | CC BY | ROC curves for HMGB1 in diagnostic of RA patients in active phase |
| Zhou2012 | Figure 1 | `figs/Zhou2012/PPAR2012-145654.001.jpg` | OA (see paper) | Fenofibrate inhibited the differentiation of Th17 cells in vitro. (a) Total T cells were isolated from mouse s |
| Zhou2012 | Figure 2 | `figs/Zhou2012/PPAR2012-145654.002.jpg` | OA (see paper) | The effect of fenofibrate on Th17 cell differentiation did not involve changes of IFN-γ and IL-4 secretion. To |
| Zhou2012 | Figure 3 | `figs/Zhou2012/PPAR2012-145654.003.jpg` | OA (see paper) | WY14643, GW7647, and bezafibrate did not inhibit the differentiation of Th17 cells. Total T cells and CD4+ T c |
| Zhou2012 | Figure 4 | `figs/Zhou2012/PPAR2012-145654.004.jpg` | OA (see paper) | Fenofibrate reduced IL-21 production in the Th17 differentiation system. Total T cells were isolated from mous |
| Zhou2012 | Figure 5 | `figs/Zhou2012/PPAR2012-145654.005.jpg` | OA (see paper) | Fenofibrate reduced the activation of STAT3 in the Th17 differentiation system. (a) Total T cells were isolate |
| vanBoheemen2021 | Figure 1 | `figs/vanBoheemen2021/rmdopen-2021-001591f01.jpg` | CC BY-NC | STAPRA study flow chart. STAPRA, STAtins to Prevent Rheumatoid Arthritis. |
| vanBoheemen2021 | Figure 2 | `figs/vanBoheemen2021/rmdopen-2021-001591f02.jpg` | CC BY-NC | Kaplan-Meier arthritis-free survival curves of atorvastatin and placebo groups by intention-to-treat analysis. |
