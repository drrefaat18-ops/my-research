# Harness Kit

Builds a personal AI "harness" for your work: rules, step plan, memory, source ingestion, and automatic quality gates.

1. Unzip this folder into your project root (keep the folder name `harness-kit`).
2. Open your CLI AI tool in the project (Claude Code, Codex, Gemini CLI, Cursor).
3. Say: `Read harness-kit/START-HERE.md and follow it.`
4. Answer its questions. It will not build anything until you approve its design.
5. Needs Python 3.9+. Nothing else is installed without asking you first.

Afterwards you may delete `harness-kit/`; the harness lives in your project.

| File | For |
|---|---|
| `START-HERE.md` | the AI: install protocol |
| `PRINCIPLES.md` | everyone: 21 rules (map, memory, gates, retry cap, layers, lanes, failure triage, pruning) |
| `templates/*_template.py` | gate, hook, ingest, session brief, evals, edit-loop warning |
| `templates/steps-file.md`, `verifier.md`, `permission-lanes.md`, `harness-checklist.md` | step contract, reject-first verifier, lanes by reversibility, audit + prune |
