---
tags: [review-article, RA, repurposing]
target: Q2 international journal (chosen by Dr. Ahmed Morad after delivery)
deadline: 2026-11-08
status: writing
updated: 2026-10-19
---

# RA Drug Repurposing Review — Plan

> ⚠️ The ODR plan (4,500 words, 45–55 refs, OA-only, deadline 2026-10-06) is **obsolete**. Daily steps live in [[START-HERE]]; this file holds the targets and the outline.

**Title:** Old Drugs, New Targets: Repurposing Cardiometabolic Agents for Rheumatoid Arthritis
**Type:** narrative review with a structured, reproducible literature search (Methods + Figure 4 search overview). Never call it "systematic" or "semi-systematic" in the manuscript; quality checklist = SANRA (Baethge 2019).

## Fixed targets
| Item | Target | Status 2026-10-19 (after step 16) |
|---|---|---|
| Words (body, no refs/tables) | ≥ 6,500 (minimum only; no cap until journal chosen) | ~9,900 in drafts Day1–6 (Introduction ~1,340 of it, script count) |
| Unique references | ≥ 80 | 112 cited in drafts · 124 in `papers/` |
| Recent refs (year ≥ 2021, `cite_check.py`) | ≥ 40% | 64/110 = 58% |
| Figures | 4 original + graphical abstract | 0 final |
| Tables | 3 | 0 final |
| Overlap / AI detectors | 0% / ≤ 20% each | Day1–3 pass (overlap vs `papers/` only) |
| Overlap corpus | `papers/` + `overlap-only/` (prior OA reviews, comparison only, not cited) | step 6.1 pending; every section, incl. unwritten ones, gated at the end of its own step; full manuscript at step 27 |

## Source rules
- Every specific study cited to its own paper, saved in `papers/` (open access or EKB download).
- Mechanism claims cited to mechanistic (lab) papers or mechanism reviews — never to cohort, case–control or outcome-trial papers.
- Every animal dose is followed by its human equivalent dose (HED table in [[study-cards]]; method ref Nair & Jacob 2016).
- Cohort/case–control results worded "associated with", never "reduced".
- No second-hand citations: a highlight from a primary paper's Introduction/Background/Discussion that describes other groups' work is not a source → cite the original. Enforced by `scripts/secondary_check.py` (part of `review_gate.py`, added 2026-10-07; 12 flags open, all with an identified original (START-HERE 5.1), fixed in items 6–10).

## Outline, word budget, reference budget
"Have" = already cited in drafts or saved in `papers/` and assigned. "New" = still to find/screen.

| # | Section | Words now | Words target | Refs have | Refs new | Refs total |
|---|---|---|---|---|---|---|
| — | Abstract + keywords | 0 | 250 | — | — | 0 |
| 1 | Introduction (burden → DMARD limits → repurposing → gap in prior reviews → aim) | ~1,340 (paragraphs 1–4, steps 15–16) | 1,200 | 13 cited: GBD2023, Almoallim2026, Natalucci2025, VanMullem2026, AlRayes2026, Nagy2021, Said2025, Gebrye2026, Sertkaya2024, Mulcahy2025, Akodad2026, Barkhane2023, Qin2023 · step 16: Alshammari2026, Ren2023, Pan2024, Buonanno2026, Bilgin2025 (Nallathambi2024 stays once, in Day3; WangQ2025 is a cohort → GLP-1 section) | — | ~17 |
| 2 | Methods (databases, dates, terms, criteria, counts) | 0 | 300 | — | ~1 | ~1 |
| 3 | Pathophysiology + druggable pathways (Fig 1) | 0 | 700 | 2 (Ding2023, Kondo2021) — Malemud2013 dropped (OMICS, predatory) | ~7 | ~9 |
| 4.1 | Antidiabetics intro | 54 | 60 | 1 | — | 1 |
| 4.1.1 | Metformin | 548 | 650 | 7 + Abdallah2021, Naffaa2020, Qin2023, NairJacob2016 (+ Alshammari2026 re-cited) | 3 in hand: Zhou2001, Gwinn2008, Nagai2013 (replace Son2014 intro) | ~14 |
| 4.1.2 | Pioglitazone | 478 | 550 | 5 + Hsieh2021, Ormseth2014 | Varga2011 in hand (PPAR, shared with 4.2.2) + 1 identified: Romeo2012 (replaces Ormseth2013 abstract) | 9 |
| 4.1.3 | GLP-1 RAs | 453 | 550 | 3 + WangQ2025, Malik2026, Buonanno2026 (re-cite) | 3 identified: Zheng2019, Bendotti2022, Drucker2018 (EKB) | ~8 |
| 4.1.4 | SGLT2 inhibitors | 340 | 450 | 2 + Kachhadia2026 | 1 identified: Dobashi2026 (EKB) | ~4 |
| 4.1.5 | DPP-4 inhibitors (moved from 4.4) | (in 4.4) | 150 | 1 (Kathe2018) | ~1 | ~2 |
| 4.2 | Lipid-lowering intro | 44 | 50 | Hansildaar2021 (replaces Kitas2019 here) | — | 1 |
| 4.2.1 | Statins | 426 | 650 | 7 + McCarey2004, Tang2011, Hu2024 | 2 identified: Kwak2000 (EKB), Greenwood2006 (free) + Leung2003, Palmer2004 (replace Vandebriel2012 discussion); Greenwood2006 also replaces Ren2023 for HMG-CoA | ~14 |
| 4.2.2 | Fenofibrate | 109 | 250 | 2 + Goto2010, Shirinsky2013 | — | 4 |
| 4.3 | ARBs | 456 | 500 | 4 | 2 identified: Goto1990, Walsh2000 (replace Wang2013 intro) + ~1 human study to find | ~7 |
| 4.4 | Emerging candidates (1 sentence + Table 2) | 286 | 80 | 4 (in Table 2) | — | 4 |
| 4.5 | Comparative synthesis (NEW, Day3, step 17 done 2026-10-20) | ~320 | 250 | 13 re-cited: Fu2026, Son2014, ElDemerdash2025, Nematalla2026, Ibrahim2020, McCarey2004, Alshammari2026, Ormseth2013, Marder2013, Kitas2019, Mostafa2020, Goto2010, Yen2026 | 0 (no new source needed) | 13 |
| 5 | Challenges: part 1 safety/interactions with MTX & glucocorticoids (step 18 done 2026-10-21, Day5, ~557 words, over the 300–350 target); part 2 trial design, dose gap, review limits (step 19) | ~557 | 600 | 3 new: Dobashi2026, Tsushima2026, Kalantari2024; re-cited: Kitas2019, Abdallah2021, Gharib2021, Shahin2011, Shirinsky2013, Kellner2025, Ormseth2013, Mostafa2020, Israel2026 | step-18 search (16 queries) added none | ~12 |
| 6 | Conclusion | 0 | 150 | — | — | 0 |
| | **Total** | **~3,430** | **~6,890** | **~77** (+ Gwinn2008) | **~22 to find** | **~99** |

### Recency budget
- Recent (≥ 2021) now: 11. Planned additions already in hand: Abdallah2021, Hu2024, Hsieh2021, Qin2023, Hansildaar2021, GBD2023, Nagy2021, Gao2024, Ding2023, Kondo2021, Alshammari2026, Nallathambi2024, Buonanno2026, WangQ2025, Malik2026, Kachhadia2026, Tsushima2026 → **28**.
- Downloaded at item 5.2: 3 recent (Bendotti2022, Dobashi2026, Kalantari2024) + Nematalla2026, Loizidis2026 → **33**. The other 12 (incl. Gwinn2008) are older mechanism papers replacing second-hand citations.
- 40% of ~99 = 40 → **at least 7 of the ~22 refs still to find must be 2021 or later** (priority: Egyptian burden/cost data, safety data, pathophysiology reviews). If recency falls short at item 22, prefer recent mechanism reviews over the older originals where one source covers both.
- Checkpoints: START-HERE item 11 (after drug sections) and item 22 (before Word file).

### References still to find (~22) — items 5 and 5.1 done 2026-10-07
| Section | n | What | Recent (≥ 2021) needed | When screened |
|---|---|---|---|---|
| 1 Introduction | 0 | ✅ done at step 15 (10 new OA sources, 2023–2026). Not found: Egypt-specific cost/access data, 2023+ metformin/TZD incidence study, 2023+ insulin-resistance meta-analysis (Europe PMC only). Step 16: prior-reviews paragraph + gap ("to our knowledge"), 1 new source (Bilgin2025, abstract) | — | steps 15–16 |
| 5 Challenges | 3 | safety part done (step 18): Dobashi2026, Tsushima2026, Kalantari2024; trial-design refs still for step 19 | ≥ 3 | item 18 ✅ / 19 |
| 3 Pathophysiology | 7 | inflammatory signalling pathways targeted by the drugs (+1 replaces Malemud2013) | 2–3 | item 11 |
| 4.3 ARBs | 1 | human study if found | — | item 11 |
| 4.1.5 DPP-4 inhibitors | 1 | human study | — | item 11 |
| 2 Methods | 1 | search-method reference | 0 | item 12 |
| 4.5 Synthesis | 0 | not needed: section built from papers already cited (step 17, 2026-10-20) | — | item 17 ✅ |
| **Total** | **22** | | **≥ 7** | |

Intro + Challenges + Pathophysiology = 18 of 22 and carry most of the recency → item 11 screening is still the critical step.

## Similar work & source audit (2026-10-07)
Details and numbers: [[study-cards]] (last two sections).

**Positioning:** prior reviews each cover one drug or one class → our gap = 4 classes together + HED + safety with MTX/steroids + shared-pathway comparison + Egyptian trials.

| Added to `papers/` | Type | Used in | Role |
|---|---|---|---|
| Alshammari2026 (BMC Rheumatol) | SR/MA, metformin | 1 Intro gap · 4.1.1 · 5 | pooled DAS28/CRP + trial-design gaps |
| Nallathambi2024 (Mediterr J Rheumatol) | narrative review, metformin + SGLT2i | 1 Intro gap · 4.1.4 | "no RA clinical data for SGLT2i" |
| Buonanno2026 (J Pers Med) | scoping review, GLP-1 RA | 1 Intro gap · 4.1.3 · 5 | mechanism leads + biphasic RA-risk point |
| WangQ2025 (Clin Rheumatol) | cohort, GLP-1 RA vs DPP-4i in RA | 4.1.3 · 4.5 | thromboembolic HR 0.76 |
| Zheng2019 (Int Immunopharmacol) — **to download, EKB** | in vitro RA-FLS, dulaglutide | 4.1.3 | mechanism in joint cells (replaces Israel2026) |
| Malik2026 (Eur Heart J Cardiovasc Pharmacother, OA) | target-trial emulation, semaglutide in RA + T2DM | 4.1.3 · 4.5 | MACCE HR 0.75, driven by heart failure |
| Kachhadia2026 (J Clin Med Res, OA) | cohort, SGLT2i vs DPP-4i in RA + T2DM | 4.1.4 | MACE not significant → "sparse, inconclusive" |
| Tsushima2026 (J Diabetes Investig, OA) | target-trial emulation, SGLT2i in IMID + T2DM | 5 | UTI not higher; genital infection HR 2.31 |
| NairJacob2016 (J Basic Clin Pharm, OA) | dose-conversion guide | 4.1–4.3 · Table 1 | HED method |

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
Sources: candidate list (`find_sources.py`) → user downloads to `papers/pdf/` → `pdf2md.py <Key> <DOI>` (or JATS / abstract-only stub) → Claude highlights the paper's OWN result, never intro/discussion summaries of other work (`highlight.py` warns).
Brief (Claude) → Copilot ([[Copilot-Prompt]]) → `drafts/DayN.md` → "خلصت" → `review_gate.py` (incl. `secondary_check.py`) → sentence-level fixes → Grammarly chunk ≤ 20% (HumanizeAI dropped 2026-10-08: same text 0% → 99%).
Style rules are enforced by `scripts/review_gate.py`; judgement items by [[review_rubric]] at item 23.
