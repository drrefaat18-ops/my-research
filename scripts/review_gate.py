"""One command for every deterministic check on review drafts:
style_check (register, AI phrases, hidden-Unicode watermarks, profile) + cite_check + overlap_check,
and with --full also structure_check over all drafts.

Usage (from the review folder):
    PYTHONIOENCODING=utf-8 python ../scripts/review_gate.py drafts/Day2.md
    PYTHONIOENCODING=utf-8 python ../scripts/review_gate.py --full          # all drafts + structure
Exit 1 if anything is flagged. Called automatically by review_hook.py.
"""
import glob, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_check, overlap_check, structure_check, style_check  # noqa: E402


def gate(path):
    """Findings for one draft as printable lines."""
    d = os.path.dirname(os.path.abspath(path))
    papers_dir = os.path.join(d, "..", "papers")
    md = open(path, encoding="utf-8").read()
    out = [f"[style] [{s}] {w} → {x}" for s, w, x in style_check.check(md)]
    drafts = [open(p, encoding="utf-8").read() for p in sorted(glob.glob(os.path.join(d, "*.md")))]
    out += [f"[cite] [{s}] {w} → {x}" for s, w, x in cite_check.check(md, cite_check.papers_in(papers_dir), drafts)]
    sources = {os.path.basename(p)[:-3]: open(p, encoding="utf-8").read()
               for p in glob.glob(os.path.join(papers_dir, "*.md"))}
    pct, rep = overlap_check.check(md, sources)
    out += [f"[overlap {pct:.1f}%] {n} matches ← {src}: {s[:90]}" for n, src, s in rep]
    return out


def main(args):
    full = "--full" in args
    files = [a for a in args if a != "--full"] or sorted(glob.glob("drafts/Day[1-9]*.md"))
    total = 0
    for f in files:
        found = gate(f)
        total += len(found)
        print(f"\n== {f}: {len(found)} issue(s)")
        print("\n".join("  " + x for x in found))
    if full:
        found = structure_check.check([open(p, encoding="utf-8").read() for p in sorted(glob.glob("drafts/Day*.md"))])
        total += len(found)
        print(f"\n== structure: {len(found)} issue(s)")
        print("\n".join(f"  [{a}] {b}" for a, b in found))
    print("\n✅ gate clean" if not total else f"\n⚠️ {total} issue(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
