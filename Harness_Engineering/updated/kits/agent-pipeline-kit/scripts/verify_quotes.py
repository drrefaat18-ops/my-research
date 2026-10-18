"""Verify evidence-card quotes verbatim against source files (agent pipeline, phase 3).

Cards file: one card per line, `Tag | line | exact quote` (lines starting with # are skipped).
Each quote must appear in <sources_dir>/<Tag>.md on that line (whitespace, hyphen and
apostrophe variants normalised). OK = on the stated line, MOVED = elsewhere in the file
(fix the line number), FAIL = not in the file (drop the card). Exit 1 if any FAIL.

Usage:
    python scripts/verify_quotes.py cards.txt "08 - RA Repurposing Review/papers"
    python scripts/verify_quotes.py --demo
"""
import os, re, sys, tempfile

DASHES = str.maketrans({"‐": "-", "‑": "-", "’": "'", "‘": "'", "“": '"', "”": '"'})


def norm(s):
    return re.sub(r"\s+", " ", s.translate(DASHES)).strip()


def check(cards, src_dir):
    out = []
    for raw in cards:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        try:
            tag, line, quote = (p.strip() for p in raw.split("|", 2))
            line = int(line)
        except ValueError:
            out.append(("BAD", raw.strip()[:60], 0, "expected: Tag | line | quote"))
            continue
        path = os.path.join(src_dir, tag + ".md")
        if not os.path.exists(path):
            out.append(("UNREADABLE", tag, line, quote))
            continue
        lines = open(path, encoding="utf-8").read().splitlines()
        q = norm(quote.strip('"'))
        if 0 < line <= len(lines) and q in norm(lines[line - 1]):
            out.append(("OK", tag, line, quote))
        else:
            hit = next((i + 1 for i, l in enumerate(lines) if q in norm(l)), None)
            out.append(("MOVED", tag, hit, quote) if hit else ("FAIL", tag, line, quote))
    return out


def demo():
    d = tempfile.mkdtemp()
    open(os.path.join(d, "Smith2020.md"), "w", encoding="utf-8").write("title\nDAS28 fell by 9.3% (P = 0.046).\n")
    r = check(["# comment", "Smith2020 | 2 | DAS28 fell by 9.3%", "Smith2020 | 1 | fell by 9.3%",
               "Smith2020 | 2 | fell by 12%", "Jones2021 | 1 | x", "garbage"], d)
    assert [x[0] for x in r] == ["OK", "MOVED", "FAIL", "UNREADABLE", "BAD"], r
    assert r[1][2] == 2
    print("demo ok")


def main():
    if "--demo" in sys.argv:
        return demo()
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    res = check(open(sys.argv[1], encoding="utf-8").read().splitlines(), sys.argv[2])
    for status, tag, line, quote in res:
        print(f"{status:10} {tag} L{line}  {quote[:70]}")
    bad = sum(r[0] != "OK" for r in res)
    print(f"\n{len(res) - bad}/{len(res)} OK" + (f"; {bad} need action" if bad else ""))
    sys.exit(1 if any(r[0] in ("FAIL", "UNREADABLE", "BAD") for r in res) else 0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
