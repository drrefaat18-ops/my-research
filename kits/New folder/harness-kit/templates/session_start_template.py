"""Session-start brief. TEMPLATE: copy to harness/session_start.py (next to hook.py and gate.py).

Runs when a new AI session starts (SessionStart-style hook) and injects a short brief so the AI
orients itself before any work: agent shortlist, current step, gated files (size + gate result on
changed ones), smallest sources (likely empty/truncated conversions), git-changed files.
Output: Claude Code JSON ({"hookSpecificOutput": {"additionalContext": ...}}); with --plain, plain text
(for tools whose session hook reads stdout, or to run by hand when the tool has no such hook).
A crash never blocks the session (exit 0 + warning).
Usage: python harness/session_start.py [--plain]   |   python harness/session_start.py --selftest
"""
import glob, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hook import ROOT, gated_files, run_gate  # noqa: E402  (same GATED globs as the edit hook)

STEPS_FILE = "{{STEPS_FILE}}"        # TEMPLATE: e.g. "STEPS.md"; first "- [ ]" line = current step
AGENT_DIR = "{{AGENT_DIR}}"          # TEMPLATE: e.g. ".claude/agents"; "" if the user has no agent files
AGENTS = ["{{AGENT_NAME}}"]          # TEMPLATE: role files that fit this work (file names without .md); [] if none
SOURCES_MD = "sources/md"
OPENING_LINE = ("Picked inline role: <agent file> (<why>)")  # TEMPLATE: match the user's RULE 1 wording


def next_step(path):
    try:
        for line in open(path, encoding="utf-8"):
            if line.lstrip().startswith("- [ ]"):
                return line.strip()[6:200]
    except OSError:
        return f"steps file not found: {STEPS_FILE}"
    return "all steps checked"


def git_changed():
    try:
        r = subprocess.run(["git", "status", "--porcelain", "-uall"], cwd=ROOT, capture_output=True,
                           text=True, encoding="utf-8", timeout=20)
        return [l[3:].strip().strip('"') for l in r.stdout.splitlines() if l.strip()]
    except Exception:
        return []


def brief():
    changed = git_changed()
    agents = [a for a in AGENTS if AGENT_DIR and os.path.exists(os.path.join(ROOT, AGENT_DIR, a + ".md"))]
    out = [f"SESSION START BRIEF - before any work, reply with one line: '{OPENING_LINE}', "
           "then summarize this brief in 2-3 lines (current step, gate findings, suspect sources).",
           "Agents: " + (", ".join(agents) or "none listed"),
           "Current step: " + next_step(os.path.join(ROOT, STEPS_FILE)),
           "Gated files:"]
    for f in sorted(gated_files()):
        rel = os.path.relpath(f, ROOT).replace("\\", "/")
        words = len(re.findall(r"\w+", open(f, encoding="utf-8", errors="replace").read()))
        line = f"  {rel}: {words} words"
        if rel in changed:  # ponytail: gate only changed files, keeps session start fast
            code, res = run_gate([f])
            found = [l.strip() for l in res.splitlines() if l.strip().startswith("[")]
            line += ", changed, gate " + ("pass" if not code else f"{len(found)} findings: " + " | ".join(x[:80] for x in found))
        out.append(line)
    srcs = sorted(glob.glob(os.path.join(ROOT, SOURCES_MD, "*.md")), key=os.path.getsize)
    out.append(f"Sources: {len(srcs)} files; smallest (check conversion): " +
               (", ".join(f"{os.path.basename(p)} {os.path.getsize(p) // 1024}KB" for p in srcs[:5]) or "none"))
    out.append("Git-changed: " + (", ".join(changed) or "none"))
    return "\n".join(out)


def selftest():
    import tempfile
    d = tempfile.mkdtemp()
    p = os.path.join(d, "steps.md")
    open(p, "w", encoding="utf-8").write("- [x] **1.** old\n- [ ] **2.** next one\n")
    assert next_step(p) == "**2.** next one"
    open(p, "w", encoding="utf-8").write("- [x] done\n")
    assert next_step(p) == "all steps checked"
    assert next_step(os.path.join(d, "missing.md")).startswith("steps file not found")
    print("session_start selftest ok")
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        sys.exit(selftest())
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        text = brief()
        print(text if "--plain" in sys.argv else json.dumps(
            {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": text}}, ensure_ascii=False))
    except Exception as e:  # never block session start; tell the AI to run it by hand
        print(f"session_start error: {e!r} - run python harness/session_start.py --plain yourself", file=sys.stderr)
    sys.exit(0)
