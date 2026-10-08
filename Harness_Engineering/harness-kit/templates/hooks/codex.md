# Wiring the gate in Codex CLI

Rules file: `AGENTS.md` (from `templates/rules-file.md`).

1. Check whether this Codex version supports hooks: read its docs / `codex --help` / config reference.
   Hook support and field names change between versions — verify, don't assume.
2. **If hooks exist:** register `python harness/hook.py` to run after file edits and on user prompts.
   Confirm what the event JSON looks like (log one event to a file first) and adjust `edited_path()`
   in `hook.py` if the field names differ. Confirm a non-zero exit actually reaches the model.
3. **If no hooks:** put this line in `AGENTS.md` under Gates, and tell the user this is weaker than a hook:
   `MANDATORY before saying done: run python harness/gate.py <changed files>, show the output, fix line by line. After 3 failures on a file, stop and ask.`
4. **Session start:** if Codex has a session-start hook, run `python harness/session_start.py --plain` there and confirm its stdout reaches the model. If not, add to `AGENTS.md` under Session start: `MANDATORY first command of every session: python harness/session_start.py --plain`.
5. Agent policy (RULE 1): if Codex has an approval/sandbox mode that gates sub-tasks or commands, set it to match the user's choice; otherwise RULE 1 is text-only — say so.
