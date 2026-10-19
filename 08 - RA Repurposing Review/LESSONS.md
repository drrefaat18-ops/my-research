# Lessons

Lesson ladder (harness-kit PRINCIPLES 15). Every correction or failure is logged here before it becomes a rule.

## Ladder
- **observation** - seen once. Keep it here; change nothing.
- **pattern** - seen twice in different tasks. Look for the root cause.
- **candidate** - a proposed upgrade: the smallest reusable change, plus the eval case that proves it. Waits for the user.
- **confirmed** - the user approved; enforced by a named check, and the failure is an eval case in `scripts/evals/`.

Promote only what changes future behaviour. Task-specific corrections stay under the START-HERE step.

## Upgrade review (after a failed run or a user correction)
1. Do not repair the output yet. Classify the root cause: missing instruction | missing context |
   weak procedure | missing check | bad tool contract | permission | insufficient evidence | ambiguous task.
2. Find the lesson below: new = observation; seen before = climb one rung.
3. At candidate: propose the change (file, exact lines) and the eval case. Change nothing yet.
4. After the user's yes: apply it, add the case to `scripts/evals/`, run `python scripts/evals.py`, mark it confirmed.

## Step-done line
Every START-HERE step ends with one line under it: `lesson | <what changed or what to watch>` or `lesson | none`.

## Lessons

| Lesson | Rung | Seen (date, task) | Enforced by |
|---|---|---|---|
| Evidence quote not in the paper (ESR "stayed higher") | confirmed | 2026-10-10, pipeline first run | `verify_quotes.py`, eval E001 |
| Acronym used but never defined (STAT3, STAT5) | confirmed | 2026-10-18, Day1 gate | `cite_check.py`, eval E002 |
| Claim taken from a paper's Introduction (other people's work) | confirmed | 2026-10-10, pipeline rule 5 | `secondary_check.py`, eval E003 |
| Brief link to a missing block id | confirmed | 2026-10-08, prep-work SOP | `check_links.py`, eval E004 |
| Citation tag with no paper file | confirmed | 2026-10-08, own-paper sources rule | `cite_check.py`, eval E005 |
| Parallel edits on drafts trip the gate STOP | confirmed | 2026-10, Day drafts | `review_hook.py` retry cap; one draft edit at a time |
| Evidence gathered inline instead of Haiku agents | confirmed | 2026-10, user correction | CLAUDE.md pipeline + `.claude/workflows/evidence.js`; no script check |
| Arabic and English mixed inside one sentence | confirmed | 2026-10, user preference | memory only; no script check |
| Optional kit part skipped on own cost judgement instead of asking (knowledge graph) | observation | 2026-10-18, kit update | not yet: optional kit items are asked, not dropped |
| Graph build cost 1.62M Haiku tokens for 97 files (estimate was ~1M from the kit's 93-note vault); scope glob also caught 45 full-text papers | observation | 2026-10-18, first graph build | not yet: count files and words before announcing a cost |
| `evidence` workflow got `claims` as an array of objects; the prompt showed "[object Object]", 2 Haiku agents searched nothing (~110k tokens). Bad tool contract: `evidence.js` line 30 does not check the type | confirmed | 2026-10-18, step 14 | `evidence.js` throws unless `claims` is a string; eval E006 (user delegated the yes: "اشتغل agentic") |
| Step started without an agent plan under START-HERE; source search (web) run inline. Same family as "evidence gathered inline" | pattern | 2026-10-19, step 15 (user correction) | not yet: write the agent plan under the step and announce before any search |
| Batch of draft fixes planned as one edit but sent as a partial edit; it counted as the 3rd gate failure and tripped STOP with 8 fixes still pending. Weak procedure: known-deferred findings (cross-draft acronyms) make every edit "fail", so each edit spends one of 3 tries | observation | 2026-10-19, step 15 | not yet: build the whole replacement first, then one edit; consider letting the gate ignore findings recorded as deferred |
| Acronym duplicate check counted data brackets "(95% UI …)", "(HR 0.91)" as definitions and missed plurals "(DMARDs)"; false duplicates made every Day5 edit fail. Bad tool contract | confirmed | 2026-10-19, step 15 (user: fix everything now) | `cite_check.py` first-token rule + plural match, eval E007 |
| `ledger.py` skips tags inside multi-tag brackets (`[Zhou2001; Gwinn2008]`), so Gwinn2008 shows Day1 only and "cited once" is wrong | observation | 2026-10-18, step 14 | not yet: missing check |
| Introduction summarising earlier reviews repeated Day1 numbers and a once-only source (Nallathambi2024 in Day3); ledger.py was run only after the real edit, so it cost a second draft edit | observation | 2026-10-19, step 16 | not yet: run ledger.py on the scratch copy before the real edit |
| isolate_blocks.py on a paper shifts line numbers, so earlier evidence cards for that paper failed verify_quotes (5 of 24) | observation | 2026-10-19, step 16 | not yet: renumber cards by quote after isolating (scratch script), or highlight before collecting cards |
| Section 3 opened by re-defining RA ("chronic … autoimmune … disability"), repeating the Introduction's first sentence; read as two papers. Writer drafts each Day file alone, so section openers are never compared | observation | 2026-10-19, user correction (Day4 vs Day5) | not yet: section openers must not re-define RA; only Introduction defines the disease |
| Haiku graph agent reported "chunk written and validated" (61 nodes) but no file existed; orchestrator then searched, found academy-brain's chunk in the shared root and moved it in by mistake (caught by merge: wrong source files + 6 dangling). Failed write ≠ done | observation | 2026-10-19, end-of-work graph update | not yet: check the chunk path and its source_file values before merge |
| graph_audit.py merge/publish use the shared D:/vault/_graphify-stage/graphify-out, also used by academy-brain: .graphify_root, labels, manifest and a pending chunk there belong to academy-brain; merge would ingest its chunk and then delete it, and our published graph already carries its community names ("Trainer Payroll"). Bad tool contract | confirmed | 2026-10-19, step 16 end-of-work (user: fix it) | \graph_audit.py\ stages under _graphify-stage/<project>/ and refuses a root owned by another project (.graphify_owner); eval E008 |
