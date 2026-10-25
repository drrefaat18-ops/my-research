# Harness Checklist

From harness-kit PRINCIPLES 21. Run before giving agents more autonomy, on a model change, and monthly (next: 2026-11-25). Answer yes / no + the file or check that proves it.

Audit 2026-10-25 (kit update):

| # | Question | Principle | Answer + evidence |
|---|---|---|---|
| 1 | Is "done" defined before a step starts (deliverable, non-goals, acceptance)? | 8 | partly: START-HERE steps name deliverable + date; acceptance = CLAUDE.md "Mark done only after confirmation"; non-goals not per step |
| 2 | Can the AI find the right context without loading everything? | 2 | yes: CLAUDE.md Project Map + `session_start.py` brief; but CLAUDE.md is 85+ lines (kit target 60) |
| 3 | Does every tool and script have one purpose and a clear failure message? | 4 | yes for gate scripts (Project Map list); `scripts/` also holds ~30 old one-off scripts (prune candidates) |
| 4 | Are decisions stored in files, not only in chat? | 3 | yes: memory/, LESSONS.md, START-HERE step notes |
| 5 | Does completion need evidence (a gate prints PASS), not a claim? | 4, 5 | yes: `review_gate.py`, `check_links.py`, `evals.py`, `lesson |` line |
| 6 | Is checking done by something other than the builder? | 7 | yes: pipeline step 9 Sonnet reality-checker + verifier prompt in `.claude/agents/testing-reality-checker.md` |
| 7 | Are risky actions blocked by a permission or guard, not by a sentence? | 18 | yes: `permission-lanes.md` → settings ask/deny; gap: `papers/` delete has no deny rule |
| 8 | Does every loop have a retry cap, an edit-loop warning and a budget? | 1, 6, 20 | yes: review_hook 3-fail cap, `edit_loop.py`, RULE 0 + `cost.py` |
| 9 | Can work resume after a crash or a fresh session? | 13 | yes: `session_start.py` + START-HERE + memory |
| 10 | Does each real failure leave a rule, a check and an eval case behind? | 14, 15 | yes: LESSONS.md ladder + `scripts/evals/` (15 cases) |

## Prune
For each rule in CLAUDE.md and each gate check: which incident is it for, and did it fire since the last audit?
- No incident named: find it or delete the rule.
- Never fired across a month and the model changed: propose deletion to the user (an eval still covers it).

Open from this audit: (a) CLAUDE.md over 60 lines; (b) old one-off scripts in `scripts/`; (c) `papers/` closed lane has no hard block.
