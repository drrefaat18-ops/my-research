<!-- TEMPLATE: the evidence ledger, saved next to the brief. scripts/ledger_check.py reads the three tables below
     by their headings and column names; keep both. Cells may not contain "|". Dates YYYY-MM-DD. Delete TEMPLATE comments. -->
# Ledger {{TASK_ID}}

## Sources
<!-- kind: primary | independent | official-doc | post | snippet | memory | other. origin: who first made the claim
     (two sources with one origin are not independent). -->
| id | url_or_path | publisher | kind | origin | published | accessed |
|---|---|---|---|---|---|---|
| S1 | https://example.org/report | Example Org | primary | Example Org | 2026-01-10 | 2026-01-12 |

## Claims
<!-- status: supported | contested | unverified | stale | n/a. fact_type: a key of the freshness windows. -->
| id | claim | status | fact_type | checked | note |
|---|---|---|---|---|---|
| C1 | In test Y, setup Z, item X scored 82 on task A | supported | stable | 2026-01-12 | |

## Evidence
<!-- one row per claim-source pair; passage copied exactly; not_established = what the passage does NOT show. -->
| claim | source | passage | not_established |
|---|---|---|---|
| C1 | S1 | "Item X scored 82 on task A under setup Z." | performance outside setup Z |
