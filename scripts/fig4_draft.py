import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out = "08 - RA Repurposing Review/Figure_4_Draft.png"
fig, ax = plt.subplots(figsize=(10, 10)); ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
def box(x, y, w, h, txt, grey=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                 fc="#f3f3f3" if grey else "#eef4fb", ec="#777" if grey else "#1f4e79", lw=1.4))
    ax.text(x + w/2, y + h/2, txt, ha="center", va="center", fontsize=10)
def arrow(x1, y1, x2, y2):
    ax.annotate("", (x2, y2), (x1, y1), arrowprops=dict(arrowstyle="-|>", color="#333", lw=1.3))
for y, lab in [(8.2, "Identification"), (5.4, "Screening"), (1.6, "Included")]:
    ax.text(0.15, y, lab, rotation=90, va="center", fontsize=11, weight="bold", color="#1f4e79")
box(0.7, 7.0, 5.2, 2.4, "Records identified, Europe PMC\n(6 Oct 2026; re-run 11 Oct, same counts)\nn = 628\n\nstatins 384 · metformin 79 · pioglitazone 65\nARBs 40 · fenofibrate 22 · DPP-4i 17\nGLP-1 RA 12 · SGLT2i 9")
box(6.6, 7.6, 3.2, 1.2, "Duplicates removed\n(same record in >1 search)\nn = 24", grey=True); arrow(5.9, 8.2, 6.55, 8.2)
box(1.6, 4.9, 3.4, 1.0, "Records screened\nn = 604"); arrow(3.3, 7.0, 3.3, 5.95)
box(6.6, 4.9, 3.2, 1.0, "Not included\nn = 556", grey=True); arrow(5.0, 5.4, 6.55, 5.4)
box(6.6, 2.6, 3.2, 1.5, "Other sources\nn = 31\n(primary studies outside the\nsearch, reviews, meta-analyses,\nlabels, registries, methods)", grey=True)
box(1.6, 2.8, 3.4, 1.0, "Included from the search\nn = 48"); arrow(3.3, 4.9, 3.3, 3.85)
box(1.6, 0.8, 3.4, 1.0, "References cited in the review\nn = 79"); arrow(3.3, 2.8, 3.3, 1.85)
arrow(8.2, 2.6, 5.05, 1.3)
ax.set_title("Figure 4 (draft): literature search and study selection", fontsize=13, weight="bold")
plt.savefig(out, dpi=200, bbox_inches="tight"); print("saved", out)
