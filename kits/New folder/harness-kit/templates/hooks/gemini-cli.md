# Wiring the gate in Gemini CLI

Rules file: `GEMINI.md` (from `templates/rules-file.md`).

1. Check this Gemini CLI version's hook support in its docs (settings.json `hooks`; after-tool and
   before-prompt style events). Names and payloads change between versions — verify, don't assume.
2. **If hooks exist:** register `python harness/hook.py` on the after-file-write/edit event and on the
   user-prompt event. Log one event payload to a file first; adjust `edited_path()` in `hook.py` to its
   field names. Confirm a blocking exit code (often 2) returns the stderr text to the model.
3. **If no hooks:** add the mandatory-gate line to `GEMINI.md` (see `codex.md` step 3) and tell the user it is weaker.
4. **Session start:** if Gemini CLI has a session-start hook, run `python harness/session_start.py --plain` there (log one payload; confirm stdout reaches the model). If not, add the mandatory first-command line to `GEMINI.md` (see `codex.md` step 4).
5. RULE 1: use the CLI's tool-approval settings to require confirmation for sub-agent/extension tools if the user chose approval; otherwise RULE 1 is text-only — say so.
