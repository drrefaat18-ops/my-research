# Kit Standard

A kit carries a **way of working** from one project to any other. It holds the method, never the
project it came from. Read by the AI that builds a kit (the `kit-builder` skill) and by anyone reviewing one.

## What a kit is
- **Portable:** phases, roles, rules (each with its *Why:*), checks, failure lessons, scripts.
- **Left behind:** names (people, companies, products, places), paths, field vocabulary, prices, dates
  tied to the source project, its language rules, its tools' private names. Each becomes a `{{PLACEHOLDER}}`
  that the install interview fills, or is deleted.
- A lesson from the source survives only as a generic sentence: "a number cited to the method, not the
  source that gave it", never the drug, course or client it was about.

## Shape (copy the existing kits)
```
<name>-kit/
  README.md        human, <= 15 lines: what it does, 5 numbered install steps, file table
  START-HERE.md    AI install protocol: hard rules, Phase 1 Interview -> 2 Design -> 3 Build -> 4 Pilot/Prove,
                   each phase ends by stopping for the user; nothing is created before the Build yes
  <RULES>.md       the method: short numbered rules, each with *Why:* (PRINCIPLES / PIPELINE / GRAPHS style)
  templates/ or agents/ or scripts/ or workflows/   files with {{PLACEHOLDERS}} and TEMPLATE: comments
```
- Every `{{PLACEHOLDER}}` is filled by a Phase 1 question or a Phase 3 step. No orphan placeholder.
- Every script: stdlib only (or names its install and asks), `--selftest` with neutral sample data, a
  crash never blocks the user's session.
- The kit says which other kits it plugs into, and plugs into an existing harness instead of duplicating it.
- English, plain words, no project names in examples (use Acme, Widget, item_x).

## Done when
1. `python kits/_tools/agnostic_check.py kits/<name>-kit --terms <source terms file>` -> 0 leaks.
2. Every script's `--selftest` passes (output shown, not claimed).
3. `grep -o "{{[A-Z_]*}}"` list matches what START-HERE fills.
4. The owner has read the method-vs-domain table and said yes.
