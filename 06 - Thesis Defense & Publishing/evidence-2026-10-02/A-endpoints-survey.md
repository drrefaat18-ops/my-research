# A. Endpoints survey: what a Q1/Q2 journal expects from a rat CFA-AIA drug study

Prepared 2026-10-02. Read-only research. Every paper cited here was checked against its PubMed E-utilities esummary/efetch record or its Europe PMC core record. Endpoints were taken only from text that was retrieved and read (full-text XML or abstract). The source for each paper is marked in Section 3.

Study it applies to: female Wistar rats with CFA adjuvant-induced arthritis (AIA). Treatment Day 16-45 with oral micronized PEA ± prednisolone 5 mg/kg, compared with prednisolone 10 mg/kg, tacrolimus and baricitinib. 9 groups.

---

## 1. Search log (all searches run 2026-10-02)

| # | Engine | Query (exact) | Hits | Used for |
|---|---|---|---|---|
| 1 | PubMed esearch | `Curtis MJ[au] AND Br J Pharmacol[ta] AND experimental design analysis` | 4 | BJP guidance 2015/2018/2022/2025 |
| 2 | PubMed esearch | `Hayer S[au] AND SMASH` | 1 | SMASH |
| 3 | PubMed esearch | `Bolon B[au] AND arthritis models` | 13 | Bolon 2011 |
| 4 | PubMed esearch | `Bevaart L[au] AND arthritis models` | 4 | Bevaart 2010 |
| 5 | PubMed esearch | `Bendele A[au] AND animal models arthritis` | 50 | Bendele (located) |
| 6 | PubMed esearch | `Bendele A[au] AND J Musculoskelet Neuronal Interact[ta]` | 3 | Bendele 2001 |
| 7 | PubMed esearch | `ARRIVE guidelines 2.0[ti]` | 10 | ARRIVE 2.0 |
| 8 | PubMed esearch | `Percie du Sert N[au] AND ARRIVE Essential 10` | 7 | ARRIVE 2.0 (incl. BJP co-publication) |
| 9 | WebSearch | `Curtis 2022 "Planning experiments" BJP guidance III randomisation blinded analysis "group sizes" requirements n=5` | 9 links | Curtis 2022 content (Wiley full text returned 403) |
| 10 | WebSearch | `Curtis 2025 "Guidance on the planning and reporting of experimental design and analysis" British Journal of Pharmacology` | 9 links | Confirms that the 2025 update exists |
| 11 | Europe PMC REST | `(TITLE:"adjuvant-induced arthritis" OR TITLE:"adjuvant arthritis" OR TITLE:"CFA-induced arthritis" OR TITLE:"Freund" OR TITLE:"adjuvant induced arthritis") AND (ABSTRACT:rat OR ABSTRACT:rats) AND PUB_YEAR:[2021 TO 2026] AND SRC:MED AND PUB_TYPE:"journal article" AND HAS_FT:Y` | 89 | Open-access full-text pool (any journal) |
| 12 | Europe PMC REST | `(TITLE_ABS:"adjuvant-induced arthritis" OR TITLE_ABS:"adjuvant arthritis" OR TITLE_ABS:"CFA-induced arthritis" OR TITLE_ABS:"adjuvant induced arthritis") AND (ABSTRACT:rat OR ABSTRACT:rats) AND PUB_YEAR:[2021 TO 2026] AND SRC:MED AND (JOURNAL:"Br J Pharmacol" OR "Biomed Pharmacother" OR "J Ethnopharmacol" OR "Int Immunopharmacol" OR "Phytomedicine" OR "Front Pharmacol" OR "Inflammopharmacology" OR "Eur J Pharmacol" OR "Life Sci" OR "Arthritis Res Ther")` | 171 | Target-journal pool. By journal: Inflammopharmacology 43, Int Immunopharmacol 32, J Ethnopharmacol 31, Phytomedicine 24, Front Pharmacol 21, Biomed Pharmacother 7, Eur J Pharmacol 5, Arthritis Res Ther 3, Life Sci 3, Br J Pharmacol 2 |

Retrieval attempts that failed (stated so they are not mistaken for evidence):
- The Wiley full text of Curtis 2018 and Curtis 2022 returned HTTP 403. Curtis 2018 was then read in full from the PMC website (PMC5843711).
- Curtis 2022 and 2025 have no PMC copy. The 2022 content below comes from a search-engine summary only. The 2025 content was not read.
- The Bendele 2001 PDF returned a 404 on the JMNI site, so only the abstract was read.
- Bevaart 2010 has no abstract in PubMed and no open full text. It was identified and verified, but its content was not read.
- SCImago (used for quartile checks) was blocked by a Cloudflare challenge. **No journal quartile was verified**, so every journal below is "quartile not verified".

How papers were selected. From pool 12, rat in-vivo AIA/CFA studies that tested a drug, extract or compound were chosen by reading titles and abstracts. Up to about 3-8 per journal were taken, spread across 2021-2026. Retracted papers (2), reviews, FLS-only/mechanism-only papers, mouse or CIA studies (PMIDs 39444614 and 42036000 were excluded after reading the abstract) and non-drug studies were excluded. The target journals are mostly paywalled. To get Methods-level data, 19 open-access rat AIA drug papers from pool 11 (other journals) were added to the 10 open-access papers from pool 12. Result: **29 papers read in full text (Methods + Results)** and **30 papers read as abstract only**, 59 in total.

---

## 2. Reporting standards: requirements that affect endpoints, design and analysis

### 2.1 ARRIVE 2.0: the "Essential 10"
Percie du Sert N, et al. *The ARRIVE guidelines 2.0: Updated guidelines for reporting animal research.* PLoS Biol 2020. PMID 32663219, DOI 10.1371/journal.pbio.3000410 (full text read, PMC7360023). The same text was co-published in Br J Pharmacol 2020 (PMID 32662519, DOI 10.1111/bph.15193). Explanation & Elaboration: PMID 32663221, DOI 10.1371/journal.pbio.3000411.

The Essential 10 are the minimum requirement (quoted or closely paraphrased from the guideline table):
1. **Study design.** Name the groups compared, including controls (or give the rationale if there is no control), and state the experimental unit.
2. **Sample size.** Give the exact number of experimental units per group and in total, and *explain how the sample size was decided*, including any a priori calculation.
3. **Inclusion/exclusion criteria.** Say whether they were set a priori. Report every animal or data point excluded per group and the reason.
4. **Randomisation.** State whether it was used and the method used to generate the sequence. Describe how confounders such as treatment/measurement order and cage location were minimised.
5. **Blinding.** State who knew the group allocation at each stage: allocation, conduct, outcome assessment and analysis.
6. **Outcome measures.** Define all outcomes clearly. *For hypothesis-testing studies, specify the primary outcome measure (the one used to determine sample size).*
7. **Statistical methods.** Give the method for each analysis and the software. Say how assumptions were checked and what was done if they were not met.
8. **Experimental animals.** Species, strain/substrain, sex, age, weight, provenance and health status.
9. **Experimental procedures.** What, how, when, how often, where and why, for every group including controls.
10. **Results.** For every experiment, give descriptive statistics with variability (e.g., mean and SD) and, where applicable, the effect size with a confidence interval.

### 2.2 British Journal of Pharmacology design and analysis guidance (Curtis et al.)
Records verified in PubMed:
- Curtis MJ 2015, PMID 26114403, DOI 10.1111/bph.12856 (original guidance; not read).
- **Curtis MJ 2018**, *Experimental design and analysis and their reporting II: updated and simplified guidance for authors and peer reviewers.* Br J Pharmacol. PMID 29520785, DOI 10.1111/bph.14153. **Full text read (PMC5843711).**
- **Curtis MJ 2022**, *Planning experiments: Updated guidance on experimental design and analysis and their reporting III.* Br J Pharmacol. PMID 35673806, DOI 10.1111/bph.15868. Abstract read; body read only through a search-engine summary (Wiley returned 403).
- **Curtis MJ 2025**, *Guidance on the planning and reporting of experimental design and analysis.* Br J Pharmacol. PMID 39865712, DOI 10.1111/bph.17441. Its existence is verified. **Content not read**, so check it before submission.

Rules verified from the Curtis 2018 full text (quotations are exact):
- **n ≥ 5 before any statistics.** "any data set containing groups of n < 5 must not be subjected to statistical analysis, and findings must be labelled as 'exploratory' or 'preliminary'."
- **n means independent units.** "group size is the number of independent values, so one sample run five times is n = 1, not n = 5." Technical replicates (for example ELISA duplicates) do not add to n.
- **Equal groups, randomisation and blinding.** "Studies should be designed to generate groups of equal size, using randomization and blinded analysis where possible (with credible justification if not possible). If group sizes become unequal during a study owing to technical failure this must be explained in the Results." Replacing lost values by pre-defined criteria is encouraged.
- **Triage rejection.** Papers that combine "a lack of randomization and blinding, unequal group sizes, and statistical analysis applied when n is <5 ... will now result in triage rejection."
- **Post hoc tests.** "After ANOVA, post hoc tests may be run only if F achieves the necessary level of statistical significance (i.e. P < 0.05) and there is no significant variance inhomogeneity." Writing only "ANOVA followed by Tukey's test" is not enough.
- **One P threshold.** Define it in Methods and "not varied later in Results (by presentation of multiple levels of significance)".
- **Non-Gaussian data.** Use log-transformation or a non-parametric test. Normalised Western blot and qPCR data need the correct Y-axis label ("fold matched control" or "fold control mean") and the matching type of test.
- **Outliers.** Include them unless exclusion criteria are justified. If outliers will be included, power-analysis n "increased by 50% ... is advisable".
- **Power analysis** sets the minimum n, and using only the minimum carries a high false-negative risk.

Curtis 2022 (abstract plus a secondary summary only; verify against the PDF): the update focuses on "randomisation, blinded analysis and balance of group sizes". The summary says randomisation is *required* in prospective drug studies, with a statement of how it was done; blinded data collection and blinded analysis are expected; n < 5 datasets are exploratory and get no comparative statistics; and technical replicates must be averaged into one independent value.

### 2.3 SMASH recommendations for histological scoring
Hayer S, et al. *'SMASH' recommendations for standardised microscopic arthritis scoring of histological sections from inflammatory arthritis animal models.* Ann Rheum Dis 2021;80:714-726. PMID 33602797, DOI 10.1136/annrheumdis-2020-219247 (full text read, PMC8142455).

- **Models covered: mouse CIA, CAIA, hTNF-Tg197 and rat pristane-induced arthritis (PIA). AIA is not specifically addressed.** The authors say the recommendations are "applicable to any other inflammatory arthritis model". For a rat model, SMASH's own rat example is PIA.
- Rec 1: **do a sample-size calculation** before the experiment (primary outcome, effect size, SD, power, alpha).
- Rec 2: for systemic models, **hind paws (ankle/tarsal joints) rather than front paws**. Rec 10: score ≥3 ankle/tarsal joints on sagittal sections or ≥6 tarsal joints on transverse sections. **Implication: the protocol's knee-only histology departs from SMASH (and from Bolon's Tier 1, below). Either switch to or add the hind-paw ankle, or justify the knee explicitly.**
- Rec 4: paraffin sections, not cryosections. Rec 5: formalin overnight at 4 °C for rats. The text notes that fixation "must not exceed 24 hours" where enzyme activity or delicate epitopes matter (TRAP/IHC). That is relevant to the NF-κB p65 and TLR4 IHC.
- Rec 6: decalcify in 14% EDTA (2-4 weeks for rats) or 5% formic acid. SMASH Table 5 rates EDTA as highly compatible with IHC and formic acid as "not compatible with some epitopes". **For p65/TLR4 IHC, EDTA is the safer choice.**
- Rec 7: H&E, TRAP and Safranin O or toluidine blue are the recommended stains.
- Rec 9: score **synovial inflammation, bone erosion, cartilage destruction and proteoglycan depletion as separate parameters**.
- Rec 11-13: ≥2 non-serial sections per animal, averaged to one value per animal. Ideally the consensus of 2 independent observers. **Blinded analysis** (agreement 9.9/10).
- Rec 14: semi-quantitative score of 0-3 per parameter. Rec 18 and Rec 22 give explicit 0-3 descriptors for inflammation and for bone erosion.
- Rec 24-25: score cartilage as proteoglycan loss plus erosion **on SafO- or TB-stained sections**. Under SMASH, H&E alone does not give a cartilage score.

### 2.4 Authoritative reviews of rodent arthritis models
- **Bolon B, et al. 2011.** *Rodent preclinical models for developing novel antiarthritic molecules: comparative biology and preferred methods for evaluating efficacy.* J Biomed Biotechnol 2011:569068. PMID 21253435, DOI 10.1155/2011/569068 (full text read, PMC3022224).
  - Rat AIA, CIA and SCW are "preferred models"; "Lesions of AIA are most severe and consistent".
  - **Tier 1 "Routine Screening Tests ... used on all RMIA in our laboratory": total body weight, hind-paw swelling, BMD loss, histopathology.** Body weight and paw swelling are recorded daily from disease onset. Plethysmography is "best suited for massively swollen AIA hind paws".
  - Histology is done on the hind paw (ankle/tarsus): slide 1 H&E (leukocyte infiltration, skeletal erosion, periosteal proliferation); optional cathepsin K IHC; Safranin O or toluidine blue for matrix integrity.
  - Their AIA protocol: animals "randomly assigned to treatment groups (n = 6 to 8)", which they justify by low between-animal variability.
- **Bendele A. 2001.** *Animal models of rheumatoid arthritis.* J Musculoskelet Neuronal Interact 1(4):377-85. PMID 15758488, no DOI in PubMed. **Abstract only.** It names rat adjuvant arthritis among models "with a proven track record of predictability for efficacy in humans" and lists corticosteroids, methotrexate, NSAIDs, cyclosporin A, leflunomide, IL-1ra and soluble TNF receptors as active. The full text was not accessible, so no endpoint recommendations are claimed from it.
- **Bevaart L, Vervoordeldonk MJ, Tak PP. 2010.** *Evaluation of therapeutic targets in animal models of arthritis: how does it relate to rheumatoid arthritis?* Arthritis Rheum 62(8):2192-205. PMID 20506322, DOI 10.1002/art.27503. **Verified record, but content not read** (no abstract and no open full text). Nothing is attributed to it.

---

## 3. Paper extraction table (59 papers: 29 read in full text, 30 read as abstract only)

Quartile is not verified for any journal (SCImago was blocked). "Full text" means the Europe PMC full-text XML was parsed from the Methods heading to the Discussion. Endpoints were found with keyword patterns and then manually adjudicated sentence by sentence for in-vivo context; in-vitro-only and network-pharmacology mentions were removed (see Limitations). "Abstract only" papers were coded by reading the abstract. **An endpoint that is absent from an abstract may still have been measured.**

Endpoint codes: Score = arthritis score/index; Paw = paw volume/thickness/ankle diameter; BW = body weight; JointHist = joint histology (H&E/histopathology; adipose-only histology excluded); SafO/TB = Safranin-O or toluidine blue; uCT = micro-CT; OS = oxidative-stress marker; CBC = haematology; LFT/KFT = liver/kidney function; Spl/Thy = spleen/thymus index; Pain = nociceptive/behavioural tests; IHC/IF = immunohistochemistry or immunofluorescence (any tissue). Design column: whether the Methods text contains a statement on randomisation / blinding / sample-size calculation / ARRIVE (keyword-based, full text only).

| # | PMID | DOI | First author | Year | Journal | Title (truncated) | n/group | Endpoints measured in vivo | Source read | Design statements (Rand/Blind/SampleSize/ARRIVE) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 34295151 | 10.2147/dddt.s320599 | Wang R | 2021 | Drug Des Devel Ther | Qing-Luo-Yin Alleviated Monocytes/Macrophages-Mediated Inflammation in Rats with Adjuvant-... | 8 | Score, Paw, BW, IL1b, IL6, IL10, ACPA, RF, CRP, MDA, GSH, SOD, MAPK, WB, qPCR, ELISA, CBC | Full text | N/N/N/N |
| 2 | 36845667 | 10.2147/dddt.s391606 | Liu J | 2023 | Drug Des Devel Ther | Anti-Arthritic Effect of Edaravone Against Complete Freund Adjuvant Induced Arthritis via ... | 10 | Score, Paw, BW, TNF, IL1b, IL6, IL17, IL10, RF, CRP, MDA, GSH, SOD, CAT, NFkB, ELISA, CBC, LFT/KFT, Spl/Thy | Full text | N/Y/N/N |
| 3 | 36032089 | 10.3389/fimmu.2022.928436 | Umar S | 2022 | Front Immunol | Penta-o-galloyl-beta-d-Glucose (PGG) inhibits inflammation in human rheumatoid arthritis s... | not found | Score, JointHist, uCT, TNF, IL1b, WB, IHC/IF, ELISA | Full text | N/Y/N/N |
| 4 | 34305602 | 10.3389/fphar.2021.692806 | Hu YH | 2021 | Front Pharmacol | α-Mangostin Alleviated Inflammation in Rats With Adjuvant-Induced Arthritis by Disrupting ... | 6 | Paw, BW, IL1b, IL6, MDA, GSH, SOD, WB, qPCR, ELISA, CBC | Full text | N/N/N/N |
| 5 | 34122110 | 10.3389/fphar.2021.683698 | Meng M | 2021 | Front Pharmacol | Anti-Rheumatoid Arthritic Effects of Paris Saponin VII in Human Rheumatoid Arthritis Fibro... | not found | Score, Paw, BW, JointHist, TNF, IL1b, IL6, WB, ELISA, Spl/Thy | Full text | Y/N/N/N |
| 6 | 34393779 | 10.3389/fphar.2021.694507 | Dai W | 2021 | Front Pharmacol | Clinical Evidence-Guided Anti-rheumatoid Arthritis Study of Shuji Tablet in Adjuvant-Induc... | 12 | Score, Paw, BW, JointHist, TNF, IL1b, IL6, ELISA, Spl/Thy | Full text | Y/N/N/N |
| 7 | 35242033 | 10.3389/fphar.2022.810052 | Alzarea SI | 2022 | Front Pharmacol | Butin Attenuates Arthritis in Complete Freund's Adjuvant-Treated Arthritic Rats: Possibly ... | 6 | Score, Paw, BW, JointHist, TNF, IL1b, IL6, IL10, MDA, GSH, SOD, CAT, NO, ELISA, CBC, LFT/KFT | Full text | N/N/N/N |
| 8 | 35401173 | 10.3389/fphar.2022.744915 | Huang D | 2022 | Front Pharmacol | Analgesic and Anti-Arthritic Activities of Polysaccharides in Chaenomeles speciosa. | 10 | Paw, JointHist, TNF, IL1b, IL6, ELISA | Full text | N/N/N/N |
| 9 | 35784680 | 10.3389/fphar.2022.880350 | Zhou Y | 2022 | Front Pharmacol | Antirheumatoid Arthritic Effects of Sabia parviflora Wall. Leaf Extracts via the NF-κB Pat... | 8 | Paw, BW, JointHist, TNF, IL1b, IL6, IL10, NFkB, IHC/IF, ELISA, Spl/Thy | Full text | Y/N/N/N |
| 10 | 37305547 | 10.3389/fphar.2023.1136459 | Sajid-Ur-Rehman M | 2023 | Front Pharmacol | Antiarthritic potential of the butanol fraction of Sesuvium sesuvioides: An in vitro, in v... | 6 | Paw, BW, JointHist, TNF, IL6, MDA, GSH, SOD, ELISA, CBC | Full text | N/N/N/N |
| 11 | 40213683 | 10.3389/fphar.2025.1559744 | Dai Y | 2025 | Front Pharmacol | Gastrodin attenuates rheumatoid arthritis by targeting KAT8 to inhibit the lactylation of ... | 5 | Score, Paw, JointHist, IL6, IHC/IF | Full text | Y/N/N/N |
| 12 | 40932869 | 10.3389/fphar.2025.1615519 | Chen Y | 2025 | Front Pharmacol | Xuetongsu attenuates synovial inflammation in rheumatoid arthritis by inhibiting the IL-23... | 6 | Score, Paw, BW, JointHist, SafO/TB, TRAP, Xray, uCT, IL17, NFkB, WB, IHC/IF, CBC, LFT/KFT | Full text | Y/N/N/N |
| 13 | 37809969 | 10.1016/j.heliyon.2023.e20105 | Zhou Y | 2023 | Heliyon | Carboxyamidotriazole alleviates pannus formation and cartilage erosion in rats with adjuva... | 4 | Paw, BW, JointHist, MAPK, WB, IHC/IF | Full text | Y/Y/N/N |
| 14 | 36482036 | 10.1007/s10787-022-01104-w | Rafik ST | 2023 | Inflammopharmacology | Methotrexate conjugated gold nanoparticles improve rheumatoid vascular dysfunction in rat ... | 10 normal; 40 AIA over 4 arms (~10, inferred) | Paw, JointHist, CRP, IHC/IF, ELISA, CBC, LFT/KFT | Full text | Y/Y/N/Y |
| 15 | 41870773 | 10.1007/s10787-026-02168-8 | Mosaad NEG | 2026 | Inflammopharmacology | Evaluation of the anti-inflammatory effect of ectoine-leflunomide combination in adjuvant-... | 8 | Paw, BW, JointHist, TNF, IL1b, IL10, ACPA, MDA, GSH, NO, NFkB, WB, qPCR, ELISA | Full text | Y/N/N/N |
| 16 | 41989683 | 10.1007/s10787-026-02198-2 | Gowayed MA | 2026 | Inflammopharmacology | Anti-arthritic efficacy of geraniol and methotrexate via miRNA-driven NLRP3 inflammasome s... | 8 | Score, Paw, JointHist, Xray, TNF, IL1b, NFkB, qPCR, IHC/IF, ELISA, LFT/KFT | Full text | Y/Y/N/Y |
| 17 | 39201397 | 10.3390/ijms25168710 | Pružinská K | 2024 | Int J Mol Sci | Astaxanthin, Compared to Other Carotenoids, Increases the Efficacy of Methotrexate in Rat ... | 8-16 | Score, Paw, BW, IL1b, IL17, SOD, CAT, qPCR, ELISA | Full text | Y/N/N/N |
| 18 | 41736485 | 10.1111/jcmm.71030 | Li J | 2026 | J Cell Mol Med | Anti-Arthritic Potential of Pyrazoline Derivative Against Complete Freund's Adjuvant Induc... | 4 | Score, Paw, JointHist, TNF, RF, CRP, MDA, GSH, SOD, CAT, ELISA, CBC, LFT/KFT | Full text | Y/N/N/N |
| 19 | 41268308 | 10.1016/j.jgr.2025.07.001 | Zhou K | 2025 | J Ginseng Res | Total saponins of Panax japonicus alleviate adjuvant-induced arthritis in rats by regulati... | 5-6 (figure legends) | Score, Paw, uCT, IL1b, IL6, WB, IHC/IF, ELISA, CBC | Full text | N/N/N/N |
| 20 | 39669913 | 10.1155/mi/1995952 | Han W | 2024 | Mediators Inflamm | Peptide BG From Bitter Gourd (Momordica Charantia) Improves Adjuvant-Induced Arthritis by ... | 8 | Score, Paw, BW, JointHist, TNF, IL1b, RF, CRP, WB, IHC/IF, ELISA | Full text | Y/N/N/N |
| 21 | 36615560 | 10.3390/molecules28010366 | Zeng W | 2023 | Molecules | The Effective Treatment of Purpurin on Inflammation and Adjuvant-Induced Arthritis. | 8 | Paw, BW, JointHist, TNF, IL1b, IL6, IL10, NFkB, IHC/IF, ELISA, Pain | Full text | Y/N/N/N |
| 22 | 38675650 | 10.3390/molecules29081830 | Zafar F | 2024 | Molecules | Onosma bracteatum Wall Aqueous-Ethanolic Extract Suppresses Complete Freund's Adjuvant-Ind... | 6 | Score, Paw, BW, JointHist, Xray, TNF, IL6, CRP, qPCR, CBC, LFT/KFT, Pain | Full text | N/N/N/N |
| 23 | 33924354 | 10.3390/nu13041268 | Tsiklauri L | 2021 | Nutrients | Bioflavonoid Robinin from Astragalus falcatus Lam. Mildly Improves the Effect of Metothrex... | 8 | Paw, BW, IL17, ELISA, CBC | Full text | N/N/N/N |
| 24 | 37836391 | 10.3390/nu15194108 | Chrastina M | 2023 | Nutrients | Crocus sativus L. Extract (Saffron) Effectively Reduces Arthritic and Inflammatory Paramet... | 9 | Score, Paw, BW, IL1b, IL17, CRP, qPCR, ELISA | Full text | Y/N/N/N |
| 25 | 41379787 | 10.1371/journal.pone.0337472 | Chaichamnong N | 2025 | PLoS One | Anti-arthritic and endothelial protective effects of Derris scandens extract in adjuvant-i... | 10-14 (varies) | Score, Paw, BW, TNF, IL1b | Full text | Y/Y/N/Y |
| 26 | 37520245 | 10.7717/peerj.15532 | Alshehri S | 2023 | PeerJ | Protective effect of fustin against adjuvant-induced arthritis through the restoration of ... | 6 | Score, Paw, TNF, IL1b, IL6, MDA, GSH, SOD, ELISA, CBC, LFT/KFT | Full text | Y/N/N/Y |
| 27 | 34693865 | 10.1080/13880209.2021.1991386 | Si M | 2021 | Pharm Biol | Qingluoyin granules protect against adjuvant-induced arthritis in rats via downregulating ... | 10 | Score, Paw, JointHist, TNF, IL1b, IL6, NFkB, WB, IHC/IF, ELISA, Spl/Thy | Full text | Y/Y/N/N |
| 28 | 37111711 | 10.3390/pharmaceutics15041225 | Faheem MA | 2023 | Pharmaceutics | Chrysin Is Immunomodulatory and Anti-Inflammatory against Complete Freund's Adjuvant-Induc... | 10 | Score, BW, JointHist, TNF, IL10, RF, CRP, NFkB, qPCR, CBC | Full text | N/Y/N/N |
| 29 | 34504248 | 10.1038/s41598-021-97474-2 | Tang Y | 2021 | Sci Rep | Pentahydroxy flavonoid isolated from Madhuca indica ameliorated adjuvant-induced arthritis... | 18 (n=5-6 per assay) | Paw, BW, JointHist, TNF, IL1b, IL6, RF, CRP, MDA, GSH, SOD, NO, NFkB, WB, ELISA, CBC, LFT/KFT, Pain | Full text | N/N/N/Y |
| 30 | 33550047 | 10.1016/j.biopha.2021.111347 | Abdel Jaleel GA | 2021 | Biomed Pharmacother | 'Methyl palmitate attenuates adjuvant induced arthritis in rats by decrease of CD68 synovi... | not in abstract | Paw, BW, JointHist, TNF, IL1b, IHC/IF, Spl/Thy | Abstract only | n/a |
| 31 | 34243601 | 10.1016/j.biopha.2021.111635 | Shirani K | 2021 | Biomed Pharmacother | Comparative evaluation of the protective effects of oral administration of auraptene and u... | not in abstract | Paw, JointHist, TNF, IL17, IL10, NO, ELISA | Abstract only | n/a |
| 32 | 33745959 | 10.1016/j.ejphar.2021.174044 | Lal R | 2021 | Eur J Pharmacol | Activation of the Nrf2/HO-1 signaling pathway by dimethyl fumarate ameliorates complete Fr... | not in abstract | Score, Paw, TNF, IL1b, ACPA, RF, CRP, MDA, GSH, SOD, CAT, NO, NFkB, Pain | Abstract only | n/a |
| 33 | 36608862 | 10.1016/j.ejphar.2023.175490 | Ishikawa G | 2023 | Eur J Pharmacol | Comparison of the effects of peficitinib and tofacitinib in the adjuvant-induced arthritis... | not in abstract | Score, Paw, JointHist, Pain, imaging(BMD/US) | Abstract only | n/a |
| 34 | 39182545 | 10.1016/j.ejphar.2024.176940 | Kulhari U | 2024 | Eur J Pharmacol | Nuciferine inhibits TLR4/NF-κB/MAPK signaling axis and alleviates adjuvant-induced arthrit... | not in abstract | Score, Paw, JointHist, Xray, TNF, IL1b, IL10, MDA, NFkB, TLR4, MAPK | Abstract only | n/a |
| 35 | 35212850 | 10.1007/s10787-022-00930-2 | Akhter S | 2022 | Inflammopharmacology | Nerolidol: a potential approach in rheumatoid arthritis through reduction of TNF-α, IL-1β,... | not in abstract | Paw, BW, JointHist, Xray, TNF, IL1b, IL6, IL10, SOD, CAT, NFkB, qPCR, CBC | Abstract only | n/a |
| 36 | 35764864 | 10.1007/s10787-022-00998-w | Arab HH | 2022 | Inflammopharmacology | Targeting inflammation and redox perturbations by lisinopril mitigates Freund's adjuvant-i... | not in abstract | Score, Paw, JointHist, TNF, IL1b, IL6, IL17, MDA, GSH, NFkB, WB, IHC/IF, ELISA, Pain | Abstract only | n/a |
| 37 | 36542211 | 10.1007/s10787-022-01118-4 | Hannan A | 2023 | Inflammopharmacology | Quercetin-loaded chitosan nanoparticles ameliorate adjuvant-induced arthritis in rats by r... | 5 | Paw, JointHist, TNF, IL6, CBC, LFT/KFT, OS(other/unspecified) | Abstract only | n/a |
| 38 | 37083920 | 10.1007/s10787-023-01229-6 | Afnan A | 2023 | Inflammopharmacology | Chrysin, a 5,7-dihydroxyflavone restrains inflammatory arthritis in rats via subsiding oxi... | not in abstract | Paw, BW, JointHist, TNF, IL1b, IL6, IL10, RF, CRP, MDA, SOD, CAT, NFkB, CBC, Spl/Thy, Pain | Abstract only | n/a |
| 39 | 38748385 | 10.1007/s10787-024-01480-5 | Sial NT | 2024 | Inflammopharmacology | Arbutin attenuates CFA-induced arthritis by modulating expression levels of 5-LOX, NF‑κB, ... | not in abstract | Paw, BW, JointHist, Xray, TNF, IL1b, IL6, IL17, IL10, ACPA, CRP, MDA, GSH, SOD, CAT, NFkB, qPCR, CBC | Abstract only | n/a |
| 40 | 39207636 | 10.1007/s10787-024-01537-5 | Siddique R | 2024 | Inflammopharmacology | Gingerol nanoparticles attenuate complete Freund adjuvant-induced arthritis in rats via ta... | not in abstract | TNF, IL1b, IL6, IL17, RF, qPCR | Abstract only | n/a |
| 41 | 40332704 | 10.1007/s10787-025-01736-8 | Saleem N | 2025 | Inflammopharmacology | Amelioration of pain and adjuvant-induced arthritis by syringic acid via modulation of beh... | not in abstract | Score, Paw, JointHist, Xray, TNF, IL1b, IL6, qPCR, ELISA, CBC, Spl/Thy, Pain, OS(other/unspecified) | Abstract only | n/a |
| 42 | 34836794 | 10.1016/j.intimp.2021.108352 | Wang R | 2021 | Int Immunopharmacol | Mangiferin exert protective effects on joints of adjuvant-induced arthritis rats by regula... | not in abstract | Score, Paw, JointHist, Xray, MDA, GSH, SOD, CAT, NO, IHC/IF | Abstract only | n/a |
| 43 | 35944459 | 10.1016/j.intimp.2022.109068 | Abdel-Rafei MK | 2022 | Int Immunopharmacol | Concerted regulation of OPG/RANKL/ NF‑κB/MMP-13 trajectories contribute to ameliorative ca... | not in abstract | Score, Paw, BW, JointHist, TNF, IL1b, IL6, IL17, IL10, NFkB | Abstract only | n/a |
| 44 | 37130441 | 10.1016/j.intimp.2023.110231 | Abd-Elhalem SS | 2023 | Int Immunopharmacol | Macrophage Polarization Towards M2 Phenotype by Curcuminoids Through NF-κB Pathway Inhibit... | not in abstract | Paw, BW, JointHist, IL1b, IL10, NFkB, IHC/IF, CBC, Spl/Thy | Abstract only | n/a |
| 45 | 37348232 | 10.1016/j.intimp.2023.110517 | Nawaz S | 2023 | Int Immunopharmacol | Linalool: Monoterpene alcohol effectiveness in chronic synovitis through lowering Interleu... | not in abstract | Score, Paw, BW, Xray, TNF, IL1b, IL6, IL17, IL10, qPCR, CBC, Spl/Thy, Pain | Abstract only | n/a |
| 46 | 38971108 | 10.1016/j.intimp.2024.112573 | Liu X | 2024 | Int Immunopharmacol | Tianhe Zhuifeng Gao reverses inflammatory response and attenuates bone/cartilage destructi... | not in abstract | Score, Paw, BW, RF, CRP, Spl/Thy, Pain | Abstract only | n/a |
| 47 | 39837014 | 10.1016/j.intimp.2025.114112 | Li Y | 2025 | Int Immunopharmacol | Targeting p38 MAPK signaling pathway and neutrophil extracellular traps: An important anti... | not in abstract | MAPK | Abstract only | n/a |
| 48 | 33418032 | 10.1016/j.jep.2021.113779 | El-Shiekh RA | 2021 | J Ethnopharmacol | Therapeutic potential of russelioside B as anti-arthritic agent in Freund's adjuvant-induc... | 8 | JointHist, TNF, IL1b, IL6, NFkB, OS(other/unspecified) | Abstract only | n/a |
| 49 | 34015366 | 10.1016/j.jep.2021.114209 | Lee J | 2021 | J Ethnopharmacol | Anti-inflammatory, and anti-arthritic effects by the twigs of Cinnamomum cassia on complet... | not in abstract | Paw, IHC/IF, Pain | Abstract only | n/a |
| 50 | 36610673 | 10.1016/j.jep.2023.116146 | Zhou M | 2023 | J Ethnopharmacol | Euphorbium total triterpenes improve Freund's complete adjuvant-induced arthritis through ... | not in abstract | Score, Paw, BW, JointHist, TNF, IL1b, IL6, RF, CRP, NFkB | Abstract only | n/a |
| 51 | 36702447 | 10.1016/j.jep.2023.116175 | Luo Y | 2023 | J Ethnopharmacol | Anti-rheumatoid arthritis potential of Rhododendron molle G. Don leaf extract in adjuvant ... | not in abstract | Score, Paw, BW, JointHist, IL1b, IL6 | Abstract only | n/a |
| 52 | 38565410 | 10.1016/j.jep.2024.118138 | El-Gendy ZA | 2024 | J Ethnopharmacol | Anti-inflammatory and anti-rheumatic effects of Phoenix dactylifera L. (date palm) seed by... | not in abstract | Paw, BW, JointHist, TNF, IL1b, IL6, IL17, NO, NFkB | Abstract only | n/a |
| 53 | 34453939 | 10.1016/j.lfs.2021.119910 | Souza KS | 2021 | Life Sci | Low dose of quercetin-loaded pectin/casein microparticles reduces the oxidative stress in ... | not in abstract | Paw, MDA, GSH, LFT/KFT | Abstract only | n/a |
| 54 | 36682523 | 10.1016/j.lfs.2023.121411 | Chuang KC | 2023 | Life Sci | Therapeutic effects of kefir peptides on adjuvant-induced arthritis in rats through anti-i... | not in abstract | JointHist, Xray, NFkB, MAPK | Abstract only | n/a |
| 55 | 33799223 | 10.1016/j.phymed.2021.153522 | Xie Y | 2021 | Phytomedicine | Wutou decoction ameliorates experimental rheumatoid arthritis via regulating NF-kB and Nrf... | not in abstract | NFkB | Abstract only | n/a |
| 56 | 35870375 | 10.1016/j.phymed.2022.154339 | Shen Y | 2022 | Phytomedicine | Magnoflorine attenuates inflammatory responses in RA by regulating the PI3K/Akt/NF-κB and ... | not in abstract | JointHist | Abstract only | n/a |
| 57 | 37163904 | 10.1016/j.phymed.2023.154857 | Liu FY | 2023 | Phytomedicine | Therapeutic effects of shikonin on adjuvant-induced arthritis in rats and cellular inflamm... | not in abstract | Score, Paw, JointHist, TNF, IL1b, IL6, WB, IHC/IF, ELISA | Abstract only | n/a |
| 58 | 37603974 | 10.1016/j.phymed.2023.155021 | Ren M | 2023 | Phytomedicine | Anti-rheumatoid arthritis effects of total saponins from Rhizoma Panacis Majoris on adjuva... | not in abstract | Score, Paw, JointHist, IL1b, IL6, WB, ELISA | Abstract only | n/a |
| 59 | 41072281 | 10.1016/j.phymed.2025.157313 | Huan QC | 2025 | Phytomedicine | Tangeretin formulated in a self-nano-emulsifying drug-delivery system (SNEDDS) alleviates ... | not in abstract | (none named in abstract) | Abstract only | n/a |

---

## 4. Frequency table: endpoint, then number (%) of papers

Sorted by frequency in the full-text tier. **Use the full-text column as the main estimate.** Abstracts systematically under-report routine endpoints: for example, ELISA appears in 79% of full texts but only 17% of abstracts, and body weight in 69% vs 37%. Composite rows are computed per paper.

| Endpoint | Full text (n=29) | Abstract only (n=30) | All (n=59) |
|---|---|---|---|
| Clinical severity (score OR paw) | 29/29 (100%) | 23/30 (77%) | 52/59 (88%) |
| Paw volume/thickness/diameter | 27/29 (93%) | 23/30 (77%) | 50/59 (85%) |
| Any of TNF-α/IL-1β/IL-6 | 25/29 (86%) | 20/30 (67%) | 45/59 (76%) |
| ELISA | 23/29 (79%) | 5/30 (17%) | 28/59 (47%) |
| Body weight | 20/29 (69%) | 11/30 (37%) | 31/59 (53%) |
| Histology H&E | 20/29 (69%) | 21/30 (70%) | 41/59 (69%) |
| IL-1β | 20/29 (69%) | 18/30 (60%) | 38/59 (64%) |
| Arthritis score/index | 19/29 (66%) | 13/30 (43%) | 32/59 (54%) |
| TNF-α | 19/29 (66%) | 17/30 (57%) | 36/59 (61%) |
| Score AND paw | 17/29 (59%) | 13/30 (43%) | 30/59 (51%) |
| IL-6 | 16/29 (55%) | 15/30 (50%) | 31/59 (53%) |
| Hematology/CBC | 14/29 (48%) | 7/30 (23%) | 21/59 (36%) |
| Western blot | 11/29 (38%) | 3/30 (10%) | 14/59 (24%) |
| IHC/IF on joint | 11/29 (38%) | 6/30 (20%) | 17/59 (29%) |
| Any NF-κB/TLR4/MAPK | 11/29 (38%) | 14/30 (47%) | 25/59 (42%) |
| Any oxidative-stress marker | 10/29 (34%) | 13/30 (43%) | 23/59 (39%) |
| All three TNF-α+IL-1β+IL-6 | 10/29 (34%) | 12/30 (40%) | 22/59 (37%) |
| CRP/ESR | 9/29 (31%) | 5/30 (17%) | 14/59 (24%) |
| MDA/lipid peroxidation | 9/29 (31%) | 7/30 (23%) | 16/59 (27%) |
| GSH | 9/29 (31%) | 5/30 (17%) | 14/59 (24%) |
| SOD | 9/29 (31%) | 5/30 (17%) | 14/59 (24%) |
| NF-κB | 9/29 (31%) | 13/30 (43%) | 22/59 (37%) |
| Liver/kidney safety | 9/29 (31%) | 2/30 (7%) | 11/59 (19%) |
| qPCR | 8/29 (28%) | 5/30 (17%) | 13/59 (22%) |
| IL-10 | 7/29 (24%) | 8/30 (27%) | 15/59 (25%) |
| RF | 6/29 (21%) | 5/30 (17%) | 11/59 (19%) |
| IL-17 | 5/29 (17%) | 7/30 (23%) | 12/59 (20%) |
| Spleen/thymus index | 5/29 (17%) | 6/30 (20%) | 11/59 (19%) |
| Any joint imaging (X-ray/CT/BMD/US) | 5/29 (17%) | 8/30 (27%) | 13/59 (22%) |
| CAT | 4/29 (14%) | 5/30 (17%) | 9/59 (15%) |
| X-ray/radiography | 3/29 (10%) | 7/30 (23%) | 10/59 (17%) |
| Micro-CT/CT | 3/29 (10%) | 0/30 (0%) | 3/59 (5%) |
| NO/nitrite | 3/29 (10%) | 4/30 (13%) | 7/59 (12%) |
| Pain/behaviour | 3/29 (10%) | 8/30 (27%) | 11/59 (19%) |
| ACPA/anti-CCP | 2/29 (7%) | 2/30 (7%) | 4/59 (7%) |
| MAPK (p38/ERK/JNK) | 2/29 (7%) | 3/30 (10%) | 5/59 (8%) |
| Safranin-O/Toluidine (cartilage) | 1/29 (3%) | 0/30 (0%) | 1/59 (2%) |
| TRAP (osteoclast) | 1/29 (3%) | 0/30 (0%) | 1/59 (2%) |
| Cartilage stain or TRAP | 1/29 (3%) | 0/30 (0%) | 1/59 (2%) |
| TLR4 | 0/29 (0%) | 1/30 (3%) | 1/59 (2%) |

Design-reporting statements in the 29 full texts (keyword detection in Methods/Results): randomisation mentioned in 17/29 (59%), blinding in 8/29 (28%), **a sample-size or power calculation in 0/29 (0%)**, ARRIVE cited in 5/29 (17%).

Group size, full-text tier (n per group, 27/29 papers reported it; for ranges the lower bound is used): median 8, range 4-18. n = 4 in 2 papers (Heliyon 37809969; J Cell Mol Med 41736485), which would fail the BJP n ≥ 5 rule. Most common values: 6, 8 and 10.

---

## 5. Core-set conclusion with evidence

### 5.1 What appears in ≥70% of papers (the empirical minimum core)
Full-text tier, n = 29:
1. **A clinical severity readout: 100%** (29/29 measured an arthritis score or paw swelling). **Paw volume/thickness/ankle diameter alone: 93%** (27/29; 85% of all 59 papers). This is the closest thing to a universal endpoint.
2. **At least one of TNF-α, IL-1β or IL-6: 86%** (25/29; 76% of all 59). All three together: only 34% (10/29).
3. **Joint histology (H&E/histopathology): 69%** (20/29; 69% of all 59). Borderline, but it is effectively universal in practice, and SMASH and Bolon both treat it as essential.
4. Body weight is just below the cut-off at **69%** (20/29). Bolon lists it as a Tier 1 test "used on all" rodent arthritis studies.

### 5.2 Frequent but not universal (about 50-69%)
Arthritis score/index 66%; IL-1β 69%; TNF-α 66%; IL-6 55%; score and paw together 59%.

### 5.3 Optional (<50%), the "added value" tier
Haematology/CBC 48%; Western blot 38%; IHC/IF 38%; any NF-κB/TLR4/MAPK readout 38% (NF-κB 31%, MAPK 7%, TLR4 0% in full text; 2% of all 59); **any oxidative-stress marker 34%** (39% of all 59; MDA 31%, GSH 31%, SOD 31%, CAT 14%, NO 10%); liver/kidney safety 31%; CRP/ESR 31%; qPCR 28%; IL-10 24%; RF 21%; IL-17 17%; spleen/thymus index 17%; any joint imaging 17% (X-ray 10%, micro-CT 10%); pain/behaviour 10%; **ACPA/anti-CCP 7%**; Safranin-O/TB 3%; TRAP 3%.

### 5.4 What this means for the PEA protocol (evidence-based, budget-aware)
- **Gap 1, critical.** The protocol's endpoint list has no paw volume/ankle diameter, no arthritis score and no body weight. These are the most frequent endpoints (93% / 66% / 69%), and Bolon Tier 1 requires them. They cost almost nothing: a plethysmometer or water displacement, calipers, a balance. **Without them, a reviewer cannot see clinical efficacy.** Add them, recorded serially (for example every 2-3 days from Day 0 to Day 45), with a defined 0-4 per-paw score.
- **Gap 2, design reporting.** BJP (Curtis 2018) and ARRIVE require: n ≥ 5 independent rats per group, equal n, a stated randomisation method, blinded outcome assessment (score, paw volume, histology), a named primary outcome and a sample-size justification. In this survey 0/29 papers reported a sample-size calculation and 8/29 reported blinding, so reporting these would put the study **above** the published norm at zero cost. A primary outcome such as paw-volume AUC or the Day-45 arthritis score lets the n be justified.
- **Gap 3, histology site and stains.** The protocol scores the knee. SMASH (Rec 2 and 10) and Bolon both use the **hind-paw ankle/tarsal joints**. Either switch, or add the ankle and justify the knee. If cartilage damage is claimed, SMASH Rec 24-25 requires **Safranin-O or toluidine blue** (cheap) and separate 0-3 scores for inflammation, erosion and cartilage. Use EDTA decalcification for the p65/TLR4 IHC (SMASH Table 5).
- **Cytokines.** A cytokine panel is expected (86%). Measuring 1-2 of TNF-α, IL-1β and IL-6 already matches the majority. All three appears in only about a third of papers, so the full set is not required for acceptance.
- **ACPA (7%), TLR4 (0-2%) and p38/MAPK (7-8%) are uncommon in this literature.** They are not part of the acceptance core. They add mechanistic novelty but can be cut first under Rule 0 if the budget forces a choice.
- **Oxidative stress (34-39%) is optional but common in pharmacology and natural-product journals** (for example Inflammopharmacology, Eur J Pharmacol and DDDT papers in this sample). The cheapest informative pair, MDA plus GSH, matches what is usually reported (each about 24-31%). Doing it would satisfy the supervisor without moving the study outside the norm.
- **Optional but cheap safety and systemic readouts.** CBC (48%), and liver/kidney function (ALT/AST/creatinine, 31%). For a study comparing prednisolone, tacrolimus and baricitinib, a basic safety panel strengthens the steroid-sparing argument at low cost. This is an inference, not a measured frequency.
- **Imaging (X-ray/micro-CT) is in only 17-22%** of papers and is not required.

Bottom line from the evidence. **Minimum core for acceptance:** (1) serial paw volume or ankle diameter plus an arthritis score, (2) body weight, (3) blinded joint histology (H&E; SafO if cartilage is claimed), and (4) at least one serum pro-inflammatory cytokine, together with ARRIVE/BJP-compliant design reporting (n ≥ 5 equal groups, randomisation, blinding, primary outcome, sample-size justification). Everything else, including ACPA, TLR4, p38 MAPK, oxidative stress, CBC, imaging and qPCR/WB, is optional mechanistic or safety depth. It appears in under half of published Q1/Q2-type papers.

---

## 6. Limitations

1. **The sample is not exhaustive or random.** Papers were chosen by title and abstract from two Europe PMC pools, spread across journals and years. Pool 12 had 171 hits and 40 were screened (2 excluded). The 19 open-access additions come from journals outside the user's target list, and their quartile is unknown.
2. **No journal quartile was verified** (SCImago was blocked). "Q1/Q2" was not confirmed for any journal.
3. **Extraction method.** In the full-text tier, endpoints were found by regular expressions over the text from Methods to Discussion, then adjudicated by hand where an in-vivo-context filter disagreed with the raw match (about 60 decisions; see `work/disagree.txt`). Some in-vitro or adipose-tissue mentions may remain, or real in-vivo measurements may have been missed (for example, cytokine panels described only in figures). Four papers were checked against their abstracts, and 2 false-positive histology entries (adipose tissue only) were removed. "Measured" was recorded, not "reported as significant".
4. **The abstract tier under-counts** routine endpoints and methods (ELISA, body weight, haematology). It is reported separately for that reason.
5. **Design-statement detection is keyword-based.** "random" may catch non-allocation uses and "blind" may catch other uses. Sample-size calculation (0/29) was searched as "sample size", "power analysis", "power calculation" and "G*Power".
6. **Gaps in reading the guidelines.** Curtis 2018, ARRIVE 2.0, SMASH and Bolon 2011 were read in full. Curtis 2022 was read as abstract plus a secondary summary. Curtis 2025 was not read. Bendele 2001 was read as abstract only. Bevaart 2010 was not read. Check the 2025 BJP guidance before submission if BJP is the target.
7. **SMASH does not cover AIA.** Applying it to AIA rests on the authors' own statement that it applies to "any other inflammatory arthritis model".
8. Frequency is not the same as necessity. A reviewer may still ask for something rare, or not ask for something common. The table shows what the field actually reports, not what any one editor will demand.

Working files (scripts, raw records, adjudication log) are in `C:\Users\ET\AppData\Local\Temp\claude\d--vault-my-research\a5058813-26f4-4134-995a-deb7f3d65210\scratchpad\rework\work\`.
