# Report audit-2026-10 (read-only audit, nothing fixed)

Date: 2026-10-22. Roles (inline): research-synthesist + academic-statistician + healthcare-clinical-evidence-agent + testing-reality-checker.
Agents: 6 Haiku (research-synthesist.md) + 1 Sonnet (testing-reality-checker role) = 7 of the 8 + 2 cap. Skeptic panel (A4) deferred by user choice.
Sub-agent tokens: Haiku ≈ 851k, Sonnet ≈ 174k, total ≈ 1.03M.
Every agent finding was re-checked by the orchestrator; 5 were false positives and were dropped (see "Dropped").

## A6 Scores (1–5)

| Area | Score | Evidence |
|---|---|---|
| Support | 4 | 60 of 62 high-risk numeric sentences match the paper; 1 contested (F1), 1 unverified (F2) |
| Coverage | 2 | Section 5 part 2, Conclusions, Abstract, Tables 1–2 and Figures 1, 2, 4 not written yet; Section 4.4 is one uncited sentence |
| Recency | 4 | Plan definition (year ≥ 2021, cite_check.py): 69/115 = 60%, target met. Stricter 2024–2026: 40/115 = 34.8% |
| Source strength | 3 | 41 of 115 are animal or in vitro (36%); 13 are abstract-only or labels/registry; one pioglitazone mechanism rests on a single abstract (Fu2026) |
| Wording calibration | 4 | No "causes" or "leads to" for observational data; 3 mild overreaches (F5, F6, F7) |
| Overlap | 3 | 7+-word runs: Day1 5.5%, Day2 6.2%, Day3 8.5%, Day4 13.3% |
| Consistency | 3 | RCT, ARB, IL defined in several drafts; Methods says 79 references cited, drafts carry 115 tags; author name differs between byline and email |
| Method transparency | 3 | Strategy stated (Europe PMC, 8 searches, counts); single database, exclusion reasons not recorded, no limitations section yet |

## Reference totals vs targets

| Item | Now | Target |
|---|---|---|
| Unique tags cited in drafts | 115 (all have papers/<Tag>.md) | ≥ 80 |
| Paper files | 124 (9 never cited) | — |
| Cited from 2021–2026 (plan definition) | 69 / 115 = 60% | ≥ 40%, met |
| Cited from 2024–2026 (stricter) | 40 / 115 = 34.8% | about 10 more needed only if this definition is used |
| Words (Day0–Day6) | ≈ 12,570 | ≥ 6,500 (floor only) |
| Full text / abstract-only / label or registry (cited) | 102 / 8 / 5 | — |
| Design (cited, title keywords, approximate) | animal 23, in vitro 18, cohort 21, RCT 20, meta-analysis 7, MR 6, cross-sectional 4, review or guideline 11, label 3, unclassified 2 | — |

Never cited: Abuhelwa2021, Bu2021, Chmielewski2026, Du2019, Lin2020, Malemud2013, Oh2017, Sarabi2016, Tao2019.

## UNREADABLE (failed read, not "nothing found")

- Mostafa2020 Table III body (caption only in papers/Mostafa2020.md)
- NairJacob2016 Table 1 (mouse Km): basis of the Day1 "810–1,220 mg" figure
- Tang2011 table: P-value columns unlabeled in the extracted text
- Supplementary Table S1 cited in Methods: no file in the folder
- Figures 1, 2, 4 and Tables 1, 2: no files, so figure arrows vs text could not be checked
- Claims not in the 62-sentence sample (doses, percentages, mechanisms without HR/OR/CI/P) were not re-verified

## Findings

id | severity | location | evidence | proposed fix (NOT applied)

1. F1 | blocker | Day1:51 | [C1] contested. Draft: "Larger, longer placebo-controlled trials with disease activity as the primary end point are needed before statins can be used to treat RA itself." McCarey2004 (^mccarey2004-1): "116 patients with rheumatoid arthritis were randomised in a double-blind placebo-controlled trial…"; START-HERE line 197 already marks this sentence wrong | Reword to "larger and longer trials" without implying none exist.
2. F2 | fix | Day2:44 | [C2] unverified. Draft: "candesartan produced larger falls in serum CRP, IL-1β and TNF-α (post hoc P < 0.05)". Paper text line 87 gives only the three-group ANOVA; Table III body not extracted | Re-extract Table III from the PDF; drop "post hoc P < 0.05" if no pairwise test is reported.
3. F3 | fix | Day5 (§1 end) | [C12] unverified. "To our knowledge, no earlier review has considered antidiabetic, lipid-lowering and antihypertensive drugs together in RA…" No search ledger exists (CLAUDE.md research rule) | Run a research-kit ledger (lanes primary, independent, counter) or soften the sentence.
4. F4 | blocker | Day5 §5 | Section 5 part 2 (trial design, dose gap, limits of this review) not written; no limitations section | Step 19 as planned; include single database, unrecorded exclusions, single screener.
5. F5 | fix | Day3 WangQ2025 sentence | [C5] supported (number). Draft "the 5-year risk … was 24% lower (HR 0.76)"; paper: "associated with a 24% lower risk of all thrombotic events (Hazard ratio (HR), 0.76…)" | Say "hazard … over up to 5 years".
6. F6 | fix | Day3:48 | [C4] supported (inference). Draft: "The authors inferred a possible increase in RA risk from these cell experiments [Han2021]." Abstract: "…increased proinflammatory cytokine production, indicating an enhanced risk of RA development" | Drop "from these cell experiments".
7. F7 | note | Day5:33 | [C3] supported. ITT (primary) no difference; draft then says "An excess appeared in the as-treated analysis" | Add "secondary" before as-treated.
8. F8 | fix | Day1:25 | STAT5 never defined in Day1–Day6 (Day4 defines STAT and STAT3 only); review_gate and cite_check agree | Spell out STAT5 at first use.
9. F9 | fix | Day1, Day2, Day4 | RCT, ARB and IL defined in more than one draft (review_gate, cite_check) | Keep one definition at first use in the assembled order (Intro, Methods, Pathophysiology, Section 4).
10. F10 | fix | Day4 Methods | "eight searches … 48 included" plus "31 references came from outside the search" = 79; drafts cite 115 tags; plan says 112 | Recount from ledger.py at assembly and update Methods.
11. F11 | fix | Day1–Day4 Fu2026 (6 citations) | Abstract-only; Day4:24 pioglitazone mitophagy chain and Day3:60 class comparison rest on it alone | Get the full text, or mark the claims "reported in an abstract" and cut to one citation per section.
12. F12 | fix | Day3 Nematalla2026 (5 citations) | Abstract-only; draft writes "AIA rats", abstract says CFA-induced arthritis | Use "CFA-induced"; try for the full text.
13. F13 | fix | papers/Chung2008.md, papers/Qiao2024.md | 371 and 373 words but no "Abstract only" banner | Check source; add the banner and limit claims to the abstract (paper edit, later step).
14. F14 | note | references overall | Plan target (≥ 2021) met at 60%; only 34.8% are from 2024–2026 | Optional at step 22: add recent primary papers to Sections 4.4 and 5 (the 9 uncited files are partly on the drop list: Malemud2013, Sarabi2016).
15. F15 | blocker | 02-Figures-Map.md; Day1, Day3, Day4 | Figures 1, 2, 4 were due 15–19 Oct; no fig file; Table 1 (Day1) and Table 2 (Day3) cited but not built | Step 21: build Fig 2, then Fig 1, Fig 4, Tables 1–2; check every arrow against the text.
16. F16 | blocker | Day5 §6, Day6 | Conclusions, Abstract and Keywords empty | Step 20 as planned.
17. F17 | fix | Day0:12, Day0:19 | Byline "Riffat Ibrahim Riffat" vs email "Rafaat.Ibrahim@…"; corresponding email "[EMAIL]" | User to give the official spelling and the email.
18. F18 | fix | Day5 §5 end | "Monitoring may be sensible." names no tests (RULE 0: lab has no ELISA reader or qPCR) | Name routine outsourced tests: liver enzymes, kidney function, CBC.
19. F19 | fix | Day4 (overlap 13.3%), Day2 | 7+-word runs: Day2 Kondo2021 NFATC1 sentence (7 runs), Day4 Chen2020 STAT3 sentence (3), Day1 Pan2024 subgroup sentence (3) | Rewrite those sentences in own words.
20. F20 | fix | Day1 §4.2.1 Statins | About 2.5–3 times its 650-word target; four MR paragraphs (Hu2024, Ma2023, Qiao2024, Huang2024) | Merge the MR studies into one paragraph.
21. F21 | note | Day3 §4.4 | One sentence, no citation (cite_check "paragraph with no citation") | Add Table 2 callout and one citation per drug, or use the 9 uncited papers.
22. F22 | note | Day3 §4.1.5 DPP-4 | Two paragraphs vs 150-word plan | Trim or update the plan.
23. F23 | note | Day1–Day3 | "for a 60-kg adult [NairJacob2016]" about 7 times; "should be interpreted with caution" and "hypothesis-generating" 6–8 times each | Vary openers in the line edit.
24. F24 | note | Day1–Day3 | DAS28 used alone (Intro defines DAS28-CRP only); HED never defined; IFN-γ defined twice | Fix at assembly.
25. F25 | note | Day1, Day2, Day4 | Sentence-length SD 9.8, 8.8, 9.2 (benchmark ≥10); Day4 opener connectors 4.4% (5–15); Day2 two connectors in one paragraph | Line edit.
26. F26 | note | Day3 Kachhadia2026 | Paper gives follow-up as median 3.1 vs 6.4 years in Results and mean 3.9 vs 6.4 years elsewhere | Keep "median" and cite the Results.
27. F27 | note | Day1 Tang2011 | P < 0.001 for DAS28 is read from a table whose P column is unlabeled | Confirm from the PDF.
28. F28 | note | Day0 Funding | "This research received no external funding." Work is self-funded | Optional: "self-funded by the authors".
29. F29 | note | 4.2a-Statins.md and 3 other briefs | 27 brief links "not highlighted or block too long" (check_links); none broken | Fix highlights when that brief is next used.
30. F30 | note | graph_audit | 32 [note], 0 [fix]; 4 "superseded" Intro claims confirmed absent from drafts | None.

## Dropped (agent flags the orchestrator disproved)

- "Within this cohort" (Day1:18) points to ManriqueArija2021, the sentence before it; correct.
- Ibrahim2020 "species omitted" (Day3:48): the sentence before names "AIA rats".
- Roy2017 "species omitted" (Day2): "the same model" refers to the rat model in the sentence before.
- Tsushima2026 comparator: metformin is named in the sentence before.
- Peterson2021 "US not confirmed": paper uses OptumLabs, Medicare Advantage.

## Script output summary (A1)

- review_gate.py: 36 issues (Day1 11, Day2 7, Day3 8, Day4 10, Day5 0, Day6 0)
- cite_check.py: 7 (STAT5; RCT, ARB, IL duplicates; Day3 uncited paragraph). No "SGLT" DEF_SPAN false positive this run.
- secondary_check.py: 0 second-hand sources
- overlap_check.py: Day1 5.5%, Day2 6.2%, Day3 8.5%, Day4 13.3%, Day5 0%, Day6 0%
- style_check.py: 5
- ledger.py: 115 tags, 0 without a file, 25 cited once, 3 "same tag + number" flags (all checked: no error; Fu2026 "18" = IL-18). Tool-suspect: skips multi-tag brackets, so counts may be low.
- check_links.py (12 briefs): 0 broken, 27 weak
- evals.py: 8 pass, 0 still failing
- graph_audit.py audit: 702 nodes, 1,783 edges, 32 [note]
