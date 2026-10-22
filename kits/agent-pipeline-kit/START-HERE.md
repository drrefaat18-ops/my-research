# START HERE — Agent Pipeline Install Protocol (for the AI)

You are installing a multi-agent writing pipeline into this project. Read `PIPELINE.md` now; read
`PROMPTS.md` and `agents/` only in Phase 3.

## Hard rules for this protocol
- Four phases, in order. Each ends by stopping and waiting for the user.
- Talk to the user in their language; one question per message, your recommendation first.
- Create nothing before Phase 3 approval. Spawn no agent before the Phase 4 pilot, and announce it first.
- If the project has a harness (rules file, gate scripts, hooks), plug into it; do not duplicate it.

## Phase 1 — Interview (skip what the project already answers, and say so)
1. **Work:** what is written (review, report, brief…), for whom, in which language? Where do drafts live?
2. **Sources:** where are they, in what format, with line-addressable text (markdown)? If not, how are they converted? Which stable ID do they carry (DOI, case number, URL…)? What must every evidence card record (date, party, n…)?
3. **Brief:** does a per-sentence plan exist before writing (ideas, required wording, exclusions)? Where?
4. **Style rules:** is there one file of writing rules? If not, collect them into one.
5. **Checks:** which scripts or commands judge a draft (overlap, citations, style, links)? Which hook runs them?
6. **Budget & agents:** usage limits; may sub-agents be spawned; any model limits? (Default: Opus orchestrates, Haiku reads/checks, one Sonnet writes.)
7. **Citation format:** how are sources tagged in text, e.g. `[Author2024]`?

## Phase 2 — Design (in chat, compact)
- Roles table filled for this project (agent → model → role file → job), sizing rule.
- Phase list adapted (which gate command in phase 5–6, where notes go).
- Files to create: `.claude/agents/` role files (from `agents/`, placeholders filled), `scripts/verify_quotes.py`, a pipeline section (≤ 12 lines) in the rules file.
Stop. Build only after an explicit yes.

## Phase 3 — Build
- Copy role files; replace every `{{…}}`; the writer points to the ONE style-rules file.
- Copy `scripts/verify_quotes.py`; run `python scripts/verify_quotes.py --demo` and show the output.
- Add the pipeline section to the rules file, pointing to `PIPELINE.md`'s phases.

## Phase 4 — Pilot (prove it on one small real unit, 4–6 sentences)
Run phases 1–9 for real, announcing each spawn. Show the human:
1. `verify_quotes.py` result (target: all OK).
2. Gate findings before and after the fix round.
3. The review table: sentence → quote → source link.
4. Usage: sub-agent tokens per role.
Report failures as they happened. Hand over a one-screen guide: how to start a section, what the human reviews, where notes go.
