"""
Scientific Quality Control — checks claims, not just files.

The existing run_qc_audit.py / run_logical_qc.py / gap_audit.py gates only test
whether a phrase/link/file EXISTS. That certifies vault hygiene, not that the
underlying scientific claim is true or properly hedged. This script adds the
missing half: overclaim language, statistical overreach on n=2 pilot data,
the missing-control-arm synergy trap, cross-document dose/group parity, and
regression tests for citation errors already found once (so they can't
silently reappear as "PASSED" elsewhere).

This is a heuristic linter, not a fact-checker. A PASS here means "no known
red flag pattern found" — it does not mean a human still shouldn't read the
manuscript before submission.
"""
import re
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("d:/vault/my research")
REPORT_PATH = VAULT_ROOT / "07 - Automated QC & Audits" / "scientific_qc_report.md"

NEGATION_CUES = [
    "ممنوع", "لا تقل", "لا تكتب", "لا تدّعي", "لا تدعي", "احذر", "تذكير", "ليس", "وليس",
    "do not", "don't", "never write", "never claim", "never apply", "never assert",
    "never", "avoid", "banned", "zero inferential", "not proven", "not a proven",
    "غير مقبول", "خطأ", "wrong", "incorrect", "misattribut",
]

def _has_nearby_negation(text: str, pos: int, window: int = 120) -> bool:
    span = text[max(0, pos - window): pos + window].lower()
    return any(cue.lower() in span for cue in NEGATION_CUES)


def gate_overclaim_language():
    """Gate A: banned overclaim phrases in thesis-facing (06) notes."""
    banned = [
        r"100\s*%.{0,20}(novelty|جدة)", r"جدة.{0,20}100\s*%",
        r"لم يُنفَّذ قط.{0,30}تاريخ", r"لم يسبق لأحد.{0,30}تاريخ",
        r"first study in the history", r"never.{0,20}history of medicine",
        r"definitively proven synerg", r"proven synergy",
        r"no (international )?reviewer (could|can) (question|dispute)",
        r"لا يقوى أي محكم", r"\bairtight\b",
    ]
    folder = VAULT_ROOT / "06 - Thesis Defense & Publishing"
    hits = []
    for f in folder.glob("*.md"):
        text = f.read_text(encoding="utf-8", errors="ignore")
        for pat in banned:
            for m in re.finditer(pat, text, re.IGNORECASE):
                if not _has_nearby_negation(text, m.start()):
                    line_no = text.count("\n", 0, m.start()) + 1
                    hits.append((f.name, line_no, m.group(0)[:60]))
    return len(hits) == 0, hits


def gate_pilot_statistical_overreach():
    """Gate B: inferential-statistics language inside quarantined n=2 pilot notes."""
    pilot_dir = VAULT_ROOT / "04 - Experimental Protocols & Pilot"
    banned = [r"p\s*<\s*0\.0", r"\bANOVA\b", r"\bTukey\b", r"statistically significant"]
    hits = []
    for f in pilot_dir.glob("Pilot-*.md"):
        text = f.read_text(encoding="utf-8", errors="ignore")
        if "n=2" not in text and "QUARANTINE" not in text.upper():
            continue
        for pat in banned:
            for m in re.finditer(pat, text, re.IGNORECASE):
                if not _has_nearby_negation(text, m.start()):
                    line_no = text.count("\n", 0, m.start()) + 1
                    hits.append((f.name, line_no, m.group(0)))
    return len(hits) == 0, hits


def gate_missing_control_arm_synergy_trap():
    """Gate C: 'synergy' claims not hedged near the known missing Pred-5-alone arm."""
    official = (VAULT_ROOT / "04 - Experimental Protocols & Pilot" / "Official-Institutional-Protocol-Final.md").read_text(encoding="utf-8")
    has_pred5_alone = bool(re.search(r"Prednisolone\s*\(?5\s*mg/kg\)?\s*(Monotherapy|alone)", official, re.IGNORECASE))

    hedges = [
        "absence of", "غياب", "لغياب", "prevents mathematical", "precludes",
        "comparative regimen efficacy", "cannot", "لا يمكن إثبات",
        "not proof", "not proven", "not established", "requires the missing",
        "lacks the standalone", "no standalone", "does not apply", "does not include",
        "hypothesized", "cooperative", "framed as", "reframed", "musyc", "bliss/loewe",
        "if a validated synergy model", "مؤشراً استكشافياً", "تآزر", "مثبت",
        "do not claim", "do not itself establish",
    ]
    folder = VAULT_ROOT / "06 - Thesis Defense & Publishing"
    hits = []
    if not has_pred5_alone:
        for f in folder.glob("*.md"):
            text = f.read_text(encoding="utf-8", errors="ignore")
            for m in re.finditer(r"synerg", text, re.IGNORECASE):
                window = text[max(0, m.start() - 1500): m.start() + 1500].lower()
                if not any(h in window for h in hedges):
                    line_no = text.count("\n", 0, m.start()) + 1
                    hits.append((f.name, line_no, text[max(0, m.start()-30):m.start()+30].replace("\n", " ")))
    return len(hits) == 0, hits, has_pred5_alone


def gate_pilot_dose_parity():
    """Gate D: dose values in the pilot rationale doc vs the actual pilot data notes."""
    pilot_dir = VAULT_ROOT / "04 - Experimental Protocols & Pilot"
    rationale = (pilot_dir / "Pilot-Study-Rationale-and-Protocol.md").read_text(encoding="utf-8")
    blood = (pilot_dir / "Pilot-Blood-Work-Final-Observations.md").read_text(encoding="utf-8")
    wbc = (pilot_dir / "Pilot-WBC-Final-Observations.md").read_text(encoding="utf-8")

    dose_pat = re.compile(r"(\d+(?:\.\d+)?)\s*mg/kg")
    rationale_doses = set(dose_pat.findall(rationale))
    data_doses = set(dose_pat.findall(blood)) | set(dose_pat.findall(wbc))

    overlap = rationale_doses & data_doses
    passed = len(overlap) > 0
    detail = {
        "rationale_doses": sorted(rationale_doses, key=float),
        "data_doses": sorted(data_doses, key=float),
        "overlap": sorted(overlap, key=float),
    }
    return passed, detail


KNOWN_CITATION_REGRESSIONS = [
    {
        "file": "02 - Molecular Axis & Mechanisms/p38-MAPK-and-Knee-Pathology.md",
        "bad_pattern": r"MKP-1\s*\(?DUSP1\)?",
        "caveat_any_of": ["unpublished", "dipyridamole", "not a direct pea", "exploratory candidate", "not an established pea mechanism"],
        "description": "DUSP1/MKP-1 induction asserted as a PEA mechanism. Original cited source ([[Paper-Selective-amplification-of-glucocorticoid-anti-inflammatory]]) is about dipyridamole+prednisolone and labels the GILZ/DUSP1 data 'unpublished'. See [[Novelty-and-Affordable-Biomarker-Decision-2026-09-06]] item 1.",
    },
    {
        "file": "03 - Collective Literature Matrix/Studies/Study-11-Antioxidant-and-Angiostatic-Effect-of-Spirulina-pl.md",
        "bad_pattern": r"[Ff]emale Wistar",
        "caveat_any_of": ["male wistar", "original uses male", "source uses male"],
        "description": "Note claims female Wistar rats. Original source (Ali, Barakat & Hassan, PLOS ONE 2015, DOI 10.1371/journal.pone.0121523) used MALE Wistar rats, 250-300g. See [[Novelty-and-Affordable-Biomarker-Decision-2026-09-06]] item 2.",
    },
]

def gate_citation_regressions():
    """Gate E: known-bad citations must carry their correction caveat, or they've silently regressed."""
    hits = []
    for reg in KNOWN_CITATION_REGRESSIONS:
        path = VAULT_ROOT / reg["file"]
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if re.search(reg["bad_pattern"], text):
            if not any(re.search(r"\b" + re.escape(c) + r"\b", text, re.IGNORECASE) for c in reg["caveat_any_of"]):
                hits.append((path.name, reg["description"]))
    return len(hits) == 0, hits


def main():
    print("=== Running Scientific Quality Control (claim-level, not file-level) ===")
    lines = [
        "# 🔬 Scientific Quality Control Report (Claim-Level Audit)",
        f"> **Generated:** {datetime.now().isoformat()}",
        "",
        "{VERDICT}",
        "",
        "> **Scope:** overclaim language, statistical overreach on quarantined pilot data,",
        "> the missing-control-arm synergy trap, cross-document dose parity, and citation regressions.",
        ">",
        "> [!WARNING] What this is and is not",
        "> This complements — it does not replace — [[master_qc_audit]], [[gap_audit_report]] and [[logical_qc_report]],",
        "> which verify **vault hygiene** (files exist, links resolve, phrases are present). This script verifies",
        "> **claim-level red flags**: language that overstates evidence, statistics misapplied to n=2 data,",
        "> synergy claims unhedged against the known missing Prednisolone-5-alone arm, dose mismatches between",
        "> linked documents, and citations already found once to misattribute a source. A PASS here is a heuristic",
        "> 'no known red flag found', not proof the manuscript is correct — a human read before submission is still required.",
        "",
        "---",
        "",
    ]

    all_passed = True

    ok, hits = gate_overclaim_language()
    all_passed &= ok
    lines.append(f"## {'🟢 PASSED' if ok else '🔴 FAILED'}: Gate A — Overclaim Language (novelty/synergy absolutism)")
    lines.append("")
    if hits:
        lines.append("| File | Line | Matched phrase |")
        lines.append("|:---|:---:|:---|")
        for fname, ln, snippet in hits:
            lines.append(f"| {fname} | {ln} | `{snippet}` |")
    else:
        lines.append("No unhedged absolutist novelty/synergy language found in `06 - Thesis Defense & Publishing/`.")
    lines.append("")
    lines.append("---\n")

    ok, hits = gate_pilot_statistical_overreach()
    all_passed &= ok
    lines.append(f"## {'🟢 PASSED' if ok else '🔴 FAILED'}: Gate B — Statistical Overreach on Quarantined n=2 Pilot Data")
    lines.append("")
    if hits:
        lines.append("| File | Line | Matched phrase |")
        lines.append("|:---|:---:|:---|")
        for fname, ln, snippet in hits:
            lines.append(f"| {fname} | {ln} | `{snippet}` |")
    else:
        lines.append("No p-values / ANOVA / 'statistically significant' language found asserted on n=2 pilot files.")
    lines.append("")
    lines.append("---\n")

    ok, hits, has_pred5 = gate_missing_control_arm_synergy_trap()
    all_passed &= ok
    lines.append(f"## {'🟢 PASSED' if ok else '🔴 FAILED'}: Gate C — Missing-Control-Arm Synergy Trap")
    lines.append("")
    lines.append(f"Official protocol contains a standalone Prednisolone 5 mg/kg monotherapy arm: **{has_pred5}**.")
    if not has_pred5:
        lines.append("Without that arm, every 'synergy' claim must be hedged within ~1500 chars by an acknowledgement of the limitation, or reframed as comparative regimen efficacy.")
    lines.append("")
    if hits:
        lines.append("| File | Line | Context |")
        lines.append("|:---|:---:|:---|")
        for fname, ln, snippet in hits:
            lines.append(f"| {fname} | {ln} | `...{snippet}...` |")
    else:
        lines.append("Every 'synergy' mention in `06 - Thesis Defense & Publishing/` has a nearby hedge, or the control arm exists.")
    lines.append("")
    lines.append("---\n")

    ok, detail = gate_pilot_dose_parity()
    all_passed &= ok
    lines.append(f"## {'🟢 PASSED' if ok else '🔴 FAILED'}: Gate D — Pilot Rationale vs Pilot Data Dose Parity")
    lines.append("")
    lines.append(f"- Doses in `Pilot-Study-Rationale-and-Protocol.md`: {', '.join(detail['rationale_doses']) or '(none found)'}")
    lines.append(f"- Doses in `Pilot-Blood-Work` + `Pilot-WBC` observation notes: {', '.join(detail['data_doses']) or '(none found)'}")
    lines.append(f"- Overlap: {', '.join(detail['overlap']) or '**NONE — these describe two different dosing designs.**'}")
    if not ok:
        lines.append("")
        lines.append("> [!CAUTION] These three documents currently describe two incompatible pilot designs. Confirm which one was actually run before writing Methods.")
    lines.append("")
    lines.append("---\n")

    ok, hits = gate_citation_regressions()
    all_passed &= ok
    lines.append(f"## {'🟢 PASSED' if ok else '🔴 FAILED'}: Gate E — Known Citation-Integrity Regressions")
    lines.append("")
    if hits:
        lines.append("| File | Issue |")
        lines.append("|:---|:---|")
        for fname, desc in hits:
            lines.append(f"| {fname} | {desc} |")
    else:
        lines.append("Both previously-found citation errors (DUSP1/dipyridamole, Spirulina rat sex) now carry their correction caveat.")
    lines.append("")
    lines.append("---\n")

    verdict = "🟢 ALL SCIENTIFIC-QC GATES PASSED (no known red flags)" if all_passed else "🔴 SCIENTIFIC-QC GATES FAILED — see gates below"
    report_text = "\n".join(lines).replace("{VERDICT}", f"## Final Verdict: {verdict}")

    REPORT_PATH.write_text(report_text, encoding="utf-8")
    print(f"\nReport written to: {REPORT_PATH}")
    print(f"Overall: {'PASSED' if all_passed else 'FAILED'}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
