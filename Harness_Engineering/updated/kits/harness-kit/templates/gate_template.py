"""Quality gate (sensor). TEMPLATE: copy to harness/gate.py and add one check_* per failure mode.

Usage:  python harness/gate.py FILE [FILE ...]     -> numbered findings, exit 0 pass / 1 fail
        python harness/gate.py --selftest
Finding format: file:line: check: message
Stdlib only.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root (harness/..)
SOURCES_MD = os.path.join(ROOT, "sources", "md")

# Links to source anchors: [text](sources/md/name.md#^p3-2)  or  [[name#^p3-2]]
MD_LINK = re.compile(r"\]\(([^)\s]*sources/md/[^)#\s]+)#\^([\w-]+)\)")
WIKI_LINK = re.compile(r"\[\[([^\]|#]+)#\^([\w-]+)(?:\|[^\]]*)?\]\]")
ANCHOR = re.compile(r"\^([\w-]+)\s*$", re.M)


def check_placeholders(path, lines):
    """Leftover placeholders. TEMPLATE: example check — keep, edit, or delete."""
    for i, ln in enumerate(lines, 1):
        if re.search(r"\{\{[A-Z_]+\}\}|\bTODO\b|\bTBD\b", ln):
            yield i, "leftover placeholder"


def _anchors(md_file, cache={}):
    if md_file not in cache:
        try:
            cache[md_file] = set(ANCHOR.findall(open(md_file, encoding="utf-8").read()))
        except OSError:
            cache[md_file] = None
    return cache[md_file]


def check_source_links(path, lines):
    """PRINCIPLES 11 — every source link resolves to an existing file and anchor."""
    here = os.path.dirname(os.path.abspath(path))
    for i, ln in enumerate(lines, 1):
        targets = [(os.path.normpath(os.path.join(here, f)), a) for f, a in MD_LINK.findall(ln)]
        targets += [(os.path.join(SOURCES_MD, n.strip() + ("" if n.endswith(".md") else ".md")), a)
                    for n, a in WIKI_LINK.findall(ln)]
        for f, a in targets:
            got = _anchors(f)
            if got is None:
                yield i, f"broken link: no file {os.path.basename(f)}"
            elif a not in got:
                yield i, f"broken link: no anchor ^{a} in {os.path.basename(f)}"


CLAIM = re.compile(r"\d")  # TEMPLATE: what counts as a factual claim in this work (here: any number)


def check_provenance(path, lines):
    """PRINCIPLES 11 — a paragraph containing a claim must carry a source link or [unverified]."""
    start, para = 1, []
    for i, ln in enumerate(lines + [""], 1):
        if ln.strip():
            if not para:
                start = i
            para.append(ln)
            continue
        text = " ".join(para)
        para = []
        if not text or text.lstrip().startswith(("#", "<!--", "|", "```")):
            continue
        if CLAIM.search(text) and not (MD_LINK.search(text) or WIKI_LINK.search(text)
                                       or "[unverified]" in text):
            yield start, "claim without source link (add link or mark [unverified])"


CHECKS = [check_placeholders, check_source_links, check_provenance]  # TEMPLATE: register new checks here


def run(paths):
    findings = []
    for p in paths:
        try:
            lines = open(p, encoding="utf-8").read().splitlines()
        except OSError as e:
            findings.append(f"{p}:0: io: {e}")
            continue
        for chk in CHECKS:
            for line, msg in chk(p, lines):
                findings.append(f"{p}:{line}: {chk.__name__[6:]}: {msg}")
    return findings


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    findings = run(argv)
    for n, f in enumerate(findings, 1):
        print(f"{n}. {f}")
    print("PASS" if not findings else f"FAIL: {len(findings)} finding(s)")
    return 1 if findings else 0


def selftest():
    import tempfile
    global SOURCES_MD
    d = tempfile.mkdtemp()
    SOURCES_MD = os.path.join(d, "sources", "md")
    os.makedirs(SOURCES_MD)
    open(os.path.join(SOURCES_MD, "s1.md"), "w", encoding="utf-8").write("Rate was 12%. ^p1-1\n")
    good = os.path.join(d, "good.md")
    open(good, "w", encoding="utf-8").write(
        "# Title\n\nRate was 12% [[s1#^p1-1]].\n\nOpinion without numbers.\n\n"
        "Guess of 5 [unverified].\n\nSee [s](sources/md/s1.md#^p1-1) for 12.\n")
    bad = os.path.join(d, "bad.md")
    open(bad, "w", encoding="utf-8").write(
        "Rate was 40%.\n\nX [[s1#^p9-9]] and [[nope#^p1-1]].\n\nTODO finish\n")
    assert run([good]) == [], run([good])
    got = " ".join(run([bad]))
    for want in ("claim without source", "no anchor ^p9-9", "no file", "placeholder"):
        assert want in got, (want, got)
    print("gate selftest ok")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(selftest() if sys.argv[1:] == ["--selftest"] else main(sys.argv[1:]))
