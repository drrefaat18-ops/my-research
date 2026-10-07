"""Secondary-citation check: a ==highlight== in the Introduction/Background/Discussion of a primary
paper that describes OTHER people's work (reference marker, 'studies have shown', or mechanism
wording) must not be the source of a draft claim -> cite the original paper instead.

Usage (from the review folder):
    PYTHONIOENCODING=utf-8 python ../scripts/secondary_check.py drafts/Day1.md
    python ../scripts/secondary_check.py --demo
Fix: replace the source in the draft, then remove the ==...== marks from that highlight in papers/.
"""
import os, re, sys

TAG = re.compile(r"\[([A-Za-z]+\d{4}[a-z]?)\]")
HL = re.compile(r"([^\n=]{0,400}?)==([^=]+)==([^\n=]{0,40})")  # text before (own-study cue), highlight, after
BG = re.compile(r"introduction|background|discussion", re.I)
METHODS = re.compile(r"^#+ .*\b(methods|patients and|materials)\b", re.I | re.M)  # no Methods = review
OWN = re.compile(r"\b(our|we|this study|the present study|the current study|in this (cohort|trial|study))\b", re.I)
REF = re.compile(r"\[\d+(?:[,–-]\s?\d+)*\]|[a-z)]\s?\d{1,3}(?:[,–-]\s?\d{1,3})*\s*(?:[.;]|$)|\bet al\b")
OTHERS = re.compile(r"\b(other studies|previous(ly)? (studies|reported)|studies have|have (been )?shown|"
                    r"was reported|were reported|has been (suggested|reported|shown)|a recent study|reports|"
                    r"evidence (indicates|suggests|shows))\b", re.I)
# ponytail: word list, not NLP; add words if a mechanism highlight slips through
MECH = re.compile(r"\b(receptor|pathway|signal\w*|cytokine|NF-?κB|TNF|IL-\d|interleukin|macrophage|"
                  r"lymphocyte|T cell|isoprenyl\w*|prenyl\w*|MHC|histocompatibility|AMPK|mTOR|STAT\d|"
                  r"expression|phosphorylation|secretion|mevalonate|agonist)\b", re.I)


def secondary(text):
    """(section, highlight) pairs that look like second-hand claims; empty for reviews."""
    if not METHODS.search(text):
        return []
    out, sec = [], ""
    for ln in text.splitlines():
        if ln.startswith("#"):
            sec = ln.lstrip("# ").strip()
            continue
        for before, h, after in HL.findall(ln):
            if BG.search(sec) and not OWN.search(before + h) and (
                    REF.search(h) or REF.match(after) or OTHERS.search(h) or MECH.search(h)):
                out.append((sec, h))
    return out


def check(md, papers_dir):
    issues = []
    for tag in sorted(set(TAG.findall(md))):
        path = os.path.join(papers_dir, tag + ".md")
        if os.path.exists(path):
            for sec, h in secondary(open(path, encoding="utf-8").read()):
                issues.append((tag, f"highlight in {sec} is second-hand → cite the original study", h[:90]))
    return issues


def demo():
    paper = ("# T\n## Methods\nx\n## Introduction\n"
             "==Statins decrease isoprenylation of Ras and Rho [27].==\n"
             "==Drug repurposing is cheap.==\n"
             "## Results\n==Metformin cut DAS28 by 1.2 in our trial.==\n"
             "## Discussion\n==Other studies have shown benefit in mice.==\n"
             "==Experimental evidence indicates a link.==\n"
             "==In this trial, CRP fell by 30%.==\n"
             "==It lowers TNF== 2.\n"
             "## Introduction\nIn the present study, we tested it. ==STAT3 phosphorylation fell.==\n")
    got = [h for _, h in secondary(paper)]
    assert got == ["Statins decrease isoprenylation of Ras and Rho [27].",
                   "Other studies have shown benefit in mice.",
                   "Experimental evidence indicates a link.", "It lowers TNF"], got
    assert secondary(paper.replace("## Methods", "## Overview")) == []  # reviews are exempt
    print("demo ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--demo"]:
        demo(); sys.exit()
    total = 0
    for path in sys.argv[1:]:
        papers_dir = os.path.join(os.path.dirname(os.path.abspath(path)), "..", "papers")
        found = check(open(path, encoding="utf-8").read(), papers_dir)
        total += len(found)
        print(f"\n== {path}: {len(found)} second-hand source(s)")
        for tag, what, h in found:
            print(f"  [{tag}] {what}\n      → {h}")
    sys.exit(1 if total else 0)
