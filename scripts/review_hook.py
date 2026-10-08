"""Claude Code hook for the RA review (registered in .claude/settings.json).

PostToolUse (Write/Edit/MultiEdit): when Claude edits 08 - RA Repurposing Review/drafts/*.md,
  strip hidden-Unicode watermark chars, run review_gate on that file, and on findings exit 2 so
  the findings go back to Claude, which must fix them before reporting done.
UserPromptSubmit: when the user's message contains "خلصت", run review_gate on every draft changed
  since the last commit and add the result to Claude's context (exit 0, stdout).
Any other event/path: exit 0 silently. A crash never blocks the session (exit 0).
"""
import contextlib, io, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.join(HERE, "..", "08 - RA Repurposing Review")
sys.path.insert(0, HERE)


def run_gate(files):
    import review_gate, style_check
    for f in files:  # watermark strip first, so findings are about the cleaned text
        md = open(f, encoding="utf-8", newline="").read()
        new = style_check.strip_hidden(md)
        if new != md:
            open(f, "w", encoding="utf-8", newline="").write(new)
    buf = io.StringIO()
    cwd = os.getcwd()
    os.chdir(REVIEW)
    try:
        with contextlib.redirect_stdout(buf):
            code = review_gate.main([os.path.relpath(f, REVIEW) for f in files])
    finally:
        os.chdir(cwd)
    return code, buf.getvalue()


def changed_drafts():
    out = subprocess.run(["git", "status", "--porcelain", "--", "drafts"], cwd=REVIEW,
                         capture_output=True, text=True, encoding="utf-8").stdout
    paths = [re.sub(r'^"|"$', "", ln[3:].strip()) for ln in out.splitlines()]
    root = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=REVIEW,
                          capture_output=True, text=True).stdout.strip()
    return [os.path.join(root, p) for p in paths if re.search(r"drafts/Day[1-9].*\.md$", p)]


MAX_FAILS = 3  # initial edit + 2 fix attempts; then escalate to the user instead of looping


def fail_count(session, path, findings):
    """Consecutive gate failures for this draft in this session; reset on pass.
    Identical findings twice in a row = no progress, jump straight past the cap."""
    import tempfile
    sid = re.sub(r"\W", "", session)
    state = os.path.join(tempfile.gettempdir(), f"review_hook_{sid}.json")
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


def is_draft(path):
    p = path.replace("\\", "/")
    return "RA Repurposing Review/drafts/" in p and re.search(r"/Day[1-9][^/]*\.md$", p)


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # Windows console is cp1252; findings carry ✅/α/µ
    sys.stderr.reconfigure(encoding="utf-8")
    ev = json.loads(sys.stdin.buffer.read().decode("utf-8"))
    name = ev.get("hook_event_name")
    if name == "PostToolUse":
        path = (ev.get("tool_input") or {}).get("file_path", "")
        if not is_draft(path):
            return 0
        code, out = run_gate([path])
        fails = fail_count(ev.get("session_id", ""), path, out if code else None)
        if code and fails > MAX_FAILS:
            sys.stderr.write(f"review_gate STOP: this draft failed {fails} times in a row (or the same "
                             "findings came back). Do NOT edit it again. Show the user these findings "
                             "verbatim, propose the fix in one line each, and wait for their decision:\n" + out)
            return 2
        if code:
            sys.stderr.write("review_gate found issues in the draft you just edited. Fix them "
                             "sentence by sentence (never regenerate a paragraph) before saying done:\n" + out)
            return 2
        return 0
    if name == "UserPromptSubmit" and "خلصت" in ev.get("prompt", ""):
        files = changed_drafts()
        if not files:
            print("review_gate: no changed drafts since the last commit.")
            return 0
        code, out = run_gate(files)
        print("review_gate ran automatically on the drafts the user changed. Report these "
              "results to the user as the numbered error list (workflow step C):\n" + out)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # ponytail: never block the session on a hook bug; say so instead
        print(f"review_hook error (gate skipped): {e!r}", file=sys.stderr)
        sys.exit(0)
