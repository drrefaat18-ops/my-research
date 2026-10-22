# Agent Pipeline Kit

A writing pipeline for source-based work (reviews, reports, theses, legal or technical briefs):
one strong model orchestrates, cheap agents gather and check evidence, one agent writes, and a
human only reviews. Every sentence ends up traceable to a verbatim quote in a source file.

Proven on a literature review (2026-10-10): 23 of 23 agent quotes matched the sources verbatim,
source overlap fell from 10.6% to 1.8%, and the pipeline caught an unsupported claim plus a summary
source whose own references did not support the sentence it was cited for.

1. Unzip this folder into your project root (keep the name `agent-pipeline-kit`).
2. Works best on top of `harness-kit` (rules file, gates, hooks). Without it, the gate step becomes a manual command.
3. Open Claude Code in the project and say: `Read agent-pipeline-kit/START-HERE.md and follow it.`
4. It interviews you, shows a design, and builds nothing until you approve.
5. Needs Python 3.9+ and a tool that can spawn sub-agents with a model choice (Claude Code: Opus, Sonnet, Haiku).

| File | For |
|---|---|
| `START-HERE.md` | the AI: install protocol |
| `PIPELINE.md` | everyone: the phases, roles and rules |
| `PROMPTS.md` | the AI: spawn-prompt templates |
| `agents/*.md` | role files to copy into `.claude/agents/` |
| `scripts/verify_quotes.py` | checks evidence quotes verbatim against sources |
