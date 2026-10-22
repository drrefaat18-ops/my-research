# Loop Rules

**An agent has a goal, not an instruction. A loop makes it reliable. A check that can fail makes it a loop.**

## Agents
1. **Know the level you run at.** 1 chat (you are the engine) -> 2 tools (it fetches what it needs) -> 3 multi-step
   (goal in, finished output out, you are not in between) -> 4 unattended (schedule or trigger, you read the result).
   *Why:* the model is the same at every level; what moves you up is what surrounds it. Add one piece at a time.
2. **An agent = tools + memory in files + a loop that runs to done.** Missing one, it is a chat with extras.
   *Why:* without tools it waits for you, without memory it repeats itself, without a loop it hands back every step.
3. **Give each agent one job and its rules in the system prompt** (`templates/agent-*.md`): what to do, in which
   order, what to refuse, what to say when it cannot find the answer.
   *Why:* the system prompt is read at the start of every session; a rule said once in chat falls out of context.
4. **Facts the agent always needs go in the system prompt or rules file; everything else is a file it reads on demand.**
   *Why:* the always-loaded text is paid for on every message; keep it short (`harness-kit` PRINCIPLES 2).

## Memory
5. **The agent writes its own memory.** Mid-task, long session and new session: the Checkpoint, Compress and Resume sections of `templates/checkpoint.md`
   (Resume gets the last checkpoint pasted in). Checkpoints live in `{{HANDOFF_FILE}}`, not chat.
   *Why:* long tasks drop the goal out of context, closed sessions start from zero, interrupted ones forget where
   they stopped. One fix covers all three: a short, specific record on disk.

## Loops
6. **Build a loop only when all four hold:** it repeats regularly; the result can be graded without a human; it
   runs from goal to result with no human step in the middle; "done" is a fact, not a feeling.
   *Why:* miss one and the loop costs more than doing the task by hand.
7. **The check must be able to fail:** a test that passes or not, a score against a threshold, a rubric with hard
   criteria, a gate script (`{{CHECK_COMMAND}}`).
   *Why:* without a real check the loop produces drafts and calls them done.
8. **Self-scoring drafts, it never declares DONE.** The draft loop (`templates/draft-loop.md`) may score itself to
   choose the next fix; the final pass/fail comes from a script or from a checker with a fresh context that sees
   only the output (`graph-workflow-kit` skeptic panel).
   *Why:* the reasoning that made a mistake is the reasoning checking for it; a writer grading itself is lenient.
9. **Two exits, always:** the check passes, or the cap is hit (`{{MAX_TRIES}}` tries) -> stop and report what failed.
   Same findings twice -> stop early.
   *Why:* a loop that cannot solve the problem keeps spending until something stops it.
10. **Keep a record of what already ran** (attempt, what failed, what changed) and fix the weakest gap first, one
    per pass, locally.
    *Why:* without the record it retries what failed; regenerating the whole output fixes one error and adds others.
11. **Build in this order:** run it by hand in one session until it works -> save it as a template -> add the check
    and the cap -> only then schedule it.
    *Why:* what is unreliable by hand fails faster and costs more on a schedule.
12. **Count kept outputs, not tokens.** Every pass resends a context that grows. Log each run as kept or discarded
    in `{{LOG_DIR}}` and run `scripts/keep_rate.py`; below `{{KEEP_RATE_MIN}}` (default 0.5, a rule of thumb) fix the
    check or go back to doing it by hand.
    *Why:* ten runs to keep four is a bill for ten; the keep rate is the one number that says the loop earns its cost.

## Graphs
13. **When the work splits into independent jobs, use a graph, not a longer loop:** `graph-workflow-kit` (fake-edge
    test, diamond, skeptic panel, loop until dry). Describe the graph to the real workflow tool; a YAML block in a
    prompt is a description, not an executor.
    *Why:* parallel jobs only run in parallel when something actually runs them.
