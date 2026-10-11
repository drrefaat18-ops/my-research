# Claude Code Autonomous Agent Teams Setup

## Agent roles

**Opus 5.5** acts as the lead architect, scoping architecture and validating pull requests.

**Sonnet 5.5** teammates take isolated Git worktrees and implement features at medium effort.

**Haiku 5.5** swarms the peer-to-peer bus as a dedicated scout and fuzzer, stepping in at three critical moments:

1. **Before a contract locks:** Does the frontend payload match the backend schema?
2. **When a test breaks twice:** Are we patching the bug or just hiding the symptom?
3. **Before calling done:** What attack surface or edge race did everyone overlook?

**Sonnet 5.5 builds. Haiku 5.5 swarms. Opus 5.5 merges and ships.**

Jev engineering runs the identical pattern one layer down: mechanical decisions that need no reasoning (which file to open, which tool to invoke, retry or abort) execute in 16ms, so frontier models only wake up when execution paths actually diverge.

> **Plan on high. Delegate on medium. Keep Haiku 5.5 on P2P call.**

## Full team setup

- **Opus 5.5 (high):** Coordinates the session and synthesizes PRs.
- **`teammate-ux` (Sonnet 5.5):** Builds client state inside a separate Git worktree.
- **`teammate-back` (Sonnet 5.5):** Writes endpoints and handles Redis atomic locks.
- **`teammate-scout` (Haiku 5.5):** Runs invariant fuzzing and AST parsing at 340 tok/s.
- **Messaging:** All teammates communicate directly over peer-to-peer messaging without coordinator drag.
- **Coordination:** `tasks.json` manages file-level mutex locks so nobody steps on another worktree.

## Prompt to paste into Claude Code

```text
Configure my Claude Code workspace for autonomous agent teams:

1. Enable experimental agent teams in ~/.claude/settings.json:
   - Set CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS to 1 in env block
   - Set teammateMode to auto
   - Pin main lead model: opus with effortLevel: high

2. Audit ~/.claude/agents and create teammate profiles fitting ux, backend, and scout:
   - teammate-ux: model: sonnet, effort: medium, isolation: worktree
   - teammate-back: model: sonnet, effort: medium, isolation: worktree
   - teammate-scout: model: haiku, tools: Read, Grep, Glob, SendMessage

3. Configure shared task coordination in ~/.claude/CLAUDE.md:
   - Initialize tasks.json for task dependencies and atomic file mutexes
   - Teammates resolve contracts directly over peer-to-peer messaging without lead intervention
   - Enforce Haiku scout schema verification before teammates mark tasks completed

4. Quality gate:
   - Opus lead reviews synthesized worktree diffs and validates test suites before final merge

Show every configuration diff first. Do not apply edits until confirmed.
```
