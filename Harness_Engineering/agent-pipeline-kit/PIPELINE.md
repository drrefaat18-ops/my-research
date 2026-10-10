# The Pipeline

**Orchestrator plans and judges. Haiku reads. Sonnet writes. Scripts verify. The human decides.**

## Roles

| Agent | Model | Role file | Job | Edits files? |
|---|---|---|---|---|
| Orchestrator | Opus (main session) | your review/synthesis role | plan, verify, insert, accuracy review | yes, the only one |
| Evidence × N | Haiku | `agents/evidence-extractor.md` | evidence cards with verbatim quotes + line numbers | no |
| Writer × 1 | Sonnet, effort high | `agents/writer.md` | sentences from the brief + verified cards only | no |
| Checker | Haiku | `agents/checker.md` | runs gates, turns output into a numbered list | no |
| Source hunter (on demand) | Haiku | `agents/evidence-extractor.md` | finds originals behind second-hand claims | no |

**Sizing:** one evidence agent per 4–6 sources (or per topic), at most 4 in parallel. Always one writer per
section — two writers give two voices, repeated claims and broken transitions.

## Phases

| # | Who | Parallel? | Output |
|---|---|---|---|
| 0 | Orchestrator | — | git checkpoint; roles in place |
| 1 Plan | Orchestrator | — | claims needed per sentence; sources split across evidence agents |
| 2 Evidence | Haiku × N | yes | cards: design, n, dose/setting, verbatim quote, line, section, evidence level, author limits |
| 3 Verify | `verify_quotes.py` | — | every quote checked on its line; FAIL cards dropped |
| 4 Write | Sonnet | — | sentences + the card lines each rests on, or `CANNOT WRITE: reason` |
| 5 Insert | Orchestrator | — | text placed in the draft; gate/hook runs |
| 6 Check | Haiku | — | numbered findings: blocker / fix / note |
| 7 Fix | same Sonnet (resume) | — | max 3 rounds, then escalate to the human |
| 8 Accuracy | Orchestrator | — | statistics, evidence level, wording strength, over-reach |
| 9 Review | Human | — | table: sentence → quote → link; decides open points |

## Rules

1. **Announce before every spawn:** how many agents, each one's name, model and job. No silent spawns.
2. **Only the orchestrator edits files.** Sub-agents return text. Gates then run in one session and retry caps count correctly.
3. **Quote, don't summarise.** Evidence agents copy text character-for-character with its line number. The script checks it — trust nothing unverified, from any model, Opus included.
4. **Unreadable ≠ absent.** A failed read, search or tool is reported as `UNREADABLE`/`NOT FOUND`, never as "no evidence".
5. **Primary sources.** A claim found in a paper's introduction/discussion, or in a review, is traced to the original. Reviews often cite originals that do not say what the review says.
6. **The writer gets nothing but the brief, the verified cards and the paragraph context.** No new facts, no numbers outside the cards; our own interpretation carries no citation and is hedged.
7. **Style rules live in one file** that the writer reads every run; never copy them into prompts.
8. **Verify before proposing.** IDs, titles and abstracts that a sub-agent found on the web are re-fetched by the orchestrator (e.g. Europe PMC API) before the human sees them.
9. **Abstract-only sources** only when the human cannot reach the full text; store the official abstract verbatim (check it char-for-char), note what it does NOT say, cite only that.
10. **Notes go into the work files** (steps file, source file), not only chat.

## What it caught on its first run

- A sentence claiming ESR "stayed higher" — the paper compared ESR only at baseline.
- A mechanism cited to a review whose own references were about a different receptor.
- Number strings copied in source order (21 seven-word matches) — split and reordered.
- A dose sentence cited only to the conversion method, not to the study that gave the dose.
