# Graph Workflow Kit

Turns a straight-line agent ("do A, then B, then C") into a graph: independent jobs fan out on a
cheap model, plain code merges them for free, skeptics verify before anything reaches you, and one
strong model judges. Built on Claude Code dynamic workflows (the `Workflow` tool, `.claude/workflows/`).

Source: "Graph Engineering with Claude: 14-Step roadmap" (@0xCodez), adapted and hardened on the
Techno Square vault harness (2026-10-16).

1. Unzip this folder into your project root (keep the name `graph-workflow-kit`).
2. Works on its own; works best on top of `harness-kit` (rules, gates) and `agent-pipeline-kit` (evidence, writer).
3. Open Claude Code in the project and say: `Read graph-workflow-kit/START-HERE.md and follow it.`
4. It interviews you, shows a design, and builds nothing until you approve.
5. Needs Python 3.9+ (the guard) and Node (optional, to syntax-check workflows). Nothing is installed.

| File | For |
|---|---|
| `START-HERE.md` | the AI: install protocol |
| `GRAPHS.md` | everyone: the rules (nodes, edges, barriers, verifiers, model tiers, cost) |
| `scripts/workflow_guard.py` | PreToolUse hook: asks before any Agent/Workflow spawn; denies agent() calls with no model or a banned one |
| `scripts/check_workflow.js` | runs a workflow file against stub agents (syntax + logic, zero tokens) |
| `workflows/diamond.js` | fan out, reduce in code, optional synthesis |
| `workflows/skeptic-panel.js` | N lenses per claim, keep by majority vote |
| `workflows/loop-until-dry.js` | unknown-size discovery that stops after K empty rounds |
| `scripts/graph_audit.py` | optional knowledge-graph audit with graphify, read-only toward the notes: stage outside the project, keep ids on update, safe merge (no lost edges), publish, gate-style findings (GRAPHS.md section 8) |
| `settings-snippet.json` | the hook and permission lines to merge into `.claude/settings.json` |
