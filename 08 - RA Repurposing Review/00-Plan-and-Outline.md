---
tags: [review-article, RA, repurposing, ODR]
deadline: 2026-10-06
journal: Octahedron Drug Research (odr.journals.ekb.eg)
status: planning
---

# RA Drug Repurposing Review — Plan

**Title (final):** Old Drugs, New Targets: Repurposing Cardiometabolic Agents for Rheumatoid Arthritis
**Target:** ~4500 words · 45–55 refs · open-access full text only · narrative + search strategy

## Drug selection (evidence screen, Europe PMC, 2026-09-29)

| Drug | OA primary papers | Best evidence | Verdict |
|---|---|---|---|
| Statins | many | RCT (TARA) + cohorts + animal | ✅ Main |
| Metformin | ~39 | animal (CIA) + cohorts | ✅ Main |
| Pioglitazone (PPARγ) | ~12 | RCT (2013) + animal | ✅ Main |
| Fenofibrate (PPARα) | 3 | Th17 in vitro + AIA rats | ✅ Main (thesis link) |
| GLP-1 RA | ~5 | cohorts 2025–26 | ✅ Main |
| SGLT2i | ~5 | animal 2025 + cohort 2026 | ✅ Main |
| Losartan (ARB) | ~6 | AIA rats + PBMC | ✅ Main |
| Propranolol | 2 | 1 rat + 1 clinical (negative) | ➖ Emerging table |
| SSRIs (sertraline) | 2 | CIA 2026 only | ➖ Emerging table |
| Allopurinol | ~0 RA-specific | gout only | ➖ Emerging table |
| DPP-4i (sitagliptin) | 0 animal | paradoxical (SDF-1) | ➖ Emerging table |
| Amitriptyline | 1 | SphK1 hypothesis | ➖ Emerging table |
| Valproate | 1 | HDAC hypothesis | ➖ Emerging table |

7 main sections + 1 "emerging candidates" table = cheaper in words, still shows breadth.

## Outline + word budget

| # | Section | Words |
|---|---|---|
| — | Abstract (written LAST) | 250 |
| 1 | Introduction: RA burden, limits of current therapy (cost/toxicity/non-response), why repurposing, aim | 500 |
| 2 | Methods: search strategy | 200 |
| 3 | RA pathophysiology & druggable pathways (+ Figure 1) | 600 |
| 4.1 | Antidiabetics: metformin 400 · pioglitazone 300 · GLP-1 RA 300 · SGLT2i 250 | 1250 |
| 4.2 | Lipid-lowering: statins 450 · fenofibrate 300 | 750 |
| 4.3 | Antihypertensive: losartan/ARBs | 300 |
| 4.4 | Emerging candidates (Table 2) | 200 |
| 5 | Challenges & future perspectives | 400 |
| 6 | Conclusion | 150 |
| | **Total** | **~4600** |

Tables: T1 = mechanisms & evidence per drug · T2 = emerging candidates. Figure 1 = pathway map (Claude draws).

## Schedule

| Day | Date | Work |
|---|---|---|
| 1 | 09-30 | Metformin + statins |
| 2 | 10-01 | Pioglitazone + fenofibrate |
| 3 | 10-02 | GLP-1 RA + SGLT2i + losartan |
| 4 | 10-03 | Pathophysiology + emerging table |
| 5 | 10-04 | Intro + methods + challenges |
| 6 | 10-05 | Conclusion + abstract · Claude: refs + Word formatting |
| 7 | 10-06 | Supervisor check · submit |

## Workflow per section
1. Claude posts paper cards (what to read, what to extract, tag).
2. Claude dictates sentence-by-sentence points.
3. User rewrites in own style in Word, keeps `[Tag]`.
4. Claude reviews text for accuracy.
5. Checks after EVERY edit (both must be clean): `python ../scripts/overlap_check.py drafts/DayN.md papers` (0%) and `python ../scripts/style_check.py drafts/DayN.md`.
6. Style rules (validated 2026-10-04, Day1–3 = 0–1% AI on several detectors):
   - Funnel: background → mechanism → animals → humans → limits → conclusion; each group (4.1, 4.2) opens with a 2–3 sentence intro.
   - Each evidence paragraph opens with a short topic sentence (5–10 words) before study details; merge same-topic paragraphs.
   - Sentences ≤40 words (split: design | result); plain words; max 1 opening connector per paragraph; no trailing participle clauses.
   - Vary section closings (max 2 "trials are needed").
   - Every claim = the paper's own result (open-access primary only).
7. Reading PDF: `python ../scripts/make_review_pdf.py` → `Section-4-Drafts-Day1-3.pdf`.

## Section status (2026-09-29)
- ✅ briefs ready: [[4.1a-Metformin]] · [[4.1b-PPAR-agonists]] · [[4.1c-GLP1-RA]] · [[4.1d-SGLT2i]] · [[4.2a-Statins]] · [[4.3-ARBs-Losartan]]
- ⏳ todo: 3 Pathophysiology · 4.4 Emerging table · 1 Intro · 2 Methods · 5 Challenges · 6 Conclusion · Abstract
- 32 OA full-text papers in `papers/`; 7 dropped (no OA full text)

## Pending
- [ ] ODR Guide for Authors PDF + template (EKB blocks bots — user saves manually)
