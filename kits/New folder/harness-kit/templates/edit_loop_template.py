"""Edit-loop warning (PRINCIPLES 20): counts edits per file per session after each edit tool call; at
{{EDIT_LOOP_LIMIT}} edits (and every {{EDIT_LOOP_LIMIT}} more) it tells the AI to stop and re-plan. Warns only, never blocks.
TEMPLATE: save as harness/edit_loop.py; wire it to the tool's after-edit event (templates/hooks/<tool>).
The JSON reply below is Claude Code's PostToolUse "additionalContext"; other tools: print the message instead.
Usage: python harness/edit_loop.py < event.json   |   python harness/edit_loop.py --selftest
"""
import json, os, re, sys, tempfile

LIMIT = 5                                     # TEMPLATE: set to {{EDIT_LOOP_LIMIT}} (Phase 3 answer)


def bump(session, path, state_dir=None):
    """Edits to this file in this session, including this one."""
    sid = re.sub(r"\W", "", session or "nosession")
    state = os.path.join(state_dir or tempfile.gettempdir(), f"edit_loop_{sid}.json")
    try:
        with open(state, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        data = {}
    key = os.path.normcase(os.path.abspath(path))
    data[key] = data.get(key, 0) + 1
    with open(state, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return data[key]


def message(path, n):
    if n < LIMIT or n % LIMIT:
        return None
    return (f"EDIT LOOP: {os.path.basename(path)} edited {n} times this session. Stop editing it. Say in one line what "
            "each edit tried, classify the failure (prompt, context, harness, loop, graph), and change the plan or ask "
            "the user before the next edit.")


def main():
    ev = json.loads(sys.stdin.buffer.read().decode("utf-8") or "{}")
    ti = ev.get("tool_input") or {}
    path = ti.get("file_path") or ti.get("notebook_path") or ti.get("path")
    msg = path and message(path, bump(ev.get("session_id", ""), path))
    if msg:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": msg}}))
    return 0


def selftest():
    d = tempfile.mkdtemp()
    p, q = os.path.join(d, "a.txt"), os.path.join(d, "b.txt")
    counts = [bump("s", p, d) for _ in range(LIMIT * 2)]
    assert counts == list(range(1, LIMIT * 2 + 1))
    assert bump("s", q, d) == 1 and bump("other", p, d) == 1        # per file, per session
    warned = [n for n in counts if message(p, n)]
    assert warned == [LIMIT, LIMIT * 2], warned                       # warns at the limit, then every limit more
    print("edit_loop selftest ok")
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        sys.exit(selftest())
    try:
        sys.exit(main())
    except Exception as e:  # a hook bug never blocks the session
        print(f"edit_loop error (skipped): {e!r}", file=sys.stderr)
        sys.exit(0)
