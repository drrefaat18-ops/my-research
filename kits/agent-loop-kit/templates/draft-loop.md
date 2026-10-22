<!-- TEMPLATE: draft loop in one prompt (LOOPS 7-10). Install fills {{MAX_TRIES}} and {{CHECK_COMMAND}}; [brackets] per use. -->
Work in a loop on the goal below. Do not stop early.

GOAL: [exactly what to produce]

CRITERIA (measurable, no soft passes):
- [criterion 1]
- [criterion 2]
- [criterion 3]

EACH PASS:
1. DRAFT - produce or improve the work.
2. SCORE - rate each criterion 1-10, harshly. This score only picks the next fix.
3. GAPS - list exactly what is still weak.
4. CALL - every score >= 8 -> write READY FOR CHECK and stop. Otherwise write NEXT PASS and fix the single
   weakest gap, changing only the lines it needs.

RULES:
- Keep a one-line record per pass: pass number, weakest gap, what changed.
- After {{MAX_TRIES}} passes, or the same weakest gap twice, stop and report what still fails.
- No questions. Make a reasonable assumption, note it, continue.
- READY FOR CHECK is not done. Done = `{{CHECK_COMMAND}}` passes, or a fresh checker that sees only the output says keep.
