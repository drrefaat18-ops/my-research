---
id: "NF-kB-p65-and-Cytokines"
title: "NF-κB p65 Activation Cascade & Pro-inflammatory Cytokine Matrix (TNF-α, IL-1β, IL-6, ACPA)"
category: "Biomarker-Signaling"
tags: [nf-kb, p65, ikb-alpha, tnf-alpha, il-1beta, il-6, acpa, elisa, ihc, master-thesis]
qc_status: "PASSED-DEEP-AUDIT"
qc_auditor: "agency-clinical-evidence-agent"
---

# NF-κB p65 Transcriptional Axis & Pro-Inflammatory Cytokine Cascade

> **Central Inflammatory Hub in Rheumatoid Arthritis:**  
> Nuclear Factor kappa B (NF-$\kappa$B) is the master transcription factor governing synovial hyperplasia, inflammatory osteoclastogenesis, and cartilage erosion in Complete Freund's Adjuvant (CFA) arthritis.

---

## 1. Classical (Canonical) NF-κB Activation Pathway in Adjuvant Arthritis

In the CFA rat model, mycobacterial peptidoglycans, lipoarabinomannan, and endogenous damage-associated molecular patterns (DAMPs) engage toll-like and cytokine receptors on synovial macrophages and fibroblast-like synoviocytes (FLS):

```
[Mycobacterial CFA DAMPs / TNF-α / IL-1β]
                   │
                   ▼
[Receptor Engagement (TLR4, TNFR1, IL-1R)]
                   │
                   ▼
[Activation of IKK Complex (IKKα, IKKβ, NEMO/IKKγ)]
                   │
                   ▼ (Phosphorylation of Ser32 & Ser36 on IκBα)
[IκBα Polyubiquitination & 26S Proteasomal Degradation]
                   │
                   ▼
[Liberation of Canonical Heterodimer: p65 (RelA) / p50]
                   │
                   ▼ (Nuclear Translocation through Nuclear Pore Complexes)
[Binding to Promoter κB-Sites (5'-GGGRNYYYCC-3')]
                   │
                   ▼
[Transcription of Inflammatory Cytokines, Enzymes, & Autoantibody Drivers]
     ├── TNF-α, IL-1β, IL-6, IL-17A
     ├── COX-2, iNOS, mPGES-1
     ├── MMP-1, MMP-3, MMP-13, ADAMTS-4/5
     └── RANKL (driving joint osteoclast bone erosion)
```

---

## 2. Molecular Target Interventions: PEA + Prednisolone Synergy

The core thesis hypothesis relies on a **dual-clamp suppression** of the NF-$\kappa$B p65 pathway at two distinct biochemical loci:

```
                  [Canonical NF-κB Activation Cascade]
                                   │
                                   ▼
             [IκBα Phosphorylation & Degradation Step]
                                   │
                ✅ m-PEA via PPAR-α Transactivation of IκBα
                (Restores & overexpresses cytosolic IκBα clamp)
                                   │
                                   ▼
             [p65/p50 Nuclear Translocation & DNA Binding]
                                   │
                ✅ Prednisolone via GR-α Physical Transrepression
                (Tethers p65 and recruits HDAC2 corepressor complex)
                                   │
                                   ▼
          💥 ZERO TRANSCRIPTION of TNF-α, IL-1β, IL-6, COX-2
```

### 1. Palmitoylethanolamide (m-PEA) Genomic Action (Cytosolic Stabilization):
- **PPAR-$\alpha$ Direct Agonism:** PEA binds the ligand-binding domain of PPAR-$\alpha$, inducing heterodimerization with Retinoid X Receptor (RXR).
- **Induction of I$\kappa$B$\alpha$ Synthesis:** The PPAR-$\alpha$/RXR heterodimer binds Peroxisome Proliferator Response Elements (PPRE) in the promoter of the *NFKBIA* gene (encoding I$\kappa$B$\alpha$), stimulating continuous de novo synthesis of I$\kappa$B$\alpha$.
- **Retention in Cytoplasm:** Newly synthesized I$\kappa$B$\alpha$ binds free p65/p50 heterodimers in the cytosol, masking their Nuclear Localization Signals (NLS) and trapping them in the inactive state.

### 2. Prednisolone Genomic Action (Nuclear Transrepression):
- **Glucocorticoid Receptor Activation:** Prednisolone diffuses across the plasma membrane and binds cytosolic Glucocorticoid Receptor alpha (GR-$\alpha$), causing dissociation of heat shock proteins (HSP90, HSP70).
- **Direct Protein-Protein Tethering:** The ligand-bound GR-$\alpha$ translocates into the nucleus and physically binds the p65 subunit of NF-$\kappa$B without directly binding DNA (*tethering transrepression*).
- **Epigenetic Chromatin Compaction:** GR-$\alpha$ recruits **Histone Deacetylase 2 (HDAC2)** to the promoter regions of *TNF*, *IL1B*, and *IL6*, deacetylating core histones and condensing chromatin into a transcriptionally silent conformation.

---

## 3. Thesis Biomarker Panel & Target Metrics

In Dr. Refaat's experimental protocol, the NF-$\kappa$B cytokine axis is monitored across multiple biological compartments:

| Compartment | Biomarker | Analytical Technique | Pathological CFA Value | Target Combo Value (PEA + Pred) |
|:---|:---|:---:|:---:|:---:|
| **Knee Synovium** | **Phospho-NF-$\kappa$B p65** | Immunohistochemistry (IHC) | Strong intense nuclear staining ($>70\%$ synoviocytes) | Sparse, cytoplasmic-restricted staining ($<15\%$) |
| **Knee Synovium** | **Total I$\kappa$B$\alpha$** | Western Blot / ELISA | Profound depletion due to degradation ($<25\%$ normal) | Restored to normal/supranormal ($>90\%$ normal) |
| **Circulating Serum**| **TNF-$\alpha$** | Rat-specific ELISA | $280 - 450\text{ pg/mL}$ (Marked elevation) | $60 - 95\text{ pg/mL}$ ($>75\%$ suppression) |
| **Circulating Serum**| **IL-1$\beta$** | Rat-specific ELISA | $190 - 320\text{ pg/mL}$ (Pannus driver) | $40 - 70\text{ pg/mL}$ ($>75\%$ suppression) |
| **Circulating Serum**| **IL-6** | Rat-specific ELISA | $350 - 580\text{ pg/mL}$ (Systemic inflammation) | $80 - 120\text{ pg/mL}$ ($>76\%$ suppression) |
| **Circulating Serum**| **ACPA / RF** | Turbidimetry / ELISA | High positive autoantibody titer | Significant reduction ($>60\%$ reduction) |

---

## 4. Zettelkasten Bidirectional Connections
- Cross-talk Axis: [[PPARa-and-GR-Crosstalk-Axis]]
- MAPK Joint Cascade: [[p38-MAPK-and-Knee-Pathology]]
- Official 9-Group Protocol: [[Official-Institutional-Protocol-Final]]
- Pharmacological Monograph: [[PEA-Comprehensive-Pharmacological-Monograph]]
- Pilot Evidence Confirmation: [[Pilot-Blood-Work-Final-Observations]]
- Baricitinib Benchmark: [[Baricitinib-Comparison]]
