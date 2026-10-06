---
tags: [review-article, checklist]
use: internal peer review (START-HERE item 20, 27/10) — Claude fills it; scripts cannot judge these
sources: Imbad0202/academic-research-skills (academic-paper-reviewer review_criteria_framework, quality_rubrics §2.3); Master-cai/Research-Paper-Writing-Skills (paper-review.md, SKILL.md)
---

# Internal review rubric

Run first: `python ../scripts/review_gate.py --full` (style + citations + overlap + structure). This rubric covers only what needs judgement.

Rating per item: **EXCEEDS / MEETS / PARTLY_MEETS / DOES_NOT_MEET** + location + one-line reason + fix. No total score.

## A. Seven dimensions
1. **Originality** — what does a reader learn that existing RA-repurposing reviews do not give? (one clear angle: cardiometabolic drugs, graded evidence)
2. **Methodological rigor** — search reproducible (databases, dates, terms, inclusion); selection applied consistently; no OA-only selection bias.
3. **Evidence sufficiency** — each drug has its key human studies (e.g. TARA for statins); counter-evidence and null trials reported, not hidden.
4. **Argument coherence** — reverse outline: thesis → each topic sentence → evidence under it. Any paragraph that does not map gets cut or moved.
5. **Writing quality** — one message per paragraph, stated in its first sentence; stable terms; academic register (style_check profile in range).
6. **Literature integration** — synthesis, not a list of studies: where results agree, where they conflict, and why (design, dose, population).
7. **Significance** — clinical take-home per drug class; who should be trialled next and how.

## B. Review-article items
- [ ] Evidence level named for every claim (preclinical / observational / RCT / meta-analysis); cohort data worded "associated with", never "reduced".
- [ ] Every cited study supports the exact sentence (own Results/Abstract, rule G) — spot-check ≥ 10 tags against papers/.
- [ ] Risk of bias / limits of the main studies stated (sample size, open label, short follow-up, confounding by indication).
- [ ] Heterogeneity across studies explained, not ignored.
- [ ] Conclusions do not exceed the evidence (no "effective in RA" from animal data).
- [ ] Limitations of this review stated (narrative design, language, databases).
- [ ] Emerging-drug section fits the title scope, or is cut.

## C. Section moves
- **Abstract**: background → gap → aim/scope → main themes (drug classes, strongest evidence) → implication. ≤ 250 words, no citations.
- **Introduction**: RA burden → limits of current DMARDs and why → repurposing rationale → gap in existing reviews → this review's aim and structure (last paragraph).
- **Each drug section**: background → mechanism → animal → human → limits → one-line verdict.
- **Challenges**: scope limits, not fixable defects; concrete trial designs.
- **Conclusion**: problem → strongest evidence → take-home → concrete next step.

## D. Verdict
Mark each failing item **needs revision** or **needs new source** → list fixes with day in START-HERE.
