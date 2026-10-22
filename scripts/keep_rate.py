"""Keep rate per loop (LOOPS 12): kept outputs / runs, from log lines `loop | <name> | kept|discarded [| note]`.

Usage: python keep_rate.py <log dir or .md files> [--min 0.5] [--min-runs 4]
       python keep_rate.py --selftest
Exit 1 if a loop with at least --min-runs runs is below --min.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

LINE = re.compile(r"^\s*[-*]?\s*loop\s*\|\s*([^|]+?)\s*\|\s*(kept|discarded)\b", re.I | re.M)


def count(texts):
    runs = defaultdict(lambda: [0, 0])  # name -> [kept, total]
    for text in texts:
        for name, verdict in LINE.findall(text):
            runs[name][1] += 1
            runs[name][0] += verdict.lower() == "kept"
    return runs


def report(runs, min_rate, min_runs):
    low = []
    for name, (kept, total) in sorted(runs.items()):
        rate = kept / total
        flag = total >= min_runs and rate < min_rate
        low += [name] * flag
        print(f"{'LOW ' if flag else 'ok  '}{name}: {kept}/{total} kept ({rate:.0%})")
    if not runs:
        print("no `loop |` lines found")
    return low


def selftest():
    sample = "\n".join(["loop | widget-scan | kept", "- loop | widget-scan | discarded | weak check",
                        "loop | widget-scan | discarded", "loop | widget-scan | discarded",
                        "loop | item_x | kept", "lesson | none"])
    runs = count([sample])
    assert runs["widget-scan"] == [1, 4], runs
    assert runs["item_x"] == [1, 1], runs
    assert report(runs, 0.5, 4) == ["widget-scan"]  # item_x has too few runs to judge
    assert report(count([""]), 0.5, 4) == []
    print("selftest PASS")


def main(argv):
    if "--selftest" in argv:
        return selftest()
    opts = {"--min": 0.5, "--min-runs": 4}
    paths = []
    it = iter(argv)
    for a in it:
        if a in opts:
            opts[a] = float(next(it))
        else:
            paths.append(Path(a))
    files = [f for p in paths for f in (sorted(p.glob("*.md")) if p.is_dir() else [p])]
    texts = [f.read_text(encoding="utf-8", errors="replace") for f in files]
    return 1 if report(count(texts), opts["--min"], opts["--min-runs"]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
