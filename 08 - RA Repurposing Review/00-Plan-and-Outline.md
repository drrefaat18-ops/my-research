---
tags: [review-article, RA, repurposing]
target: Q2 international journal (chosen by Dr. Ahmed Morad after delivery)
deadline: 2026-11-08
status: writing
updated: 2026-10-07
---

# RA Drug Repurposing Review — Plan

> ⚠️ The ODR plan (4,500 words, 45–55 refs, OA-only, deadline 2026-10-06) is **obsolete**. Daily steps live in [[START-HERE]]; this file holds the targets and the outline.

**Title:** Old Drugs, New Targets: Repurposing Cardiometabolic Agents for Rheumatoid Arthritis
**Type:** narrative review with a structured, reproducible literature search (Methods + Figure 4 search overview). Never call it "systematic" or "semi-systematic" in the manuscript; quality checklist = SANRA (Baethge 2019).

## Fixed targets
| Item | Target | Status 2026-10-07 |
|---|---|---|
| Words (body, no refs/tables) | 6,500–7,000 | ~3,430 (drug sections only) |
| Unique references | ≥ 80 | 35 cited · 56 in `papers/` |
| Recent refs (year ≥ 2021, `cite_check.py`) | ≥ 40% | 11/35 = 31% |
| Figures | 4 original + graphical abstract | 0 final |
| Tables | 3 | 0 final |
| Overlap / AI detectors | 0% / ≤ 20% each | Day1–3 pass |

## Source rules
- Every specific study cited to its own paper, saved in `papers/` (open access or EKB download).
- Mechanism claims cited to mechanistic (lab) papers or mechanism reviews — never to cohort, case–control or outcome-trial papers.
- Every animal dose is followed by its human equivalent dose (HED table in [[study-cards]]; method ref Nair & Jacob 2016).
- Cohort/case–control results worded "associated with", never "reduced".

## Outline, word budget, reference budget
"Have" = already cited in drafts or saved in `papers/` and assigned. "New" = still to find/screen.

| # | Section | Words now | Words target | Refs have | Refs new | Refs total |
|---|---|---|---|---|---|---|
| — | Abstract + keywords | 0 | 250 | — | — | 0 |
| 1 | Introduction (burden → DMARD limits → repurposing → gap in prior reviews → aim) | 0 | 700 | 3 (GBD2023, Nagy2021, Gao2024) + 3 prior reviews found 2026-10-07 (Alshammari2026, Nallathambi2024, Buonanno2026) | ~5 | ~11 |
| 2 | Methods (databases, dates, terms, criteria, counts) | 0 | 300 | — | ~1 | ~1 |
| 3 | Pathophysiology + druggable pathways (Fig 1) | 0 | 700 | 2 (Ding2023, Kondo2021) — Malemud2013 dropped (OMICS, predatory) | ~7 | ~9 |
| 4.1 | Antidiabetics intro | 54 | 60 | 1 | — | 1 |
| 4.1.1 | Metformin | 548 | 650 | 7 + Abdallah2021, Naffaa2020, Qin2023 (+ Alshammari2026 re-cited) | HED ref | ~11 |
| 4.1.2 | Pioglitazone | 478 | 550 | 5 + Hsieh2021, Ormseth2014 | — | 7 |
| 4.1.3 | GLP-1 RAs | 453 | 550 | 3 + WangQ2025, Buonanno2026 (re-cite) | ~2 (Zheng2019 mechanism, EKB + 1 recent human) | ~6 |
| 4.1.4 | SGLT2 inhibitors | 340 | 450 | 2 | ~3 recent | ~5 |
| 4.1.5 | DPP-4 inhibitors (moved from 4.4) | (in 4.4) | 150 | 1 (Kathe2018) | ~1 | ~2 |
| 4.2 | Lipid-lowering intro | 44 | 50 | Hansildaar2021 (replaces Kitas2019 here) | — | 1 |
| 4.2.1 | Statins | 426 | 650 | 7 + McCarey2004, Tang2011, Hu2024 | ~1 mechanism | ~11 |
| 4.2.2 | Fenofibrate | 109 | 250 | 2 + Goto2010, Shirinsky2013 | — | 4 |
| 4.3 | ARBs | 456 | 500 | 4 | ~1 | ~5 |
| 4.4 | Emerging candidates (1 sentence + Table 2) | 286 | 80 | 4 (in Table 2) | — | 4 |
| 4.5 | Comparative synthesis (NEW) | 0 | 250 | re-cites | ~1 | ~1 |
| 5 | Challenges: safety/interactions with MTX & steroids (NEW), trial design, dose gap, review limits | 0 | 600 | — | ~8 | ~8 |
| 6 | Conclusion | 0 | 150 | — | — | 0 |
| | **Total** | **~3,430** | **~6,890** | **~55** | **~31** | **~86** |

### Recency budget
- Recent (≥ 2021) now: 11. Planned additions already in hand: Abdallah2021, Hu2024, Hsieh2021, Qin2023, Hansildaar2021, GBD2023, Nagy2021, Gao2024, Ding2023, Kondo2021, Alshammari2026, Nallathambi2024, Buonanno2026, WangQ2025 → **25** (2026-10-07 audit + similar-work read).
- 40% of ~86 = 35 → **at least 10 of the ~31 new refs must be 2021 or later** (priority: GLP-1/SGLT2 human studies, Egyptian burden/cost data, safety data).
- Checkpoints: START-HERE item 11 (after drug sections) and item 22 (before Word file).

### New references to find (~31)
| Section | n | What | Recent (≥ 2021) needed | When screened |
|---|---|---|---|---|
| 1 Introduction | 5 | Egypt RA burden, biologic cost, MTX toxicity (prior reviews: 3 already found, see [[study-cards]]) | ~4 | item 11 |
| 5 Challenges | 8 | safety/interactions with MTX & steroids, drug-specific risks in RA, trial-design refs | ≥ 4 | item 11 |
| 3 Pathophysiology | 7 | inflammatory signalling pathways targeted by the drugs (+1 replaces Malemud2013) | 2–3 | item 11 |
| 4.1.3 GLP-1 RAs | 2 | Zheng2019 dulaglutide-FLS (EKB; alt. Tao2019 / Du2019) replaces Israel2026 for mechanism + 1 recent human study (WangQ2025 already found) | 1 | item 5 |
| 4.1.4 SGLT2 inhibitors | 3 | human studies | 3 | item 5 |
| 4.1.1 Metformin | 1 | Nair & Jacob 2016 (HED method) | 0 | item 5 |
| 4.2.1 Statins | 1 | lab mechanism ref for Ras/Rho + MHC-II (replaces Chodick2010; verify Kwak 2000) | 0 | item 5 |
| 4.3 ARBs | 1 | human study if found | — | item 11 |
| 4.1.5 DPP-4 inhibitors | 1 | human study | — | item 11 |
| 2 Methods | 1 | search-method reference | 0 | item 12 |
| 4.5 Synthesis | 1 | review of the shared pathway | — | item 17 |
| **Total** | **31** | | **≥ 10** | |

Intro + Challenges = 16 of 34 and carry most of the recency → item 11 screening is the critical step.

## Similar work & source audit (2026-10-07)
Details and numbers: [[study-cards]] (last two sections).

**Positioning:** prior reviews each cover one drug or one class → our gap = 4 classes together + HED + safety with MTX/steroids + shared-pathway comparison + Egyptian trials.

| Added to `papers/` | Type | Used in | Role |
|---|---|---|---|
| Alshammari2026 (BMC Rheumatol) | SR/MA, metformin | 1 Intro gap · 4.1.1 · 5 | pooled DAS28/CRP + trial-design gaps |
| Nallathambi2024 (Mediterr J Rheumatol) | narrative review, metformin + SGLT2i | 1 Intro gap · 4.1.4 | "no RA clinical data for SGLT2i" |
| Buonanno2026 (J Pers Med) | scoping review, GLP-1 RA | 1 Intro gap · 4.1.3 · 5 | mechanism leads + biphasic RA-risk point |
| WangQ2025 (Clin Rheumatol) | cohort, GLP-1 RA vs DPP-4i in RA | 4.1.3 · 4.5 | thromboembolic HR 0.76 |
| Zheng2019 (Int Immunopharmacol) — **to download, EKB** | in vitro RA-FLS, dulaglutide | 4.1.3 | mechanism (replaces Israel2026) |

| Excluded / caution | Reason | Rule |
|---|---|---|
| Malemud2013 | OMICS, predatory | ❌ removed from 3 Pathophysiology |
| Sarabi2016 | Electronic Physician, not MEDLINE, PMC inactive | ❌ never cite |
| Kumar 2023 / 2024 | weak venues, high risk of bias | ❌ cite only via Alshammari2026 |
| Chen 2020 preprint | Research Square | ❌ cite published Chen2020 only |
| Conference abstracts in Buonanno2026 | not peer-reviewed full papers | ❌ never cite |
| Fan2020 | Ann Transl Med delisted from WoS 2023 | ⚠️ only with Son2014 |
| Cardoso2018 | low-tier, in vitro | ⚠️ supporting only |
| Zhang2023 | correction 2023-12 | ⚠️ read correction first |
| AbdelElGaphar2018 | DOI missing | add DOI/URL before item 21 |

## Tables & figures
- T1 animal studies (+ HED column) · T2 emerging candidates · T3 human studies (drug, design, n, dose, duration, outcome) — built from [[study-cards]].
- Fig 1 pathogenesis + druggable pathways · Fig 2 drug → shared-pathway convergence · Fig 3 evidence map · Fig 4 search/selection flow. Details: [[02-Figures-Map]].

## Workflow per section
Brief (Claude) → Copilot ([[Copilot-Prompt]]) → `drafts/DayN.md` → "خلصت" → `review_gate.py` → sentence-level fixes → HumanizeAI (in context) + Grammarly chunk ≤ 20%.
Style rules are enforced by `scripts/review_gate.py`; judgement items by [[review_rubric]] at item 23.
