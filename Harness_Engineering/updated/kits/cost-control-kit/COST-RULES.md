# Cost Rules

A bill is price times volume. A cheaper token never makes a long session short; fewer tokens is the part you control.
Four meters run at once: **input** (read fresh), **output** (written, thinking included), **cache write** (stored
for reuse), **cache read** (reused). Each rule below attacks one of them.

1. **Measure one real session before changing anything.** Record total, the four-meter split, and how many
   corrections the output needed (`templates/baseline.md`, `scripts/cost.py`).
   *Why:* the dominant meter differs per workload; fixing the wrong one saves nothing.
2. **The tool's dollar figure is an estimate; the vendor's billing page is the number.**
   *Why:* local estimates use list price and miss discounts, credits and caps.
3. **Effort starts at the model's default and goes up one task at a time, on evidence.** Know the override order
   (environment variable > flag/session command > saved setting > model default) and check the variable first.
   *Why:* thinking is billed as output, the most expensive meter; a stray variable silently outranks every saved setting.
4. **Search and summary agents run on the cheapest tier, read-only.** Override the tool's built-in search agent by
   its exact name, not with a new one beside it. An agent with no model field inherits the main session's model.
   *Why:* a file search does not need the top tier; a cheap model with write tools costs more in rework than it saves.
5. **Match the model to the job.** Mid tier for routine turns; top tier for architecture and multi-step reasoning;
   above-top only after the top tier failed. An advisor pattern (cheap main, strong advisor at decision points)
   is measured, not assumed.
   *Why:* every advisor call re-reads the whole conversation uncached; if it fires every turn the saving is gone.
6. **Shrink what is resent.** Clear between unrelated tasks; compact only while the cache is warm and say what to
   keep; keep the always-loaded rules file short and move workflow detail into on-demand skills; disable unused
   tool servers; write specific prompts and stop a wrong direction at once.
   *Why:* every request carries the whole conversation; a one-line question late in a long session pays for all of it.
7. **Filter noisy command output before the model reads it, and keep the exit code.** Rewrite only an exact, bare
   command (no `; & | $` quotes or newlines); save the full log to disk and say where.
   *Why:* `cmd | head` reports head's status, so a failing run looks green; a prefix match would auto-approve
   whatever is chained after it.
8. **Keep the cache warm.** Pick the model at session start; do not resume a huge idle session with a one-line
   question; read the cache-hit line in the usage report and chase the cause it names.
   *Why:* rewriting a cached context costs many times reading it; long pauses, model switches, compaction,
   speed-mode toggles and changed tool definitions all force a rewrite.
9. **Pay for speed or discount only on purpose.** Fast mode for a short sprint, then off; batch for work that can wait.
   *Why:* fast mode multiplies every meter; left on overnight it doubles a whole day.
10. **Find the spenders that run while you are away:** scheduled tasks, loops, goal check-ins, cross-session
    messages, sub-agents, agent teams, background daemons. Each firing resends the full context.
    *Why:* nobody is at the keyboard to notice; the usage report's attribution rows are the only witness.
11. **Put a hard ceiling on unattended runs** (budget cap + max turns) and a spend limit on shared accounts.
    *Why:* lowering spend is steering; only a limit is a seatbelt. Caps check an estimate, so leave headroom.
12. **(Optional) Move fixed-choice decisions off the top tier.** A call qualifies when every valid answer can be
    listed in advance, a person would settle it at a glance, and it runs often. Shadow-run at least 30 real past
    cases and explain every disagreement before switching.
    *Why:* a decision model can be confidently wrong; vendor accuracy claims are claims.
13. **Prove each change on one checkable task.** Fresh session, same prompt, same acceptance check; change exactly
    one thing; run each side twice; keep it only if cost fell and corrections did not rise.
    *Why:* rework is cost, and a single run is noise. Repricing the same tokens on another model is arithmetic,
    not a forecast; models spend different token counts on the same task.

**Will not do:** make a hard task easy. If a task needs the top tier at high effort, lowering either moves the cost
from the bill to your afternoon.
