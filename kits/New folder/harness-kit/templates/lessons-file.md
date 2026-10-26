# Lessons

TEMPLATE: the lesson ladder (PRINCIPLES 15). Every correction or failure is logged here before it
becomes a rule. Delete this line after copying.

## Ladder
- **observation** - seen once. Keep it here; change nothing.
- **pattern** - seen twice in different tasks. Look for the root cause.
- **candidate** - a proposed upgrade: the smallest reusable change, plus the eval case that proves it. Waits for the user.
- **confirmed** - the user approved; enforced by a named check, and the failure is an eval case.

Promote only what changes future behaviour. Task-specific corrections stay with the task.

## Upgrade review (after a failed run or a user correction)
1. Do not repair the output yet. Classify the root cause: missing instruction | missing context |
   weak skill or procedure | missing check | bad tool contract | permission | insufficient evidence | ambiguous task.
2. Find the lesson below: new = observation; seen before = climb one rung.
3. At candidate: propose the change (file, exact lines) and the eval case. Change nothing yet.
4. After the user's yes: apply it, add the case to `harness/evals/`, run `harness/evals.py`, mark it confirmed.

## Lessons

| Lesson | Rung | Seen (date, task) | Enforced by |
|---|---|---|---|
| {{e.g. announcement date used as release date}} | observation | {{date, task}} | not yet |
