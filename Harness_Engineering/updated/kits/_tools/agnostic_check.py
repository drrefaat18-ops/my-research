"""Leak check for an agnostic kit: finds traces of the project the kit was extracted from.

Flags, per file and line:
  term    a word from agnostic-terms.txt (next to this script) or from --terms FILE (one per line, # comments)
  path    an absolute machine path (C:\\..., /home/..., /Users/...)
  email   an e-mail address
  script  a non-Latin letter (kits are written in English; a quoted name or rule from the source leaked)
Usage:  python agnostic_check.py KIT_DIR [--terms FILE]   -> findings, exit 0 clean / 1 leaks
        python agnostic_check.py --selftest
Stdlib only.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEXT = {".md", ".py", ".js", ".json", ".txt", ".yaml", ".yml", ".toml", ".html", ".csv", ".sh", ".ps1"}
PATTERNS = {
    "path": re.compile(r"\b[A-Za-z]:[\\/][\w ]|/(?:home|Users)/\w"),
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"),
    "script": re.compile(r"[^\x00-\u024F\u2000-\u2BFF\uFE00-\uFE0F\U0001F000-\U0001FFFF]"),  # ponytail: Latin + punctuation/symbols/emoji allowed
}


def load_terms(*files):
    terms = []
    for f in files:
        if f and Path(f).is_file():
            terms += [t.strip() for t in Path(f).read_text(encoding="utf-8").splitlines()
                      if t.strip() and not t.lstrip().startswith("#")]
    return terms


def check(kit, terms):
    term_re = re.compile("|".join(re.escape(t) for t in terms), re.I) if terms else None
    found = []
    for p in sorted(Path(kit).rglob("*")):
        if not p.is_file() or p.suffix.lower() not in TEXT:
            continue
        for n, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            hits = [("term", term_re.search(line))] if term_re else []
            hits += [(k, rx.search(line)) for k, rx in PATTERNS.items()]
            for kind, m in hits:
                if m:
                    found.append(f"{p.relative_to(kit).as_posix()}:{n}: [{kind}] {m.group(0)!r} in: {line.strip()[:100]}")
    return found


def selftest():
    import tempfile
    with tempfile.TemporaryDirectory() as t:
        k = Path(t)
        (k / "README.md").write_text("Generic kit. Fill {{PROJECT_NAME}}.\n", encoding="utf-8")
        (k / "bad.md").write_text("Built for Acme Corp.\nSee D:\\work\\x.\nMail a@b.com\nقاعدة\n", encoding="utf-8")
        out = check(k, ["acme corp"])
        kinds = sorted(re.search(r"\[(\w+)\]", f).group(1) for f in out)
        ok = kinds == ["email", "path", "script", "term"] and all(f.startswith("bad.md") for f in out)
    print("agnostic_check selftest " + ("ok" if ok else f"FAIL {out}"))
    return 0 if ok else 1


def main(argv):
    if argv == ["--selftest"]:
        return selftest()
    if not argv or argv[0].startswith("-"):
        print(__doc__)
        return 2
    extra = argv[argv.index("--terms") + 1] if "--terms" in argv else None
    found = check(Path(argv[0]), load_terms(HERE / "agnostic-terms.txt", extra))
    for i, f in enumerate(found, 1):
        print(f"{i}. {f}")
    print(f"{len(found)} leaks in {argv[0]}")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
