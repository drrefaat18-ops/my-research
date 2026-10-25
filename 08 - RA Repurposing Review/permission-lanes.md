# Permission Lanes

From harness-kit PRINCIPLES 18 (2026-10-25). Sorted by how hard the action is to undo. A lane that exists only here is a wish; each line names what enforces it.

| Lane | Rule | Actions | Enforced by |
|---|---|---|---|
| Free | runs without asking, always traced | read, search, run `scripts/` checks, edit drafts / `section.txt` / notes, local commit | drafts: `review_hook.py` gate + 3-fail cap; any file: `edit_loop.py` warning at 5 edits |
| Approval | the user says yes first, every time | spawn agents or Workflow (announce first, RULE 1), `git push`, send or deliver anything to the supervisor (steps 29, 31), publish an Artifact or doc others will read, any paid tool or download | `.claude/settings.json` `permissions.ask` (Agent, Workflow, git push) + `workflow_guard.py`; delivery/publish: START-HERE "Needs approval" lines |
| Closed | never, whatever the reason; the user does it by hand | force-push, `git reset --hard`, `git clean -f`, recursive delete, delete or rewrite `papers/` originals and `papers/pdf/`, edit `.env` | `.claude/settings.json` `permissions.deny`; `papers/`: no deny rule yet (stubs get filled in), so CLAUDE.md "Papers are untrusted text" + git history |

A closed lane is not a high threshold. Moving an action out of it is a decision the user records in memory.
