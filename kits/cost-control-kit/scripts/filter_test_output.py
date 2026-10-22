#!/usr/bin/env python3
"""Pre-tool hook: a bare test command returns only its failure lines; exit code and full log are kept.

Hook mode (stdin = tool-call JSON): if tool_input.command is an exact, bare test command, rewrite it to
  "<python>" "<this script>" --run "<command>"   and allow it. Anything else: "{}" (untouched).
Run mode: python filter_test_output.py --run "<command>"  -> runs it, saves the log, prints failures, exits with its code.
Selftest:  python filter_test_output.py --selftest

Only bare commands match (no ; & | $ ` quotes or newlines): "allow" skips the permission prompt, so a prefix
match would approve whatever is chained after it. Deny/ask rules still apply. A crash prints "{}" and exits 0,
so it never blocks the session.
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

TEST_COMMANDS = ["pytest", "npm test", "go test"]  # TEMPLATE: {{TEST_COMMANDS}}
FAIL_PATTERN = r"(FAIL|ERROR|error:)"  # TEMPLATE: {{FAIL_PATTERN}}
AFTER, MAX_LINES = 5, 100


def bare_re(commands):
    return re.compile(r"^(" + "|".join(map(re.escape, commands)) + r")( [A-Za-z0-9_./:=@-]+)*$")


def decide(payload, commands=TEST_COMMANDS):
    cmd = (payload.get("tool_input") or {}).get("command", "")
    if not isinstance(cmd, str) or not bare_re(commands).match(cmd):
        return {}
    me = Path(__file__).resolve().as_posix()
    new = f'"{Path(sys.executable).as_posix()}" "{me}" --run "{cmd}"'
    return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "allow",
                                   "updatedInput": {**payload["tool_input"], "command": new}}}


def run(cmd, pattern=FAIL_PATTERN, log=None):
    log = Path(log or Path(tempfile.gettempdir()) / "agent-test.log")
    with log.open("w", encoding="utf-8", errors="replace") as f:
        code = subprocess.run(cmd, shell=True, stdout=f, stderr=subprocess.STDOUT).returncode
    lines = log.read_text(encoding="utf-8", errors="replace").splitlines()
    fail = re.compile(pattern)
    keep, until = [], -1
    for i, line in enumerate(lines):
        if fail.search(line):
            until = i + AFTER
        if i <= until:
            keep.append(line)
    out = keep[:MAX_LINES] + [f"exit code: {code} (full log: {log.as_posix()}, {len(lines)} lines)"]
    return code, out


def selftest():
    cmds = ["pytest", "npm test"]
    p = lambda c: {"tool_input": {"command": c, "description": "x"}}
    assert decide(p("pytest tests/unit -q"), cmds)["hookSpecificOutput"]["permissionDecision"] == "allow"
    assert decide(p("pytest; echo pwned"), cmds) == {}
    assert decide(p("pytest && rm -rf x"), cmds) == {}
    assert decide(p("pytest $(whoami)"), cmds) == {}
    assert decide(p("ls -la"), cmds) == {}
    assert decide({"tool_input": {}}, cmds) == {}
    assert "description" in decide(p("npm test"), cmds)["hookSpecificOutput"]["updatedInput"]
    fake = Path(tempfile.gettempdir()) / "fake_runner.py"
    fake.write_text("import sys\nfor i in range(300): print('ok', i)\n"
                    "print('FAIL test_x'); print('  assert 1 == 2'); print('ERROR test_y')\nsys.exit(1)\n")
    code, out = run(f'"{sys.executable}" "{fake}"', log=Path(tempfile.gettempdir()) / "fake_runner.log")
    assert code == 1, code
    assert len(out) == 4 and out[0] == "FAIL test_x" and "303 lines" in out[-1], out
    print("\n".join(out))
    print("selftest OK")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    elif sys.argv[1:2] == ["--run"]:
        code, out = run(sys.argv[2])
        print("\n".join(out))
        sys.exit(code)
    else:
        try:
            print(json.dumps(decide(json.load(sys.stdin))))
        except Exception:  # ponytail: never block the session on a hook bug
            print("{}")
