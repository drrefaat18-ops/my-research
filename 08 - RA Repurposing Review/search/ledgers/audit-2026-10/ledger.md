# Ledger audit-2026-10

## Sources
| id | url_or_path | publisher | kind | origin | published | accessed |
|---|---|---|---|---|---|---|
| S1 | papers/McCarey2004.md | Lancet | primary | McCarey2004 |  | 2026-10-22 |
| S2 | papers/Mostafa2020.md | journal article | primary | Mostafa2020 |  | 2026-10-22 |
| S3 | papers/Dobashi2026.md | abstract only | primary | Dobashi2026 |  | 2026-10-22 |
| S4 | papers/Han2021.md | J Cell Physiol (abstract only) | primary | Han2021 |  | 2026-10-22 |
| S5 | papers/WangQ2025.md | journal article | primary | WangQ2025 |  | 2026-10-22 |
| S6 | papers/Fu2026.md | abstract only | primary | Fu2026 |  | 2026-10-22 |
| S7 | papers/Yu2026.md | J Diabetes Investig | primary | Yu2026 |  | 2026-10-22 |
| S8 | papers/Kitas2019.md | Arthritis Rheumatol | primary | Kitas2019 |  | 2026-10-22 |
| S9 | papers/Kim2015.md | journal article | primary | Kim2015 |  | 2026-10-22 |
| S10 | papers/Kathe2018.md | journal article | primary | Kathe2018 |  | 2026-10-22 |
| S11 | papers/Peterson2021.md | journal article | primary | Peterson2021 |  | 2026-10-22 |

## Claims
| id | claim | status | fact_type | checked | note |
|---|---|---|---|---|---|
| C1 | Day1:51 Placebo-controlled trials with disease activity as primary end point are still needed for statins in RA | contested | stable | 2026-10-22 | TARA already ran one; START-HERE line 197 marks the sentence wrong |
| C2 | Day2:44 Candesartan lowered CRP, IL-1β and TNF-α more than control (post hoc P < 0.05) | unverified | stable | 2026-10-22 | Table III body not in papers/Mostafa2020.md; text gives only the omnibus ANOVA |
| C3 | Day5:33 UTI excess with SGLT2i in the as-treated analysis (aIRR 1.64) | supported | stable | 2026-10-22 | ITT (primary) found no difference; label as-treated as secondary |
| C4 | Day3:48 Han2021 authors inferred higher RA risk from cell experiments | supported | stable | 2026-10-22 | Abstract states the inference but not that it rests on the cell experiments alone |
| C5 | Day3 WangQ2025 5-year thrombotic risk 24% lower with GLP-1 analogs (HR 0.76) | supported | stable | 2026-10-22 | Number matches; it is a hazard ratio over follow-up, not a 5-year risk |
| C6 | Day3:60 Only pioglitazone conferred benefit among antidiabetic classes | supported | stable | 2026-10-22 | Abstract only; doses and species not reported |
| C7 | Day3 GLP-1RA vs DPP-4i all-cause mortality HR 0.68 | supported | stable | 2026-10-22 | |
| C8 | Day1 TRACE RA: no DAS28 difference | supported | stable | 2026-10-22 | |
| C9 | Day3 DPP-4i vs metformin plus non-DPP-4i HR 0.66 for RA | supported | stable | 2026-10-22 | |
| C10 | Day3 DPP-4i not associated with RA (OR 1.16) | supported | stable | 2026-10-22 | rounding of 1.156 |
| C11 | Day1:51 Peterson2021 is a US case-control study | supported | stable | 2026-10-22 | |
| C12 | Day5 No earlier review has considered these three drug classes together in RA with HED and MTX safety | unverified | volatile | 2026-10-22 | novelty claim; no search ledger exists |
| C13 | 60 of 62 high-risk numeric sentences in Day1, Day2, Day3 and Day5 match their papers | supported | stable | 2026-10-22 | Haiku cards; 1 contested (C1 context), 1 unverified (C2) |

## Evidence
| claim | source | passage | not_established |
|---|---|---|---|
| C1 | S1 | "116 patients with rheumatoid arthritis were randomised in a double-blind placebo-controlled trial to receive 40 mg atorvastatin or placebo as an adjunct to existing disease-modifying antirheumatic drug therapy." | that larger or longer trials are unnecessary |
| C2 | S2 | "The three groups were significantly different in the percentage of mean changes for CRP, DAS28, HAQ-DI, IL-1β and TNF-α levels from baseline to the end of the treatment." | a pairwise candesartan versus control test |
| C3 | S3 | "However, AT analysis demonstrated statistically significant association (adjusted incidence rate ratio 1.64, 95% CI 1.26-2.13)." | a difference in the primary ITT analysis |
| C3 | S3 | "ITT analysis showed no significant difference between SGLT2i and other antidiabetic drug." | |
| C4 | S4 | "DPP4 inhibitors sitagliptin and vildagliptin increased proinflammatory cytokine production" | that the risk inference rests only on cell data |
| C5 | S5 | "GLP-1 analogs were associated with a 24% lower risk of all thrombotic events (Hazard ratio (HR), 0.76 [95% CI: 0.70–0.83]; p < 0.0001)" | a fixed 5-year absolute risk |
| C6 | S6 | "Results demonstrate that solely thiazolidinediones (pioglitazone [PIOG]) confer superior efficacy, whereas the other anti-diabetic agents provide minimal or no therapeutic benefits." | doses, species, effect sizes |
| C7 | S7 | "GLP‐1 RA use was associated with lower all‐cause mortality (HR 0.68; 95% confidence intervals (CI), 0.58–0.80)" | causation |
| C8 | S8 | "There were no significant differences between groups in RA disease activity (DAS28), severity (HAQ DI), or quality of life (EQ‐5D)." | |
| C9 | S9 | "with the PS-stratified hazard ratio of 0.66 (95% CI 0.44–0.99) for RA" | comparison with TZD or sulfonylureas |
| C10 | S10 | "DPP-4i therapy was not significantly associated with the development of RA after adjusting for covariates (OR = 1.156, 95% CI 0.936–1.429)." | |
| C11 | S11 | "identified health information for commercially insured and Medicare Advantage beneficiaries" | |
| C13 | S7 | "No significant difference was observed for MACE (HR 0.96; 95% CI, 0.89–1.04)." | the other 59 matches, which are in the Haiku cards (not saved) |
