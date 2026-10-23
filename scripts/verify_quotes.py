"""Verify evidence-card quotes verbatim against source files (agent pipeline, phase 3).

Cards file: one card per line, `Tag | line | exact quote` (lines starting with # are skipped).
Each quote must appear in <sources_dir>/<Tag>.md on that line (whitespace, hyphen and
apostrophe variants normalised; ==highlight== marks and ^block-ids ignored, so isolate_blocks.py
does not break old cards). OK = on the stated line, MOVED = elsewhere in the file, or split over
lines by isolate_blocks.py (fix the line number: --fix rewrites them), FAIL = not in the file
(drop the card). Exit 1 if any FAIL.

The cards file must carry a `# source: <evidence workflow run | Haiku agent id>` line: evidence
comes from Haiku agents, never gathered inline by the orchestrator (confirmed lesson).

Usage:
    python scripts/verify_quotes.py cards.txt "08 - RA Repurposing Review/papers"
    python scripts/verify_quotes.py cards.txt "08 - RA Repurposing Review/papers" --fix   # renumber MOVED
    python scripts/verify_quotes.py --demo
"""
import os, re, sys, tempfile

DASHES = str.maketrans({"‐": "-", "‑": "-", "’": "'", "‘": "'", "“": '"', "”": '"'})


SOURCE = re.compile(r"^#\s*source:\s*\S", re.I | re.M)


def norm(s):
    return re.sub(r"\s+", " ", s.translate(DASHES)).strip()


def norm_src(s):
    """A paper line without Obsidian highlight marks and trailing block id."""
    return norm(re.sub(r"\s\^[\w-]+\s*$", "", s).replace("==", ""))


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
        lines = [norm_src(l) for l in open(path, encoding="utf-8").read().splitlines()]
        q = norm(quote.strip('"')).replace("==", "")
        if 0 < line <= len(lines) and q in lines[line - 1]:
            out.append(("OK", tag, line, quote))
            continue
        hit = next((i + 1 for i, l in enumerate(lines) if q in l), None) or split_hit(lines, q)
        out.append(("FAIL", tag, line, quote) if not hit else ("OK" if hit == line else "MOVED", tag, hit, quote))
    return out


def split_hit(lines, q):
    """First line of a quote that isolate_blocks.py split over several blocks, else None."""
    starts, text = [], ""
    for i, l in enumerate(lines):
        if l:
            starts.append((len(text), i + 1))
            text += l + " "
    at = text.find(q)
    return None if at < 0 else max(n for pos, n in starts if pos <= at)


def fix(cards, res):
    """cards lines with each MOVED card's line number replaced by where the quote is now."""
    moved = iter(res)  # one result per card line, in order
    out = []
    for raw in cards:
        if not raw.strip() or raw.lstrip().startswith("#"):
            out.append(raw)
            continue
        status, tag, line, quote = next(moved)
        out.append(f"{tag} | {line} | {quote}" if status == "MOVED" else raw)
    return out


def demo():
    d = tempfile.mkdtemp()
    open(os.path.join(d, "Smith2020.md"), "w", encoding="utf-8").write("title\nDAS28 fell by 9.3% (P = 0.046).\n")
    cards = ["# comment", "Smith2020 | 2 | DAS28 fell by 9.3%", "Smith2020 | 1 | fell by 9.3%",
             "Smith2020 | 2 | fell by 12%", "Jones2021 | 1 | x", "garbage"]
    r = check(cards, d)
    assert [x[0] for x in r] == ["OK", "MOVED", "FAIL", "UNREADABLE", "BAD"], r
    assert r[1][2] == 2
    assert fix(cards, r)[2] == "Smith2020 | 2 | fell by 9.3%", fix(cards, r)
    # isolate_blocks.py split 'ESR fell. ==CRP fell by 20%.== Both held.' into blocks with ids
    open(os.path.join(d, "Lee2019.md"), "w", encoding="utf-8").write(
        "title\nESR fell.\n\n==CRP fell by 20%.== ^lee2019-1\n\nBoth held.\n")
    r = check(["Lee2019 | 2 | CRP fell by 20%", "Lee2019 | 2 | ESR fell. CRP fell by 20%. Both", "Lee2019 | 4 | CRP fell by 20%"], d)
    assert [(x[0], x[2]) for x in r] == [("MOVED", 4), ("OK", 2), ("OK", 4)], r
    assert not SOURCE.search("Smith2020 | 2 | x") and SOURCE.search("# source: evidence workflow wf_abc\nx")
    print("demo ok")


def main():
    if "--demo" in sys.argv:
        return demo()
    args = [a for a in sys.argv[1:] if a != "--fix"]
    if len(args) != 2:
        sys.exit(__doc__)
    text = open(args[0], encoding="utf-8").read()
    res = check(text.splitlines(), args[1])
    if not SOURCE.search(text):
        res.insert(0, ("BAD", "source", 0, "no '# source: <evidence workflow run | Haiku agent id>' line; "
                                           "cards must come from Haiku agents, not inline"))
    if "--fix" in sys.argv and any(r[0] == "MOVED" for r in res):
        open(args[0], "w", encoding="utf-8").write("\n".join(fix(text.splitlines(), [r for r in res if r[1] != "source"])) + "\n")
        print(f"--fix: {sum(r[0] == 'MOVED' for r in res)} line number(s) rewritten in {args[0]}")
    for status, tag, line, quote in res:
        print(f"{status:10} {tag} L{line}  {quote[:70]}")
    bad = sum(r[0] != "OK" for r in res)
    print(f"\n{len(res) - bad}/{len(res)} OK" + (f"; {bad} need action" if bad else ""))
    sys.exit(1 if any(r[0] in ("FAIL", "UNREADABLE", "BAD") for r in res) else 0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
