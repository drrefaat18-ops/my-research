"""Tool hook: runs the gate after the AI edits a gated file. TEMPLATE: copy to harness/hook.py.

Reads the hook event JSON on stdin (Claude Code / Gemini CLI / Cursor style — verify field names
against your tool's docs). After an edit to a gated path:
  pass -> exit 0 (counter reset)
  fail -> exit 2, findings on stderr (fed back to the AI to fix line by line)
  fail N times in a row, or identical findings twice -> exit 2 with a STOP message: show findings, wait for the human.
On the user's "done" word in a prompt event: runs the gate on all gated files, prints results (exit 0).
A crash never blocks the session (exit 0 + warning).
Usage: python harness/hook.py < event.json      |   python harness/hook.py --selftest
"""
import fnmatch, json, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GATE = os.path.join(ROOT, "harness", "gate.py")
GATED = ["{{GATED_GLOB}}"]   # TEMPLATE: e.g. ["drafts/*.md", "src/*.py"] relative to ROOT; * also matches subfolders
DONE_WORDS = ["done"]          # TEMPLATE: the user's word(s) for "I finished", in their language
MAX_FAILS = 3                  # TEMPLATE: user's retry cap (PRINCIPLES 6)


def is_gated(path):
    rel = os.path.relpath(os.path.abspath(path), ROOT).replace("\\", "/")
    return not rel.startswith("..") and any(fnmatch.fnmatch(rel, g) for g in GATED)


def gated_files():
    out = []
    for d, _, fs in os.walk(ROOT):
        out += [os.path.join(d, f) for f in fs if is_gated(os.path.join(d, f))]
    return out


def run_gate(files):
    r = subprocess.run([sys.executable, GATE, *files], capture_output=True, text=True, encoding="utf-8")
    return r.returncode, r.stdout


def fail_count(session, path, findings, state_dir=None):
    """Consecutive failures for this file in this session; reset on pass (findings=None).
    Identical findings twice in a row = no progress -> jump past the cap."""
    sid = re.sub(r"\W", "", session or "nosession")
    state = os.path.join(state_dir or tempfile.gettempdir(), f"harness_hook_{sid}.json")
    try:
        data = json.load(open(state, encoding="utf-8"))
    except (OSError, ValueError):
        data = {}
    key = os.path.normcase(os.path.abspath(path))
    prev = data.get(key, {"n": 0, "out": None})
    if findings is None:
        data.pop(key, None)
        n = 0
    else:
        n = MAX_FAILS + 1 if findings == prev["out"] else prev["n"] + 1
        data[key] = {"n": n, "out": findings}
    json.dump(data, open(state, "w", encoding="utf-8"))
    return n


def edited_path(ev):
    ti = ev.get("tool_input") or ev.get("toolInput") or {}
    return ti.get("file_path") or ti.get("path") or ev.get("file_path") or ""


def main():
    ev = json.loads(sys.stdin.buffer.read().decode("utf-8") or "{}")
    prompt = ev.get("prompt") or ""
    if prompt:
        if any(w in prompt for w in DONE_WORDS):
            files = gated_files()
            code, out = run_gate(files) if files else (0, "no gated files")
            print("Gate ran because the user said they are done. Report these findings as a numbered list:\n" + out)
        return 0
    path = edited_path(ev)
    if not path or not is_gated(path):
        return 0
    code, out = run_gate([path])
    n = fail_count(ev.get("session_id", ""), path, out if code else None)
    if code and n > MAX_FAILS:
        sys.stderr.write(f"GATE STOP: {path} failed {n} times in a row or findings did not change. "
                         "Do NOT edit it again. Show the user these findings verbatim, propose a one-line "
                         "fix for each, and wait for their decision:\n" + out)
        return 2
    if code:
        sys.stderr.write("Gate found issues in the file you just edited. Fix them line by line "
                         "(never regenerate the whole section) before saying done:\n" + out)
        return 2
    return 0


def selftest():
    d = tempfile.mkdtemp()
    s, p = "t", os.path.join(d, "x.md")
    assert fail_count(s, p, "a", d) == 1 and fail_count(s, p, "b", d) == 2
    assert fail_count(s, p, "b", d) == MAX_FAILS + 1        # same findings -> stop
    assert fail_count(s, p, None, d) == 0                   # pass resets
    assert [fail_count(s, p, x, d) for x in "cdef"] == [1, 2, 3, 4]
    print("hook selftest ok")
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        sys.exit(selftest())
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        sys.exit(main())
    except Exception as e:  # never block the session on a hook bug; say so instead
        print(f"hook error (gate skipped): {e!r}", file=sys.stderr)
        sys.exit(0)
