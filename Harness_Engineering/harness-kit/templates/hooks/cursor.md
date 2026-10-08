# Wiring the gate in Cursor

Rules file: `.cursorrules` or `.cursor/rules/*.mdc` (from `templates/rules-file.md`; keep it ≤ 60 lines).

1. Check this Cursor version's hook support (`.cursor/hooks.json`, after-file-edit style events) in its docs.
   Verify event names and payloads — don't assume.
2. **If hooks exist:** run `python harness/hook.py` after file edits. Log one payload first; adjust
   `edited_path()` in `hook.py`. Check whether the hook output reaches the agent; if it does not, the hook
   only informs the user — then also add the mandatory-gate line (step 3).
3. **If no hooks / output not fed back:** add to the rules file:
   `MANDATORY before saying done: run python harness/gate.py <changed files>, show the output, fix line by line. After 3 failures on a file, stop and ask.`
   Tell the user this is weaker than a blocking hook.
4. RULE 1: set Cursor's agent/command approval settings to match the user's choice; otherwise RULE 1 is text-only — say so.
