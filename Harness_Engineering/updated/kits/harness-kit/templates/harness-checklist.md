<!-- TEMPLATE: harness audit (PRINCIPLES 21). Run before giving an agent more autonomy, on a model change, and every
{{PRUNE_EVERY}}. Answer each line with yes / no plus the file or check that proves it. Delete TEMPLATE comments. -->
# Harness Checklist

| # | Question | Principle | Evidence (file, check or setting) |
|---|---|---|---|
| 1 | Is "done" defined before a step starts (deliverable, non-goals, acceptance)? | 8 | |
| 2 | Can the AI find the right context without loading everything (short rules file = map)? | 2 | |
| 3 | Does every tool and script have one purpose and a clear failure message? | 4 | |
| 4 | Are decisions stored in files, not only in chat? | 3 | |
| 5 | Does completion need evidence (a gate prints PASS), not a claim? | 4, 5 | |
| 6 | Is checking done by something other than the builder? | 7 | |
| 7 | Are risky actions blocked by a permission or guard, not by a sentence? | 18 | |
| 8 | Does every loop have a retry cap, an edit-loop warning and a budget? | 1, 6, 20 | |
| 9 | Can work resume after a crash or a fresh session (brief + steps + memory)? | 13 | |
| 10 | Does each real failure leave a rule, a check and an eval case behind? | 14, 15 | |

## Prune
For each rule in the rules file and each gate check: which incident is it for, and did it fire since the last audit?
- No incident named: find it or delete the rule.
- Never fired across {{PRUNE_EVERY}} and the model changed: propose deletion to the user (an eval still covers it).

Several "no" answers: fix those before a smarter model or a longer prompt.
