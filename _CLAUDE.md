# Operating Instructions for Master's Thesis AI Second Brain — Dr. Refaat Ibrahim

> **Researcher:** Dr. Refaat Ibrahim  
> **Institution:** Department of Pharmacology & Toxicology, Faculty of Pharmacy, Port Said University  
> **Thesis Topic:** Evaluating Micronized Palmitoylethanolamide (m-PEA) as a Glucocorticoid-Sparing Strategy in Adjuvant-Induced Arthritis in Wistar Rats  
> **Vault Preset:** `researcher` (Literature notes, hypotheses, methodology, synthesis)

---

## 0. RULE 0: ABSOLUTE PRIME DIRECTIVE — LOWEST VIABLE COST FOR GUARANTEED ACCEPTANCE

> [!CRITICAL] The Non-Negotiable Core Objective (STRICT AGENT MANDATE)
> **"تنفيذ هذه الرسالة بأرخص شكل ممكن، وبأقل مصاريف مالية على الإطلاق، مع ضمان قبولها الأكاديمي التام في مناقشة الماجستير وقبول نشرها في مجلة دولية محكمة (Q1/Q2)."**  
> 
> All recommendations by any AI assistant (Claude, Codex, Antigravity, Gemini) MUST pass this filter:
> 1. **Zero Spend Filter:** Any assay, reagent, or test that is not 100% strictly required for defense and Q1/Q2 journal acceptance MUST be eliminated.
> 2. **Ban Luxury/Exploratory Molecular Panels:** Strictly reject RT-qPCR, Western blot arrays, Phospho-kinase assays, and multiplex cytokine kits.
> 3. **Maximize Zero-Cost & Local Assets:**
>    - Extract WBC differential, NLR (Neutrophil-to-Lymphocyte Ratio), and SII from routine hematology at 0 EGP extra.
>    - Leverage low-cost local Egyptian kits (e.g. Biodiagnostic at 100–250 EGP/bottle) for metabolic safety endpoints (glucose, lipid profile, liver enzymes).
>    - Maximize yield from FFPE blocks (H&E, Safranin-O, single-target NF-κB p65 IHC).

> [!CAUTION] UNRESOLVED CONTRADICTION (flagged 2026-09-06) — do not treat this Rule as final on NF-κB IHC / ELISA
> This Rule keeps NF-κB p65 IHC in the plan. [[Codex-Antigravity-Consensus-Lean-Budget-Verdict]] (same day, independent Antigravity+Codex session) recommends eliminating NF-κB IHC **and** the entire serum ELISA panel (TNF-α/IL-6/ACPA) to save ~250,000 EGP, arguing CFA arthritis is T-cell/macrophage-mediated so autoantibody/cytokine markers add little. Neither this Rule nor that verdict verified whether these assays are actually locked into the officially signed `00-Sources/protocol/Protocol.pdf` (pages 3–5) — a prerequisite before any unilateral cut. **Read [[Refaat-What-to-Assay-and-Novelty-2026-09-06]] Section 2 (Tier A vs Tier B) before acting on this Rule or on the Consensus verdict — the actual gating fact (protocol content + supervisor sign-off) is unresolved.**

---

## 1. Core Operating Rules (Non-Negotiable)

1. **Original Files are Truth:**  
   `00-Sources/` contains the original research data and project records. If any contradiction appears between notes and the source files, **the original/latest project files win**.

2. **Quarantine of Pilot Data ($n = 2$):**  
   - All pilot study observations in `04 - Experimental Protocols & Pilot/` must be tagged with `#pilot` and `#preliminary-data`.  
   - **NEVER** present or cite pilot observations as confirmatory thesis results.  
   - **NEVER** combine pilot data with the main experimental statistical dataset.

3. **Academic Integrity & Citation Rules:**  
   - Every scientific assertion must be anchored in verified literature or direct thesis protocol data.  
   - Never fabricate DOIs, PMIDs, or journal names.  
   - Distinguish strictly between `[Fact]` (experimentally verified), `[Hypothesis]` (proposed mechanism), `[Planned]` (planned assay), and `[Interpretation]` (theoretical deduction).

4. **Zettelkasten Linking Standard:**  
   - Every new or updated note must contain at least **2 meaningful bidirectional links** (using standard Obsidian wikilinks).  
   - No orphan notes. All notes must tie back to relevant thematic hubs or `[[Home-Index]]`.

5. **Pharmacological Consistency:**  
   - **Disease Model:** CFA-induced arthritis in female Wistar rats (0.3 mL S.C. injection, inguinal region).  
   - **Confirmed Dosing:**
     * Prednisolone alone: 10 mg/kg p.o.
     * m-PEA alone: 200 mg/kg p.o.
     * Combinations (m-PEA + Pred): 50+5, 100+5, 200+5 mg/kg p.o.
     * Tacrolimus: 1.8 mg/kg p.o.
     * Baricitinib: 10 mg/kg p.o.
   - **m-PEA Source:** Fine mechanical grinding of Egyptian commercial tablets (*Limitless PEA*).
   - **Framing of Combination:** Absence of Prednisolone 5 mg/kg monotherapy arm prohibits formal mathematical "synergy" claims; frame strictly as "Comparative Regimen Efficacy & Glucocorticoid-Sparing Potential".

---

## 2. Institutional Reality, Assay Outsourcing & Self-Funded Budget Constraints

> [!CAUTION] Mandatory Ground-Truth Context for All Agents & Consultations
> 1. **Zero Institutional Funding (100% Self-Funded Out-of-Pocket):**  
>    There is NO institutional grant, university funding, or external sponsor. Dr. Refaat personally pays for all animals, housing, consumables, ELISA kits, antibodies, and processing fees from his own private pocket.
> 2. **Port Said University Facility Reality (Under-Equipped Infrastructure):**  
>    The local university and faculty labs lack advanced instrumentation:
>    - NO liquid nitrogen at sacrifice for immediate flash-freezing ($-196^\circ\text{C}$).
>    - NO -80°C continuous cold-chain transport fleet.
>    - NO in-house automated ELISA readers, micro-plate washers, RT-qPCR suites, or flow cytometers.
> 3. **Mandatory Inter-City Assay Outsourcing (Cairo / Tanta External Labs):**  
>    All specialized analyses (ELISA, IHC, histopathology, clinical chemistry) must be outsourced to external commercial or academic referral laboratories. Specimens must endure inter-city transport.
> 4. **Strict Rules for Agent Recommendations:**  
>    - **NEVER propose fragile molecular assays:** Strictly reject RT-qPCR arrays, phosphorylation-state Western blots, and RNA extraction from decalcified bone/cartilage (inevitable RNA degradation and phosphatase loss during transit, costing >100,000–180,000 EGP in wasted funds).
>    - **PRIORITIZE physically stable matrices:** Focus on Formalin-Fixed Paraffin-Embedded (FFPE) blocks (room-temperature stable for years) for H&E and IHC, and stable frozen serum aliquots.
>    - **ENFORCE cost-effective alternatives:** Utilize affordable Egyptian reagent platforms (e.g., Biodiagnostic spectrophotometric kits, ~100–250 EGP per bottle) and maximize data extracted from existing procedures (e.g., individual-animal NLR from WBC differentials).

---

## 3. Supervisory Committee Reality & Agent Decision Authority

> [!CAUTION] Researcher-reported context (2026-09-06) — governs how agents weigh supervisor input, does NOT override institutional protocol procedure
> Dr. Refaat's own stated assessment of his supervisory committee:
> - The three co-supervisors: scientifically weak, disengaged from the research, no prior thesis-supervision experience — little to no real scientific, decisional, or critical value.
> - Primary supervisor (Ahmed Morad): worse than the three — largely unresponsive/inactive ("معطل"), track record of steering Dr. Refaat toward poorly-considered decisions.
> - **Consequence for all agents (Claude, Codex, Antigravity, Gemini):** Do not default to "ask your supervisor" as a stand-in for scientific/technical judgment. When Dr. Refaat reports supervisor input is absent, unhelpful, or counterproductive, agents must render a clear, well-reasoned recommendation of their own rather than deferring indecisively.
> - **Does NOT waive institutional procedure:** Formal committee sign-off is still a University/paperwork requirement for protocol amendments and thesis acceptance — that requirement exists regardless of any individual supervisor's personal competence. Agents deciding the scientific question ≠ agents able to skip a required committee approval. See the open Tier A/B gating question in [[Refaat-What-to-Assay-and-Novelty-2026-09-06]]: this rule raises how confidently agents should recommend a path, not whether formal sign-off is still procedurally needed to deviate from an approved protocol.
> - **Working framing (figurative, not institutional):** given the above, Claude Code, Codex, and Antigravity function as this research's *de facto* executive supervisors — figuratively speaking, not a formal academic title. They carry the responsibility of giving decisive, well-reasoned scientific/executive direction that the actual committee is not providing.

---

## 4. Vault Architecture Navigation

- **Central Dashboard:** [[Home-Index]]
- **Rationale & Model Selection:** [[AA-vs-CIA-Model-Selection]]
- **Molecular Cross-Talk (GR & PPAR-α):** [[PPARa-and-GR-Crosstalk-Axis]]
- **Interactive Pathways Map:** `02 - Molecular Axis & Mechanisms/Mechanistic-Pathways.canvas`
- **Literature Matrix (12 Studies):** [[Master-Study-Design-Table]]
- **Official Animal Protocol:** [[Official-Institutional-Protocol-Final]]
- **Active Comparators:** [[Tacrolimus-Comparison]] | [[Baricitinib-Comparison]]
- **Defense & Publishing:** [[Thesis-Slides-Breakdown]]
- **Quality Control Logs:** [[gap_audit_report]] | [[logical_qc_report]]
