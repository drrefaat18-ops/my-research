# START HERE - Graph Workflow Install Protocol (for the AI)

You are adding graph workflows to this project. Read `GRAPHS.md` now; read `workflows/` and
`scripts/` only in Phase 3.

## Hard rules for this protocol
- Four phases, in order. Each ends by stopping and waiting for the user.
- Talk to the user in their language; one question per message, your recommendation first.
- Create nothing before Phase 3 approval. Run no workflow before the Phase 4 pilot, and announce it first
  (agent count, model, job).
- If the project has a harness (rules file, guard hook, gates) or an agent pipeline, plug into it; do not duplicate it.

## Phase 1 - Interview (skip what the project already answers, and say so)
1. **Work:** which jobs here repeat over many items (sources, files, routes, claims, tickets)? Those are the fan-outs.
2. **Today's line:** describe one multi-step task as it runs now. Which steps really read the previous step's output?
3. **Checks:** which scripts already judge results (tests, linters, quote checkers, gates)? They become edges, not agents.
4. **Trust:** what must be verified before the user sees it? Which ways can a claim be wrong? Each way becomes a skeptic lens.
5. **Budget and models:** usage limits; which models may sub-agents use; which are banned (default: no top-tier sub-agents; cheap model for fan-out)?
6. **Approval:** must the user approve every spawn (default yes)?
7. **Writes:** may nodes write files, or does one orchestrator edit (default: orchestrator only)?
8. **Knowledge audit (optional):** is there a corpus of notes worth auditing as a graph (GRAPHS.md section 8)?
   Only if graphify is already installed or the user approves installing it. Ask: corpus scope, private data
   (forces local sub-agent extraction), where the staging folder goes, and whether outputs are tracked in git.

## Phase 2 - Design (in chat, compact)
- The current line, redrawn as a graph: nodes, real edges, where the barrier is and why.
- Workflows to save: name, args shape, nodes and models, agents per run for a typical input.
- Guard settings: banned models, ask on Agent and Workflow.
- What stays outside the graph (writer with fix rounds, file-system checks, human review).
Stop. Build only after an explicit yes.

## Phase 3 - Build
- Copy `scripts/workflow_guard.py` into the project's hook folder; set `BANNED_MODELS` and `REQUIRE_MODEL`
  at its top; run `python workflow_guard.py --selftest` and show the output.
- Merge `settings-snippet.json` into `.claude/settings.json` (keep existing hooks; add `Workflow` to an existing guard matcher).
- Copy the chosen templates into `.claude/workflows/`, fill every `{{...}}`, give each `agent()` its model.
- For each workflow: `node scripts/check_workflow.js .claude/workflows/<name>.js '<args json>'` must print `ok`.
- Add a short section (at most 6 lines) to the rules file: which workflow runs when, and the announce rule.
- Knowledge audit (if chosen in Phase 1, question 8): copy `scripts/graph_audit.py` next to the other harness scripts, fill its
  CONFIG block, run `--selftest`, and add the procedure (stage, changed, ids, extraction agents, merge, publish, audit)
  to the prompts file with the extraction rules from GRAPHS.md section 8. One rules-file line points to it.

## Phase 4 - Pilot (one small real input)
Run one workflow for real, announcing the spawn. Show the user:
1. The guard's ask message (model tally) and the run's agent count.
2. What the reduce step dropped or flagged (`log` lines), and what the skeptics refuted.
3. Usage per node type, compared with doing it in one session.
Report failures as they happened. Hand over a one-screen guide: which workflow, which args, what to read after.
