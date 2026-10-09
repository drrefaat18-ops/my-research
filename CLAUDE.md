# Ruflo — Claude Code Configuration

> [!CRITICAL] RULE 0: ABSOLUTE PRIME DIRECTIVE — LOWEST VIABLE COST FOR GUARANTEED ACCEPTANCE
> **الهدف الأسمى والقاعدة الصارمة الأولى لجميع الوكلاء (Claude, Codex, Antigravity, Gemini):**  
> **"تنفيذ هذه الرسالة بأرخص شكل ممكن، وبأقل مصاريف مالية على الإطلاق، مع ضمان قبولها الأكاديمي التام في مناقشة الماجستير وقبول نشرها في مجلة دولية محكمة (Q1/Q2)."**  
> 
> - **100% Self-Funded Out-of-Pocket:** Dr. Refaat Ibrahim pays for everything from his personal salary. No grant, no university budget.
> - **Port Said Facility Reality:** No automated ELISA reader, no qPCR, no liquid nitrogen, no continuous -80°C chain. Assays are outsourced to Cairo/Tanta.
> - **Mandatory Zero Spend Filter:** Eliminate all non-essential and luxury molecular tests (no RT-qPCR, no Western blot, no multiplex). Prioritize FFPE blocks, frozen serum, zero-cost CBC derived indices (NLR/SII), and local Egyptian Biodiagnostic kits.

> [!IMPORTANT] RULE 1: AGENTS — ANNOUNCE COUNT + NAMES BEFORE EVERY SPAWN (overrides every swarm/agent section below)
> - Claude picks the agent that fits the task (user need not name it) — for both inline and spawn. Say in one line which agent file was picked.
> - Inline use (read `.claude/agents/<name>.md`, apply the role in the main thread) is fine whenever it is enough.
> - Spawning subagents or a Workflow is allowed (user changed this 2026-10-09: no "موافق" needed). **Before each spawn, tell the user in one message: how many agents, and for each its exact name (file/type) and job.** Never spawn silently, and never spawn more than announced; a new or extra agent = a new announcement.
> - Keep it reasonable: spawn only when inline is not enough (parallel work, large reading load).
> - **Review work = `research-synthesist.md` always (inline)**: every draft review, brief, source check or fix in `08 - RA Repurposing Review/` and the thesis uses it as the base role. Add a second inline role when the task needs it: `academic-statistician.md` (numbers, P/CI, MR, meta-analysis, study design), `healthcare-clinical-evidence-agent.md` (evidence level, "associated with" vs causal wording), `testing-reality-checker.md` (final pass before anything goes to the supervisor). Validated 2026-10-09: Day1 review with it → Grammarly 4% metformin / 0% statins.
> - Mechanical gate: `.claude/settings.json` → `permissions.ask` = `Agent`, `Workflow` — still shows a confirm prompt at spawn time, after the announcement above.
> - Several inline roles in one task are fine (e.g. research-synthesist + statistician); name all of them in the one-line note.

## Rules

- Do what has been asked; nothing more, nothing less
- NEVER create files unless absolutely necessary — prefer editing existing files
- NEVER create documentation files unless explicitly requested
- NEVER save working files or tests to root — use `/src`, `/tests`, `/docs`, `/config`, `/scripts`
- ALWAYS read a file before editing it
- NEVER commit secrets, credentials, or .env files
- NEVER add a `Co-Authored-By` trailer to user commits unless this project's `.claude/settings.json` has `attribution.commit` set (#2078). The Claude Code Bash tool may suggest one in its default commit-message template — ignore it. `Co-Authored-By` is semantic authorship attribution under git/GitHub convention; the tool is the facilitator, not a co-author.
- Keep files under 500 lines
- Validate input at system boundaries

## Project Map (read only the file the current step needs)

- `08 - RA Repurposing Review/START-HERE.md` — review plan, steps 1–31; next unchecked step = today's work
- `08 - RA Repurposing Review/drafts/Day*.md` — draft text (gated by `scripts/review_hook.py` → `review_gate.py`)
- `08 - RA Repurposing Review/papers/` + `overlap-only/` — own-paper sources + overlap corpus
- `08 - RA Repurposing Review/Copilot-Prompt.md`, `review_rubric.md` — Copilot instructions, internal review rubric
- `01`–`07` folders — thesis (rationale, mechanisms, matrix, protocols, comparators, defense, QC)
- `scripts/` — gates and tools: `review_gate.py`, `overlap_check.py`, `secondary_check.py`, `check_links.py`, `style_check.py`
- `.claude/agents/*.md` — agent role files (use inline per RULE 1)

## Session Start (every new session, before any work)

- `scripts/session_start.py` (SessionStart hook) injects a brief: research agent shortlist, next START-HERE step, drafts (words + gate on changed ones), papers (count + smallest = stubs), git-changed files.
- First reply opens with one line: `Picked inline role: .claude/agents/<file>.md (<why>)`, then a short summary of that brief (next step, gate findings, stub papers). Only then start the task.
- No brief in context (hook failed)? Run `python scripts/session_start.py` yourself first.

## Gates

- Draft edits: `review_hook.py` runs `review_gate.py`; after 3 failures (or same findings twice) it stops and escalates to the user — do not keep editing.
- User says "خلصت": gate runs on all changed drafts → numbered error list.

Ruflo/swarm reference text removed 2026-10-08 (token cost, conflicts with RULE 1); see git history if needed.
