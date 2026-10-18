"""Figure 1 draft: RA joint inflammation and the pathways repurposed drugs target.
Every label must match a card in .claude/state/step14/fig1_cards.txt (verify_quotes.py).
Usage: python scripts/fig1_draft.py  -> 08 - RA Repurposing Review/Figure_1_Draft.png + .pdf
"""
import matplotlib.pyplot as plt

OUT = "08 - RA Repurposing Review/Figure_1_Draft"
CELL, MED, APPROVED, LINK = "#4a7bb7", "#c0392b", "#555", "#999"

fig, ax = plt.subplots(figsize=(24, 15))
ax.set_xlim(0, 24.5); ax.set_ylim(-1.6, 14.2); ax.axis("off")


def box(x, y, s, fc="#f2f2f2", ec="#333", fs=12.5, ha="center", color="black", weight="normal"):
    ax.text(x, y, s, ha=ha, va="center", fontsize=fs, color=color, weight=weight,
            bbox=dict(boxstyle="round,pad=0.4", fc=fc, ec=ec))


def arrow(p0, p1, kind="act", c="#333", lw=2, ls="-"):
    style = {"act": "-|>", "inh": "-[,widthB=0.6,lengthB=0"}[kind]
    ax.annotate("", p1, p0, arrowprops=dict(arrowstyle=style, color=c, lw=lw, ls=ls, mutation_scale=18,
                                            shrinkA=4, shrinkB=4))


def note(x, y, s, c="#333", ha="left", fs=10.5, va="bottom"):
    ax.text(x, y, s, ha=ha, va=va, fontsize=fs, color=c,
            bbox=dict(boxstyle="square,pad=0.1", fc="white", ec="none", alpha=0.9))


# ---- A. In the RA joint (paragraphs 1-2 of Section 3) ----
ax.text(0.2, 13.8, "A. In the RA joint", fontsize=17, weight="bold")
box(1.3, 12.2, "DCs", fc=CELL, ec=CELL, color="white", weight="bold", fs=14)
box(4.4, 12.2, "T cells", fc=CELL, ec=CELL, color="white", weight="bold", fs=14)
arrow((1.95, 12.2), (3.6, 12.2), c=CELL)
note(2.75, 12.35, "recruit and\nactivate", c=CELL, ha="center", fs=10)
TARGET_CELLS = {"B cells": 12.9, "Macrophages": 11.9, "Synoviocytes (FLS)": 10.9, "Chondrocytes": 9.9, "Osteoclasts": 8.9}
for name, y in TARGET_CELLS.items():
    box(8.4, y, name, fc="#dfe9f5", ec=CELL, fs=12)
    arrow((5.2, 12.2), (7.0, y), c=CELL, lw=1.6)
note(9.75, 10.9, "aggressive,\ntumour-like", c=CELL, fs=10, va="center")
note(6.1, 13.25, "stimulate", c=CELL, ha="center", fs=10)
box(3.2, 10.2, "IL-6 · IL-21 · IL-23\n→ STAT3 → Th17 differentiation", fc="#fdf2e9", ec=MED, fs=11.5)
arrow((4.4, 11.75), (3.9, 10.75), c=CELL, lw=1.6)
note(4.3, 11.2, "differentiate", c=CELL, fs=10, va="center")
box(5.6, 6.9, "TNF-α · IL-6 · IL-1β · MMPs\n(also IL-17, IL-21, IL-23)", fc="#fdecea", ec=MED, fs=13, weight="bold")
arrow((8.4, 8.45), (6.6, 7.45), c=MED)
box(1.5, 5.1, "TNF-α and IL-6R\nantagonists\n(clinical use)", fc="#eeeeee", ec=APPROVED, fs=11.5)
arrow((1.9, 5.75), (4.1, 6.55), kind="inh", c=APPROVED)
note(2.2, 6.35, "TNF-α, IL-6", c=APPROVED, fs=10)
box(5.6, 4.7, "Synovial cell proliferation\nCartilage and bone damage", fc="#ffffff", ec=MED, fs=12.5)
arrow((5.6, 6.35), (5.6, 5.25), c=MED)
box(4.8, 2.3, "RANKL\n(TNF superfamily)", fc="#fdecea", ec=MED, fs=12)
box(8.6, 2.3, "Osteoclast\ndifferentiation", fc="#dfe9f5", ec=CELL, fs=12)
arrow((5.95, 2.3), (7.6, 2.3), c=MED)
ax.plot([11.3, 11.3], [-0.6, 14.0], color="#bbb", lw=1.2)

# ---- B. Intracellular pathways and drug entry points (paragraphs 2-3) ----
ax.text(11.6, 13.8, "B. Intracellular pathways and repurposed-drug entry points", fontsize=17, weight="bold")
TX = 15.6  # targets are right-aligned here; drug arrows end at TX + 0.15
TARGETS = {"JAK/STAT": 12.6, "NF-κB": 11.2, "PI3K/AKT": 10.0, "MAPK · WNT · SYK": 9.0, "AMPK": 7.4,
           "mTORC1": 5.9, "PPAR-γ": 4.5, "HMG-CoA reductase": 3.0, "AT1R": 1.6}
for name, y in TARGETS.items():
    box(TX, y, name, ha="right", fs=13, weight="bold")
note(11.6, 10.0, "proliferation, metabolism,\nangiogenesis, survival", c="#555", fs=9.5, va="center")
note(11.6, 6.6, "six metabolic pathways\n(glycolysis, TCA, PPP, FAO,\nFAS, amino acids) act in\nRA progression;\nCD4+ T: glycolysis → PPP;\nFLS: anaerobic glycolysis,\nlactate ↑",
     c="#555", fs=9.5, va="center")
arrow((15.0, 7.05), (15.0, 6.3), kind="inh", c="#1f77b4")
note(15.15, 6.65, "raptor phosphorylation,\nenergy stress [cells]", c="#1f77b4", fs=9.5, va="center")

# (drug, y, colour, target, label, kind)
X0 = 21.0
DRUGS = [
    ("JAK inhibitors", 13.1, APPROVED, "JAK/STAT", "FDA-approved; baricitinib (JAK1/2) approved for RA", "inh"),
    ("Fenofibrate", 12.1, "#9467bd", "JAK/STAT", "STAT3 activation ↓, IL-21 ↓; may reduce\nTh17 differentiation [cells]", "inh"),
    ("Dulaglutide", 11.0, "#17becf", "NF-κB", "linked to JNK/NF-κB signalling in FLS [cells]", "inh"),
    ("Metformin", 8.0, "#1f77b4", "AMPK", "activates AMPK in hepatocytes [cells]", "act"),
    ("Dapagliflozin", 6.9, "#8c564b", "AMPK", "p-AMPK/t-AMPK ↑ in AIA rat joints [animal]", "act"),
    ("Pioglitazone", 4.5, "#2ca02c", "PPAR-γ", "mitophagy ↑ → inflammasome ↓, IL-1β, IL-18 ↓ [abstract];\nTNF-α-induced FLS: IL-1β, IL-6, IL-8 ↓, IL-10 ↑ [cells]", "act"),
    ("Statins", 3.0, "#ff7f0e", "HMG-CoA reductase", "IFN-γ-induced MHC-II ↓; L-mevalonate reverses [cells]", "inh"),
    ("Losartan", 1.6, "#d62728", "AT1R", "experimental arthritis ameliorated [animal]", "inh"),
]
for name, y, c, tgt, label, kind in DRUGS:
    box(22.75, y, name, fc=c, ec=c, color="white", weight="bold", fs=13.5)
    y1 = TARGETS[tgt] + (0.25 if name in ("JAK inhibitors", "Metformin") else -0.25 if name in ("Fenofibrate", "Dapagliflozin") else 0)
    arrow((X0, y), (TX + 0.15, y1), kind=kind, c=c)
    if name == "Fenofibrate":  # below its arrow, so it does not collide with the JAK inhibitor label
        note(TX + 0.45, y1 - 0.12, label, c=c, fs=10, va="top")
    else:
        note(TX + 0.45, y1 + (0.15 if name == "JAK inhibitors" else 0.08), label, c=c, fs=10)

# cross-panel links (grey dashed): pathway output feeds panel A
arrow((14.2, 11.2), (7.6, 7.25), c=LINK, lw=1.3, ls="--")
note(10.6, 8.3, "NF-κB → IL-1β, IL-6, TNF-α", c="#777", fs=9.5, ha="center")
arrow((13.6, 12.6), (5.25, 10.6), c=LINK, lw=1.3, ls="--")
arrow((14.6, 1.6), (5.9, 2.0), c=LINK, lw=1.3, ls="--")
note(12.6, 1.95, "RA synovial cells: Ang II ↑ RANKL via AT1R;\nAT1R blocker (olmesartan) prevents it, AT2R blocker does not [cells]", c="#777", fs=9.5, ha="center")
note(11.6, 4.5, "PPAR-γ reduced\nin RA FLS [cells]", c="#2ca02c", fs=9.5, va="center")

# legend
ax.annotate("", (1.6, -0.5), (0.4, -0.5), arrowprops=dict(arrowstyle="-|>", lw=2, color="#333", mutation_scale=18))
ax.text(1.8, -0.5, "activates / increases", va="center", fontsize=12)
ax.annotate("", (6.0, -0.5), (4.8, -0.5), arrowprops=dict(arrowstyle="-[,widthB=0.6,lengthB=0", lw=2, color="#333"))
ax.text(6.2, -0.5, "inhibits / decreases", va="center", fontsize=12)
ax.annotate("", (10.4, -0.5), (9.2, -0.5), arrowprops=dict(arrowstyle="-|>", lw=1.3, ls="--", color=LINK, mutation_scale=18))
ax.text(10.6, -0.5, "link between panels", va="center", fontsize=12)
ax.text(14.2, -0.5, "[cells] in vitro · [animal] rodent model · [abstract] abstract only · no patient data in panel B",
        va="center", fontsize=12, color="#555")
ax.text(0.4, -1.25, "Grey boxes = approved therapies. DCs, dendritic cells; FLS, fibroblast-like synoviocytes; MMPs, matrix metalloproteinases; "
        "PPP, pentose phosphate pathway; FAO/FAS, fatty acid oxidation/synthesis; AIA, adjuvant-induced arthritis.",
        va="center", fontsize=11, color="#555")
ax.set_title("Figure 1 (draft): joint inflammation in RA and the pathways that repurposed drugs target", fontsize=19, weight="bold")

if __name__ == "__main__":
    plt.savefig(OUT + ".png", dpi=600, bbox_inches="tight")
    plt.savefig(OUT + ".pdf", bbox_inches="tight")
    print("saved", OUT + ".png/.pdf")
