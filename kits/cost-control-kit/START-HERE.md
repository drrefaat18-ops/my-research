# START HERE - Cost Control Kit Install Protocol (for the AI)

You are installing cost control into this project's AI tool setup. Read `COST-RULES.md` now; read `templates/`
and `scripts/` only in Phase 3.

## Hard rules for this protocol
- Four phases, in order. Each ends by stopping and waiting for the user.
- Talk to the user in their language; batch open questions; your recommendation first.
- Phases 1-2 are read-only: change no setting, create no file, before the Phase 3 yes.
- Never print an API key or token you find. If a secret sits in a settings file, warn the user and leave it.
- If the project has a harness (rules file, gates, hooks, guard), plug into it: register the filter hook beside
  the existing hooks, never replace them. Hooks and gates: `harness-kit`. Multi-agent spend: `agent-pipeline-kit`.

## Phase 1 - Interview + audit (skip what the files already answer, and say so)
Run `templates/audit-prompt.md` against the setup first, then ask only what is still open:
1. **Models:** top, mid and cheapest tier ids in use -> `{{TOP_MODEL}}`, `{{MID_MODEL}}`, `{{CHEAP_MODEL}}`;
   current list prices per meter -> `templates/prices.json` (from the vendor's pricing page; date -> `{{PRICES_CHECKED_DATE}}`).
2. **Tool surfaces:** the usage/context report commands -> `{{USAGE_CMD}}`; where per-model effort is saved
   -> `{{EFFORT_SETTING_PATH}}`; settings files that load -> `{{SETTINGS_FILES}}`; agent definitions dir -> `{{AGENTS_DIR}}`;
   the built-in search agent's exact name -> `{{SEARCH_AGENT_NAME}}`.
3. **Cache:** cache lifetime on this plan -> `{{CACHE_TTL}}`.
4. **Context:** always-loaded rules file -> `{{RULES_FILE}}`; its line budget -> `{{RULES_MAX_LINES}}`.
5. **Tests:** bare test commands run here (or none) -> `{{TEST_COMMANDS}}`; what a failure line looks like -> `{{FAIL_PATTERN}}`.
6. **Unattended runs:** scripts or schedules that call the tool non-interactively -> `{{BUDGET_USD}}`, `{{MAX_TURNS}}`.
7. **Baseline:** one real task the user runs often and can check -> where baselines are kept `{{BASELINE_DIR}}`.

## Phase 2 - Design (in chat, compact)
- Audit table: one row per rule 3-11 -> evidence (file and key) -> fine / fix.
- The three fixes that matter most, each tied to a rule number, each with the exact setting change.
- What you skip and why (no tests -> no filter hook; no unattended runs -> no caps).
Stop. Build only after an explicit yes.

## Phase 3 - Build
- Fill `templates/prices.json`, copy it and `scripts/cost.py` next to the project's other scripts; run
  `python cost.py --selftest` and show the output.
- Apply the approved setting changes in `{{SETTINGS_FILES}}` / `{{EFFORT_SETTING_PATH}}`, one key at a time, after
  reading each file.
- Search agent: fill `templates/search-agent.md` with `{{CHEAP_MODEL}}`, save it under `{{AGENTS_DIR}}` with the
  built-in search agent's exact name.
- Filter hook (only if `{{TEST_COMMANDS}}` is not none): set `TEST_COMMANDS` and `FAIL_PATTERN` in
  `scripts/filter_test_output.py`, run `--selftest`, register it as a pre-tool hook on the shell tool.
- Unattended runs: add the budget cap and max-turns flags with `{{BUDGET_USD}}` / `{{MAX_TURNS}}`.
- Add at most 5 lines to `{{RULES_FILE}}` pointing to the rules (clear between tasks, model at start, measure first).
- Copy `templates/baseline.md` to `{{BASELINE_DIR}}`; each task fills `{{TASK_NAME}}`.

## Phase 4 - Prove (one real task, COST-RULES 13)
Show the user: the baseline (`{{USAGE_CMD}}` output through `cost.py`), the one change tested, the second run, and
the verdict keep / revert. Report the numbers as measured; claim no saving you did not measure.
