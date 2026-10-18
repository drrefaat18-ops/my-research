"""SessionStart hook: brief Claude on the review state before any work.

Prints {"hookSpecificOutput": {"additionalContext": ...}} with:
research agent shortlist, next START-HERE step, drafts (words + gate result),
papers (count + smallest files = likely stubs), git-changed review files.
"""
import glob, json, os, re, subprocess, sys, time

ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REV = os.path.join(ROOT, "08 - RA Repurposing Review")
BOOKMARK = os.path.join(ROOT, ".claude", "state", "bookmark.json")  # local, gitignored
# ponytail: fixed shortlist of agent files that fit this vault; edit when a new role is needed
AGENTS = ["research-synthesist", "healthcare-clinical-evidence-agent", "academic-statistician",
          "testing-reality-checker", "engineering-technical-writer", "specialized-master-plan-architect"]


def next_step():
    for line in open(os.path.join(REV, "START-HERE.md"), encoding="utf-8"):
        if line.lstrip().startswith("- [ ]"):
            return line.strip()[6:200]
    return "all steps checked"


def gate(path):
    try:
        r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "review_gate.py"), path],
                           cwd=REV, capture_output=True, text=True, encoding="utf-8", timeout=40,
                           env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        flagged = [l.strip() for l in r.stdout.splitlines() if l.strip().startswith("[")]
        return "pass" if r.returncode == 0 else f"{len(flagged)} findings: " + " | ".join(f[:80] for f in flagged)
    except Exception as e:
        return f"gate error: {e.__class__.__name__}"


def git(*args):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        raise RuntimeError(r.stderr.strip()[:120])
    return r.stdout


def since_bookmark():
    """Commits + review files changed since last session's bookmark; moves the bookmark only on success."""
    prev = json.load(open(BOOKMARK, encoding="utf-8")) if os.path.exists(BOOKMARK) else None
    head = git("rev-parse", "HEAD").strip()
    if prev and subprocess.run(["git", "cat-file", "-e", prev["head"] + "^{commit}"], cwd=ROOT,
                                   stderr=subprocess.DEVNULL).returncode:
        line = f"Since last session: bookmark commit {prev['head'][:8]} gone (rebase?), reset"
    elif prev and prev["head"] != head:
        n = len(git("rev-list", f"{prev['head']}..{head}").split())
        files = git("-c", "core.quotepath=off", "diff", "--name-only", prev["head"], head, "--", REV).splitlines()
        line = f"Since last session ({prev['date']}): {n} commits; review files: " + \
               (", ".join(f[len("08 - RA Repurposing Review/"):] for f in files[:8]) or "none")
    else:
        line = "Since last session: " + ("no new commits" if prev else "first run, bookmark set")
    os.makedirs(os.path.dirname(BOOKMARK), exist_ok=True)
    json.dump({"head": head, "date": time.strftime("%Y-%m-%d %H:%M")}, open(BOOKMARK, "w", encoding="utf-8"))
    return line


def main():
    out = ["SESSION START BRIEF — before any work, reply with one line: "
           "'Picked inline role: .claude/agents/<file>.md (<why>)' then use this brief."]
    unreadable = []

    def section(name, fn):
        # a failed read is reported as unreadable, never as "nothing new"
        try:
            fn()
        except Exception as e:
            unreadable.append(f"{name} ({e.__class__.__name__}: {str(e)[:80]})")

    section("agents", lambda: out.append("Research agents: " + ", ".join(
        a for a in AGENTS if os.path.exists(os.path.join(ROOT, ".claude/agents", a + ".md")))))
    section("START-HERE", lambda: out.append("Next step: " + next_step()))
    section("bookmark", lambda: out.append(since_bookmark()))
    changed = []

    def drafts():
        changed.extend(l[3:].strip('"') for l in git("status", "--porcelain", "-uall", "--", REV).split("\n") if l.strip())
        out.append("Drafts:")
        for p in sorted(glob.glob(os.path.join(REV, "drafts", "Day*.md"))):
            words = len(re.findall(r"\w+", open(p, encoding="utf-8").read()))
            rel = "drafts/" + os.path.basename(p)
            g = gate(rel) if any(c.endswith(rel) for c in changed) else None
            if g and g.startswith("gate error"):
                unreadable.append(f"gate on {rel}")
            out.append(f"  {rel}: {words} words" + (f", changed, gate {g}" if g else ""))

    def papers():
        ps = sorted(glob.glob(os.path.join(REV, "papers", "*.md")), key=os.path.getsize)
        out.append(f"Papers: {len(ps)} files; smallest (stub?): " +
                   ", ".join(f"{os.path.basename(p)[:-3]} {os.path.getsize(p) // 1024}KB" for p in ps[:5]))

    def evals():
        r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "evals.py"), "-q"], cwd=ROOT,
                           capture_output=True, text=True, encoding="utf-8", timeout=60,
                           env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        out.extend(l for l in r.stdout.splitlines() if l.strip())

    section("drafts/git", drafts)
    section("papers", papers)
    section("evals", evals)
    out.append("Git-changed in review: " + (", ".join(changed) or "none"))
    out.append("UNREADABLE this session (do not treat as 'nothing'): " + (", ".join(unreadable) or "none"))
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                             "additionalContext": "\n".join(out)}}, ensure_ascii=False))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
