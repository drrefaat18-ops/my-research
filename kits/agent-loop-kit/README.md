# Agent Loop Kit

Moves an AI tool from chat to agent: one-job system prompts, memory the agent writes to disk, and loops that stop
only when a real check passes or a cap is hit, with a keep-rate count that says whether a loop is worth its cost.

1. Copy this folder into your project root (keep the name `agent-loop-kit`).
2. Works on its own; best with `harness-kit` (gates, retry cap) and `graph-workflow-kit` (parallel jobs, skeptics).
3. Open your AI tool in the project and say: `Read agent-loop-kit/START-HERE.md and follow it.`
4. It interviews you, shows a design, and builds nothing until you approve.
5. Needs Python 3.9+. Nothing is installed.

| File | For |
|---|---|
| `START-HERE.md` | the AI: install protocol |
| `LOOPS.md` | everyone: 13 rules (agent levels, memory, when a loop pays, checks, caps, keep rate) |
| `templates/agent-research.md`, `agent-data.md`, `agent-code.md` | one-job agent system prompts |
| `templates/draft-loop.md` | a loop in one prompt that ends at READY FOR CHECK, not DONE |
| `templates/checkpoint.md` | checkpoint, compress and resume prompts |
| `scripts/keep_rate.py` | kept / runs per loop from log lines; flags loops below the threshold |
