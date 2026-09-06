---
id: "Main-Protocol-7-Groups"
title: "Official Master's Thesis Protocol: Complete Experimental Design, Animal Regimens & Laboratory Procedures"
source_file: "00-Sources/protocol/Protocol.pdf"
category: "Experimental-Protocol"
tags: [animal-protocol, female-wistar-rats, cfa-arthritis, 7-groups, m-pea, prednisolone, tacrolimus, baricitinib, detailed-methods]
qc_status: "PASSED"
qc_auditor: "agency-clinical-evidence-agent"
---

# Official Master's Thesis Experimental Protocol

**Institution:** Department of Pharmacology & Toxicology, Faculty of Pharmacy, Port Said University  
**Researcher:** Dr. Refaat Ibrahim  
**Animal Species:** Female Wistar Rats (*Rattus norvegicus*), adult, healthy  
**Disease Model:** Adjuvant-Induced Arthritis (AA) via Complete Freund's Adjuvant (CFA)  

---

## 1. Experimental Design & Animal Care
- **Housing & Acclimation:** Animals housed under standard laboratory conditions (temperature: $22 \pm 2^\circ\text{C}$, relative humidity: $55 \pm 5\%$, 12-hour light/dark cycle) with *ad libitum* access to standard rodent chow and water. Acclimated for at least 7 days prior to induction.
- **Randomization:** Animals randomly allocated into experimental and control cohorts with baseline weight balancing.

---

## 2. Arthritis Induction Protocol (Day 0)
- **Induction Agent:** Complete Freund's Adjuvant (CFA) containing heat-killed *Mycobacterium tuberculosis* ($1\text{ mg/mL}$).
- **Dose & Route:** Single **0.3 mL subcutaneous injection**.
- **Injection Site:** Right inguinal / proximal thigh region above the right hind limb.
- **Arthritis Latency:** Synovial inflammation, erythema, and paw edema develop progressively over **Days 1–15**.

---

## 3. Confirmed Treatment Regimens & Dosing Matrix (Days 16–45)
Treatments are administered once daily by oral gavage ($p.o.$) for **30 consecutive days** (Day 16 to Day 45 post-induction):

| Group # | Cohort Name | Daily Treatment & Dose | Regimen & Route | Scientific Function & Hypothesis |
|:---:|:---|:---:|:---:|:---|
| **G1** | **Prednisolone Alone** | Prednisolone 10 mg/kg | p.o., daily | Positive standard glucocorticoid control |
| **G2** | **m-PEA Alone** | m-PEA 200 mg/kg | p.o., daily | Full autacoid monotherapy reference |
| **G3** | **Combo Tier 1 (Low)** | m-PEA + Prednisolone (50 + 5 mg/kg) | p.o., daily | Test steroid-sparing threshold at low PEA |
| **G4** | **Combo Tier 2 (Mid)** | m-PEA + Prednisolone (100 + 5 mg/kg) | p.o., daily | Intermediate synergistic evaluation tier |
| **G5** | **Combo Tier 3 (High)** | m-PEA + Prednisolone (200 + 5 mg/kg) | p.o., daily | Maximal synergy & steroid-sparing tier |
| **G6** | **Tacrolimus** | Tacrolimus 1.8 mg/kg | p.o., daily | Calcineurin inhibitor / T-cell active comparator |
| **G7** | **Baricitinib** | Baricitinib 10 mg/kg | p.o., daily | Targeted JAK1/JAK2 inhibitor active comparator |

*(Appropriate healthy vehicle control and CFA-arthritic untreated control groups run in parallel as established in lab records).*

---

## 4. Drug Preparation & Administration
- **m-PEA Preparation:** Prepared from Egyptian commercial **Limitless PEA** tablets. Tablets are finely pulverized using an analytical mortar and pestle to obtain a uniform micronized powder, suspended in vehicle daily prior to oral administration.
- **Prednisolone, Tacrolimus, Baricitinib:** Formulated in appropriate vehicle to guarantee homogenous dosing at constant volume ($1\text{ mL}/100\text{ g}$ body weight).

---

## 5. Sampling, Euthanasia & Laboratory Endpoints (Day 46)
- **Blood Collection:** Animals are anesthetized, and blood is collected via cardiac puncture. Centrifuged at $3000\text{ rpm}$ for 15 minutes at $4^\circ\text{C}$ to separate serum; stored at $-80^\circ\text{C}$.
- **Serum ELISA Assays:**
  * Anti-Citrullinated Protein Antibodies (**ACPA**)
  * Tumor Necrosis Factor-alpha (**TNF-α**)
  * Interleukin-1 beta (**IL-1β**)
  * Interleukin-6 (**IL-6**)
- **Knee Joint Dissection & Histopathology:**
  * Knee joints excised, fixed in $10\%$ neutral buffered formalin, decalcified in $10\%$ EDTA solution, embedded in paraffin wax.
  * Serial sections ($4–5\;\mu\text{m}$) stained with Hematoxylin & Eosin (H&E) and Safranin-O.
  * Microscopic grading of synovial hyperplasia (pannus), leukocyte infiltration, cartilage degradation, and bone erosion.
- **Tissue Molecular Signaling:**
  * **NF-κB p65:** Immunohistochemistry (IHC) on knee joint tissue sections.
  * **p38 MAPK:** Phosphorylated and total p38 MAPK measured by tissue ELISA in joint homogenates.
  * *(Toll-like receptor 4 / TLR4 status subject to confirmation against final completed lab assays).*

---

## 6. Comprehensive Statistical Analysis Plan
- **Normality & Homoscedasticity:** Data assessed for normal distribution using Shapiro-Wilk test, and homogeneity of variance using Levene's test.
- **Parametric Data (ELISA & Paw Volumes):** Expressed as Mean $\pm$ Standard Error of the Mean (SEM). Analyzed using **One-Way Analysis of Variance (ANOVA)** followed by **Tukey's Post-Hoc Test** for all pairwise comparisons, and **Dunnett's Post-Hoc Test** for comparisons against the arthritic control group.
- **Non-Parametric Data (Histological & Arthritis Scores):** Analyzed using the **Kruskal-Wallis test** followed by **Dunn's post-hoc multiple comparison test**.
- **Significance Threshold:** $p < 0.05$ considered statistically significant. Statistical analyses performed using GraphPad Prism software.

---

## 7. Second Brain Cross-References
- Model Selection Rationale: [[AA-vs-CIA-Model-Selection]]
- Dosing Benchmarks: [[PEA-Animal-Dosing-Benchmarks-NFkB]]
- Molecular Cross-Talk: [[PPARa-and-GR-Crosstalk-Axis]]
- Tablet Preparation: [[PEA-Tablet-Preparation]]
- Comparators: [[Tacrolimus-Comparison]] | [[Baricitinib-Comparison]]
- Quarantined Pilot: [[Pilot-Study-Rationale-and-Protocol]]
- Master Dashboard: [[Home-Index]]
