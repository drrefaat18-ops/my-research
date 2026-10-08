# Harness Kit — Design Spec

**Date:** 2026-10-08
**Status:** Draft, awaiting user review
**Output folder:** `Harness_Engineering/harness-kit/` (self-contained; user zips and sends it)

## 1. Purpose

A portable folder that any CLI AI coding tool (Claude Code, Codex, Gemini CLI, Cursor) can read to **design and build a personal harness for whatever work its user does** — not only research. The AI must interview the user and get approval before building anything.

Success = a colleague unzips the folder into their project, tells their CLI tool `Read harness-kit/START-HERE.md and follow it`, answers a short interview, approves a design, and ends with a working harness: rules file, steps file, memory, ingested sources, and tested Python gates wired to their tool.

## 2. Constraints

- Language: English (AI-facing). The AI talks to the user in the user's language.
- Target: CLI tools that read files and run commands. No chat-only support.
- No personal content from the origin project (no names, paths, thesis details).
- Python stdlib only for kit code. Extra libraries only after the user approves by name.
- Every generated file under 500 lines; the rules file under 60 lines.

## 3. Folder layout

```
harness-kit/
  README.md                 human-facing, ~10 lines: unzip, open CLI, say the start sentence
  START-HERE.md             AI-facing protocol: 5 phases with hard gates
  PRINCIPLES.md             the rules + one-line "why" each; AI consults while designing
  templates/
    rules-file.md           skeleton for CLAUDE.md / AGENTS.md / GEMINI.md / .cursorrules
    steps-file.md           step skeleton: deliverable, non-goals, acceptance criteria
    memory/INDEX.md         memory index skeleton
    memory/_example.md      one-fact-per-file format (frontmatter: name, description, type)
    gate_template.py        sensor skeleton: file in → numbered findings → exit 0/1
    hook_template.py        tool hook: runs gate after edits, retry cap, escalation
    ingest_template.py      source converter skeleton with provenance + anchors
    hooks/claude-code.json  PostToolUse / UserPromptSubmit / permissions.ask wiring
    hooks/codex.md          how to wire gates in Codex (or "mandatory command" fallback)
    hooks/gemini-cli.md     same for Gemini CLI
    hooks/cursor.md         same for Cursor
```

## 4. START-HERE.md — the protocol

The AI must not skip or merge phases. Each phase ends by waiting for the user.

**Phase 1 — Interview** (one question per message, multiple choice where possible):
1. What is the work, and what does the finished deliverable look like?
2. Budget: money, usage limits, time. → becomes RULE 0 (lowest cost that still meets the goal).
3. Agents: how do you want them used? (inline only / spawn with per-agent approval / free / other) → becomes RULE 1 + mechanical gate where the tool supports it.
4. Sources of truth: what are they, where do they live, what formats? Where must a fact trace back to (page, paragraph, row)?
5. Failure modes: what mistakes happened before or worry you? → each becomes one gate check.
6. Forbidden: what must the AI never touch or do?
7. Done: how do we know a step / the whole work is finished? → acceptance criteria.
8. Environment: which CLI tool, OS, is Python installed?

**Phase 2 — Write-back:** short note separating "you said" from "I assume". Wait for corrections.

**Phase 3 — Design:** list every file to be created, every gate check (what it catches, how), ingestion plan (formats → converter → library choice), agent policy. Wait for approval.

**Phase 4 — Build:** fill templates, write gate/ingest scripts, wire hooks. Library installs: name each, ask, then install.

**Phase 5 — Prove:** for each gate check, run it on one passing and one failing example and show output; confirm the hook blocks on failure and the retry cap escalates. Ingest one real source end-to-end. Then hand over with a one-screen summary of how to use the harness.

## 5. PRINCIPLES.md — the rules

Each with a one-line reason:
1. **Budget comes from the user** — RULE 0 is their number, not the AI's guess.
2. **Map, not encyclopedia** — rules file is short; it points to files, the AI reads only what the step needs.
3. **Memory lives in files** — chat is scratch; decisions, preferences, open issues go to memory files.
4. **Sensors before autonomy** — a quality the AI cannot measure is a quality it cannot keep.
5. **Dual encoding** — every hard rule is written in text AND enforced by a gate/permission.
6. **Retry cap** — 3 failed gate runs, or identical findings twice, → stop, show findings, wait for the human.
7. **Writer ≠ reviewer** — the pass that produces is not the pass that judges; the gate and a separate review pass judge.
8. **Bounded steps** — every step has deliverable, non-goals, acceptance criteria.
9. **Agent policy is the user's** — whatever they chose in Phase 1; ask before deviating.
10. **Fix locally** — fix the flagged sentence/line, never regenerate the whole unit.
11. **No fact without a source** — claims cite an ingested source anchor, or are marked "unverified".

## 6. Source ingestion layer

- `sources/raw/` — originals, never edited.
- `sources/md/` — one markdown file per source. Header: source, original path/URL, date ingested, type, content hash. Body anchored per page/paragraph/row (e.g. `^p12-3`) so links resolve to an exact location.
- `ingest_template.py` behaviour: convert, write header, add anchors, skip unchanged files (hash), print a report of failures and empty/short outputs (never silently skip).
- Library choice offered to the user in Phase 3:
  - **one broad tool** (`markitdown`) — single install, all formats;
  - **per-format libraries** (`pymupdf`, `python-docx`, `openpyxl`) — lighter, keeps page numbers more precisely.
  - Stdlib formats (txt, md, html, csv, xml, json) always convert without installs.
- Ingestion gates:
  - **provenance check** — every claim in the work carries a link to a `sources/md` anchor; unlinked claims are findings.
  - **link check** — every link resolves to an existing file and anchor.
  - **conversion check** — output not empty; size/page count plausible versus the original.

## 7. Gate + hook contract

- `gate_template.py`: CLI `python gate.py <file>...`; prints numbered findings `file:line: rule: message`; exit 0 pass / 1 fail. One function per check, registered in a list, so the AI adds checks from Phase 1 failure modes.
- `hook_template.py`: reads the tool's hook event JSON from stdin; after an edit to a gated path runs the gate; on failure exits 2 with findings (fed back to the AI); keeps a per-session, per-file failure counter in the OS temp dir; resets on pass; at the cap prints a STOP message instructing the AI to show findings and wait. A crash in the hook never blocks the session (exit 0 with a warning).
- Tools without hooks: the rules file states the gate command is mandatory before saying "done"; the spec marks this as weaker than a hook.

## 8. Testing (of the kit itself, before handover to the user)

- `gate_template.py` and `hook_template.py` each carry an `assert`-based self-check runnable with `python <file> --selftest`.
- `ingest_template.py` self-check converts a small inline txt/csv/html sample and verifies header + anchors.
- Dry run: walk the protocol on one non-research example (e.g. a small coding or translation project) and confirm every phase gate stops the AI.

## 9. Non-goals

- No chat-only (web UI) support.
- No GUI, no installer, no dependency manager.
- No copy of the origin project's scripts or content; templates are rewritten generically.
- No multi-agent orchestration framework; agent use is whatever the user chooses.
