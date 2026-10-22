# Cost Control Kit

Cuts what an AI coding-agent session costs without cutting quality: measure first, then attack the meter that dominates.

1. Copy this folder into your project root (keep the name `cost-control-kit`).
2. Open your CLI AI tool in the project.
3. Say: `Read cost-control-kit/START-HERE.md and follow it.`
4. Answer its questions. It changes no setting until you approve its design.
5. Needs Python 3.9+. Nothing else is installed without asking.

| File | What |
|---|---|
| `COST-RULES.md` | the method: 13 rules, each with its why |
| `scripts/cost.py` | usage line -> dollars per model, and where the money goes |
| `scripts/filter_test_output.py` | pre-tool hook: test runs return failures only, exit code kept |
| `templates/` | price table, search-agent definition, read-only audit prompt, baseline sheet |
