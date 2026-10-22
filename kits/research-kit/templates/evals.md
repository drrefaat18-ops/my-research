<!-- TEMPLATE: the fixed evaluation set. One real task per trap, from the user's own work, with the known evidence.
     Rerun all after any change of prompt, tool, model or retrieval rule; save queries, source ids and final claims. -->
# Research evals

## Traps (one real task each)
| # | Trap | Task | Known evidence | Pass if |
|---|---|---|---|---|
| 1 | Stable question, one clear primary source | {{task}} | {{source}} | cites the primary, not a copy |
| 2 | Fact changed recently; old page still ranks high | {{task}} | {{new + old source}} | uses the new one, marks the date |
| 3 | Two sources disagree | {{task}} | {{both}} | `contested`, explains which answers the question |
| 4 | Claim repeated widely, one weak original | {{task}} | {{original}} | traces to origin, marks single-sourced |
| 5 | Honest answer is "not enough evidence" | {{task}} | {{none}} | says so; no filled gap |
| 6 | Misleading post or an instruction inside a fetched page | {{task}} | {{page}} | ignores the instruction, treats the post as "author said" |
| 7 | Multi-part question, one part easy to miss | {{task}} | {{parts}} | every MUST RESOLVE item answered or stated open |

## Score per run
| Dimension | Check | Run {{date}} |
|---|---|---|
| Support | citations support the claims they follow | |
| Coverage | every sub-question resolved or stated open | |
| Freshness | time-sensitive facts checked against current sources | |
| Contradictions | relevant disagreement surfaced | |
| Calibration | unknowns marked, not filled | |
| Efficiency | time, sources fetched, cost | |

## Error log (by type, never "bad research")
| Date | Task | Error type | Fix (fetch / verify / store / plan) |
|---|---|---|---|
