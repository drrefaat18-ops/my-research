"""Figure 2 draft: repurposed drugs on shared RA pathways.
Every label must match a card in .claude/state/step11/fig2_cards.txt (verify_quotes.py).
Usage: python scripts/fig2_draft.py  -> 08 - RA Repurposing Review/Figure_2_Draft.png + .pdf
"""
import matplotlib.pyplot as plt

OUT = "08 - RA Repurposing Review/Figure_2_Draft"
DRUGS = {"Metformin": (13.6, "#1f77b4"), "Pioglitazone": (10.2, "#2ca02c"), "Fenofibrate": (7.0, "#9467bd"),
         "Losartan": (4.0, "#d62728"), "Simvastatin": (1.2, "#ff7f0e")}
TARGETS = {"AMPK": 14.2, "mTOR": 12.8, "STAT3": 11.3, "Th17 / Treg": 9.8, "TNF-α / IL-1β / IL-6": 8.2,
           "Osteoclasts / bone erosion": 6.6, "Cartilage": 5.2, "PPAR-γ": 3.9, "Th1 / IFN-γ": 2.6,
           "Ang II / AT1R / AT2R": 1.2}
# (drug, target, label, offset within target box, kind) kind: "effect" or "none" (tested, no effect)
ARROWS = [
    ("Metformin", "AMPK", "pAMPK ↑ mouse T cells (Son2014); AMPK-α1 ↑ RA-FLS (Chen2020)", 0, "effect"),
    ("Metformin", "mTOR", "pmTOR ↓ osteoclast cultures (Son2014); RAPTOR protein ↓ RA-FLS (Chen2020)", 0, "effect"),
    ("Metformin", "STAT3", "CD4+ pSTAT3+ cells ↓ CIA mice (Son2014)", 0.25, "effect"),
    ("Fenofibrate", "STAT3", "pSTAT3 ↓ at 20 µM, mouse T cells (Zhou2012)", -0.25, "effect"),
    ("Metformin", "Th17 / Treg", "Th17 ↓, Treg ↑ CIA mice (Son2014)", 0.25, "effect"),
    ("Fenofibrate", "Th17 / Treg", "IL-17+ cells, IL-21 ↓ mouse T cells in vitro (Zhou2012)", -0.25, "effect"),
    ("Metformin", "TNF-α / IL-1β / IL-6", "IL-6, TNF-α, IL-1β ↓ RA-FLS (Chen2020)", 0.4, "effect"),
    ("Pioglitazone", "TNF-α / IL-1β / IL-6", "IL-1β 63%, TNF-α 77% ↓ at 30 mg/kg; tissue unclear (Koufany2008)", 0, "effect"),
    ("Simvastatin", "TNF-α / IL-1β / IL-6", "TNF-α release ↓, reversed by mevalonate; RA patient cells (Leung2003)", -0.4, "effect"),
    ("Metformin", "Osteoclasts / bone erosion", "TRAP, cathepsin K, MMP-9 mRNA ↓ osteoclast cultures (Son2014)", 0.25, "effect"),
    ("Pioglitazone", "Osteoclasts / bone erosion", "bone erosions ↓ AIA rats (Koufany2008)", -0.25, "effect"),
    ("Pioglitazone", "Cartilage", "tested: cartilage NOT protected (Koufany2008)", 0, "none"),
    ("Pioglitazone", "PPAR-γ", "PPAR-γ target genes ↑ AIA rats (Koufany2008)", 0, "effect"),
    ("Simvastatin", "Th1 / IFN-γ", "CIA ↓; IL-12, IFN-γ ↓ (Leung2003)", 0, "effect"),
    ("Losartan", "Ang II / AT1R / AT2R", "serum Ang II ↓; AT1R ↓, AT2R ↑ in spleen and synovium, AIA rats (Wang2013)", 0, "effect"),
]
X0, X1 = 3.0, 15.6  # arrow start (drug edge) / end (target edge)

fig, ax = plt.subplots(figsize=(20, 15.5))
ax.set_xlim(0, 20); ax.set_ylim(-1.2, 15.2); ax.axis("off")
for name, (y, c) in DRUGS.items():
    ax.text(1.6, y, name, ha="center", va="center", fontsize=15, weight="bold", color="white",
            bbox=dict(boxstyle="round,pad=0.4", fc=c, ec=c))
for name, y in TARGETS.items():
    ax.text(15.75, y, name, ha="left", va="center", fontsize=14,
            bbox=dict(boxstyle="round,pad=0.35", fc="#f2f2f2", ec="#333"))
for drug, tgt, label, off, kind in ARROWS:
    y0, c = DRUGS[drug]
    y1 = TARGETS[tgt] + off
    if kind == "effect":
        ax.annotate("", (X1, y1), (X0, y0), arrowprops=dict(arrowstyle="-|>", color=c, lw=2, mutation_scale=18))
    else:  # tested, no effect: dotted grey line ending in a cross, no arrowhead
        ax.plot([X0, X1 - 0.15], [y0, y1], ls=":", lw=2.2, color="#888")
        ax.text(X1 - 0.05, y1, "✕", ha="center", va="center", fontsize=16, color="#888", weight="bold")
    ax.text(X1 - 0.45, y1 + 0.07, label, ha="right", va="bottom", fontsize=10.5, color=c if kind == "effect" else "#666",
            bbox=dict(boxstyle="square,pad=0.1", fc="white", ec="none", alpha=0.85))

ax.set_title("Figure 2 (draft): repurposed drugs on shared RA pathways", fontsize=18, weight="bold")
ax.plot([4.2, 5.0], [-0.3, -0.3], color="#333", lw=2)
ax.text(5.15, -0.3, "solid arrow = effect shown in the paper (abstract / results / figure legend)", va="center", fontsize=12)
ax.plot([4.2, 4.85], [-0.8, -0.8], ls=":", color="#888", lw=2.2)
ax.text(4.95, -0.8, "✕", va="center", ha="center", fontsize=14, color="#888", weight="bold")
ax.text(5.15, -0.8, "dotted line ending in ✕ = tested, no effect", va="center", fontsize=12)
ax.text(13.9, -0.55, "No PPAR-α arrow: the authors say fenofibrate's Th17 effect\n\"might be\" PPAR-α independent (Zhou2012).",
        va="center", fontsize=11, color="#555")

if __name__ == "__main__":
    plt.savefig(OUT + ".png", dpi=145, bbox_inches="tight")
    plt.savefig(OUT + ".pdf", bbox_inches="tight")
    print("saved", OUT + ".png/.pdf")
