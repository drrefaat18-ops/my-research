<!-- TEMPLATE: permission lanes (PRINCIPLES 18). Fill each lane in Phase 3 from the user's Q6 answers, then map every
line onto the tool's own permission settings or the guard script; a lane that exists only here is a wish.
Delete TEMPLATE comments. -->
# Permission Lanes

| Lane | Rule | Actions | Enforced by |
|---|---|---|---|
| Free | runs without asking, always traced | read, search, run checks, {{FREE_ACTIONS}} | {{FREE_ENFORCEMENT}} |
| Approval | the user says yes first, every time | send, publish, deploy, pay, spawn agents, {{APPROVAL_ACTIONS}} | {{APPROVAL_ENFORCEMENT}} |
| Closed | never, whatever the reason; the user does it by hand | delete originals, rotate secrets, force-push the main line, {{CLOSED_ACTIONS}} | {{CLOSED_ENFORCEMENT}} |

<!-- TEMPLATE: Enforced by = the setting or script that blocks it (e.g. a permissions "deny" entry, a guard path list,
a protected branch). Sort by how hard the action is to undo, not by how often it happens. -->

A closed lane is not a high threshold. Moving an action out of it is a decision the user records in memory.
