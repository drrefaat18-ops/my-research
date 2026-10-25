# Harness Principles

The model is the CPU; the context window is RAM; the harness is everything else — files, rules,
checks, memory. When an AI keeps failing, fix the harness, not the adjectives in the prompt.

1. **Budget comes from the user.** RULE 0 = lowest cost that still meets the user's goal, using *their* numbers.
   *Why:* the AI cannot see the bill; unbounded agents and retries burn limits silently.
2. **Map, not encyclopedia.** The rules file is short and points to files; read only what the current step needs.
   *Why:* everything in the rules file is paid for on every message and dilutes attention.
3. **Memory lives in files.** Decisions, preferences, open issues → memory files. Chat is scratch.
   *Why:* sessions end, contexts reset, models change; files survive all three.
4. **Sensors before autonomy.** Every quality that matters gets a script that measures it.
   *Why:* asking the model "are you sure?" makes it confirm its own bias; a script gives ground truth.
5. **Dual encoding.** Every hard rule is written in the rules file AND enforced by a gate, hook, or permission.
   *Why:* text rules get skipped under load; a gate does not.
6. **Retry cap.** After N failed gate runs (default 3) on one file, or identical findings twice, stop, show findings, wait for the human.
   *Why:* a fix loop that does not converge only spends budget.
7. **Writer ≠ reviewer.** The pass that produces never judges itself; the gate and a separate review pass judge.
   *Why:* a model defends its own draft; a separate adversarial pass attacks it.
8. **Bounded steps.** Each step states deliverable, non-goals, acceptance criteria.
   *Why:* without a contract, the AI decides when it is finished — usually early.
9. **Agent policy is the user's.** Use agents exactly as the user chose; name the agent before using it; ask before deviating.
   *Why:* agents multiply cost and hide work from the user.
10. **Fix locally.** Fix the flagged line or sentence; never regenerate the whole unit.
    *Why:* regenerating fixes one error and silently introduces others.
11. **No fact without a source.** Every factual claim links to an anchor in `sources/md/`, or is marked `[unverified]`.
    Ingestion is checked three ways: *provenance* (claims carry links), *links* (each link resolves to a real anchor),
    *conversion* (no empty or truncated source).
    *Why:* model memory is plausible, not reliable; a link lets anyone check the claim in seconds.
12. **Originals are read-only.** `sources/raw/` is never edited; conversions are regenerated from it.
    *Why:* a corrupted source silently corrupts every claim built on it.
13. **Orient before acting.** Every session starts with a script-made brief (agent pick, current step, gate state, suspect sources) and the AI states its agent pick in one line before working.
    *Why:* a fresh session knows nothing; without a brief it guesses the task and skips the state the last session left.
14. **Failures are test cases.** Every real failure becomes a case in `harness/evals/` (the bad input plus what the
    check must say); every harness change replays them all, and step-done fails on a regression.
    *Why:* "it feels better now" is not evidence; old failures are the only stable yardstick, and they come back silently.
15. **Corrections climb a ladder.** A correction is logged as an observation; seen twice it is a pattern; a proposed
    smallest reusable fix is a candidate; the user's yes makes it a confirmed rule with a named check and an eval.
    Every step ends with a `lesson |` log line (or `lesson | none`).
    *Why:* a correction left in chat is lost at session end; promoting every preference makes the system rigid.
16. **Audit the links, not only the lines.** Gates check one file at a time; once the notes pass a few dozen, run a
    periodic cross-note audit (a knowledge graph, see `graph-workflow-kit` GRAPHS.md section 8) for unsourced links,
    legacy facts linked as current and one entity under several names. Its findings go through the normal fix path.
    *Why:* a claim can be correct in each note and still wrong between notes; no per-file check sees that.
17. **Find the broken layer first.** Wrong job = prompt. Fluent but wrong or stale = context. Says done without proof,
    acts unsafely, forgets between sessions = harness. Repeats itself = loop. Agents collide or duplicate work = graph.
    *Why:* a longer prompt only fixes the first layer; most failures live lower and survive every rewrite.
18. **Lanes by reversibility, enforced outside the model.** Reversible (read, search, test, edit a working copy) runs
    free with a trace; outward-facing (send, deploy, pay, publish) needs the user's yes; hard to undo (delete data,
    rotate secrets, force-push the main line) is a closed lane, not a high threshold. See `templates/permission-lanes.md`.
    *Why:* a sentence in a prompt is a wish; a permission is a wall, and thresholds get lowered when someone is in a hurry.
19. **Classify a failure before retrying it.** Timeout: pause, then retry. Bad arguments: repair the call. Missing
    information: fetch it. Check failure: change the work, never the check. Permission denied: ask the user.
    Same failure twice with nothing changed: stop and write down what was tried.
    *Why:* "try again" pays repeatedly for the same mistake; each class has its own cheap fix.
20. **Watch for edit loops.** Many edits to one file in one session (default 5) raise a warning to step back and
    re-plan; it warns, it does not block (`templates/edit_loop_template.py`).
    *Why:* an agent in a loop makes small variations of the same edit and cannot see that the plan is wrong.
21. **Every rule traces to an incident; prune the rest.** Each line in the rules file names the failure behind it
    (in the line, its *Why:*, or the lessons file). On a model change, or every {{PRUNE_EVERY}}, run
    `templates/harness-checklist.md` and delete rules and checks that no longer catch anything.
    *Why:* a rule with no incident costs attention on every message; parts of a harness make up for weaknesses newer
    models no longer have, and an unpruned harness becomes the next thing to debug.
