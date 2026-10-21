# Study cards — patient & genetic studies (2026-10-06)

Every number below appears verbatim in `papers/<Key>.md` (grep-checked) and in the raw PDF text (`papers/text/<Key>.txt`).
⚠️ = caution before citing.

## Metformin

### Abdallah2021 — Int Immunopharmacol
- **Design:** randomized, double-blind, placebo-controlled trial; single centre (Menoufia, Egypt); NCT04068246
- **n:** 120 randomized (60 metformin + MTX, 60 placebo + MTX); 12 dropped out (6 per group)
- **Population:** active RA, non-diabetic, aged 24–58 years, on MTX
- **Dose:** XR metformin 1000 mg once daily + MTX 7.5 mg IM weekly
- **Duration:** 12 weeks
- **Results:**
  - ACR20: 80.8% vs 54.7% (p = 0.001; NNT = 3.75)
  - ACR50: 32.1% vs 13.5% (p = 0.0047)
  - ACR70: 16.4% vs 6.8% (p = 0.0038)
  - DAS28-3 (CRP) change: −2.4 vs −1.6
  - HAQ-DI change: −0.49 vs −0.38 (p = 0.0022)
  - TNF-α: 27.58 → 8.27 vs 26.22 → 16.89 pg/mL (between-group p = 0.01)
  - IL-6: 78.52 → 29.75 vs 73.2 → 45.46 pg/mL (p = 0.002)
  - IL-17A, NF-κB and MDA fell more; IL-10 rose more (all between-group p ≤ 0.002)
  - Safety: no serious adverse effects
- **Limitations (authors):** small sample; single region; no radiographs; only 12 weeks
- ⚠️ MTX 7.5 mg/week is a low dose. Signs in some Table 3 cells (DAS28-ESR, CRP) are garbled in the PDF. In the DAS ≤5.1 subgroup, LDAS was 53.7% vs 85.7%, favouring placebo, yet the text calls it an increase.

### Naffaa2020 — Scand J Rheumatol
- **Design:** retrospective population-based cohort (Maccabi, Israel); new metformin users
- **n:** 113 749 users; 558 incident RA cases; 908 121 person-years
- **Dose:** mean daily dose ≤850 / 1700 / ≥2550 mg; adherence measured as PDC
- **Duration:** initiation 1998–2014; mean follow-up 8.0 ± 4.9 years
- **Results (adjusted HR):**
  - PDC 40–59% vs <20%: 0.62 (0.45–0.84)
  - PDC 60–79%: 0.72 (0.55–0.95)
  - PDC ≥80%: 0.79 (0.62–1.00)
  - Dose ≥2550 vs ≤850 mg: 0.62 (0.46–0.84)
  - Dose 1700 vs ≤850 mg: 0.76 (0.63–0.92)
  - Women only, PDC 40–59%: 0.51 (0.35–0.75); in men the result was not significant (dose ≥2550 mg HR 0.62, 0.36–1.07)
- **Limitations (authors):** no clinical confirmation of RA; ACPA missing for most cases; possible surveillance bias; mostly people with T2DM
- ⚠️ The association does not rise steadily with adherence (it is strongest at 40–59%). The study was funded by Pfizer, AbbVie and Janssen.

## Statins

### McCarey2004 (TARA) — Lancet
- **Design:** randomized, double-blind, placebo-controlled trial; single centre (Glasgow, UK); intention-to-treat analysis
- **n:** 116 (58 vs 58)
- **Dose:** atorvastatin 40 mg/day, added to existing DMARDs
- **Duration:** 6 months
- **Results:**
  - DAS28: −0·5 vs 0·03; difference −0·52 (95% CI −0·87 to −0·17), p = 0·004
  - EULAR response: 31% vs 10%; OR 3·9 (1·42–10·72), p = 0·006
  - CRP fell 50% and ESR fell 28% relative to placebo
  - Swollen joint count: −2·69 vs −0·53 (p = 0·0058)
  - IL-6: p = 0·028
  - HAQ and tender joint count: no effect
- **Limitations (authors):** small, single centre; imbalance in methotrexate use (50% vs 26%), with the result unchanged after adjustment; statins may lower hepatic CRP directly; the effect is modest

### Tang2011 — J Lipid Res
- **Design:** randomized open-label trial without placebo, plus in-vitro Treg work
- **n:** 55 patients with RA (28 atorvastatin, 27 no atorvastatin) + 42 controls; Wuhan, China
- **Dose:** atorvastatin 20 mg/day, added to stable DMARDs
- **Duration:** 12 weeks
- **Results:**
  - DAS28: −0.41 vs −0.03 (p <0.001)
  - hs-CRP: −5.41 vs −0.06 mg/l (p <0.001)
  - ESR: −5.46 vs 0.03 mm/h (p 0.005)
  - IL-6: not significant (p 0.104)
  - Treg cells rose to 6.8% ± 1.9% vs 5.2% ± 1.1% of CD4+ cells (p < 0.05)
- ⚠️ Open-label design. The DAS28 fall (−0.41) is below the 0.6 threshold for a clinically relevant change. Adverse events were not reported.

### Hu2024 — Lipids Health Dis (replaces Qiao2024, which has no full-text access)
- **Design:** drug-target Mendelian randomization (TSMR + SMR + MVMR); European ancestry
- **n (RA GWAS):** discovery 5,539 cases / 20,169 controls; replication from FinnGen (seropositive RA)
- **Results:**
  - Genetically proxied HMGCR inhibition → lower RA risk: discovery OR = 0.45 (95%CI: 0.32, 0.63), P = 6.79 × 10⁻⁰⁶; replication OR = 0.37 (95%CI: 0.23, 0.61)
  - SMR in whole blood: OR = 0.48 (0.29, 0.82)
  - Other targets (NPC1L1, PCSK5, APOB, LDLR, CETP and others): no effect on RA
- **Limitations (authors):** European data only; genetic lifetime effect ≠ short-term drug effect; low colocalization probability (H4 22.22%)
- ⚠️ The MVMR value "OR = 0.33, 95%CI: 0.40, 0.96" is internally inconsistent (the OR lies outside its own CI). Do not cite it.

## Fenofibrate

### Goto2010 — Mod Rheumatol
- **Design:** randomized open comparative trial, fenofibrate vs statins; no placebo, no blinding; single centre (Japan)
- **n:** 44 patients with RA and dyslipidaemia (fenofibrate 23, statins 21)
- **Dose:** fenofibrate 200 mg/day; statin dose not reported (17 of 21 on atorvastatin)
- **Duration:** 6 months
- **Results (fenofibrate):**
  - Patient VAS: 49.1 ± 24.7 → 14.7 ± 11.2 mm (p < 0.0001)
  - Prednisolone dose: 3.6 → 2.0 mg/day (p = 0.0098)
  - Lipids: TC, LDL-C and TG fell; statins did not change them significantly
  - CRP and ESR: no significant change in either group
  - Safety: no adverse drug reactions
- ⚠️ No DAS28 or joint counts. The PDF symbols (→, <) were restored by standard mapping without a visual check.

### Shirinsky2013 — Rheumatol Int
- **Design:** open-label, single-arm, uncontrolled pilot study (Novosibirsk, Russia)
- **n:** 27 enrolled; 25 completed
- **Dose:** fenofibrate 145 mg/day, added to stable DMARDs (mostly MTX)
- **Duration:** 12 weeks
- **Results:**
  - DAS28 (median): 6.28 → 4.83
  - EULAR good/moderate response: 15 (60 %)
  - ACR20: 10 (40 %)
  - CRP: 20.35 → 12.2 mg/l (p 0.025)
  - IL-6: 7.58 → 3.6 pg/ml (p 0.0464)
  - TG and TC fell; HDL rose
  - Safety: 2 withdrawals for back pain; no serious adverse events
- **Limitations (authors):** small, uncontrolled, open-label; no correction for multiple comparisons

## Pioglitazone

### Hsieh2021 — Int J Clin Pract
- **Design:** nationwide case–control study; Taiwan NHIRD; controls matched 1:4 by propensity score
- **n:** 3,605 cases + 14,420 controls (all with T2DM)
- **Exposure:** the TZD class as a whole (pioglitazone not separated from rosiglitazone); cumulative DDD in the 2 years before the index date
- **Results (adjusted OR):**
  - Overall: 0.91 (95% CI 0.81–1.02), not significant
  - >365 cDDDs: 0.85 (0.73-1.01)
  - P for trend: 0.042
  - Sensitivity analysis with a 90-day lag, >365 cDDDs: 0.75 (0.63-0.89)
- **Authors' conclusion:** "TZD use might reduce the risk of RA in patients with T2DM, but it was non-statistically significant."
- **Limitations (authors):** smoking not recorded (COPD used as a proxy); obesity approximated by hyperlipidaemia
- ⚠️ Reports OR, not HR. In Table 3, the 31–90 cDDDs row reads 0.67(0.64-1.18), so the OR lies outside its own CI. Do not cite that row.

### Ormseth2014 — Arthritis Rheumatol
- ⚠️ **Not a new study:** the same 34-patient crossover trial as [Ormseth2013], with vascular outcomes reported separately. Do not count it as a separate row in Table 3.
- **Dose:** pioglitazone 45mg daily vs placebo, 8 weeks per period, with a 4-week washout
- **Results:**
  - Augmentation index: −4.7% units (95% CI, −7.9, −1.5% units), P=0.004
  - Diastolic blood pressure: −3.0 mmHg (−5.7, −0.2 mmHg), P=0.03
  - Aortic pulse wave velocity: no change (P=0.33)
  - Endothelial function (reactive hyperemia index): no change (P=0.46)
  - These effects were not mediated by the improvement in insulin resistance or inflammation

## Human equivalent doses (HED) — Claude, 2026-10-07

Method: FDA body-surface-area conversion, HED (mg/kg) = animal dose × animal Km / 37 (mouse Km 3, rat Km 6); daily human dose for 60 kg. Cite as Nair & Jacob 2016 (J Basic Clin Pharm, open access) — download at START-HERE item 5.
⚠️ Estimates for the review text only. Mark "approximately"; route differences (i.p./i.v. vs oral) must be stated.

| Study | Species, route | Animal dose | HED (60 kg) | Usual clinical dose | Verdict |
|---|---|---|---|---|---|
| Son2014 metformin | mouse, oral, 3×/week | 5 mg/mouse (weight not stated; 20–25 g → 200–250 mg/kg) | ~970–1,220 mg per dose | 500–2,550 mg/day | within range (estimate) |
| Fan2020 metformin | rat, i.p., every 3 days | 100 mg/kg | ~970 mg per dose | 500–2,550 mg/day | within range; i.p. |
| Walker2017 statins | mouse, i.v., 3 doses | 0.2 mg/kg | ~1 mg | atorvastatin 10–80 mg/day | far below clinical |
| Vandebriel2012 atorvastatin | mouse, oral | ≈10 mg/kg (stated by authors) | ~49 mg/day | 10–80 mg/day | within range |
| Vandebriel2012 pravastatin | mouse, oral | 0.8 mg/day ≈ 40 mg/kg (estimate, same ratio) | ~195 mg/day | 10–80 mg/day | ~2.4× max (estimate) |
| Castillero2012 fenofibrate | rat, oral | 300 mg/kg/day | ~2,900 mg/day | 145–200 mg/day | ~15× max |
| Koufany2008 pioglitazone | rat, oral | 30 mg/kg/day (only effective dose) | ~290 mg/day | 15–45 mg/day | ~6.5× max |
| Roy2017 pioglitazone | rat, oral | 1.35 mg/kg/day | ~13 mg/day | 15–45 mg/day | below clinical (may explain null effect alone) |
| Roy2017 MTX | rat, oral | 0.225 mg/kg/day | ~2.2 mg/day (~15 mg/week) | 7.5–25 mg/week | within range |
| Wang2013 losartan | rat, oral | 10–15 mg/kg/day | ~97–146 mg/day | 25–100 mg/day | at/just above max |
| AbdelElGaphar2018 losartan | rat, oral | 20 mg/kg/day | ~195 mg/day | 25–100 mg/day | ~2× max |
| ElDemerdash2025 dapagliflozin | rat, oral | 1 / 5 / 10 mg/kg/day | ~10 / ~49 / ~97 mg/day | 10 mg/day | 1 mg/kg ≈ clinical; best dose ~10× |

## Source audit — Claude, 2026-10-07
Crossref check of all 55 DOIs in `papers/`: **0 retractions**. One correction (Zhang2023, notice 10.1186/s40001-023-01573-x, 2023-12-16) — read it before citing any number.
  - ✅ Read 2026-10-07: the correction changes **only the ethics statement** (approval HPHP-2018-0095 → Hunan Provincial People's Hospital [2023]-59). No numbers changed. Caution: a 2023 approval for a prospective cohort may draw a reviewer question; cite as is.

| Key | Problem | Action |
|---|---|---|
| Malemud2013 | J Clin Cell Immunol = OMICS (FTC ruling 2019, $50M, predatory) | ❌ drop; use Ding2023 / Kondo2021 / Gao2024 for pathophysiology |
| Sarabi2016 | Electronic Physician: not MEDLINE, PMC inactive since 2018 | ❌ do not cite (not in drafts yet) |
| Kumar 2023 (IJHCR) + Kumar 2024 (J Cardiovasc Dis Res) | metformin RCTs inside Alshammari 2026 meta-analysis; low-quality venues | ❌ do not cite directly; cite the meta-analysis with this caveat |
| Chen 2020 preprint (10.21203/rs.2.23894/v1) | Research Square preprint, marked ✅ in `metformin.md` | cite only the published Chen2020 (Mol Ther Methods Clin Dev) |
| Fan2020 | Ann Transl Med delisted from Web of Science 2023 (article from 2020) | ⚠️ keep only alongside Son2014; never as sole support |
| Cardoso2018 | Open Rheumatol J (Bentham Open), low tier, in vitro only | ⚠️ keep as supporting, not key evidence |
| Shahin2011, AbdelElGaphar2018, Roy2017, Mostafa2020 | low-tier but legitimate (Scopus-indexed) | ✅ OK; AbdelElGaphar2018 needs its DOI/URL for the reference list |
| Zhou2012, Son2014 | Hindawi journals (PPAR Res, Mediators Inflamm) | ✅ OK (still indexed); avoid adding more Hindawi mechanistic papers |

## Similar published work — full texts in `papers/` (read 2026-10-07)

### Alshammari2026 — BMC Rheumatol (SR/MA, PROSPERO CRD420251271612)
- **Scope:** metformin as adjunct to csDMARDs only; 4 RCTs, n = 350 (Gharib2021, Abdallah2021, Kumar 2023, Kumar 2024); Egypt + India only; ≤ 6 months
- **Results (Table 3, random effects):**
  - CRP at 3 months: MD −5.99 mg/L (−7.46 to −4.52), 4 RCTs, moderate certainty
  - CRP at 6 months: MD −6.96 (−7.79 to −6.13), 3 RCTs
  - DAS28 at 3 months: MD −0.80 (−0.87 to −0.73), 3 RCTs, high certainty
  - HAQ-DI at 3 months: MD −0.12 (−0.19 to −0.05)
- **Authors' gaps:** no radiographic scores, no CV endpoints, short trials, only 1 double-blind trial
- ⚠️ Abstract says CRP MD −5.55 but Table 3 and text say −5.99 → cite −5.99. Both Kumar trials = high risk of bias (RoB 2), no registration. They cite Liang as "2025" (it is 2023) and Gharib as n = 60 (we use our own cards). Cite only the pooled numbers; take trial details from the primary papers.

### Nallathambi2024 — Mediterr J Rheumatol (narrative review)
- **Scope:** metformin + SGLT2i across all rheumatic diseases (RA, SLE, AS, Sjögren, psoriasis, SSc, gout); search Nov 2023
- **What it gives us:** confirms no RA clinical data for SGLT2i at that date (SGLT2 evidence = SLE/gout only) → supports our SGLT2 gap sentence together with Yen2026
- **Leads (metformin preclinical, for Table 1 if needed):** Kang 2013 Int Immunopharmacol (EKB) · Kim 2018 Exp Mol Med (OA) · Yang 2017 Int J Clin Exp Med (weak venue, skip) · Makar 2020 Benha Med J (Egyptian, weak, skip)
- ⚠️ Low-tier journal; cite once, in the gap paragraph only.

### Buonanno2026 — J Pers Med (scoping review, PRISMA-ScR, not registered)
- **Scope:** GLP-1 RAs in RA only (disease activity, RA risk, CV comorbidity)
- **What it gives us:**
  - mechanism leads (all in vitro RA-FLS, 2019): Zheng — dulaglutide, Int Immunopharmacol (EKB) · Tao — exenatide, IUBMB Life (EKB) · Du — lixisenatide, Int Immunopharmacol (EKB) → replaces Israel2026 as mechanism source
  - human lead: WangQ2025 (downloaded, card below)
  - "biphasic" reading of Israel2026 (higher RA risk ≤ 6 months, attenuated later) — useful for Challenges
- ⚠️ Most RA data in it are conference abstracts (Stipho, Dente, Loizidis, Beltagy, Gavazova) → do NOT cite abstracts.

### WangQ2025 — Clin Rheumatol (OA, PMC12568834)
- **Design:** retrospective cohort, TriNetX; RA + T2DM; new GLP-1 RA vs DPP-4i users; propensity matched; 5-year follow-up
- **n:** 41,153 (25,425 GLP-1 vs 15,728 DPP-4i); 8,697 per group after matching; median age 65, 70% women
- **Result:** all thromboembolic events HR 0.76 (0.70–0.83), p < 0.0001; lower MI, stroke, DVT and all-cause mortality
- ⚠️ Outcome is CV/thrombosis, not RA activity → use in GLP-1 section as cardiometabolic benefit and in 4.5 synthesis; word as "associated with".

### Our gap (intro, item 16)
None of these covers antidiabetics + lipid-lowering + ARBs together, gives HED for animal doses, covers safety with MTX/steroids, or compares drugs by shared pathway.

## Item 5 additions — Claude, 2026-10-07

### Mechanism sources (replace non-laboratory citations)

| Draft sentence | Old source (design) | New source | Status |
|---|---|---|---|
| Day1 statins ¶1: isoprenylation of Ras/Rho | Chodick2010 (cohort), ElBarbary2010 (trial) | Greenwood2006, Nat Rev Immunol, 10.1038/nri1839 — mechanism review ("protein prenylation") | ⬜ free on PMC (PMC3842637) |
| Day1 statins ¶1: IFN-γ-induced MHC-II ↓ | Chodick2010 (cohort) | Kwak2000, Nat Med, 10.1038/82219 — laboratory study; abstract confirms IFN-γ-induced MHC-II repression | ⬜ EKB |
| Day1 4.2 intro: CV risk in RA | Kitas2019 (trial) | Hansildaar2021 — "independent risk factor"; "up to a two-times higher risk" | ✅ in papers/ |
| Day3 GLP-1 ¶1: cytokines and NF-κB in joint cells | Israel2026 (case-control) | Zheng2019 (dulaglutide, RA-FLS); backups Tao2019, Du2019 | ⬜ EKB |
| Day3 GLP-1 ¶1: GLP-1R on T/B cells, monocytes, macrophages; M2 shift | Israel2026 (case-control) | Bendotti2022, Pharmacol Res, 10.1016/j.phrs.2022.106320 — review | ⬜ EKB |
| Day3 GLP-1 ¶1, first sentence: insulin, glucagon, gastric emptying | Israel2026 | Drucker2018, Cell Metab, 10.1016/j.cmet.2018.03.001 — review | ⬜ EKB (optional) |
| HED method | — | NairJacob2016 | ✅ in papers/ (OA) |

⚠️ FLS papers show effects on synovial fibroblasts, not on T/B cells or macrophages. Keep the two claims apart, each with its own source.

### Malik2026 — Eur Heart J Cardiovasc Pharmacother (OA, PMC13588637)
- **Design:** target-trial emulation, TriNetX US; obese adults with T2DM + RA, primary prevention; semaglutide vs non-GLP-1RA second-line drugs; PS matching 1:1
- **n:** 1017 vs 1017 after matching; women 81.3% vs 81.0%; follow-up up to 2 years
- **Results:**
  - MACCE: 12.7% vs. 16.5%; HR, 0.75; 95% CI, 0.60–0.94; P = 0.01
  - Heart failure: HR, 0.69, 95% CI, 0.53–0.91
  - DMARD escalation: HR, 0.75; 95% CI, 0.60–0.90; P = 0.003
  - No difference in all-cause mortality, MI or stroke
- ⚠️ Benefit driven by heart failure. DMARD escalation is an EHR proxy, not a disease-activity measure (authors say so). Word as "associated with".

### Kachhadia2026 — J Clin Med Res (OA, PMC13278687)
- **Design:** retrospective cohort, TriNetX US; RA + T2DM; SGLT2i vs DPP-4i; PS matching 1:1
- **n:** 823 SGLT2i, 284 DPP-4i → 277 matched pairs
- **Results:**
  - MACE: 43.0% vs. 48.7%; odds ratio 0.792, 95% CI: 0.567– 1.107; P = 0.172 (not significant)
  - Cox HR 1.284 (95% CI: 0.998–1.652) — authors call it non-interpretable (proportional hazards violated)
- ⚠️ Small, unequal follow-up (median 3.1 vs. 6.4 years), low-tier journal. Use only to say RA data on SGLT2i are sparse and inconclusive.

### Tsushima2026 — J Diabetes Investig (OA, PMC13398639)
- **Design:** target-trial emulation, Japanese claims; IMID + T2DM; SGLT2i vs metformin new users; IPTW
- **n:** 1,845 SGLT2i vs 1,499 metformin; RA = 65.0% vs. 68.2%
- **Results:**
  - UTI: HR 1.14, 95% CI 0.84–1.55
  - Genital infection: HR 2.31, 95% CI 1.16–4.63
  - No effect modification by immunosuppressants or glucocorticoid dose
- ⚠️ Mixed IMIDs, not RA only. The RA-only study is Dobashi2026 (Rheumatology, EKB) → prefer it; this one is backup for Challenges (safety with steroids).

### Second-hand citation fixes — Claude, 2026-10-07 (START-HERE item 5.1)
Each original was taken from the reference list of the paper that made the second-hand claim, and checked against its Europe PMC record.

| Draft sentence | Second-hand source | Original | Access |
|---|---|---|---|
| Day1 metformin: AMPK activation | Son2014 intro (ref 4) | Zhou2001, J Clin Invest, 10.1172/JCI13505 | free, PMC209533 |
| Day1 metformin: AMPK inhibits mTOR | Son2014 intro ("Metformin-activated AMPK suppresses mTOR") | Gwinn2008, Mol Cell, 10.1016/j.molcel.2008.03.003 — lab study: AMPK phosphorylates raptor, required for mTORC1 inhibition | ✅ in papers/ (free, PMC2674027) |
| Day1 metformin: mTOR → Th17 | Son2014 intro (ref 7) | Nagai2013, Ann N Y Acad Sci, 10.1111/nyas.12059 — review | EKB |
| Day1 statins: HMG-CoA reductase / mevalonate | Ren2023 discussion | Greenwood2006 (already listed) | free, PMC3842637 |
| Day1 statins: earlier CIA studies protective | Vandebriel2012 discussion (refs 13–16) | Leung2003, J Immunol, 10.4049/jimmunol.170.3.1524 · Palmer2004, Arthritis Rheum, 10.1002/art.20673 | free (publisher) · EKB |
| Day1 fenofibrate: PPAR-α agonist | Zhou2012 intro (ref 14) | Varga2011, Biochim Biophys Acta, 10.1016/j.bbadis.2011.02.014 — review | ✅ in papers/ (OA) |
| Day2 pioglitazone: PPAR-γ represses inflammatory genes | Shahin2011 intro (refs 7–10) | Varga2011 | ✅ in papers/ |
| Day2 pioglitazone: insulin resistance ⇄ inflammation | Ormseth2013 abstract | Romeo2012, Arterioscler Thromb Vasc Biol, 10.1161/ATVBAHA.111.241869 — review | free, PMC4784686 |
| Day2 ARBs: ACE up in RA blood and synovium | Wang2013 intro (refs 3–4) | Goto1990, Ann Rheum Dis (blood monocytes) · Walsh2000, Ann Rheum Dis (synovium) | free, PMC1004015 · PMC1753069 |

⚠️ Varga2011 does not mention reactive oxygen species → drop "ROS" from Day2 line 21 rather than add a reference.
⚠️ Varga2011 calls fenofibrate "hypolipidemic", not "triglyceride-lowering" → word Day1 line 54 as "lipid-lowering" or keep Zhou2012 only for its own results.
⚠️ Leung2003 / Palmer2004: confirm dose and route after download (the draft says "often high intraperitoneal doses").
⚠️ Unused second-hand highlights removed from papers/: Chodick2010 (LFA-1), Koufany2008 (PPAR-γ affinity).

### Abstract-only papers (full text not reachable) — 2026-10-07
⚠️ Saved from the Europe PMC abstract. Cite only what the abstract states.

**Dobashi2026 — Rheumatology (target-trial emulation, administrative claims; RA + T2DM)**
- ⚠️ The abstract does not name the country (step 18 checker) → do not write "Japanese" for this study.
- n: 9772 new antidiabetic users (13% SGLT2i initiators, 42% on glucocorticoids); mean 34-month follow-up
- UTI, ITT: "no significant difference between SGLT2i and other antidiabetic drug"
- UTI, as-treated: "adjusted incidence rate ratio 1.64, 95% CI 1.26-2.13"
- SGLT2i × glucocorticoid dose interaction: not significant
- ⚠️ The two analyses disagree → in Challenges, report both: no excess risk by ITT, but higher risk while on the drug. Agrees with Tsushima2026 (no UTI excess, more genital infection).

**Kalantari2024 — Biomed Pharmacother (rats, MTX hepatotoxicity)**
- MTX 20 mg/kg i.p.; empagliflozin 10 or 30 mg/kg/day i.p.
- Empagliflozin improved liver histology, AST/ALT and antioxidant enzymes; the higher dose worked better
- 💊 HED: empagliflozin 10 / 30 mg/kg rat → ~97 / ~290 mg/day for 60 kg vs clinical 10–25 mg/day → ~4–12× max, and i.p. → say so.
- ⚠️ Animal; the abstract gives MTX 20 mg/kg i.p. but does not say "single" (corrected 2026-10-21, step 18) → do not write "single dose". Supporting only.

**Nematalla2026 — J Pharmacol Exp Ther (rats, CFA arthritis; Egyptian group)**
- Liraglutide 75 μg/kg/day i.p. (prevention from day 1, or treatment from day 15 to day 56), alone or + MTX 1 mg/kg/wk i.p.
- Improved joint pathology; suppressed NF-κB/NLRP3/IL-1β and TNF-α/p38 MAPK; corrected the hexokinase 2–succinate–HIF-1α axis; "more pronounced effects when administered in combination with methotrexate"
- 💊 HED: 75 μg/kg rat → ~12 μg/kg → ~0.73 mg/day for 60 kg vs clinical 0.6–1.8 mg/day (diabetes) → **within the clinical range** (i.p. vs s.c.)
- Use: Table 1 + GLP-1 animal sentence; recent (2026); MTX-combination point useful for 4.5 and Challenges.

**Loizidis2026 — Clin Rheumatol (TriNetX cohort; RA + obesity, no diabetes)**
- Semaglutide or tirzepatide vs never-users; 3483 per cohort after matching (68 covariates)
- HF or respiratory failure, days 91–365: 0.7% vs 1.8%; "HR: 0.48; 95% confidence interval (CI): 0.30-0.78; p = 0.002"
- ⚠️ Includes tirzepatide (GLP-1/GIP), small event counts; authors call it hypothesis-generating. Pairs with Malik2026 (HF driven benefit in RA + T2DM) → "two US database studies, with and without diabetes".

## Introduction sources (step 15) — Claude, 2026-10-19
Cards: `.claude/state/step15/cards.txt` (37/37 verbatim). Cautions used in the text:
- **Natalucci2025:** abstract OR 2.38 (1.09–5.54) vs Results OR 2.35 (1.13–5.41) for the same model → cite Results. Same centre as VanMullem2026 (UCLouvain Brussels) → patients may overlap, do not pool.
- **VanMullem2026:** 18.7% D2T is among patients exposed to ≥ 1 b/tsDMARD; glucocorticoid HR 2.47 is from the post-2000 subcohort (498).
- **AlRayes2026:** cross-sectional → associations only, no direction.
- **Almoallim2026:** completers of 3 visits only; "about one in six not in remission" is derived (100 − 83.5).
- **Said2025:** Markov model, Zanzibar, provider perspective, outpatient costs; Tanzania = mortality data only. The background line on low treatment coverage is not an own result.
- **Gebrye2026:** 15 studies in 12 LMICs; pooled medical cost from 9 studies; no Egyptian study.
- **Sertkaya2024 / Mulcahy2025:** cost only, no years-to-approval figure. Pinzi2024 (Front Drug Discov) is a review with uncited figures → not used.
- **Akodad2026:** FDA CDER new-indication approvals; 7.2 years = first approval → repurposing, not compared with de novo development.
- **Barkhane2023:** stroke RR 1.30 has no CI in the text (figure only); diabetes = study-level meta-regression variable.
- Dropped: insulin-resistance sentence (the only 2024 study had no comparator and contradicted itself); metformin/TZD incidence sentence → pointer to Section 4.1, no citation.

### Bilgin2025 — Autoimmun Rev (scoping review, PRISMA-ScR; abstract only, PMID 40617296)
- **Scope:** GLP-1 RAs across rheumatic diseases (RA, PsA, SLE, OA, gout); 52 studies and seven clinical trials
- **What it gives us:** in RA and PsA, clinical impact partly linked to weight loss; most included studies at risk of bias
- ⚠️ Abstract only: cite only the abstract, no numbers beyond 52 and seven. Cited once, Introduction paragraph 4.

### Step 16 notes (2026-10-19)
- Ren2023: 19 = studies in the review; DAS28 pooled from 16 (line 98); Egger P = .012 for DAS28 (line 133); I² 86.0% in text vs 88.1% in Fig 3 caption.
- Pan2024: the only RCT stopped early, 62 patients, high risk of bias (lines 75–79).
- Buonanno2026: not RA-only (also metabolic-population trials); weight-loss caveat is "rather than exclusively" (line 226).
- Nallathambi2024: kept once, in Day3; removed from the Introduction.
- Gap checked against overlap-only reviews too: each covers one class; none converts animal doses to human equivalent doses.

## Step 17 cautions (Section 4.5 comparison) — Claude, 2026-10-20
- **Fu2026 (abstract only):** the class list follows "including", so write "several classes, including …", not "seven classes" as a closed set. "Superior efficacy" only; no species, doses or numbers. Same CIA model as Son2014, so the metformin contrast is within one model.
- **ElDemerdash2025:** rats per group differ between Methods (n = 6, line 73) and the Fig. 2 legend (n = 10, line 160); do not cite a group size. All three doses improved arthritic severity versus untreated rats (line 158).
- **Mostafa2020:** the authors call it randomized, but patients were "sub-classified into three parallel groups according to their associated medical condition" (line 56), and the groups differed at baseline (line 79). Write "described as randomized".
- **Goto2010:** allocation method and masking not reported; write "randomly assigned", never "blinded".
- **Kitas2019 (TRACE RA):** 3,002 patients (line 24), the largest statin trial in the drafts; a checker agent confused it with TARA (116) through an overlap-report quote.

### Step 18 cautions (2026-10-21, Section 5 safety)
- **Kitas2019:** CK and ALT "levels" were 12–15% higher with atorvastatin (line 173, Mann-Whitney) → never "mean". Muscle pain counted as reports, not patients. No subgroup by MTX or glucocorticoid.
- **Tsushima2026:** IMIDs + T2D, not RA only (RA 65–68%); UTI HR 1.14 (0.84–1.55) is "no significant difference", not "similar"; glucocorticoid interaction "no evidence", wide CI; genital infection is a secondary outcome. Interaction analyses were prespecified (line 22).
- **Abdallah2021:** low-dose MTX (7.5 mg/week); AE rates did not differ between groups (line 210), so ALT 15% vs 6.67% is not a liver benefit.
- **Gharib2021:** background csDMARDs; MTX never named → do not tie it to MTX.
- **Shahin2011:** MTX 15 mg/week plus NSAIDs and/or corticosteroids ≤7.5 mg/day was an entry rule; actual steroid use not reported.
- **Shirinsky2013:** uncontrolled open-label pilot; 25/27 on MTX, 12 on prednisolone; safety from patient reports.
- **Mostafa2020:** candesartan: no significant change in liver enzymes; kidney function unchanged in all groups; atorvastatin 20 mg ALT/AST rose but stayed under the upper limit (line 99). Adverse events not mentioned in the text (tables not in the file).
- **Kellner2025:** 29% stopped; reasons GI adverse effects and insurance (non-drug), split not reported; 15% had GI adverse effects.
- **Ormseth2013:** weight +0.76 kg (0.10–1.42) vs placebo; one of two pioglitazone crossover RCTs (Marder2013 is the other).
- **Chodick2010:** the statin mechanism sentences (isoprenylation of Ras/Rho, MHC-II suppression, LFA-1/ICAM-1) sit in its Discussion and cite refs 27, 32, 33 → second-hand; never highlight or cite them as Chodick2010 (the gate flags them). Day1 cites Greenwood2006 and Kwak2000.
