"""Source ingestion. TEMPLATE: copy to harness/ingest.py; keep converters for the user's formats only.

sources/raw/<file>  (originals, never edited)  ->  sources/md/<file>.md  (anchored copy)
Each output starts with a header (source, type, sha256, ingested date) and every paragraph/row ends
with an anchor  ^p<page>-<n>  (page 0 when the format has no pages), so claims can link to
[[<file>#^p3-2]]. Unchanged files (same sha256) are skipped. Failures and suspiciously short
outputs are reported, never skipped silently; exit 1 if any.

Usage:  python harness/ingest.py [--force]      |   python harness/ingest.py --selftest
Stdlib formats: txt md html htm csv tsv xml json. Others need an approved install:
  BROAD = markitdown (all formats)  or  per-format: pymupdf (pdf), python-docx (docx), openpyxl (xlsx)
"""
import csv, datetime, hashlib, html.parser, json, os, re, sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "sources", "raw")
OUT = os.path.join(ROOT, "sources", "md")
BROAD = False        # TEMPLATE: True if the user chose markitdown
MIN_CHARS = 200      # TEMPLATE: below this, the conversion is reported as suspicious


# Each converter returns a list of pages; each page is a list of paragraph strings.
def _paras(text):
    return [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def conv_text(path):
    return [_paras(open(path, encoding="utf-8", errors="replace").read())]


class _HTML(html.parser.HTMLParser):
    BLOCK = {"p", "div", "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "br", "section", "article"}

    def __init__(self):
        super().__init__()
        self.buf, self.skip = [], 0

    def handle_starttag(self, tag, a):
        self.skip += tag in ("script", "style")
        if tag in self.BLOCK:
            self.buf.append("\n\n")

    def handle_endtag(self, tag):
        self.skip -= tag in ("script", "style")

    def handle_data(self, d):
        if not self.skip:
            self.buf.append(d)


def conv_html(path):
    p = _HTML()
    p.feed(open(path, encoding="utf-8", errors="replace").read())
    return [_paras("".join(p.buf))]


def conv_csv(path):
    delim = "\t" if path.endswith(".tsv") else ","
    rows = list(csv.reader(open(path, encoding="utf-8", errors="replace", newline=""), delimiter=delim))
    if not rows:
        return [[]]
    head = rows[0]
    return [[" | ".join(f"{h}: {v}" for h, v in zip(head, r)) for r in rows[1:] if any(r)]]


def conv_xml(path):
    root = ET.parse(path).getroot()
    return [[t for t in (" ".join(e.itertext()).strip() for e in root.iter()
                         if len(e) == 0 and (e.text or "").strip()) if t]]


def conv_json(path):
    def walk(o, k=""):
        if isinstance(o, dict):
            for kk, v in o.items():
                yield from walk(v, f"{k}.{kk}" if k else kk)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                yield from walk(v, f"{k}[{i}]")
        else:
            yield f"{k}: {o}"
    return [list(walk(json.load(open(path, encoding="utf-8"))))]


def conv_pdf(path):  # needs: pymupdf (approved install)
    import fitz
    return [_paras(page.get_text()) for page in fitz.open(path)]


def conv_docx(path):  # needs: python-docx
    import docx
    return [[p.text.strip() for p in docx.Document(path).paragraphs if p.text.strip()]]


def conv_xlsx(path):  # needs: openpyxl; one "page" per sheet
    import openpyxl
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    return [[" | ".join("" if c is None else str(c) for c in row) for row in ws.iter_rows(values_only=True)
             if any(c is not None for c in row)] for ws in wb.worksheets]


def conv_broad(path):  # needs: markitdown
    from markitdown import MarkItDown
    return [_paras(MarkItDown().convert(path).text_content)]


CONVERTERS = {".txt": conv_text, ".md": conv_text, ".html": conv_html, ".htm": conv_html,
              ".csv": conv_csv, ".tsv": conv_csv, ".xml": conv_xml, ".json": conv_json,
              ".pdf": conv_pdf, ".docx": conv_docx, ".xlsx": conv_xlsx}
STDLIB = {".txt", ".md", ".html", ".htm", ".csv", ".tsv", ".xml", ".json"}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def render(name, ext, digest, pages):
    paged = len(pages) > 1
    out = ["---", f"source: sources/raw/{name}", f"type: {ext.lstrip('.')}", f"sha256: {digest}",
           f"ingested: {datetime.date.today().isoformat()}", "---", ""]
    for pi, paras in enumerate(pages, 1):
        if paged:
            out += [f"## Page {pi}", ""]
        for n, para in enumerate(paras, 1):
            out += [f"{para} ^p{pi if paged else 0}-{n}", ""]
    return "\n".join(out)


def ingest_one(src, force=False):
    """Returns (status, message). status: ok | skip | fail | short."""
    name = os.path.relpath(src, RAW).replace("\\", "/")
    ext = os.path.splitext(src)[1].lower()
    dst = os.path.join(OUT, name + ".md")
    digest = sha256(src)
    if not force and os.path.exists(dst) and f"sha256: {digest}" in open(dst, encoding="utf-8").read(400):
        return "skip", name
    conv = conv_broad if BROAD and ext not in STDLIB else CONVERTERS.get(ext)
    if conv is None:
        return "fail", f"{name}: no converter for {ext}"
    try:
        pages = conv(src)
    except ImportError as e:
        return "fail", f"{name}: missing library ({e.name}) — ask the user before installing"
    except Exception as e:
        return "fail", f"{name}: {e!r}"
    text = render(name, ext, digest, pages)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "w", encoding="utf-8").write(text)
    body = sum(len(p) for page in pages for p in page)
    if body < MIN_CHARS:
        return "short", f"{name}: only {body} chars extracted — check for scans/images or truncation"
    return "ok", name


def main(force=False):
    srcs = [os.path.join(d, f) for d, _, fs in os.walk(RAW) for f in fs] if os.path.isdir(RAW) else []
    bad = 0
    for s in sorted(srcs):
        status, msg = ingest_one(s, force)
        bad += status in ("fail", "short")
        print(f"{status.upper():5} {msg}")
    print(f"{len(srcs)} source(s), {bad} problem(s)")
    return 1 if bad else 0


def selftest():
    import tempfile
    global RAW, OUT, MIN_CHARS
    d = tempfile.mkdtemp()
    RAW, OUT, MIN_CHARS = os.path.join(d, "raw"), os.path.join(d, "md"), 10
    os.makedirs(RAW)
    samples = {"a.txt": "First para has 12 units.\n\nSecond para.",
               "b.csv": "drug,dose\nX,10 mg\nY,20 mg\n",
               "c.html": "<html><script>x=1</script><p>Hello world here</p><p>Rate 5%</p></html>",
               "d.json": '{"k": {"v": [1, 2]}}', "e.xyz": "?", "f.txt": "tiny"}
    for n, t in samples.items():
        open(os.path.join(RAW, n), "w", encoding="utf-8").write(t)
    got = {os.path.basename(s): ingest_one(os.path.join(RAW, s))[0] for s in samples}
    assert got == {"a.txt": "ok", "b.csv": "ok", "c.html": "ok", "d.json": "ok",
                   "e.xyz": "fail", "f.txt": "short"}, got
    a = open(os.path.join(OUT, "a.txt.md"), encoding="utf-8").read()
    assert "sha256:" in a and "First para has 12 units. ^p0-1" in a and "Second para. ^p0-2" in a, a
    assert "drug: Y | dose: 20 mg ^p0-2" in open(os.path.join(OUT, "b.csv.md"), encoding="utf-8").read()
    c = open(os.path.join(OUT, "c.html.md"), encoding="utf-8").read()
    assert "x=1" not in c and "Rate 5% ^p0-2" in c, c
    assert ingest_one(os.path.join(RAW, "a.txt"))[0] == "skip"
    print("ingest selftest ok")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    a = sys.argv[1:]
    sys.exit(selftest() if a == ["--selftest"] else main(force="--force" in a))
