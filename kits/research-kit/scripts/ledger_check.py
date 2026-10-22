"""Evidence-ledger gate for research-kit (templates/ledger.md format).

Usage:  python ledger_check.py LEDGER.md [--report REPORT.md] [--today YYYY-MM-DD]
        python ledger_check.py --selftest
Findings print numbered; [fix] = must change before reporting, [note] = say it in the report. Exit 1 on any [fix].
Checks:
  - a supported claim has evidence rows with a passage and a known source; a snippet or model memory never supports
  - every source has url_or_path and an accessed date; one canonical URL is listed once
  - a claim past its fact_type freshness window must be marked stale (a recheck updates `checked`)
  - a claim whose sources all share one origin is single-sourced (note)
  - a contested claim names at least one source
  - report (optional): every [C<n>] tag exists in the ledger; a tag on a non-supported claim sits on a line that says its status
Stdlib only.
"""
import datetime
import re
import sys
from pathlib import Path

# ---- CONFIG (installer fills from the interview: FRESHNESS_WINDOWS) ----------------------------
FRESHNESS_DAYS = {"live": 30, "volatile": 90, "stable": None}   # fact_type -> days; None = no expiry
# -------------------------------------------------------------------------------------------------
STATUSES = {"supported", "contested", "unverified", "stale", "n/a"}
NO_SUPPORT_KINDS = {"snippet", "memory"}


def tables(text):
    """{heading: [row dict, ...]} for every '## heading' followed by a markdown table."""
    out, head, cols = {}, None, None
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("## "):
            head, cols = s[3:].strip().lower(), None
            out.setdefault(head, [])
        elif head and s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if cols is None:
                cols = [c.lower() for c in cells]
            elif not set("".join(cells)) <= set("-: "):
                out[head].append(dict(zip(cols, cells)))
    return out


def canon(url):
    u = url.strip().lower().split("#")[0]
    u = re.sub(r"[?&](utm_\w+|ref|source)=[^&]*", "", u).rstrip("?&/")
    return re.sub(r"^https?://(www\.)?", "", u)


def date(s):
    try:
        return datetime.date.fromisoformat(s.strip())
    except ValueError:
        return None


def check(ledger_text, report_text=None, today=None):
    today = today or datetime.date.today()
    t = tables(ledger_text)
    sources = {r.get("id", ""): r for r in t.get("sources", [])}
    claims = {r.get("id", ""): r for r in t.get("claims", [])}
    evidence = t.get("evidence", [])
    found = []
    fix = lambda m: found.append(("fix", m))
    note = lambda m: found.append(("note", m))
    for name in ("sources", "claims", "evidence"):
        if name not in t:
            fix(f"missing '## {name.capitalize()}' table")

    seen = {}
    for sid, s in sources.items():
        if not s.get("url_or_path"):
            fix(f"source {sid}: no url_or_path")
        if not date(s.get("accessed", "")):
            fix(f"source {sid}: accessed date missing or not YYYY-MM-DD")
        c = canon(s.get("url_or_path", ""))
        if c and c in seen:
            fix(f"source {sid}: same URL as {seen[c]}; keep one id")
        seen.setdefault(c, sid)

    by_claim = {}
    for e in evidence:
        cid, sid = e.get("claim", ""), e.get("source", "")
        if cid not in claims:
            fix(f"evidence row for unknown claim {cid}")
        if sid not in sources:
            fix(f"claim {cid}: evidence cites unknown source {sid}")
        by_claim.setdefault(cid, []).append(e)

    for cid, c in claims.items():
        st = c.get("status", "").lower()
        rows = by_claim.get(cid, [])
        if st not in STATUSES:
            fix(f"claim {cid}: status '{st}' not one of {', '.join(sorted(STATUSES))}")
        if st == "supported":
            good = [e for e in rows if e.get("passage") and e.get("source") in sources
                    and sources[e["source"]].get("kind", "").lower() not in NO_SUPPORT_KINDS]
            if not good:
                fix(f"claim {cid}: supported without a passage from a real source (snippet/memory do not count)")
            origins = {sources[e["source"]].get("origin", "").lower() for e in good}
            if len(good) > 1 and len(origins) == 1:
                note(f"claim {cid}: {len(good)} sources, one origin ({origins.pop()}): single-sourced")
        if st == "contested" and not rows:
            fix(f"claim {cid}: contested but no source names the disagreement")
        ft = c.get("fact_type", "")
        if ft not in FRESHNESS_DAYS:
            fix(f"claim {cid}: fact_type '{ft}' has no freshness window ({', '.join(FRESHNESS_DAYS)})")
        elif FRESHNESS_DAYS[ft] is not None and st not in ("stale", "n/a"):
            d = date(c.get("checked", ""))
            if not d:
                fix(f"claim {cid}: checked date missing")
            elif (today - d).days > FRESHNESS_DAYS[ft]:
                fix(f"claim {cid}: checked {d}, past the {FRESHNESS_DAYS[ft]}-day window for '{ft}': recheck or mark stale")

    if report_text is not None:
        for n, line in enumerate(report_text.splitlines(), 1):
            for cid in re.findall(r"\[(C\d+)\]", line):
                if cid not in claims:
                    fix(f"report line {n}: [{cid}] is not in the ledger")
                    continue
                st = claims[cid].get("status", "").lower()
                if st != "supported" and st not in line.lower():
                    fix(f"report line {n}: [{cid}] is {st} but the line does not say so")
    return found


def selftest():
    good = """## Sources
| id | url_or_path | publisher | kind | origin | published | accessed |
|---|---|---|---|---|---|---|
| S1 | https://a.org/r | A | primary | A | 2026-01-01 | 2026-01-02 |
| S2 | https://b.org/x | B | independent | A | 2026-01-03 | 2026-01-04 |
## Claims
| id | claim | status | fact_type | checked | note |
|---|---|---|---|---|---|
| C1 | X scored 82 | supported | stable | 2026-01-04 | |
| C2 | X costs 5 | unverified | live | 2026-01-04 | |
## Evidence
| claim | source | passage | not_established |
|---|---|---|---|
| C1 | S1 | "X scored 82" | |
| C1 | S2 | "X got 82" | |
"""
    bad = good.replace("| S2 | https://b.org/x", "| S2 | https://www.A.org/r/?utm_source=z") \
              .replace("| C2 | X costs 5 | unverified | live | 2026-01-04 |", "| C2 | X costs 5 | supported | live | 2025-01-01 |") \
              + "| C2 | S9 | \"5\" | |\n"
    today = datetime.date(2026, 1, 20)
    g = check(good, "X scored 82 [C1]. Price unverified [C2].", today)
    b = check(bad, "X costs 5 [C2]. See [C7].", today)
    msgs = " ".join(m for _, m in b)
    checks = {
        "clean ledger: only the single-origin note": [lvl for lvl, _ in g] == ["note"] and "one origin" in g[0][1],
        "duplicate canonical URL": "same URL as S1" in msgs,
        "supported without real source": "C2: supported without" in msgs,
        "unknown source": "unknown source S9" in msgs,
        "freshness window": "past the 30-day window" in msgs,
        "report unknown tag": "[C7] is not in the ledger" in msgs,
    }
    b2 = check(good, "X costs 5 [C2].", today)
    checks["report must label non-supported"] = any("[C2] is unverified" in m for _, m in b2)
    for k, ok in checks.items():
        print(("PASS " if ok else "FAIL ") + k)
    return 0 if all(checks.values()) else 1


def main(argv):
    if argv == ["--selftest"]:
        return selftest()
    if not argv or argv[0].startswith("-"):
        print(__doc__)
        return 2
    opt = lambda k: argv[argv.index(k) + 1] if k in argv else None
    report = Path(opt("--report")).read_text(encoding="utf-8") if opt("--report") else None
    today = date(opt("--today")) if opt("--today") else None
    found = check(Path(argv[0]).read_text(encoding="utf-8"), report, today)
    for i, (lvl, m) in enumerate(found, 1):
        print(f"{i}. ledger: [{lvl}] {m}")
    print(f"{len(found)} findings")
    return 1 if any(lvl == "fix" for lvl, _ in found) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
