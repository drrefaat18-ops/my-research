# C2 — Novelty gap search (update to C-novelty.md)

Run date: **2026-10-06**. Two parallel searches filled the gaps listed in [[C-novelty]] Section 7. Scripts and raw JSON/text results: `tmp/novelty-2026-10-06/` (`api/`, `web/`). Hub: [[06-MOC-Thesis-Defense-and-Publishing]].

**Bottom line:** none of the 5 novelty claims is broken. Claim 2 (glucocorticoid-sparing) is **weakened**: a patent and a new 2026 paper already state the PEA "dose-sparing" idea. Neither tests systemic prednisolone in arthritis.

---

## 1. Sources added in this run

| Group | Sources | Result |
|---|---|---|
| Bibliographic APIs | PubMed and Europe PMC delta since 2026-09-25; Europe PMC preprints; OpenAlex **full text** (11 queries, 505 unique titles); Semantic Scholar relevance + boolean bulk; Crossref | Nothing new on PEA + GC, AIA or JAK/CNI |
| Mechanism/endpoint checks | PEA + MDA/GSH/SOD/CAT/Nrf2 + arthritis; PEA + NF-κB p65 / p38 / TLR4 + arthritis | No AIA/CFA study |
| Trial registries | ClinicalTrials.gov (69 PEA trials), ISRCTN, EU CTR, EU CTIS, WHO ICTRP*, ANZCTR*, ChiCTR*, IRCT*, PACTR* | No PEA + GC or PEA RA-activity trial beyond NCT07680101 |
| Patents | Google Patents (PEA + corticosteroid; PEA + JAK/CNI; Epitech assignee) | Dekel family (below); Epitech PEA + NSAID patents |
| Web / Scholar-style | 12 query sets; Google Scholar first 10 results ×2 before CAPTCHA | Trisolini 2026 (below) |
| Regional / non-English | EKB journals (snippets), Arabic web, CNKI/Wanfang/CQVIP (web), CyberLeninka, J-STAGE, SciELO/BVS, Russian web, Turkish web | Nothing relevant |
| Theses / conferences | Italian ETD, ACR abstracts, ICRS programme books 2008–2025, EULAR (web), veterinary sources | Nothing relevant |

\* Unreliable or blocked; see Section 4.

---

## 2. New records to cite (not in C-novelty.md)

| # | Record | ID | Class | Why it matters |
|---|---|---|---|---|
| 1 | Dekel Pharmaceuticals (Kindler S, Shmulewitz A). *Compositions and methods for treating inflammatory disorders.* Priority 2008-07-31; granted 2017-04-18 | US9623000B2 / WO2010013240A1 / EP2309858A1 | **P (claims 1–2)** | States that N-acylethanolamines have "a steroid-sparing effect". Data: **topical** PEA + hydrocortisone in croton-oil mouse ear oedema only (78% vs 40% inhibition). No arthritis, no systemic prednisolone. Earliest statement of the PEA + GC-sparing idea. |
| 2 | Trisolini S, Toti A, Lucarini E, Di Cesare Mannelli L, Ghelardini C, Micheli L. Enhancing meloxicam efficacy in acute and chronic inflammatory pain: a novel dose-sparing approach using ultramicronized palmitoylethanolamide. *Inflammopharmacology* 2026 (received 4 Aug, accepted 22 Aug, online 6 Oct 2026; open access CC BY) | 10.1007/s10787-026-02380-6 | **P (claim 2)** | **Full text read 2026-10-06.** Male Sprague-Dawley rats. CFA 50 µL into **one tibiotarsal joint** (monoarthritis, not systemic AIA). **Single oral dose on day 7**, read over 0–60 min. Doses: um-PEA 10 mg/kg + meloxicam 3 mg/kg vs meloxicam 3/10/30 mg/kg; n = 6/group. Endpoints: **paw pressure and von Frey only** (no cytokines, histology, NF-κB, oxidative stress). 2×2 factorial synergy (Slinker), p = 0.045. GW6471 showed partial PPAR-α dependence (LPS model). Authors cite Noli 2019 as the only PEA steroid-sparing evidence, so they know of no PEA + GC arthritis study. Two authors hold an Epitech grant. |
| 3 | Sharma OP, Sharma R. *Inflammopharmacology* 2026;34:3335–45 | PMID 41945007 / 10.1007/s10787-026-02197-3 | P (claim 3) | Oral PEA + Cucumis sativus, **female Wistar rats**, MIA osteoarthritis, Bliss/Loewe synergy. Same strain and sex, but OA and no GC. |
| 4 | Jung JI, et al. *Inflammopharmacology* 2021;29:1475–86 | PMID 34468900 / 10.1007/s10787-021-00870-3 | P (claims 3, 5) | Oral PEA 50/100 mg/kg in MIA OA rats lowered TNF-α, IL-1β, NO. OA, not AIA; NO only, no MDA/GSH/SOD/CAT. |
| 5 | Britti D, et al. *BMC Vet Res* 2017;13:229 | PMID 28768536 / 10.1186/s12917-017-1151-z | P (claim 3) | Oral PEA-quercetin in MIA OA and carrageenan rats; serum TNF-α, IL-1β. |
| 7 | Xu B, Wu Y, Han X-M, et al. Discovery of novel long-acting co-prodrugs NSAIDs-PEA. *J Drug Deliv Sci Technol* 2026;122:108390 (cited by Trisolini; not yet opened) | 10.1016/j.jddst.2026.108390 | P (claim 2) | PEA–naproxen co-prodrugs in the CFA pain model; reportedly no additive or synergistic interaction. Cite alongside Trisolini. |
| 6 | Epitech PEA + NSAID patents (priority 2024-02-15) | BR102025002833A2 / CN120478320A; BR102025002842A2 / CN120478363A | P (weak) | PEA as add-on to a conventional anti-inflammatory (NSAID), not a GC. |

**Bartolucci 2018 route:** primary full text is paywalled. A secondary review (Della Rocca & Gamba 2021, *Animals* 11:952, PMC8065429) describes it as **oral** micronized PEA. Abstract: single 10 mg/kg dose, 1 h after intra-TMJ CFA, read at 24–72 h (acute, monoarticular).

---

## 3. Verdict per claim (both searches agree)

| # | Claim | Verdict |
|---|---|---|
| 1 | PEA + **systemic** glucocorticoid in an arthritis model | **Still novel** |
| 2 | PEA **glucocorticoid-sparing** dose-reduction design | **Weakened, not broken.** Concept exists (Dekel patent, topical; Noli 2019, cats; Trisolini 2026, NSAID). Still first systemic/oral prednisolone reduction across graded PEA doses in arthritis. |
| 3 | Oral m-PEA over established CFA polyarthritis (days 16–45) in rats with immunological endpoints | **Still novel.** Oral PEA + cytokines exists only in MIA osteoarthritis. No ACPA, NF-κB p65 IHC or p38 with PEA anywhere. |
| 4 | PEA head-to-head vs JAK or calcineurin inhibitor | **Still novel** (zero hits in any source) |
| 5 | PEA + oxidative-stress panel (MDA, GSH, SOD, CAT) in **adjuvant** arthritis rats | **Still novel for AIA rats only.** Impellizzeri 2013 already measured MDA in CIA **mice**, so do not claim "first PEA oxidative-stress data in arthritis". |

### Updated claim wording (replaces C-novelty.md Section 6, statement 2)

> "A steroid-sparing effect of N-acylethanolamines has been proposed for topical corticosteroids in acute skin inflammation (US9623000B2), and ultramicronized PEA has recently been shown to allow dose reduction of an NSAID in inflammatory pain (Trisolini et al., 2026). To our knowledge, within the databases searched (2 and 6 October 2026), no study has tested whether oral PEA allows the dose of a systemic glucocorticoid to be reduced in experimental arthritis."

---

## 4. Still not covered (manual check by Dr. Refaat via EKB / browser)

1. **Scopus and Web of Science**: run the strings in [[C-novelty]] Section 5. Record date and hit count.
2. **EKB journals and EKB/EULC Egyptian theses**: search `palmitoylethanolamide`. PDFs were blocked from here.
3. **Google Scholar**: re-run the 6 queries in a browser; screen the first 100–200 results.
4. ~~Trisolini 2026 full text~~ — done 2026-10-06 (see Section 2, row 2). Optional: open Xu 2026 (row 7).
5. Blocked by bots or logins: CNKI/Wanfang full search, SID/Magiran, DergiPark, SciELO/LILACS, Shodhganga, OATD, ProQuest, ANZCTR, ChiCTR, IRCT, PACTR, WHO ICTRP (unreliable output), Lens/EPO patents.
6. Five conference abstract books matched PEA + steroid terms in full text, but co-occurrence within one abstract could not be checked (Inflamm Res 2015 World Congress on Inflammation, FEBS Open Bio 2024, ICI 2019, ISNI 2010, BPS 1998).
