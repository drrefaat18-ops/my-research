# Research Kit

Turns "look into this" into a research workflow that shows its work: a brief before the first query, distinct
search lanes, an evidence ledger tying every claim to an exact passage, checks for freshness, independence and
conflicts, and a report that says only what the ledger supports and labels the rest.

1. Unzip this folder into your project root (keep the name `research-kit`).
2. Works on its own; works best with `harness-kit` (gates, evals), `agent-pipeline-kit` (evidence cards, quote
   check) and `graph-workflow-kit` (parallel lanes, skeptics, targeted loops).
3. Open your AI tool in the project and say: `Read research-kit/START-HERE.md and follow it.`
4. It interviews you, shows a design, and builds nothing until you approve.
5. Needs Python 3.9+ and, for current facts, a search or fetch tool in your AI tool. Nothing is installed.

| File | For |
|---|---|
| `START-HERE.md` | the AI: install protocol |
| `RESEARCH.md` | everyone: the six stages, rules, levels, memory, evals |
| `templates/brief.md` | the research contract filled before any search |
| `templates/ledger.md` | sources, claims with status, evidence passages |
| `templates/lane-prompt.md` | prompts for primary / independent / counterevidence lanes |
| `templates/research-prompt.md` | the operator prompt (project instructions or system prompt) |
| `templates/evals.md` | seven traps and six scoring dimensions |
| `scripts/ledger_check.py` | the ledger gate: support, sources, freshness, independence, report tags |
