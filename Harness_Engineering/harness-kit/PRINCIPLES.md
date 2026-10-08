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
