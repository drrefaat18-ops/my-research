"""SessionStart hook: brief Claude on the review state before any work.

Prints {"hookSpecificOutput": {"additionalContext": ...}} with:
research agent shortlist, next START-HERE step, drafts (words + gate result),
papers (count + smallest files = likely stubs), git-changed review files.
"""
import glob, json, os, re, subprocess, sys

ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REV = os.path.join(ROOT, "08 - RA Repurposing Review")
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


def main():
    out = ["SESSION START BRIEF — before any work, reply with one line: "
           "'Picked inline role: .claude/agents/<file>.md (<why>)' then use this brief.",
           "Research agents: " + ", ".join(a for a in AGENTS if os.path.exists(os.path.join(ROOT, ".claude/agents", a + ".md"))),
           "Next step: " + next_step()]
    changed = subprocess.run(["git", "status", "--porcelain", "-uall", "--", REV], cwd=ROOT,
                             capture_output=True, text=True, encoding="utf-8").stdout.split("\n")
    changed = [l[3:].strip('"') for l in changed if l.strip()]
    out.append("Drafts:")
    for p in sorted(glob.glob(os.path.join(REV, "drafts", "Day*.md"))):
        words = len(re.findall(r"\w+", open(p, encoding="utf-8").read()))
        rel = "drafts/" + os.path.basename(p)
        dirty = any(c.endswith(rel) for c in changed)
        out.append(f"  {rel}: {words} words" + (f", changed, gate {gate(rel)}" if dirty else ""))
    papers = sorted(glob.glob(os.path.join(REV, "papers", "*.md")), key=os.path.getsize)
    out.append(f"Papers: {len(papers)} files; smallest (stub?): " +
               ", ".join(f"{os.path.basename(p)[:-3]} {os.path.getsize(p) // 1024}KB" for p in papers[:5]))
    out.append("Git-changed in review: " + (", ".join(changed) or "none"))
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                             "additionalContext": "\n".join(out)}}, ensure_ascii=False))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
