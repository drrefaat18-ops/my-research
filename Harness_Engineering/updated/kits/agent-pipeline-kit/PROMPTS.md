# Spawn Prompts

Fill `{{…}}`. Every spawn is announced to the human first (count, names, models, jobs).
All prompts start with: "Do not create or edit any file. Return text only."

## Evidence (Haiku, one per 4–6 sources, run in parallel)
```
Do not create or edit any file. Return text only.
Read and apply your role: {{ROLE_DIR}}/evidence-extractor.md
Sources (read each fully): {{SOURCES_DIR}}/{{Tag1}}.md, … {{TagN}}.md
Facts to find, per source: {{one line per fact, with the number you expect so MISMATCH can fire}}
Output the cards, then the `Tag | line | exact quote` block.
```

## Verify (orchestrator, no agent)
```
python scripts/verify_quotes.py cards.txt "{{SOURCES_DIR}}"
```
OK = keep · MOVED = fix line · FAIL / UNREADABLE = drop the card or re-ask.

## Writer (Sonnet, effort high, ONE per section)
```
Do not create or edit any file. Return text only.
1. Read and adopt your role: {{ROLE_DIR}}/writer.md
2. Read the style rules it points to.
3. Read the brief: {{BRIEF_FILE}} — only {{section/sentences}}.
4. Read the context: {{DRAFT_FILE}} lines {{a–b}}.
VERIFIED EVIDENCE CARDS (use nothing else):
{{paste verified cards, with notes such as "source says X, not Y"}}
Return per sentence: number, sentence, card lines; or CANNOT WRITE: reason.
```

## Fix round (resume the SAME writer; max 3 rounds)
```
Fix attempt {{k}} of 3. Return revised text only.
{{per finding: what matched / what is too long / which tag is missing, and the rule to apply}}
```

## Checks (Haiku)
```
Do not edit any file. Read and apply {{ROLE_DIR}}/checker.md.
Work dir: {{DIR}}. Run: {{gate command}}; {{secondary/citation check}}; {{link check}}; {{ledger}}.
Number match for sentences tagged {{tags}} in {{DRAFT_FILE}} lines {{a–b}}; calculated values: {{list}}.
Blockers = findings in lines {{a–b}} only.
```

## Source hunt (Haiku, on demand)
```
Do not create or edit any file. Read and apply {{ROLE_DIR}}/evidence-extractor.md.
Sentence that needs a primary source: "{{sentence}}". Current citation {{Tag}} is second-hand.
1. Find the references it cites for this claim (its reference list, or the publisher/PMC page).
2. For each: full citation, DOI/PMID/PMCID, free full text?, verbatim abstract quote, supports the sentence (yes/partly/no)?
3. Or search {{years}} for original studies meeting: {{criteria in priority order}}.
Rank up to 5. NOT FOUND / UNREADABLE when a step fails.
```
Then the orchestrator re-fetches each ID (e.g. Europe PMC REST) before showing the human.
