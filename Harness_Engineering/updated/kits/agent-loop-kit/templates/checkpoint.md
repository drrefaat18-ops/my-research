<!-- TEMPLATE: memory prompts (LOOPS 5). Install fills {{HANDOFF_FILE}}. Three prompts; use the one that fits. -->
## Checkpoint (mid-task)
Before we continue, write a checkpoint to {{HANDOFF_FILE}}:
1. What is complete?
2. Which decisions were made, and why?
3. What still needs to happen, in order?
4. What would a new session need to resume (files, commands, open questions)?
Under 150 words. Specific: file names, numbers, ids. A vague checkpoint is useless.

## Compress (long session)
This session is getting long. Write to {{HANDOFF_FILE}}: the original goal; what was done and found; key decisions;
what still needs to happen. Then continue from that summary as the new starting point.

## Resume (new session)
We are resuming. Read {{HANDOFF_FILE}}. Confirm in three lines where we are and what the next step is, then
continue without repeating finished work.
