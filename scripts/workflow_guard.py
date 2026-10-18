"""PreToolUse hook: owner approval for every sub-agent spawn, model rules for workflow scripts.

- Agent / Task call: ask the owner (deny if its model is banned).
- Workflow call: read the script (inline, scriptPath, or .claude/workflows/<name>.js). Deny if any agent()
  call has no literal `model:` option (it would inherit the session model) or names a banned model.
  Otherwise ask the owner, with a tally of models per call site.
A crash never blocks (exit 0, no decision). Stdlib only.
Usage: python workflow_guard.py < event.json   |   python workflow_guard.py --selftest
"""
import glob, json, os, re, sys

BANNED_MODELS = ["opus", "fable"]  # RULE 0: Opus is the orchestrator only; sub-agents = haiku/sonnet
REQUIRE_MODEL = True            # deny agent() calls that do not name a model
ASK_ON_SPAWN = True             # False: allow Agent/Workflow calls that pass the model rules without asking
ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()

JS_SKIP = re.compile(r"'(?:\\.|[^'\\\n])*'|\"(?:\\.|[^\"\\\n])*\"|`(?:\\.|[^`\\])*`|//[^\n]*|/\*.*?\*/", re.S)
MODEL_OPT = re.compile(r"\bmodel\s*:\s*(['\"`])([\w.:-]+)\1")


def workflow_agents(script):
    """Model literal (or None) of every agent(...) call. Strings and comments are blanked to find the
    calls and their closing parenthesis; the model value is read from the original text of each call."""
    blank = JS_SKIP.sub(lambda m: m.group(0)[0] + " " * (len(m.group(0)) - 2) + m.group(0)[-1]
                        if m.group(0)[0] in "'\"`" else " " * len(m.group(0)), script)
    out = []
    for m in re.finditer(r"(?<![\w.$])agent\s*\(", blank):
        depth, j = 0, m.end() - 1
        for j in range(m.end() - 1, len(blank)):
            depth += {"(": 1, ")": -1}.get(blank[j], 0)
            if depth == 0:
                break
        mo = MODEL_OPT.search(script[m.end():j])
        out.append(mo.group(2) if mo else None)
    return out


def banned(model):
    return any(b in (model or "").lower() for b in BANNED_MODELS)


def check_workflow(ti):
    script, src = ti.get("script") or "", "inline script"
    path = ti.get("scriptPath") or (ti.get("name") and os.path.join(ROOT, ".claude", "workflows", ti["name"] + ".js"))
    if not script and path:
        src = path
        try:
            script = open(path, encoding="utf-8").read()
        except OSError:
            return "ask", f"workflow '{ti.get('name') or path}' is not readable by the guard - check its agents before approving"
    models = workflow_agents(script)
    if REQUIRE_MODEL and None in models:
        return "deny", (f"{models.count(None)} of {len(models)} agent() calls in {src} have no literal model: option "
                        "(they would inherit the session model). Add model: 'haiku' or 'sonnet'")
    if any(banned(m) for m in models):
        return "deny", f"banned model in {src} (banned: {', '.join(BANNED_MODELS)})"
    tally = ", ".join(f"{m} x{models.count(m)}" for m in sorted(set(models), key=str)) or "no agent() calls found"
    return ("ask" if ASK_ON_SPAWN else None), f"workflow spawn ({tally} call sites; loops and fan-out multiply them)"


def decide(ev):
    tool, ti = ev.get("tool_name", ""), ev.get("tool_input") or {}
    if tool in ("Agent", "Task"):
        if banned(ti.get("model")):
            return "deny", f"banned sub-agent model '{ti.get('model')}'"
        who = ti.get("subagent_type") or ti.get("name") or "agent"
        return ("ask", f"spawn {who}, model {ti.get('model') or 'default'}") if ASK_ON_SPAWN else None
    if tool == "Workflow":
        d = check_workflow(ti)
        return d if d[0] else None
    return None


def main():
    d = decide(json.loads(sys.stdin.buffer.read().decode("utf-8") or "{}"))
    if d:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": d[0],
                                                 "permissionDecisionReason": d[1]}}, ensure_ascii=False))
    return 0


def selftest():
    E = lambda tool, **ti: decide({"tool_name": tool, "tool_input": ti})
    wf = lambda s: E("Workflow", script=s)
    assert E("Agent", subagent_type="Explore")[0] == "ask"
    assert E("Agent", model="opus")[0] == "deny"
    assert wf("await agent(`read ${x} (a)`, {schema: S})")[0] == "deny"                 # no model
    assert wf("await agent('x', {model: 'opus'})")[0] == "deny"
    assert wf("xs.map(x => () => agent(x.p, {label: f(x), model: 'haiku'}));\nagent('y')")[0] == "deny"
    ok = wf("// agent('comment')\nconst s = \"agent(\";\nawait agent(`p ${f(a)}`, {schema: S, model: 'haiku'})")
    assert ok[0] == "ask" and "haiku x1" in ok[1], ok
    assert workflow_agents("agent('a', {model: \"sonnet\"}); agent('b'); my.agent('c')") == ["sonnet", None]
    wf_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".claude", "workflows")
    for p in glob.glob(os.path.join(wf_dir, "*.js")):
        assert E("Workflow", scriptPath=p)[0] == "ask", p
    print("workflow_guard selftest ok")
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        sys.exit(selftest())
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.exit(main())
    except Exception as e:
        print(f"workflow_guard error (no decision): {e!r}", file=sys.stderr)
        sys.exit(0)
