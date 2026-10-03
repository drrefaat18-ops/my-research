# D-stats: sample size, contrasts, analysis plan, and audit of section 4

Scope: the 9-group CFA arthritis design (female Wistar rats, oral treatment Day 16 to 45, sacrifice Day 46) from `scripts/protocol_dump.txt`. The protocol does **not** give n per group. The "n=10 / N=90" in the 2026-09-06 file is an assumption made by an earlier AI, not a protocol fact.
Calculations: `scratchpad/rework/power.py` (scipy 1.17, exact noncentral t; Dunnett critical values from a 100k-draw null simulation). All numbers below come from that script.

## 0. Verified sources (metadata fetched via PubMed E-utilities, 2026-10-02)

| # | Reference | PMID | DOI | What it is used for |
|---|---|---|---|---|
| S1 | Arifin WN, Zahiruddin WM. Sample size calculation in animal studies using resource equation approach. Malays J Med Sci 2017;24(5):101-105 | 29386977 | 10.21315/mjms2017.24.5.11 | Mead formulas (I read the full text in PMC5772820) |
| S2 | Curtis MJ et al. Experimental design and analysis and their reporting II. Br J Pharmacol 2018;175(7):987-993 | 29520785 | 10.1111/bph.14153 | n≥5 rule, equal groups, randomisation/blinding, when post hoc tests may be run (full text read in PMC5843711) |
| S3 | Percie du Sert N et al. The ARRIVE guidelines 2.0. PLoS Biol 2020;18(7):e3000410 | 32663219 | 10.1371/journal.pbio.3000410 | Items 2-7 (full text read in PMC7360023) |
| S4 | Percie du Sert N et al. Explanation and elaboration for ARRIVE 2.0. PLoS Biol 2020;18(7):e3000411 | 32663221 | 10.1371/journal.pbio.3000411 | Practical randomisation/blinding detail (metadata only) |
| S5 | Morvaridi A, Abtahi Froushani SM, Farshid AA. Piperine with prednisolone in experimental RA. Vet Res Forum 2025;16(2):117-124 | 40099241 | 10.30466/vrf.2024.2031860.4316 | Effect size (Table 1, mean ± SD, n=10/group, male Wistar, FCA) |
| S6 | Slovák L, ..., Bauerová K. Ferulaldehyde improves the effect of methotrexate in experimental arthritis. Molecules 2017;22(11):1911 | 29113115 | 10.3390/molecules22111911 | Effect size (Table 1, % paw-volume change, mean ± SEM, n=7-8, male Lewis rats) |
| S7 | Matthews JNS, Altman DG, Campbell MJ, Royston P. Analysis of serial measurements in medical research. BMJ 1990;300:230-5 | 2106931 | 10.1136/bmj.300.6719.230 | Summary-measure (AUC) approach |

Quotes I checked in S2 full text:
- "any data set containing groups of n < 5 must not be subjected to statistical analysis".
- "Studies should be designed to generate groups of equal size, using randomization and blinded analysis".
- "After ANOVA, post hoc tests may be run only if F achieves the necessary level of statistical significance".
- "five cells from one mouse ... is not n = 5".

---

## 1. Sample size

### 1a. Mead's resource equation (S1)

For a one-way ANOVA, error DF = k(n−1), and the acceptable DF range is 10 to 20.
- k = 9 gives minimum n = 10/9 + 1 = 2.11, rounded up to **3**.
- Maximum n = 20/9 + 1 = 3.22, rounded down to **3**.
- So Mead gives **exactly 3 per group (N = 27)**, which is DF = 18.

For the between-within repeated-measures form, n = DF/(k·r) + 1.
- With r = 4 time points, n is 1.28 to 1.56. With r = 6, it is 1.19 to 1.37. Both are meaningless here.

Interpretation:
- Mead is meant for exploratory work when no SD or effect size is known (S1 says this explicitly).
- With 9 groups, Mead's maximum of n = 3 **breaks the BJP rule that every group must have n ≥ 5 before analysis (S2)**.
- Any n that is publishable (n = 5 gives DF = 36; n = 8 gives DF = 63) sits *above* Mead's upper bound.
- **Conclusion: do not use Mead to justify n in this design.** If an examiner asks, cite it only to explain why it does not apply: k = 9 forces n = 3, below the BJP minimum. Justify n by power instead (1b), because published SDs exist.

### 1b. Power-based estimate from two published AIA datasets

Effect sizes are standardized mean differences d = Δ/pooled SD. For S6, SD = SEM·√7, using n = 7 as the conservative end of the reported 7-8.

| Source | Contrast | Raw values | d |
|---|---|---|---|
| S5 arthritis index (0-12), last day | Pred 10 vs RA | 4.53±0.61 vs 7.51±0.72 | 4.47 |
| S5 | Pip50/Pred5 combo vs RA | 2.92±0.67 vs 7.51±0.72 | 6.60 |
| S5 | **Combo vs Pred 10** | 2.92±0.67 vs 4.53±0.61 | **2.51** |
| S6 % paw-volume change, day 21 | MTX vs AA | 44.9 (SD 24.3) vs 80.2 (SD 23.8) | 1.47 |
| S6 | FRA+MTX combo vs AA | 24.1 (SD 20.6) vs 80.2 | 2.52 |
| S6 | **Combo vs active monotherapy** | 24.1 vs 44.9 | **0.92** |

Caveats:
- S5 is a near-exact analogue of this thesis: natural product 50 + pred 5 vs pred 10, n = 10, no pred-5-alone arm. Its SDs are implausibly small, though: CV about 10% on an averaged 0-12 score. Effect sizes from small preclinical studies that reached significance are typically inflated. I therefore also show d halved.
- S6 has realistic, larger variance. It is a different strain and sex (male Lewis) and a different reference drug (MTX). It is a fair stand-in for the "add-on vs active comparator" gap.
- Neither paper uses this thesis's induction route: 0.3 mL CFA s.c. in the inguinal/thigh region. That route is atypical; footpad or tail-base intradermal injection is usual. Variance and responder rate in this lab are unknown. **The completed pilot study's paw and score data should replace these SDs before the n is finalised.** That costs nothing.

n per group for 80% power, two-sided, equal n:

| Contrast (d) | α = 0.05 | Holm/Bonferroni over 3 confirmatory contrasts (0.0167) | Bonferroni over 8 vs control (0.00625) |
|---|---|---|---|
| Combo vs CFA, S5 (6.60) | 2 | 4 | 5 |
| Combo vs CFA, S6 (2.52) | 4 | 5 | 7 |
| Combo vs Pred 10 superiority, S5 (2.51) | 4 | 5 | 7 |
| Same, d halved (1.26) | 11 | 15 | 19 |
| Combo vs active, S6 (0.92) | 20 | 27 | 33 |
| Same, d halved (0.46) | 75 | 101 | 123 |

Dunnett power was computed properly (8 arms vs CFA, FWER 0.05, pooled 9-group variance). The critical |t| values were 2.79 at n=5, 2.75 at n=6, 2.73 at n=8 and 2.70 at n=10.

| n/group | d = 2.52 | d = 1.5 | d = 1.2 | d = 1.0 |
|---|---|---|---|---|
| 5 | 0.88 | 0.35 | 0.20 | 0.13 |
| 6 | 0.94 | 0.45 | 0.26 | 0.17 |
| 8 | 0.99 | 0.61 | 0.38 | 0.24 |
| 10 | 1.00 | 0.74 | 0.50 | 0.33 |

What this means:
- **Efficacy vs CFA control** for combo or prednisolone: n = 5-6 is enough if the in-house effect resembles the literature (d ≥ 2.5). That is easy.
- **Weaker arms** (PEA 200 alone, low-dose combo; plausibly d ≈ 1-1.5): n = 8-10 gives only 25-75% power under Dunnett.
- **Combo vs prednisolone 10 superiority** cannot be powered within budget unless the true gap is as large as S5 reports. With realistic variance (S6), it needs 20-27 per group.

**Zero-cost power gain:** score every animal on Day 15, before treatment. Then analyse the primary outcome by ANCOVA adjusted for the Day-15 value. With a baseline-outcome correlation ρ, residual variance falls by a factor (1−ρ²). At ρ = 0.5, the effective d rises by about 15%. This is an assumption; check ρ in the pilot data.

### 1c. Attrition and non-responders

- I could not verify a published attrition or responder rate for this specific s.c. inguinal route. Use the **pilot's observed responder rate and mortality**.
- If the pilot data are unavailable, a stated *assumption* of 10-20% loss is conventional. It is not sourced.
- Better than padding every group: **over-induce, then randomise only responders on Day 15** (section 5). Non-responders are then excluded *before* allocation under a pre-registered criterion, which ARRIVE item 3a requires. They do not bias groups, and no group ends up below n = 5 (S2).

### Recommendation (n)

- **Target 8 evaluable animals per group (72).**
- Induce enough CFA rats to have 64 responders for the 8 induced arms. For example, at an assumed 85% response, induce about 76 and add 8 to 9 paraffin-oil controls. Replace the 85% with the pilot figure.
- If animals are cheap relative to assays, n = 10 per group is defensible and buys power for the weak arms. The cost driver is ELISA/IHC, not rats.
- **Cost lever:** run the free in-life outcomes (paw, score, body weight, CBC) on all animals. Run the costly assays (ELISA, IHC) on a **pre-specified random subsample of 6 per group**, chosen by the allocation holder before unblinding. That is 54 samples instead of 72-90. It still meets n ≥ 5 (S2), and the subsample must be reported as such (ARRIVE 2a).
- State honestly in Methods: "Sample size was chosen to detect d ≥ 2.5 vs CFA control (Dunnett, 80% power) based on [S5, S6 / pilot]. Comparisons between active regimens are reported as estimates with 95% CI and were not powered for superiority."

---

## 2. Primary outcome, pre-specified contrasts, multiplicity

**Primary outcome (one only):** the AUC of the arthritis score from Day 16 to 45, analysed by ANCOVA with the Day-15 score as covariate. Score the injected limb plus the contralateral paws on a defined scale.
- Alternative: AUC of contralateral (non-injected) hind-paw volume or thickness.
- Pick whichever the pilot shows is less variable and is measurable with existing equipment at zero cost. A caliper or water-displacement method is fine.
- Measure 2-3 times per week on fixed days.
- Everything else is secondary: histology, cytokines, NF-κB/TLR4 IHC, p38, NLR/SII, body weight.

**Confirmatory family** (planned contrasts on the primary outcome; Holm across 3, FWER 0.05):
1. **C1 Assay sensitivity:** Pred 10 vs CFA control. If this fails, nothing about "sparing" is interpretable.
2. **C2 Combination efficacy:** PEA/Pred 200/5 vs CFA control.
3. **C3 Glucocorticoid-sparing (estimation):** PEA/Pred 200/5 vs Pred 10. Report the difference and 95% CI, and interpret it against a pre-specified margin (below).

**Supportive, pre-specified but labelled secondary:**
- **C4 PEA dose trend at fixed pred 5:** a linear contrast across 50/5, 100/5 and 200/5 (coefficients −1, 0, +1, ideally on log-dose spacing).
  - Prednisolone is held constant across these three arms, so a positive trend is the **only within-design evidence that PEA adds to pred 5**.
  - A flat trend is ambiguous: it could mean a ceiling effect or no PEA contribution.
- **C5 PEA alone:** PEA 200 vs CFA.
- **C6 Reference agents:** tacrolimus and baricitinib each vs CFA, and each vs combo 200/5. These are descriptive, with CI.
- For the remaining all-vs-CFA comparisons, use **Dunnett with CFA as control** within each secondary outcome.
- Do **not** run Tukey on all 36 pairs. It answers questions nobody asked and spends power.

Notes:
- BJP (S2) says post hoc tests run only after a significant F. *A priori planned contrasts* are not post hoc. State in Methods that C1-C4 were pre-specified, so the F-gate does not apply to them.
- Pre-register the plan (OSF is free) or at least date-stamp it in the thesis protocol file before unblinding.

**What the missing prednisolone 5 mg/kg arm breaks:**
- Without pred-5 alone you cannot estimate (a) PEA's added effect over pred 5, or (b) interaction or synergy.
- "Combo 200/5 ≈ Pred 10" is fully explained if pred 5 alone is already ≈ pred 10. A flat glucocorticoid dose-response between 5 and 10 mg/kg in rat AIA is plausible, and this design cannot exclude it.
- So C3 alone **cannot prove sparing**. Sparing needs C3 (combo not worse than pred 10) **and** evidence that pred 5 alone is worse than pred 10, which this design lacks.
- C4 (PEA dose trend) is partial, indirect support only.
- **Zero-added-cost fix:** replace the PEA/Pred 100/5 arm with prednisolone 5 alone. It is still 9 groups at the same cost.
  - This gives a 2×2 core: CFA (0/0), Pred 5 (0/5), PEA 200 (200/0) and combo 200/5. The 50/5 arm keeps a two-point PEA dose trend.
  - It allows a direct "PEA adds to pred 5" contrast (combo vs pred 5), which is well powered if d ≥ 1.5.
  - The interaction (synergy) contrast stays underpowered: an interaction needs roughly 4× the n of a main effect of the same size. Say so; do not claim synergy.
  - This changes an approved protocol, so it needs supervisor or committee sign-off. The main agent or the user decides; I only flag it.

**Can C3 be framed as non-inferiority or equivalence?** Formally yes, but be honest about the cost.
- Non-inferiority H0: combo is worse than pred 10 by ≥ M. Use one-sided α = 0.025 and 80% power, assuming a true difference of 0. Define M as a fraction of the pred-10-vs-CFA effect.

| Variance assumption | Margin M (fraction of pred effect) | M in SD units | n/group |
|---|---|---|---|
| S5 (tiny SD, d_pred = 4.47) | 50% | 2.23 | 5 |
| S5 | 30% | 1.34 | 10 |
| S5 | 20% | 0.89 | 21 |
| S6 (realistic, d_active = 1.47) | 50% | 0.73 | 31 |
| S6 | 30% | 0.44 | 83 |
| S6 | 20% | 0.29 | 184 |

- Equivalence (two one-sided tests) needs even more.
- **Verdict: confirmatory non-inferiority is not feasible within budget** unless in-house variance is as low as S5 reports. The pilot SD decides this.
- A 50% margin ("retains half of prednisolone's effect") is too generous to call "sparing" convincingly.
- Recommended wording: report C3 as an **estimate with 95% CI** and state which margin the CI excludes. For example: "the upper CI bound excluded a loss of more than X% of the prednisolone effect". Call it *exploratory non-inferiority*, not a confirmed equivalence. Never read a non-significant C3 as "equivalent" (absence of evidence).

---

## 3. Analysis methods

**Longitudinal paw and score data**
- Primary: a per-animal **summary measure** (trapezoidal AUC from Day 16 to 45, or the mean of post-baseline values), analysed by ANCOVA with the Day-15 value as covariate and planned contrasts (S7).
  - This is robust, simple, free in R or GraphPad, and turns the time course into one number per animal.
- Sensitivity: a **linear mixed model** with outcome ~ group × time + baseline and a random intercept (± slope) per animal. In R, use `lme4`/`nlme` with `emmeans` for contrasts.
  - It handles a missed measurement or a dropout without discarding the animal.
  - Prefer it to classical repeated-measures ANOVA, which needs sphericity and complete data.
- Missing data: report the reasons. Do not use last observation carried forward. If an animal dies early, the mixed model uses its available data, and the AUC analysis excludes it with the reason stated.

**Ordinal histology scores (0-3 or 0-4 per feature; composite sum)**
- Per-feature scores are ordinal. Use **Kruskal-Wallis, then Dunn's test with Holm adjustment** on pre-specified pairs only (C1-C3, plus vs CFA). Alternatively, use **proportional-odds ordinal regression** (R `ordinal::clm`), which supports the same planned contrasts and gives odds ratios with CI.
- A composite with many levels (for example 0-20) may be analysed as continuous if the residuals behave, but say so and show the non-parametric result as sensitivity.
- Use a blinded scorer. A second blinded scorer should read a random 20% of slides, with weighted kappa reported (zero cost).

**Unit of analysis = the animal**
- Average multiple microscopic fields, sections or both knees to one value per animal. Average duplicate ELISA wells to one value; they are technical replicates (S2).
- Oral gavage is individual, so the animal is the experimental unit. Do **not** house one group per cage, though, or cage effects get confounded with treatment. Mix groups across cages, or at least spread cages across rack positions (ARRIVE 4b).
- Spread treatment groups across ELISA plates and staining batches (already in the 09-06 file; correct).

**Reporting**
- Report mean or median, SD (not SEM), the effect estimate with 95% CI for every planned contrast, and exact p values.
- Show individual data points (dot plots).
- Report n analysed per group with reasons for every exclusion (ARRIVE 3b; S2).

---

## 4. Audit of section 4 of `Refaat-What-to-Assay-and-Novelty-2026-09-06.md`

| # | Claim (summary) | Verdict | Reason |
|---|---|---|---|
| 4.1 | 36 pairwise comparisons (9×8/2). Tukey controls FWER only within one outcome, so each outcome needs its own multiplicity plan | **Correct, needs nuance** | The arithmetic is right. Tukey's control is per outcome, which is right. The real fix is not "a multiplicity plan for every outcome". It is **one primary outcome plus a small confirmatory family**; everything else is labelled secondary or exploratory, with within-outcome Dunnett. Also, Tukey all-pairs is the wrong tool here regardless: it tests questions the design does not ask. |
| 4.2 | Pre-specify the primary outcome. Use Dunnett for "all vs one control" and planned contrasts for the therapeutic question | **Correct, needs nuance** | It does not say *which* control. Dunnett vs CFA tests efficacy, **not sparing**; the sparing question is combo vs **Pred 10**, as a planned contrast or Dunnett with Pred 10 as reference. It also omits the assay-sensitivity contrast (Pred 10 vs CFA) and the PEA dose-trend contrast. Planned a priori contrasts are exempt from BJP's F-gate, and that should be stated. |
| 4.3 | Longitudinal data need repeated-measures or mixed-effects analysis, not one-way ANOVA on the endpoint only | **Needs nuance (partly wrong)** | A mixed model is a good choice. But a **summary measure (AUC) analysed by one-way ANOVA/ANCOVA is fully valid** and is the classic recommendation (S7). An endpoint-only analysis is not invalid either; it is just less efficient and must be pre-specified. Classical repeated-measures ANOVA is the weakest option (sphericity, complete-case). |
| 4.4 | Histology score is ordinal, so use Kruskal-Wallis with corrected post hoc or an ordinal model, not a continuous variable by default | **Correct** | Add: Dunn's test with Holm on *pre-specified* pairs only. A many-level composite may be treated as continuous, with justification and a non-parametric sensitivity analysis. Use a blinded second scorer with weighted kappa. |
| 4.5 | "n=10/group is not a power justification by itself"; state the effect size before claiming adequacy for any comparison other than vs disease control | **Correct, needs nuance** | The premise is wrong: **the protocol never states n=10**. The file's "N=90" (section 3) is an AI assumption that the user may have adopted. The effect size must be stated for vs-CFA comparisons too; those happen to be large (d ≈ 2.5-6.6 in S5/S6). Missing points: Mead gives only n=3 for k=9 (unusable), the BJP n≥5 floor, attrition handling, and the fact that combo vs pred 10 needs ≥20/group for superiority under realistic variance. |
| 4.6 | The animal is the unit of analysis; multiple sections or fields per animal do not raise biological n | **Correct** | Add: duplicate ELISA wells are technical replicates (S2), and cage/batch confounding must be avoided (ARRIVE 4b). |
| Missing | — | **Omissions** | (i) The **missing Pred-5-alone arm** limits the sparing inference. Section 6د of the same file handles the wording but not the statistics; the zero-cost swap is in section 2 above. (ii) No randomisation, allocation concealment or blinding procedure. (iii) No baseline (Day-15) covariate. (iv) No non-inferiority margin, or admission that one is infeasible. (v) No reporting of CI and effect size. |

---

## 5. Randomisation, allocation concealment and blinding at zero cost (ARRIVE 2.0 items 2-5, S3; S2)

1. **Day 0, before induction:**
   - Ear-punch or tail-mark every rat with a number.
   - A person **not involved in dosing or scoring** (for example a colleague or a supervisor) generates the sequence in R: `set.seed(<date>); sample(...)`. A free online generator also works. Keep the seed.
   - Use the sequence to assign rats to "paraffin-oil control" vs "CFA" in a 1:8 ratio.
2. **Day 15, after induction and before the first dose:**
   - Score every rat blinded.
   - Apply the **pre-registered responder criterion**, for example contralateral paw swelling ≥ X% or score ≥ Y. Fix X and Y from the pilot.
   - Rank responders by Day-15 score and form blocks of 8 consecutive ranks. Within each block, randomly assign one rat to each of the 8 induced arms (blocked, stratified randomisation). Groups then start balanced on disease severity at no cost.
3. **Allocation concealment:**
   - The sequence holder keeps the key, a paper list in a sealed envelope or a password-protected file.
   - The sequence holder prepares the drug suspensions in **coded opaque tubes** (letters A to I) on a fixed weekly schedule. Same vehicle, same volume (mL/kg) for every arm, including CFA control (vehicle) and paraffin control.
4. **Blinding:**
   - The dosing person knows only the codes.
   - Paw measurement and arthritis scoring are done by a person who does not dose and does not know the codes.
   - Histology, IHC and ELISA samples are relabelled with a **second random code** before dispatch to Cairo/Tanta, so the outside lab cannot infer groups from sequential numbers.
   - The statistician or analyst works on coded data. The key is broken only after the dataset is locked and exclusions are finalised.
   - State honestly where blinding is impossible. Steroid-treated rats may lose weight visibly, and S2 accepts justified exceptions. Record who knew what at each stage (ARRIVE 5).
5. **Order and position effects (ARRIVE 4b):**
   - Dose and measure in randomised or rotating order, not group by group.
   - Mix groups across cages and rack positions.
   - Run each ELISA plate and staining batch with all groups represented.
6. **Equal group sizes** by design (S2). Report every exclusion with group and reason (ARRIVE 3b).
7. **Write it down before Day 0:**
   - A one-page dated analysis plan stating the primary outcome, C1-C4, the margin for C3, the responder criterion, exclusion rules and the software.
   - Upload it to OSF (free) or attach it to the protocol file.

## Assumptions stated

- Effect sizes come from two published studies with different strain, sex, induction route and reference drug. The S5 SDs look implausibly small, so the halved-d rows are the realistic planning case.
- The 80% power and α levels are conventional choices.
- The non-inferiority calculations assume a true difference of 0. If the combination is truly slightly worse, the n is larger.
- Attrition and responder rate are unverified for this route; take them from the pilot.
