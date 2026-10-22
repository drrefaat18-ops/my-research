# START HERE - Research Kit Install Protocol (for the AI)

You are installing a source-grounded research workflow into this project. Read `RESEARCH.md` now; read
`templates/` and `scripts/` only in Phase 3.

## Hard rules for this protocol
- Four phases, in order. Each ends by stopping and waiting for the user.
- Talk to the user in their language; one question per message, your recommendation first.
- Create nothing before Phase 3 approval. Spawn no agent before the Phase 4 pilot, and announce it first
  (count, model, job).
- If the project has a harness (rules file, gates, hooks, evals) or an agent pipeline, plug into it; do not
  duplicate it. Evidence extraction and quote checks: `agent-pipeline-kit`. Lanes, skeptics, targeted loops:
  `graph-workflow-kit` (`diamond.js`, `skeptic-panel.js`, `loop-until-dry.js`). Eval replay: `harness-kit`.

## Phase 1 - Interview (skip what the project already answers, and say so)
1. **Questions:** what kinds of questions will be researched, and what decision does each answer feed?
2. **Surfaces:** which source surfaces exist here: web search/fetch tool, a private library (folder, notes,
   repository), a database or API, social posts? Which are enabled in the tool today? -> `{{SOURCE_SURFACES}}`
3. **Source ranking:** which source types count as primary for this work, which as independent, which only as leads?
   -> `{{SOURCE_RANKING}}`
4. **Freshness:** which fact types change (prices, versions, schedules, people) and how often? -> fact types and
   days for `{{FRESHNESS_WINDOWS}}` (`FRESHNESS_DAYS` in `ledger_check.py`)
5. **Levels and budget:** limits for QUICK / STANDARD / DEEP (rounds, lanes, agents, models) -> `{{SERVICE_LEVELS}}`
6. **Storage:** where briefs and ledgers live (one folder per task id) -> `{{LEDGER_DIR}}`; how raw sources are kept.
7. **Output:** what the report looks like (memo, table, note in the knowledge base) -> `{{OUTPUT_FORMAT}}`
8. **Traps:** past research failures the user has seen -> first rows of `templates/evals.md`.

## Phase 2 - Design (in chat, compact)
- The six stages mapped to this project: who does each (main session, which agent), which existing script checks it.
- Filled values for every placeholder above; freshness table; level table.
- Files to create: brief and ledger templates in `{{LEDGER_DIR}}`, `ledger_check.py` next to the other check scripts,
  the operator prompt (as a rules-file section of at most 10 lines, or the project's prompts file), the eval set.
Stop. Build only after an explicit yes.

## Phase 3 - Build
- Copy `templates/brief.md` and `templates/ledger.md` into `{{LEDGER_DIR}}/_templates/`; fill every `{{UPPER_CASE}}`
  placeholder except `{{TASK_ID}}`, which each task fills.
- Copy `scripts/ledger_check.py`; set `FRESHNESS_DAYS`; run `python ledger_check.py --selftest` and show the output.
- If the project has a gate or hook, call `ledger_check.py` from it for files under `{{LEDGER_DIR}}`.
- Add the operator prompt (`templates/research-prompt.md`) and lane prompts (`templates/lane-prompt.md`) where the
  project keeps prompts; one rules-file line points to them.
- Put the trap set (`templates/evals.md`) where the project keeps evals; one real task per trap.

## Phase 4 - Pilot (one real STANDARD question)
Run the six stages for real, announcing each spawn. Show the user:
1. The brief, and the one question asked (or the stated assumptions).
2. `ledger_check.py` output on the ledger and the report (target: no `[fix]`).
3. The report table: claim -> status -> passage -> source, with the unverified and contested claims listed.
4. Usage: rounds, lanes, sources fetched, sub-agent tokens.
Report failures as they happened. Hand over a one-screen guide: how to start a task, which level to pick,
what the user reviews, where ledgers live.
