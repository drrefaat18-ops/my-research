# C — Novelty search: oral m-PEA ± low-dose prednisolone in CFA arthritis (rats)

Search date for every query: **2026-10-02**. Searcher: automated API run (scripts and raw JSON in `scratchpad/rework/nov/`: `q.py`, `q2.py`, `q3.py`, `q4.py`, `cite.py`, `s2.py`; results in `pubmed.json`, `other.json`, `other2.json`, `q4.json`, `cite.json`).
Every record cited below was re-fetched (PubMed efetch abstract and/or Crossref/OpenAlex) during this run. Nothing is cited from memory.

Questions:
- (a) PEA (any form) + any glucocorticoid (GC), in any model or in humans
- (b) PEA in adjuvant/CFA arthritis in rats
- (c) PEA compared with a JAK inhibitor or a calcineurin inhibitor
- (d) PEA trials in RA patients

---

## 1. Search log

Synonym blocks used:
- **PEA (PubMed)** = `palmitoylethanolamide[tiab] OR "palmitoyl ethanolamide"[tiab] OR "palmitoylethanolamine"[tiab] OR "N-palmitoylethanolamine"[tiab] OR levagen[tiab] OR normast[tiab] OR "Palmitoylethanolamide"[nm]`
- **PEA (Europe PMC / OpenAlex)** = `palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine" OR levagen OR normast`
- **GC** = `prednisolone OR prednisone OR dexamethasone OR methylprednisolone OR glucocorticoid* OR corticosteroid* OR "steroid-sparing" OR "steroid sparing"`. PubMed also included betamethasone, hydrocortisone and triamcinolone.
- **MOD** = `"adjuvant arthritis" OR "adjuvant-induced" OR Freund* OR CFA OR "collagen-induced" OR arthritis OR rheumatoid OR synovitis`
- **JAK/CNI** = `baricitinib OR tofacitinib OR upadacitinib OR "JAK inhibitor*" OR "Janus kinase" OR tacrolimus OR cyclosporin* OR ciclosporin OR "calcineurin inhibitor*" OR FK506`. The extended set (Pg, Ec-R) also added ruxolitinib and oclacitinib.

| ID | Database | Exact query (abbreviated by block names above; full strings are in the scripts) | Hits | Screened |
|---|---|---|---|---|
| P0 | PubMed | PEA | 1448 | not screened (denominator only) |
| Pa | PubMed | PEA AND GC | 38 | all 38 |
| Pa2 | PubMed | PEA block + `PEA[tiab]` AND GC | 95 | all 95. Adding `PEA[tiab]` only adds noise: pea protein, polyesteramide microspheres, phenylethylamine, pulmonary endarterectomy. It was therefore dropped from later strings. |
| Pb | PubMed | PEA AND MOD | 35 | all |
| Pb2 | PubMed | PEA AND ("adjuvant arthritis" OR "adjuvant-induced" OR Freund* OR "complete Freund" OR CFA) | 7 | all |
| Pc | PubMed | PEA AND JAK/CNI | 8 | all |
| Pd | PubMed | PEA AND ("rheumatoid arthritis" OR rheumatoid) | 6 | all |
| Pd2 | PubMed | Pd AND (trial OR randomized OR randomised OR patients) | 1 | all |
| Pe | PubMed | PEA(+PEA[tiab]) AND GC AND MOD | 4 | all |
| Pf | PubMed | PEA AND (luteolin OR polydatin OR ultramicronized OR micronized OR "co-ultramicronized") AND (arthritis OR joint OR synovitis OR osteoarthritis) | 12 | all |
| Pg | PubMed | PEA AND JAK/CNI extended | 9 | all |
| Ph | PubMed | PEA AND (rat OR rats) AND (arthritis OR Freund OR adjuvant) | 26 | all |
| Pi | PubMed | Design-class check: (adjuvant arthritis / Freund / CFA)[tiab] AND (prednisolone/prednisone/dexamethasone/methylprednisolone)[tiab] AND (combination/combined/low-dose/sparing/half dose/synergis*)[tiab] AND rat(s)[tiab] | 52 | all |
| Pj | PubMed | (endocannabinoid*/cannabinoid*/N-acylethanolamine/MAGL/FAAH/NAAA) AND (dexamethasone/prednisolone/prednisone/glucocorticoid*) AND arthritis [tiab] | 8 | all |
| Ea | Europe PMC | (TITLE/ABSTRACT: PEA) AND (TITLE/ABSTRACT: GC) | 26 | all |
| Ea-FT | Europe PMC | PEA AND (prednisolone OR prednisone), full text | 231 | >200, so refined to Ea-R |
| Ea-R | Europe PMC | (TITLE/ABSTRACT: PEA) AND (prednisolone OR prednisone) anywhere in full text | 14 | all |
| Ea-FT2 | Europe PMC | PEA AND GC AND (arthritis OR "adjuvant-induced" OR "collagen-induced"), full text | 321 | >200, so refined to Ea-R2 |
| Ea-R2 | Europe PMC | (TITLE/ABSTRACT: PEA) AND GC AND arthritis terms, full text | 23 | all |
| Ea-FT3 | Europe PMC | PEA AND ("in combination with dexamethasone" OR "combined with dexamethasone" OR "combined with prednisolone" OR "in combination with prednisolone" OR "combination with methylprednisolone" OR "steroid-sparing" OR "glucocorticoid-sparing" OR "corticosteroid-sparing"), full text | 41 | all |
| Eb | Europe PMC | (TITLE/ABSTRACT: PEA) AND (TITLE/ABSTRACT: "adjuvant arthritis" OR "adjuvant-induced arthritis" OR Freund OR CFA) | 6 | all |
| Eb2 | Europe PMC | (TITLE/ABSTRACT: PEA) AND (TITLE/ABSTRACT: arthritis OR rheumatoid) | 11 | all |
| Ec | Europe PMC | PEA AND JAK/CNI AND arthritis, full text | 94 | titles scanned; refined to Ec-R |
| Ec-R | Europe PMC | (TITLE/ABSTRACT: PEA) AND JAK/CNI extended, full text | 10 | all |
| Ec2 | Europe PMC | (TITLE/ABSTRACT: PEA) AND (TITLE/ABSTRACT: JAK/CNI) | 3 | all |
| Ed | Europe PMC | (TITLE/ABSTRACT: PEA) AND (TITLE/ABSTRACT: "rheumatoid arthritis") | 4 | all |
| Ef | Europe PMC | ABSTRACT:("um-PEA" OR "PEA-um" OR "m-PEA" OR "PEA-LUT" OR "co-ultramicronized" OR "PEA-polydatin" OR "PEA/polydatin") AND arthritis/synovitis | 2 | all |
| Eg | Europe PMC | (TITLE/ABSTRACT: piperine) AND (TITLE/ABSTRACT: prednisolone) AND (arthritis OR adjuvant) | 2 | all |
| Oa | OpenAlex `title_and_abstract.search` | palmitoylethanolamide AND (prednisolone OR prednisone OR dexamethasone OR methylprednisolone OR glucocorticoid OR corticosteroid) | 42 | all |
| Ob | OpenAlex | palmitoylethanolamide AND ("adjuvant arthritis" OR "adjuvant-induced" OR Freund) | 3 | all |
| Ob2 | OpenAlex | palmitoylethanolamide AND (arthritis OR rheumatoid) | 21 | all |
| Oc | OpenAlex | palmitoylethanolamide AND (baricitinib OR tofacitinib OR JAK OR tacrolimus OR cyclosporine OR calcineurin) | 9 | all |
| Od | OpenAlex | palmitoylethanolamide AND "rheumatoid arthritis" | 8 | all |
| Sa2 | Semantic Scholar `/paper/search` | `palmitoylethanolamide glucocorticoid` | 141,689 (relevance-ranked, OR-like) | top 100 |
| Sa4 | Semantic Scholar | `palmitoylethanolamide steroid sparing` | 6,896 | top 100 |
| Sc2 | Semantic Scholar | `palmitoylethanolamide tacrolimus` | 44,172 | top 100 |
| Sb | Semantic Scholar | `palmitoylethanolamide adjuvant arthritis` | 11,218 | top 100. Only PEA hits were Impellizzeri 2013 and its erratum, plus "adjuvant therapy" uses of PEA (COVID, Parkinson's). Nothing new. |
| Sc | Semantic Scholar | `palmitoylethanolamide baricitinib` | 5,600 | top 100. PEA reviews and pain trials only; no JAK comparison. |
| Sa, Sa3, Sd | Semantic Scholar | `palmitoylethanolamide` + prednisolone / dexamethasone / rheumatoid arthritis | **not obtained (HTTP 429 rate limit, repeated retries)** | none. This is a limitation; the same concepts were covered in PubMed, Europe PMC and OpenAlex. |
| Ca | ClinicalTrials.gov v2 | query.intr=palmitoylethanolamide; query.cond=arthritis | 2 | all |
| Cb | ClinicalTrials.gov | query.intr=palmitoylethanolamide; query.cond=rheumatoid arthritis | 1 | all |
| Cc | ClinicalTrials.gov | query.intr=palmitoylethanolamide (all PEA trials) | 69 | all 69 titles and conditions |
| Cd | ClinicalTrials.gov | query.intr=palmitoylethanolamide AND (prednisone OR prednisolone OR methylprednisolone OR dexamethasone OR corticosteroid) | 1 | all |
| CC-1 | Citation chase (OpenAlex referenced_works / cites) | Impellizzeri 2013, DOI 10.1186/ar4382 | 52 refs / 81 citing | all titles |
| CC-2 | Citation chase | Morvaridi 2025, DOI 10.30466/vrf.2024.2031860.4316 | 1 ref indexed (incomplete) / 1 citing | all |
| CC-3 | Citation chase | Noli 2019, DOI 10.1111/vde.12764 | 27 / 19 | all |
| CC-4 | Citation chase | Bartolucci 2018, DOI 10.1007/s00011-018-1179-y | 39 / 23 | all |
| CC-5 | Citation chase | Bonezzi 2016, DOI 10.1124/jpet.115.230516 | 39 / 45 | all |
| X | Crossref | DOI verification of 20 key records | 19 OK; Morvaridi DOI returns Crossref 404 but resolves via doi.org to vrf.iranjournals.ir/article_719953.html (journal-hosted DOI), and the PubMed record is consistent | — |

The Semantic Scholar citation endpoints were not usable because of the same 429 throttling. Citation chasing was therefore done with OpenAlex `cites:` and `referenced_works`, which is functionally equivalent.

**PRISMA-style flow (approximate):** 1,383 records were retrieved by screened queries:
- 529 from bibliographic queries other than S2 and unrefined full-text sets
- 95 from Pa2
- 500 from S2
- 69 from CT.gov
- 247 from citation chasing

After title de-duplication of the bibliographic sets, about 390 unique records remained. Titles were screened for all of them. About 45 abstracts were read. 31 records were judged relevant or partially relevant (Section 2). **0 met criterion (a)-in-arthritis, 0 met (b) in its strict form, 0 met (c), and 0 completed RA trials met (d).**

---

## 2. Screening results

Classification key: **R** = relevant / close precedent, **P** = partially relevant, **I** = irrelevant.

### 2a. PEA + glucocorticoid (blocks Pa, Pa2, Pe, Ea, Ea-R, Ea-R2, Ea-FT3, Oa, S2, Cd)

| Record | Class | One-line reason |
|---|---|---|
| Noli 2019 Vet Dermatol, PMID 31237065 | **R** | um-PEA 15 mg/kg/day oral given during a 28-day methylprednisolone taper, then alone. RCT in 57 cats with non-flea hypersensitivity dermatitis. The only identified study that co-administers PEA with a systemic GC (dermatology, not arthritis). |
| Eberlein 2008 JEADV (ATOPA), PMID 18181976 | **P** | Topical PEA emollient in 2,456 people with atopic eczema. 56% stopped topical corticosteroids and weekly use fell 62%. Observational and uncontrolled. Human "steroid-sparing" precedent for PEA (topical, skin). |
| Kircik 2010 J Drugs Dermatol, PMID 20514790 | P | Review of a nonsteroidal PEA lamellar cream for atopic dermatitis that reduces steroid use. Not experimental. |
| NCT07609810 (Ain Shams Univ., Egypt; recruiting; start 2026-08-15) | **P** | PEA vs placebo in mild-to-moderate UC patients already on 5-ASA plus corticosteroids. A human PEA + GC background regimen (not arthritis). Registered only, no results. |
| Impellizzeri 2015 Eur J Pharmacol, PMID 25934566 | P | PEA in endotoxin uveitis in rats with **dexamethasone as a separate positive control** (no combination arm). |
| Rundle 2022 Dermatitis, PMID 33654018 | P | Topical CBD + PEA product vs mometasone in TPA ear oedema in mice. GC used as comparator only. |
| Sasso 2018 J Invest Dermatol, PMID 29054595 | P | NAAA inhibitor (raises PEA), compared with clobetasol/dexamethasone in mouse dermatitis. Not PEA itself. |
| Briskey 2023 Nutrients, PMID 38068797 | I | Levagen+ vs placebo in allergic rhinitis. GC mentioned only as standard care. |
| Nohales Alfonso 2022 Drugs Context, PMID 35106067 | I | 3 case reports. A PEA-containing supplement within multimodal care that sometimes included corticosteroid infiltrations. No controlled combination. |
| Mueller 2021 Vet Dermatol, PMID 33470011 | P | Systematic review (feline atopic syndrome). Grades GC and ciclosporin (good evidence) against PEA (low-to-moderate). No head-to-head study. |
| Hair/plasma/saliva biomarker papers measuring endocannabinoids/NAEs and cortisol, about 15 records (e.g., PMIDs 42549879, 35757050, 34676867, 38155287, 33376241, 22763622) | I | Analytical or observational co-measurement, no treatment. |
| Post-COVID olfaction systematic reviews (PMIDs 39477832, 39464360, 37531338, 36062970) | I | List PEA-luteolin and steroids as separate interventions. |
| Pa2 noise (57 records) | I | "PEA" = pea protein / polyesteramide / phenylethylamine. |
| Ea-FT3 hits that are guideline reviews in atopic dermatitis or ophthalmology (~30) | I | Reviews only. |
| Remaining Oa/Ea/S2 records | I | Reviews of PEA in general, stress endocrinology, unrelated. |

### 2b. PEA in adjuvant/CFA models in rats (blocks Pb, Pb2, Ph, Eb, Eb2, Ob, Ob2, CC-4, CC-5)

| Record | Class | One-line reason |
|---|---|---|
| **Bartolucci 2018 Inflamm Res**, PMID 30121836 | **R** | **m-PEA 10 mg/kg in rats with CFA injected into the temporomandibular joint (TMJ).** Endpoints: allodynia, oedema, TMJ damage, glial/macrophage activation (GFAP, Iba1) over 24–72 h. This is the closest "m-PEA + CFA + rat" precedent. Route is not stated in the abstract. It is acute and local, with no immunological arthritis endpoints. |
| Bonezzi 2016 J Pharmacol Exp Ther, PMID 26769918 | **R** (mechanistic) | CFA paw inflammation in rats lowers tissue PEA/OEA and raises NAAA. The NAAA inhibitor ARN726 restores PEA and reduces inflammation. **PEA itself was not administered.** |
| Aldossary 2019 Neuroreport, PMID 30418420 | P | Intraplantar PEA 50 µg on day 7 of CFA inflammatory pain in male SD rats. PPARα/TRPV1 mechanism. Pain only. |
| Gaspar 2021 Biomedicines, PMID 34072060 | P | i.p. PEA plus PPAR antagonists in CFA chronic inflammatory pain in rats. Anxiety and memory endpoints. |
| LoVerme 2006 J Pharmacol Exp Ther, PMID 16997973 | P | Acute PEA reduces hyperalgesia in CFA and carrageenan models (mice). Analgesia only. |
| **Impellizzeri 2013 Arthritis Res Ther 15(6):R192**, PMID 24246048 (erratum PMID 27149951) | **R** | Collagen-induced arthritis in **mice**. PEA 10 mg/kg i.p. or co-ultramicronized PEA+luteolin 1 mg/kg i.p. on days 25–35. Improved clinical score and histology; reduced nitrotyrosine, MDA and plasma cytokines/chemokines. No GC arm. |
| Lowin 2015 Arthritis Res Ther 17:321, PMID 26567045 | R (mechanistic) | PEA, AEA and OEA lower IL-6, IL-8 and MMP-3 in human RA/OA synovial fibroblasts via TRPV1/TRPA1 (COX-2 dependent). In vivo arm used a FAAH inhibitor in CIA mice, not PEA. |
| Geniposide AIA metabolomics, PMID 32786678 | I | PEA appears only as a detected metabolite. |
| MIA osteoarthritis PEA studies (PMIDs 34468900, 41945007; 28768536 PEA-quercetin; 27955699 and 27599446 adelmidrol) | P | PEA/analogues in OA (MIA) rat models. Not inflammatory/adjuvant arthritis. |
| Palmitoylglucosamine, PMID 31779692 | I | A different ALIAmide. |

### 2c. PEA vs JAK inhibitors / calcineurin inhibitors (Pc, Pg, Ec, Ec-R, Ec2, Oc, Sc2)

| Record | Class | One-line reason |
|---|---|---|
| Berg 2025 Immunology 176(3):385-402, PMID 40563231 | P | PEA in murine GVHD (PPAR-γ dependent; ↑Treg, ↓CD8, ↓TNF-α). Calcineurin inhibitors appear only in the full-text background. No CNI arm. |
| Mueller 2021, PMID 33470011 | P | Evidence grading only (ciclosporin, oclacitinib, PEA). No head-to-head study. |
| Tacrolimus binge-drinking mice, PMID 33294845; myeloproliferative neoplasm NAE levels, PMID 32403407; TRPV1 monoacylglycerols, PMID 24312564; mitochondrial NAE, PMID 15238272 | I | No comparison of PEA with JAK inhibitors or CNIs in inflammation. |
| S2 Sc2 top 100 | I | Tacrolimus pharmacokinetics/transplant and general PEA reviews. |
| **Any JAK inhibitor (baricitinib, tofacitinib, upadacitinib, ruxolitinib, oclacitinib) together with PEA** | — | **0 primary studies in any database.** |

### 2d. PEA in RA patients (Pd, Pd2, Ed, Od, Ca, Cb, Cc)

| Record | Class | One-line reason |
|---|---|---|
| Parisi 2021 Minerva Med 112(4):492-499, PMID 34056884 | **R** | Non-randomized comparative study in rheumatic-disease patients (RA or SpA) with neuropathy (sciatica, carpal tunnel, peripheral neuropathy). PEA 600 mg + ALC 500 mg (Kalanit) added to standard therapy vs standard therapy alone. Outcome: pain VAS. **The only published clinical PEA study enrolling RA patients.** Endpoint is neuropathic pain, not RA activity. |
| NCT07680101 (Univ. Verona; not yet recruiting; start 2026-06) | **R** | RCT of intra-articular adelmidrol 2%/HA 1% ± oral m-PEA 300 mg + um-PEA 600 mg in knee degeneration due to OA **or RA** (KL II–III). Excludes systemic corticosteroids within 1 month. No results. |
| NCT05406726 | I | PEA in knee OA (pain sensitivity). |
| NCT06273462 (Navy Medical Center San Diego) | P | PEA vs placebo in "chronic inflammatory pain conditions". RA is not specified. |
| Other 64 PEA trials on CT.gov | I | Pain, neuro-psychiatric, GI, COVID and other non-RA indications. |
| Lowin 2015 | P | Human RA synovial cells in vitro, not a trial. |
| German review 2024 (DOI 10.21248/gups.83604, "Cannabis-based Medicine und Palmitoylethanolamid als Analgetika bei Rheumaschmerzen") | P | Grey-literature review. Not a trial. Listed for completeness and not verified beyond OpenAlex metadata. |

### 2e. Design-class precedents: GC-sparing combinations in CFA/AIA rats (Pi, Pj, CC-1, CC-2). No PEA is involved, but these are the precedents a reviewer will raise.

| Record | Class | One-line reason |
|---|---|---|
| **Barbosa Retameiro 2025 Microsc Microanal 31(6):ozaf120**, PMID 41370192 | **R (closest design)** | **Female** Wistar rats (18 months old). CFA injected **into the tibiofemoral joint**. Curcumin 100 mg/kg ± **low-dose prednisone 2 mg/kg** vs prednisone 10 mg/kg, by gavage for 14 days. Endpoints: joint histology, leukocyte migration, lipoperoxidation. |
| **Ashour 2019 Mod Rheumatol 29(4):602-611**, PMID 30074417 | **R (mechanistic)** | **PPARα agonist gemfibrozil + reduced prednisolone (human-equivalent 5 mg) ≈ full dose (10 mg)** in AIA (± high-fat diet) in male Wistar rats. Greater reduction of NF-κB and HMGB1. PEA is a PPARα agonist, so this is the nearest mechanism-class GC-sparing precedent. Egyptian group. |
| Morvaridi 2025 Vet Res Forum 16(2):117-124, PMID 40099241 | R | Piperine + prednisolone at half doses vs full-dose monotherapy (prednisolone 10 mg/kg) in CFA RA, male Wistar rats (see Section 4). |
| Mirzaaghasi 2023 Antiinflamm Antiallergy Agents Med Chem 22(2):104-112, PMID 37845835 | R | Niacin + prednisolone at half doses in CFA AIA, male Wistar rats (same Urmia group as Morvaridi). |
| Du 2016 Int Immunopharmacol 31:257-265, PMID 26773773 | R | Escin + low-dose prednisone 2 mg/kg vs 10 mg/kg in AIA SD rats. Cytokines TNF-α, IL-1β, IL-6 and histology. Synergy and fewer GC adverse effects. |
| Suke 2013 Eur J Pharmacol 718:57-62, PMID 24075936 | P | PPARγ agonist pioglitazone + prednisolone in AIA, Wistar rats. TNF-α and IL-6. |
| Zimmermann 2009 Arthritis Res Ther 11:R12, PMID 19171052 | P | Dipyridamole amplifies sub-therapeutic prednisolone in CIA/AIA rats. A conceptual "dissociated GC-sparing" precedent. |
| **Nass 2021 Cannabis Cannabinoid Res 6(3):233-241**, PMID 34042520 | **R (class)** | MAGL inhibitor JZL184 (endocannabinoid tone) **alone or combined with dexamethasone** in CIA, male DBA/1 mice. The closest "endocannabinoid-system modulator + GC in arthritis" precedent. Related dissertation by Nass SR, DOI 10.33915/etd.6298 (WVU; grey literature). |
| Lowin 2012 Arthritis Rheum 64(12):3867-76, PMID 22933357 | P (rationale) | Cortisol effects in RA synovial fibroblasts depend on anandamide/endocannabinoid signalling. The authors propose combining endocannabinoid boosting with low-dose GC. |
| Other Pi hits (~43): nanocarrier dexamethasone delivery, other herbal monotherapies, historic papers | I | Not a combination GC-sparing design, or not relevant. |

---

## 3. Closest precedents (verified)

All entries were checked against PubMed records (efetch) and Crossref on 2026-10-02.

| # | Citation (verified) | PMID / DOI | Why it must be cited |
|---|---|---|---|
| 1 | Impellizzeri D, Esposito E, Di Paola R, et al., Cuzzocrea S. Palmitoylethanolamide and luteolin ameliorate development of arthritis caused by injection of collagen type II in mice. *Arthritis Res Ther*. 2013;15(6):R192. Erratum: 2016;18:101 | 24246048 / 10.1186/ar4382 | The only in vivo inflammatory-arthritis study of PEA (CIA, mice, i.p., no GC). |
| 2 | Bartolucci ML, Marini I, Bortolotti F, et al., Cuzzocrea S. Micronized palmitoylethanolamide reduces joint pain and glial cell activation. *Inflamm Res*. 2018;67(10):891-901 | 30121836 / 10.1007/s00011-018-1179-y | m-PEA in CFA-injected rat TMJ. Rules out a "first m-PEA in CFA rats" claim. |
| 3 | Bonezzi FT, Sasso O, Pontis S, et al., Piomelli D. An important role for N-acylethanolamine acid amidase in the complete Freund's adjuvant rat model of arthritis. *J Pharmacol Exp Ther*. 2016;356(3):656-663 | 26769918 / 10.1124/jpet.115.230516 | Shows PEA depletion in CFA rats, the rationale for exogenous PEA. |
| 4 | Lowin T, Apitz M, Anders S, Straub RH. Anti-inflammatory effects of N-acylethanolamines in rheumatoid arthritis synovial cells are mediated by TRPV1 and TRPA1 in a COX-2 dependent manner. *Arthritis Res Ther*. 2015;17:321 | 26567045 / 10.1186/s13075-015-0845-5 | Human RA synovial fibroblast evidence for PEA. |
| 5 | Noli C, Della Valle MF, Miolo A, Medori C, Schievano C; Skinalia Clinical Research Group. Effect of dietary supplementation with ultramicronized palmitoylethanolamide in maintaining remission in cats with nonflea hypersensitivity dermatitis: a double-blind, multicentre, randomized, placebo-controlled study. *Vet Dermatol*. 2019;30(5):387-e117 | 31237065 / 10.1111/vde.12764 / PMC6852539 | The only controlled PEA + systemic GC co-administration study found (cats, skin). Rules out "first PEA + GC combination ever". |
| 6 | Eberlein B, Eicke C, Reinhardt HW, Ring J. Adjuvant treatment of atopic eczema: assessment of an emollient containing N-palmitoylethanolamine (ATOPA study). *J Eur Acad Dermatol Venereol*. 2008;22(1):73-82 | 18181976 / 10.1111/j.1468-3083.2007.02351.x | A human (topical) steroid-sparing signal for PEA. |
| 7 | Parisi S, Ditto MC, Borrelli R, Fusaro E. Efficacy of a fixed combination of palmitoylethanolamide and acetyl-l-carnitine (PEA+ALC FC) in the treatment of neuropathies secondary to rheumatic diseases. *Minerva Med*. 2021;112(4):492-499 | 34056884 / 10.23736/S0026-4806.21.07486-3 | The only PEA clinical data in RA patients (neuropathic pain, non-randomized). |
| 8 | Ashour H, Rashed LA, El-Sebaie MM, et al. Combined gemfibrozil (PPARα agonist) with reduced steroid dose gives a similar management picture as the full steroid dose in a rat adjuvant-induced arthritis model. *Mod Rheumatol*. 2019;29(4):602-611 | 30074417 / 10.1080/14397595.2018.1508800 | PPARα-agonist GC-sparing in AIA. PEA's main receptor is PPARα, so this is the key mechanistic precedent. |
| 9 | Barbosa Retameiro AC, Boaro CT, Rodriguez DFS, et al. Curcumin (Curcuma longa) supplementation improves tibiofemoral joint outcomes in low-dose prednisone-treated experimental rheumatoid arthritis. *Microsc Microanal*. 2025;31(6):ozaf120 | 41370192 / 10.1093/mam/ozaf120 | Same design family: female Wistar rats, CFA into the knee, low-dose GC + natural compound vs full-dose GC. |
| 10 | Morvaridi A, Abtahi Froushani SM, Farshid AA. Benefits of combining piperine with prednisolone in an experimental model of rheumatoid arthritis. *Vet Res Forum*. 2025;16(2):117-124 | 40099241 / 10.30466/vrf.2024.2031860.4316 / PMC11910975 | Half-dose GC + natural compound in CFA Wistar rats. Already in the protocol. |
| 11 | Du Y, Song Y, Zhang L, Zhang M, Fu F. Combined treatment with low dose prednisone and escin improves the anti-arthritic effect in experimental arthritis. *Int Immunopharmacol*. 2016;31:257-265 | 26773773 / 10.1016/j.intimp.2016.01.006 | Same cytokine panel (TNF-α, IL-1β, IL-6) and low-dose GC design. |
| 12 | Nass SR, Steele FF, Ware TB, Libby AH, Hsu KL, Kinsey SG. Monoacylglycerol lipase inhibition using JZL184 attenuates paw inflammation and functional deficits in a mouse model of inflammatory arthritis. *Cannabis Cannabinoid Res*. 2021;6(3):233-241 | 34042520 / 10.1089/can.2020.0177 | Endocannabinoid-system drug combined with dexamethasone in CIA. Rules out "first endocannabinoid-based GC combination". |
| 13 | Mirzaaghasi S, Froushani SMA. Immunomodulatory effects of combined nicotinic acid and prednisolone in adjuvant-induced arthritis. *Antiinflamm Antiallergy Agents Med Chem*. 2023;22(2):104-112 | 37845835 / 10.2174/0118715230264101230925060355 | Same half-dose GC design (Urmia group). |
| 14 | Suke SG, Negi H, Mediratta PK, Banerjee BD, Sharma KK. Anti-arthritic and anti-inflammatory activity of combined pioglitazone and prednisolone on adjuvant-induced arthritis. *Eur J Pharmacol*. 2013;718(1-3):57-62 | 24075936 / 10.1016/j.ejphar.2013.09.019 | PPAR (γ) + GC in AIA. Optional citation. |
| 15 | ClinicalTrials.gov NCT07680101 (Univ. Verona) and NCT07609810 (Ain Shams Univ.) | registry | Disclose as ongoing or registered human work (RA knee; UC on corticosteroids). |

Optional supporting citations: Impellizzeri 2015 Eur J Pharmacol 761:28-35 (PMID 25934566; PEA vs dexamethasone as a separate control in rat uveitis), Lowin 2012 Arthritis Rheum (PMID 22933357; GC–endocannabinoid interaction in RA synovial fibroblasts), Zimmermann 2009 Arthritis Res Ther 11:R12 (PMID 19171052).

---

## 4. Verification of the two PMC links from the earlier AI file

| Link | Claimed | What it actually is (verified 2026-10-02 via NCBI esummary/efetch and the Europe PMC full-text XML) | Verdict |
|---|---|---|---|
| https://pmc.ncbi.nlm.nih.gov/articles/PMC11910975/ | "piperine + prednisolone 2025" | **Morvaridi A, Abtahi Froushani SM, Farshid AA. "Benefits of combining piperine with prednisolone in an experimental model of rheumatoid arthritis." Vet Res Forum 2025;16(2):117-124. PMID 40099241; DOI 10.30466/vrf.2024.2031860.4316.** Design: **male** Wistar rats (n = 60, 8 weeks, about 150 g; full text, Methods). CFA-induced arthritis. Five groups of n = 10: PBS, piperine 100 mg/kg orally, prednisolone 10 mg/kg orally, and the combination at half doses of each. Treatment ran from day 5 (when clinical score was ≥1) to day 23. Half-dose combination outperformed either full-dose monotherapy on severity, weight, histopathology, CRP, MPO and NO, with ↓T-bet and RORγt. Foxp3 and GATA3 did not differ from prednisolone alone. **No PEA anywhere in the text.** | **Claim correct.** Note for the protocol: the rats were male (yours are female), the GC-sparing design was a half-dose combination (not a fixed low-dose GC plus graded add-on), and the paper is mechanistically unrelated to PEA. |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC6852539/ | "PEA + methylprednisolone in feline dermatitis 2019" | **Noli C, et al. Vet Dermatol 2019;30(5):387-e117. PMID 31237065; DOI 10.1111/vde.12764.** Double-blind, multicentre placebo-controlled RCT. 57 cats with non-flea hypersensitivity dermatitis were enrolled and 25 were analysable. PEA-um 15 mg/kg orally once daily, or placebo, during a 28-day **tapering methylprednisolone** course. Responders then received PEA-um or placebo alone for 8 weeks, followed by 4 weeks off treatment. Time to relapse was 40.5 ± 7.8 days vs 22.2 ± 3.7 days (P = 0.04). Pruritus was lower at day 28 (P = 0.03). SCORFAD did not differ. Sponsor-affiliated authors (Innovet). | **Claim essentially correct, but it must be described precisely.** PEA was given as an add-on during a GC taper and then as maintenance after GC withdrawal. This is a relapse-prevention / GC-withdrawal design, not a dose-reduction efficacy comparison. It is a cat dermatology study, not arthritis, and the analysable sample was small (25 of 57). |

---

## 5. Query strings for manual Scopus and Web of Science runs (via EKB)

Run each block, record the date and hit count, and export to RIS for de-duplication against this log.

### Scopus (Advanced search)

PEA block (S-PEA):
```
TITLE-ABS-KEY ( palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine" OR "N-palmitoyl ethanolamine" OR "ultramicronized palmitoylethanolamide" OR "um-PEA" OR "PEA-um" OR "m-PEA" OR "PEA-LUT" OR levagen OR normast OR glialia )
```
(a) PEA + glucocorticoid:
```
TITLE-ABS-KEY ( palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine" OR "um-PEA" OR "PEA-um" OR "m-PEA" OR "PEA-LUT" OR levagen OR normast ) AND TITLE-ABS-KEY ( prednisolone OR prednisone OR dexamethasone OR methylprednisolone OR betamethasone OR hydrocortisone OR triamcinolone OR glucocorticoid* OR corticosteroid* OR "steroid-sparing" OR "steroid sparing" OR "glucocorticoid-sparing" OR "corticosteroid-sparing" )
```
(b) PEA + adjuvant/CFA/experimental arthritis:
```
TITLE-ABS-KEY ( palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine" OR "um-PEA" OR "PEA-um" OR "m-PEA" OR "PEA-LUT" OR levagen OR normast ) AND TITLE-ABS-KEY ( "adjuvant arthritis" OR "adjuvant-induced arthritis" OR "adjuvant induced arthritis" OR freund* OR "CFA-induced" OR "collagen-induced arthritis" OR "experimental arthritis" OR "rheumatoid arthritis" OR synovitis )
```
(c) PEA + JAK / calcineurin inhibitors:
```
TITLE-ABS-KEY ( palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine" OR "um-PEA" OR "PEA-um" OR "m-PEA" OR levagen OR normast ) AND TITLE-ABS-KEY ( baricitinib OR tofacitinib OR upadacitinib OR ruxolitinib OR oclacitinib OR filgotinib OR "JAK inhibitor*" OR "Janus kinase" OR tacrolimus OR FK506 OR cyclosporin* OR ciclosporin OR "calcineurin inhibitor*" )
```
(d) PEA in RA patients / trials:
```
TITLE-ABS-KEY ( palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine" OR "um-PEA" OR levagen OR normast ) AND TITLE-ABS-KEY ( "rheumatoid arthritis" OR "inflammatory arthritis" OR "rheumatic disease*" ) AND TITLE-ABS-KEY ( trial OR randomi* OR patient* OR cohort OR "case series" )
```
Design-class check (no PEA; expected to return the Section 2e precedents):
```
TITLE-ABS-KEY ( ( "adjuvant arthritis" OR "adjuvant-induced arthritis" OR "Freund* adjuvant" OR "CFA-induced arthritis" ) AND ( prednisolone OR prednisone OR dexamethasone ) AND ( "low dose" OR "low-dose" OR "half dose" OR "steroid-sparing" OR "glucocorticoid-sparing" OR synerg* OR combin* ) AND ( rat OR rats ) )
```

### Web of Science Core Collection (Advanced search; all editions)

(a)
```
TS=(palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine" OR "um-PEA" OR "PEA-um" OR "m-PEA" OR "PEA-LUT" OR levagen OR normast) AND TS=(prednisolone OR prednisone OR dexamethasone OR methylprednisolone OR betamethasone OR hydrocortisone OR triamcinolone OR glucocorticoid* OR corticosteroid* OR "steroid-sparing" OR "steroid sparing" OR "glucocorticoid-sparing")
```
(b)
```
TS=(palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine" OR "um-PEA" OR "PEA-um" OR "m-PEA" OR "PEA-LUT" OR levagen OR normast) AND TS=("adjuvant arthritis" OR "adjuvant-induced arthritis" OR "adjuvant induced arthritis" OR freund* OR "CFA-induced" OR "collagen-induced arthritis" OR "experimental arthritis" OR "rheumatoid arthritis" OR synovitis)
```
(c)
```
TS=(palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine" OR "um-PEA" OR "PEA-um" OR "m-PEA" OR levagen OR normast) AND TS=(baricitinib OR tofacitinib OR upadacitinib OR ruxolitinib OR oclacitinib OR filgotinib OR "JAK inhibitor*" OR "Janus kinase" OR tacrolimus OR FK506 OR cyclosporin* OR ciclosporin OR "calcineurin inhibitor*")
```
(d)
```
TS=(palmitoylethanolamide OR "palmitoyl ethanolamide" OR palmitoylethanolamine OR "N-palmitoylethanolamine" OR "um-PEA" OR levagen OR normast) AND TS=("rheumatoid arthritis" OR "inflammatory arthritis" OR "rheumatic disease*") AND TS=(trial OR randomi* OR patient* OR cohort OR "case series")
```
Design-class check:
```
TS=(("adjuvant arthritis" OR "adjuvant-induced arthritis" OR "Freund* adjuvant" OR "CFA-induced arthritis") AND (prednisolone OR prednisone OR dexamethasone) AND ("low dose" OR "low-dose" OR "half dose" OR "steroid-sparing" OR synerg* OR combin*) AND (rat OR rats))
```
Notes:
- If "m-PEA" returns polymer or chemistry noise, drop it and re-run.
- In WoS, also tick the Proceedings indexes to catch conference abstracts.
- Recommended extra free sources if time allows: Google Scholar (first 200 results for `"palmitoylethanolamide" prednisolone arthritis`), EKB Egyptian theses, and the WHO ICTRP registry (`palmitoylethanolamide` AND `arthritis`).

---

## 6. Defensible novelty statements (manuscript-ready, bounded)

**Scope sentence for Methods or Discussion:**
> "A structured literature search of PubMed, Europe PMC (including full-text and preprints), OpenAlex, Semantic Scholar and ClinicalTrials.gov, supplemented by forward and backward citation chasing, was performed on 2 October 2026 [and of Scopus and Web of Science on <date>] using the queries listed in Supplementary Table Sx."

**Statements supported by this search:**

1. **Combination with a glucocorticoid in arthritis.**
   > "To our knowledge, and within the databases and queries listed (searched 2 October 2026), no previous study has evaluated palmitoylethanolamide, in any formulation, in combination with a systemic glucocorticoid in an experimental model of arthritis. The only controlled co-administration of PEA with a systemic glucocorticoid that we identified was in feline hypersensitivity dermatitis, where ultramicronized PEA was given during and after a methylprednisolone taper to delay relapse (Noli et al., 2019)."

2. **Glucocorticoid-sparing (dose-reduction) design with PEA.**
   > "We did not identify any study that tested whether PEA allows the prednisolone dose to be reduced while preserving anti-arthritic efficacy. Comparable glucocorticoid-sparing designs have so far used other agents, including the PPARα agonist gemfibrozil (Ashour et al., 2019), curcumin (Barbosa Retameiro et al., 2025), piperine (Morvaridi et al., 2025), niacin (Mirzaaghasi & Froushani, 2023) and escin (Du et al., 2016)."

3. **Oral PEA in CFA-induced arthritis in rats with immunological endpoints.** Phrase it narrowly:
   > "Previous rat studies combining PEA with complete Freund's adjuvant addressed acute inflammatory pain after intraplantar or temporomandibular CFA injection (Aldossary et al., 2019; Bartolucci et al., 2018) or the role of PEA-degrading NAAA (Bonezzi et al., 2016). In vivo evidence for PEA in inflammatory polyarthritis comes from collagen-induced arthritis in mice (Impellizzeri et al., 2013). Within the searched databases, the present study is, to our knowledge, the first to evaluate oral micronized PEA over the course of CFA-induced arthritis in female rats using serological (ACPA, TNF-α, IL-1β, IL-6), histological and immunohistochemical (NF-κB p65, TLR4) and p38 MAPK endpoints."
   - Before using "first ... female rats ... knee", check that your model wording matches. Barbosa Retameiro 2025 already used intra-articular CFA in female Wistar rats (with curcumin, not PEA).

4. **Head-to-head comparison with targeted immunosuppressants.**
   > "No study identified in the searched databases has compared PEA directly with a JAK inhibitor (e.g., baricitinib) or a calcineurin inhibitor (e.g., tacrolimus) in any inflammatory or arthritis model."

5. **Clinical evidence in RA.**
   > "Clinical evidence for PEA in rheumatoid arthritis is limited to a non-randomized study of PEA plus acetyl-L-carnitine for neuropathic pain in patients with RA or spondyloarthritis (Parisi et al., 2021). A randomized trial including patients with RA-related knee degeneration (NCT07680101) was registered but not yet recruiting as of October 2026. No completed randomized trial of PEA on RA disease activity was identified."

**Claims to avoid** (each is contradicted or not supported):
- "First study ever to combine PEA with a corticosteroid." This is contradicted by Noli 2019 (methylprednisolone, cats). The ATOPA topical steroid reduction and the UC trial NCT07609810 (background corticosteroids) also weaken it.
- "First study of PEA in CFA / adjuvant models in rats." This is contradicted by Bartolucci 2018 (m-PEA, CFA in TMJ, rats), Aldossary 2019, Gaspar 2021 and Bonezzi 2016.
- "First study of PEA in arthritis." This is contradicted by Impellizzeri 2013 (CIA, mice) and the OA/MIA literature.
- "First steroid-sparing nutraceutical or natural-compound strategy in AIA." This is contradicted by the curcumin, piperine, niacin, escin and EGCG precedents.
- "First PPAR-based glucocorticoid-sparing approach." This is contradicted by Ashour 2019 (gemfibrozil, PPARα) and Suke 2013 (pioglitazone).
- "First endocannabinoid-system modulator combined with a glucocorticoid in arthritis." This is contradicted by Nass 2021 (JZL184 + dexamethasone, CIA).
- "PEA has never been tested in RA patients." This is contradicted by Parisi 2021, and NCT07680101 is registered.
- Any unbounded "no study has ever ..." without naming the databases and the date.
- Describing Noli 2019 as a "PEA + methylprednisolone combination efficacy trial". It was a taper and relapse-prevention design.

**Precedents that must appear in the Discussion (minimum set):** Impellizzeri 2013; Bartolucci 2018; Bonezzi 2016; Lowin 2015; Noli 2019; Parisi 2021; Ashour 2019; Barbosa Retameiro 2025; Morvaridi 2025; Du 2016; Nass 2021. Also add one line on NCT07680101.

---

## 7. Limitations of this search
- Scopus, Web of Science, Embase, Google Scholar and regional databases (EKB theses, CNKI) were **not** searched here. Strings for Scopus and WoS are provided in Section 5.
- Semantic Scholar returned results for only 5 of 8 planned queries, because of HTTP 429 rate limiting. Its relevance ranking is OR-like, so only the top 100 records per query were screened.
- Europe PMC full-text search covers the open-access subset only. OpenAlex abstract coverage is incomplete, and it returned only 1 indexed reference for Morvaridi 2025.
- Conference abstracts and non-English grey literature were captured only incidentally.
- Bartolucci 2018: the route of m-PEA administration was not verified, because the abstract does not state it. Check the full text before describing it in the Discussion.
