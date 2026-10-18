# START HERE — Harness Build Protocol (for the AI)

You are building a **harness** for this user's work: the files, rules, memory, source ingestion and
automatic checks that keep you reliable over a long project. The work can be anything (research,
code, translation, legal, teaching, business). Read `PRINCIPLES.md` now; read templates only when
Phase 4 needs them.

## Hard rules for this protocol

- Five phases, in order. Never skip or merge phases. Each phase ends by **stopping and waiting** for the user.
- Talk to the user in their language. Files you generate are in English unless they ask otherwise.
- Ask **one question per message**, multiple choice where possible, with your recommendation first.
- Do not create, install, or modify anything before Phase 4 approval. Reading the project is allowed.
- Install nothing without naming the package and getting a yes.
- Spawning sub-agents during this protocol: not allowed until the user's agent policy (Q3) exists, then follow it.

## Phase 1 — Interview

Skim the project first (folder tree, existing rules files) so you don't ask what you can see.
Then ask, one at a time (skip any the project already answers, and say so):

1. **Work:** What is the work, and what does the finished deliverable look like (file, format, size, audience)?
2. **Budget:** What can this cost — money, usage/token limits, time, deadline? → RULE 0.
3. **Agents:** How should sub-agents be used? (a) inline only — you read agent role files and act in this session; (b) spawn only after per-agent approval, naming the agent first; (c) free use within budget; (d) other. Who picks the agent — you per task, or the user? → RULE 1.
4. **Sources of truth:** What are they (papers, specs, contracts, datasets, web pages…), where do they live, what formats? Where must a fact trace back to — page, paragraph, row, timestamp?
5. **Failure modes:** What mistakes have AI tools made on this work before, or what worries you most? (Get concrete examples.) → each one becomes a gate check.
6. **Forbidden:** What must never be touched, changed, deleted, or sent anywhere?
7. **Done:** How do we know one step is finished? The whole work? → acceptance criteria.
8. **Environment:** Which CLI tool, OS, Python version? (Run `python --version` yourself if you can.)

## Phase 2 — Write-back

Send a short note:
- **You said:** facts from their answers.
- **I assume:** everything you inferred. Mark each clearly.
- **Open questions:** anything still unclear.

Stop. Apply corrections. Repeat until they confirm.

## Phase 3 — Design

Present, in chat, compactly:
1. **Files** to create, each with a one-line purpose (from `templates/`): rules file (name matches their tool: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.cursorrules`), steps file, memory folder, `sources/`, `harness/` scripts.
2. **RULE 0** text (budget) and **RULE 1** text (agents) in their words.
3. **Gate checks:** one per failure mode — what it catches, how (regex, count, compare, run tests…), which files it gates. Include the ingestion checks (§ PRINCIPLES 11).
4. **Ingestion plan:** formats → converter → install choice. Offer both:
   - one broad tool: `markitdown` (single install, all formats);
   - per-format libraries: `pymupdf` (PDF, exact pages), `python-docx`, `openpyxl` — lighter, more precise anchors.
   Stdlib formats (txt, md, html, csv, xml, json) need no install.
5. **Wiring:** how gates attach to their tool (`templates/hooks/<tool>`). If the tool has no hooks, say plainly that the gate becomes a mandatory command and is weaker.
   Include the **session-start brief** (PRINCIPLES 13): which agent files go in the shortlist, the opening line, and the session-start event it hooks to (or a mandatory first command if the tool has none).
6. **Flywheel** (PRINCIPLES 14-15): the first eval cases (one per Phase 1 failure mode, from the user's real
   examples), where the lesson ladder lives, and the step-done rule (gate + `lesson |` log line + evals replay).
7. **Retry cap:** default 3 failures or identical findings twice → stop and escalate. Ask if they want a different number.

Stop. Build only after an explicit yes. A yes to an earlier phase is not a yes to this one.

## Phase 4 — Build

Use the templates; replace every `{{PLACEHOLDER}}`; delete template guidance comments marked `TEMPLATE:`.
- Rules file ≤ 60 lines: RULE 0, RULE 1, short rules, project map, gates. Map, not encyclopedia.
- Steps file: every step has deliverable, non-goals, acceptance criteria.
- `memory/`: index + one fact per file. Seed it with Phase 1 decisions.
- `harness/gate.py` from `gate_template.py`: one `check_*` function per failure mode.
- `harness/ingest.py` from `ingest_template.py`: converters for their formats only.
- `harness/session_start.py` from `session_start_template.py`, wired to the tool's session-start event.
- `harness/hook.py` from `hook_template.py`, wired per `templates/hooks/<tool>`. Verify the tool's
  current hook format against its docs or `--help` before wiring; hook APIs change.
- `harness/evals.py` from `evals_template.py`, plus one case per Phase 1 failure mode in `harness/evals/`;
  `LESSONS.md` from `lessons-file.md`; the step-done check calls `evals.main(quiet=True)` and requires a `lesson |` log line.
- Ask before each install, naming the package.

## Phase 5 — Prove

Show real output for each, not a claim:
1. `python harness/gate.py --selftest`, `python harness/ingest.py --selftest`, `python harness/hook.py --selftest`, `python harness/session_start.py --selftest`, `python harness/evals.py --selftest`, then `python harness/evals.py` (every case passes).
2. Every gate check on one passing and one failing example.
3. Ingest one real source from the user; open a generated anchor link and confirm it lands on the right text.
4. Trigger the hook with a failing edit: confirm it blocks, and that the retry cap escalates.
5. Run `python harness/session_start.py --plain` and show the brief; tell the user the hook fires from the next session, whose first reply must open with the agent-pick line.

Then hand over a one-screen guide: daily loop, which command does what, how to add a check, how to add a source.
If anything failed, say so with the output; do not hand over a harness with an unproven gate.
