# START HERE - Agent Loop Kit Install Protocol (for the AI)

You are installing agent, memory and loop habits into this project. Read `LOOPS.md` now; read `templates/` and
`scripts/` only in Phase 3.

## Hard rules for this protocol
- Four phases, in order. Each ends by stopping and waiting for the user.
- Talk to the user in their language; batch open questions; your recommendation first.
- Phases 1-2 are read-only: create or change nothing before the Phase 3 yes.
- `{{X}}` is filled once at install; `[brackets]` stay in the installed prompts and are filled each time one is used.
- If the project has a harness (rules file, prompts file, gates, log), plug into it: prompts go into its prompts
  file, the keep-rate line into its log, the check is its gate. Never add a second rules file or log.
  Parallel work and skeptics: `graph-workflow-kit`. Sourced research: `research-kit`.

## Phase 1 - Interview (skip what the files already answer, and say so)
1. **Rules and prompts:** the always-loaded rules file -> `{{RULES_FILE}}`; where reusable prompts live -> `{{PROMPTS_FILE}}`.
2. **Memory:** where a checkpoint for the next session goes -> `{{HANDOFF_FILE}}`.
3. **Check:** the command that passes or fails an output here (gate, tests, validator) -> `{{CHECK_COMMAND}}`.
4. **Caps:** tries before a loop stops and reports -> `{{MAX_TRIES}}` (default 3, or the harness retry cap).
5. **Log:** where daily or run logs are written -> `{{LOG_DIR}}`; keep-rate threshold -> `{{KEEP_RATE_MIN}}` (default 0.5).
6. **Sources:** the project's citation rule for research findings -> `{{SOURCE_RULE}}`
   (default: "Every claim names its source and date. No source, no claim.").
7. **Candidates:** which recurring tasks the user wants as loops. Test each against LOOPS 6 in chat.

## Phase 2 - Design (in chat, compact)
- Table: candidate task -> LOOPS 6 four conditions (yes/no each) -> loop / keep manual / graph (`graph-workflow-kit`).
- Which agent templates to install, and where each prompt lands in `{{PROMPTS_FILE}}`.
- At most 5 lines for `{{RULES_FILE}}`: checkpoint before stopping, self-score never means done, cap `{{MAX_TRIES}}`,
  log every loop run as kept or discarded.
Stop. Build only after an explicit yes.

## Phase 3 - Build
- Fill the placeholders in the chosen templates and add them as sections of `{{PROMPTS_FILE}}` (read it first).
- Copy `scripts/keep_rate.py` next to the project's other scripts; run `python keep_rate.py --selftest`, show output.
- Add the approved lines to `{{RULES_FILE}}`, including the log line format: `loop | <name> | kept|discarded | <note>`.

## Phase 4 - Prove (one real loop)
Run one approved loop by hand (LOOPS 11): draft loop -> `{{CHECK_COMMAND}}` -> one log line in `{{LOG_DIR}}`.
Then `python keep_rate.py {{LOG_DIR}}` and show the output. Report the result as measured.
