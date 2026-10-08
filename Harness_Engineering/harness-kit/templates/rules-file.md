<!-- TEMPLATE: save as CLAUDE.md / AGENTS.md / GEMINI.md / .cursorrules to match the user's tool. Keep ≤ 60 lines. Delete TEMPLATE comments. -->
# {{PROJECT_NAME}} — AI Operating Rules

> **RULE 0 — BUDGET:** {{BUDGET_RULE}}
> <!-- TEMPLATE: user's own numbers, e.g. "Max 2 sub-agents per day; prefer reading one file over searching the tree; deadline 2026-12-01." -->

> **RULE 1 — AGENTS:** {{AGENT_RULE}}
> <!-- TEMPLATE: the user's Phase-1 choice verbatim, plus who picks the agent and that the agent is named before use. Add the mechanical gate line, e.g. "Gate: .claude/settings.json permissions.ask = Agent". -->

## Rules
- Do what the current step asks; nothing more. Check the step's non-goals before editing.
- Never edit `sources/raw/`. Regenerate `sources/md/` with `python harness/ingest.py`.
- Every factual claim links to a `sources/md/` anchor or is marked `[unverified]`.
- Fix flagged lines locally; never regenerate a whole section to fix one finding.
- Before saying "done": run `python harness/gate.py <changed files>` and show the result.
- After {{RETRY_CAP}} gate failures on one file (or same findings twice): stop, show findings, wait.
- Forbidden: {{FORBIDDEN}}

## Map (read only what the current step needs)
- `{{STEPS_FILE}}` — plan; the first unchecked step is the current task
- `memory/INDEX.md` — durable decisions and preferences; one fact per file
- `sources/raw/` — originals (read-only) · `sources/md/` — converted, anchored copies
- `harness/gate.py` — quality checks · `harness/ingest.py` — source conversion · `harness/hook.py` — tool hook
- {{OTHER_KEY_PATHS}}

## Gates
- Gated paths: {{GATED_GLOBS}}
- Checks: {{CHECK_LIST}}
- Wiring: {{HOOK_WIRING}} <!-- TEMPLATE: or "No hooks in this tool — running the gate before 'done' is mandatory." -->
