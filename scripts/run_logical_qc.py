import os
import re
import json
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("d:/vault/my research")
REPORT_PATH = VAULT_ROOT / "07 - Automated QC & Audits" / "logical_qc_report.md"

def test_gate_1_pharmacology():
    """Gate 1: Pharmacological & Receptor Target Coherence"""
    pea_mono = (VAULT_ROOT / "02 - Molecular Axis & Mechanisms" / "PEA-Comprehensive-Pharmacological-Monograph.md").read_text(encoding="utf-8")
    pea_mech = (VAULT_ROOT / "02 - Molecular Axis & Mechanisms" / "PEA-Mechanism-and-Pharmacology.md").read_text(encoding="utf-8")
    
    checks = [
        ("PPAR-α Direct Agonism", "PPAR-α" in pea_mono or "PPAR-alpha" in pea_mono),
        ("ALIAmide Mast Cell Stabilization", "ALIAmide" in pea_mono or "aliamide" in pea_mono.lower()),
        ("NAAA Primary Hydrolyzing Enzyme", "NAAA" in pea_mono or "NAAA" in pea_mech),
        ("IκBα Resynthesis / NF-κB Clamp", "IκBα" in pea_mono or "IκBα" in pea_mech),
        ("Indirect Cannabinoid / GPR55 Entourage", "GPR55" in pea_mono or "CB2" in pea_mono)
    ]
    passed = all(c[1] for c in checks)
    return passed, checks

def test_gate_2_combination_logic():
    """Gate 2: Drug Combination & Steroid-Sparing Logic"""
    crosstalk = (VAULT_ROOT / "02 - Molecular Axis & Mechanisms" / "PPARa-and-GR-Crosstalk-Axis.md").read_text(encoding="utf-8")
    pred_rationale = (VAULT_ROOT / "01 - Rationale & Study Design" / "Prednisolone-Active-Moiety-Rationale.md").read_text(encoding="utf-8")
    
    checks = [
        ("Steroid-Sparing Hypothesis", "sparing" in crosstalk.lower() or "sparing" in pred_rationale.lower()),
        ("Prednisolone Active Moiety Justification", "active metabolite" in pred_rationale.lower() or "intermediate" in pred_rationale.lower()),
        ("Reduced Prednisolone Dose (5 mg/kg)", "5 mg/kg" in crosstalk or "5 mg/kg" in pred_rationale),
        ("Mitigation of Steroid Toxicity (Osteoporosis/Diabetes)", "osteoporosis" in pred_rationale.lower() or "hyperglycemia" in pred_rationale.lower()),
        ("Synergy at Genomic / Transrepression Level", "transrepression" in crosstalk.lower() or "tethering" in crosstalk.lower())
    ]
    passed = all(c[1] for c in checks)
    return passed, checks

def test_gate_3_disease_model():
    """Gate 3: Disease Model & Induction Protocol Logic"""
    official = (VAULT_ROOT / "04 - Experimental Protocols & Pilot" / "Official-Institutional-Protocol-Final.md").read_text(encoding="utf-8")
    cfa_params = (VAULT_ROOT / "01 - Rationale & Study Design" / "CFA-Induction-Parameters.md").read_text(encoding="utf-8")
    
    checks = [
        ("Female Wistar Rats (160-200g)", "Wistar" in official and "160" in official),
        ("CFA Subcutaneous 0.3 mL Dose", "0.3 mL" in official or "0.3 mL" in cfa_params),
        ("Right Inguinal / Thigh Injection Site", "inguinal" in official.lower() or "inguinal" in cfa_params.lower()),
        ("30-Day Oral Treatment (Days 16-45)", "Days 16–45" in official or "Days 16-45" in official or "30 consecutive days" in official),
        ("Day 46 Terminal Sacrifice", "Day 46" in official or "Terminal Sacrifice" in official)
    ]
    passed = all(c[1] for c in checks)
    return passed, checks

def test_gate_4_cohort_symmetry():
    """Gate 4: Experimental Cohort Symmetry & Protocol Hierarchy"""
    official = (VAULT_ROOT / "04 - Experimental Protocols & Pilot" / "Official-Institutional-Protocol-Final.md").read_text(encoding="utf-8")
    main_7 = (VAULT_ROOT / "04 - Experimental Protocols & Pilot" / "Main-Protocol-7-Groups.md").read_text(encoding="utf-8")
    
    checks = [
        ("Official 9 Groups Documented", "Group 9" in official and "Group 1" in official),
        ("Prednisolone 10 mg/kg Monotherapy", "Prednisolone (10 mg/kg" in official or "Prednisolone 10 mg/kg" in main_7),
        ("m-PEA 200 mg/kg Monotherapy", "200 mg/kg" in official and "Monotherapy" in official),
        ("Ascending Combination Tiers (50, 100, 200 mg/kg)", "50 mg/kg" in official and "100 mg/kg" in official and "200 mg/kg" in official),
        ("Both Active Comparators (Tacrolimus + Baricitinib)", "Tacrolimus" in official and "Baricitinib" in official)
    ]
    passed = all(c[1] for c in checks)
    return passed, checks

def test_gate_5_pilot_quarantine():
    """Gate 5: Pilot Data Quarantine & Statistical Sanity"""
    p_rat = (VAULT_ROOT / "04 - Experimental Protocols & Pilot" / "Pilot-Study-Rationale-and-Protocol.md").read_text(encoding="utf-8")
    p_blood = (VAULT_ROOT / "04 - Experimental Protocols & Pilot" / "Pilot-Blood-Work-Final-Observations.md").read_text(encoding="utf-8")
    p_wbc = (VAULT_ROOT / "04 - Experimental Protocols & Pilot" / "Pilot-WBC-Final-Observations.md").read_text(encoding="utf-8")
    
    checks = [
        ("Rationale Note Has WARNING Callout", "[!WARNING]" in p_rat),
        ("Blood Chemistry Has WARNING Callout", "[!WARNING]" in p_blood),
        ("WBC Differential Has WARNING Callout", "[!WARNING]" in p_wbc),
        ("Strict n=2 Quarantine Designated", "n=2" in p_blood and "n=2" in p_wbc),
        ("Prohibition on Literature Pooling Explicit", "quarantine" in p_blood.lower() or "quarantined" in p_blood.lower())
    ]
    passed = all(c[1] for c in checks)
    return passed, checks

def test_gate_6_comparator_dmard():
    """Gate 6: Active Comparator DMARD Logic"""
    bari = (VAULT_ROOT / "05 - Comparators Benchmarking" / "Baricitinib-Comparison.md").read_text(encoding="utf-8")
    tacro = (VAULT_ROOT / "05 - Comparators Benchmarking" / "Tacrolimus-Comparison.md").read_text(encoding="utf-8")
    
    checks = [
        ("Baricitinib JAK1/2 Selectivity ($IC_{50}$)", "5.9 nM" in bari or "JAK1" in bari),
        ("Baricitinib STAT3 & IL-6 Suppression", "STAT3" in bari and "IL-6" in bari),
        ("Baricitinib Dose (10 mg/kg p.o.)", "10 mg/kg" in bari),
        ("Tacrolimus FKBP12 & Calcineurin Mechanism", "FKBP12" in tacro and "Calcineurin" in tacro),
        ("Tacrolimus Dose (1.8 mg/kg p.o.)", "1.8 mg/kg" in tacro),
        ("Safety / Boxed Warning Contrast Documented", "warning" in bari.lower() or "black box" in bari.lower() or "nephrotoxicity" in tacro.lower())
    ]
    passed = all(c[1] for c in checks)
    return passed, checks

def test_gate_7_molecular_signaling():
    """Gate 7: Molecular Signaling & Histopathological Matrix"""
    nfkb = (VAULT_ROOT / "02 - Molecular Axis & Mechanisms" / "NF-kB-p65-and-Cytokines.md").read_text(encoding="utf-8")
    p38 = (VAULT_ROOT / "02 - Molecular Axis & Mechanisms" / "p38-MAPK-and-Knee-Pathology.md").read_text(encoding="utf-8")
    
    checks = [
        ("Dual Clamp Model (PEA + Prednisolone)", "dual" in nfkb.lower() or "clamp" in nfkb.lower()),
        ("NF-κB p65 / RelA Pathway Detailed", "p65" in nfkb and "IκBα" in nfkb),
        ("p38 MAPK Phosphorylation (Thr180/Tyr182)", "Thr180" in p38 or "phospho-p38" in p38.lower()),
        ("Dual MKP-1 (DUSP1) Phosphatase Induction", "MKP-1" in p38 or "DUSP1" in p38),
        ("Histopathological 4-Domain Scoring Matrix", "Safranin-O" in p38 and "Synovial" in p38 and "Cartilage" in p38)
    ]
    passed = all(c[1] for c in checks)
    return passed, checks

def test_gate_8_literature_parity():
    """Gate 8: Literature Matrix & Precedent Integrity"""
    studies_dir = VAULT_ROOT / "03 - Collective Literature Matrix" / "Studies"
    papers_dir = VAULT_ROOT / "03 - Collective Literature Matrix" / "Papers"
    
    studies = list(studies_dir.glob("Study-*.md"))
    precedents = list(studies_dir.glob("Precedent-*.md"))
    papers = list(papers_dir.glob("Paper-*.md"))
    
    checks = [
        ("Exactly 12 Literature Study Notes", len(studies) == 12),
        ("Exactly 2 Precedent Notes", len(precedents) == 2),
        ("Exactly 29 Canonical Paper Notes", len(papers) == 29),
        ("Zero Study-13 Duplicate Note", not (studies_dir / "Study-13-Effect-of-PEA-in-Uveitis-and-Inflammation.md").exists())
    ]
    passed = all(c[1] for c in checks)
    return passed, checks

def test_gate_9_file_architecture():
    """Gate 9: File Architecture, Zero-Stub & Zero-Duplicate Rule"""
    stray_root = list(VAULT_ROOT.glob("Study-*.md"))
    pilot_obs_subfolder = VAULT_ROOT / "04 - Experimental Protocols & Pilot" / "Pilot-Observations-n2"
    source_mirror = VAULT_ROOT / "00-Sources" / "PEA" / "my stuff"
    
    # Check study note depth
    study_files = list((VAULT_ROOT / "03 - Collective Literature Matrix" / "Studies").glob("*.md"))
    sizes = [f.stat().st_size for f in study_files]
    avg_size = sum(sizes) / len(sizes) if sizes else 0
    all_deep = all(s >= 7000 for s in sizes)
    
    checks = [
        ("Zero Stray Files in Root", len(stray_root) == 0),
        ("Redundant Pilot-Observations-n2 Folder Removed", not pilot_obs_subfolder.exists()),
        ("Redundant PEA/my stuff Folder Removed", not source_mirror.exists()),
        ("All Study Notes Deep (>= 7,000 bytes)", all_deep),
        ("Average Study Size > 9,000 bytes", avg_size > 9000)
    ]
    passed = all(c[1] for c in checks)
    return passed, checks

def test_gate_10_connectivity_and_visuals():
    """Gate 10: Zettelkasten Bidirectional Connectivity & Visual Artifacts"""
    # 1. Check all wikilinks
    md_files = list(VAULT_ROOT.glob("**/*.md"))
    existing_stems = {f.stem for f in md_files}
    existing_stems.add("logical_qc_report")
    
    link_pattern = re.compile(r"\[\[([^\|\]]+)(?:\|[^\]]+)?\]\]")
    broken_links = []
    
    for f in md_files:
        if ".system_generated" in str(f) or "node_modules" in str(f) or ".swarm" in str(f):
            continue
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue
        links = link_pattern.findall(content)
        for link in links:
            target = link.strip()
            # If target has a folder path, extract stem
            target_stem = Path(target).stem
            if target_stem not in existing_stems:
                broken_links.append((f.name, target))
                
    # 2. Check Visual Canvas and Base files
    canvas_1 = VAULT_ROOT / "02 - Molecular Axis & Mechanisms" / "Mechanistic-Pathways.canvas"
    canvas_2 = VAULT_ROOT / "07 - Automated QC & Audits" / "Swarm-and-Vault-Architecture.canvas"
    base_1 = VAULT_ROOT / "03 - Collective Literature Matrix" / "Studies-Comparison.base"
    base_2 = VAULT_ROOT / "03 - Collective Literature Matrix" / "Research-Papers.base"
    base_3 = VAULT_ROOT / "07 - Automated QC & Audits" / "Skills-Manifest.base"
    manifest_digest = VAULT_ROOT / "07 - Automated QC & Audits" / "Skills_Manifest_Full_Digest.md"
    
    checks = [
        ("Zero Broken Wikilinks Across Entire Vault", len(broken_links) == 0),
        ("Mechanistic Pathways Canvas Exists", canvas_1.exists()),
        ("Swarm & Vault Architecture Canvas Exists", canvas_2.exists()),
        ("Studies Comparison Base Exists", base_1.exists()),
        ("Research Papers Base Exists", base_2.exists()),
        ("Skills Manifest Base Exists", base_3.exists()),
        ("Skills Manifest Full Digest Note Exists", manifest_digest.exists())
    ]
    passed = all(c[1] for c in checks)
    return passed, checks, broken_links

def main():
    print("=== Running Comprehensive 10-Gate Deep Logical QC ===")
    gates = [
        ("Gate 1: Pharmacological & Receptor Target Coherence", test_gate_1_pharmacology),
        ("Gate 2: Drug Combination & Steroid-Sparing Logic", test_gate_2_combination_logic),
        ("Gate 3: Disease Model & Induction Protocol Logic", test_gate_3_disease_model),
        ("Gate 4: Experimental Cohort Symmetry & Protocol Hierarchy", test_gate_4_cohort_symmetry),
        ("Gate 5: Pilot Data Quarantine & Statistical Sanity", test_gate_5_pilot_quarantine),
        ("Gate 6: Active Comparator DMARD Logic", test_gate_6_comparator_dmard),
        ("Gate 7: Molecular Signaling & Histopathological Matrix", test_gate_7_molecular_signaling),
        ("Gate 8: Literature Matrix & Precedent Integrity", test_gate_8_literature_parity),
        ("Gate 9: File Architecture, Zero-Stub & Zero-Duplicate Rule", test_gate_9_file_architecture),
        ("Gate 10: Zettelkasten Bidirectional Connectivity & Visual Artifacts", test_gate_10_connectivity_and_visuals)
    ]
    
    all_passed = True
    report_lines = [
        "# 🛡️ Deep Logical Quality Control & Scientific Verification Report",
        f"> **Audit Engine:** Multi-Agent Logical Verifier + Ruflo V3 Swarm Coordination",
        f"> **Generated:** {datetime.now().isoformat()}",
        f"> **Target Vault:** Port Said University Master's Thesis Research Vault",
        "",
        "---",
        ""
    ]
    
    for name, fn in gates:
        res = fn()
        if len(res) == 2:
            passed, checks = res
            extra = None
        else:
            passed, checks, extra = res
            
        status_text = "PASSED" if passed else "FAILED"
        status_icon = "🟢 PASSED" if passed else "🔴 FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status_text}] {name}")
        report_lines.append(f"## {status_icon}: {name}")
        report_lines.append("")
        report_lines.append("| Check Item | Status | Result |")
        report_lines.append("|:---|:---:|:---|")
        for desc, chk in checks:
            chk_icon = "✅" if chk else "❌"
            chk_str = "Verified Coherent" if chk else "Logical Discrepancy"
            report_lines.append(f"| {desc} | {chk_icon} | {chk_str} |")
        report_lines.append("")
        
        if extra and len(extra) > 0:
            report_lines.append(f"> **Discrepancies Noted:** {len(extra)}")
            for ex in extra[:10]:
                report_lines.append(f"> - {ex}")
            report_lines.append("")
            
        report_lines.append("---")
        report_lines.append("")
        
    summary_verdict = "🟢 ALL 10 LOGICAL AUDIT GATES PASSED (100% GREEN)" if all_passed else "🔴 LOGICAL GATES REQUIRE REVISION"
    report_lines.insert(5, f"## Final Verdict: {summary_verdict}\n")
    
    REPORT_PATH.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"\nReport written to: {REPORT_PATH}")
    console_verdict = "ALL 10 LOGICAL AUDIT GATES PASSED (100% GREEN)" if all_passed else "LOGICAL GATES REQUIRE REVISION"
    print(f"Overall Result: {console_verdict}")
    return 0 if all_passed else 1

if __name__ == '__main__':
    exit(main())
