# Graph Rules

**Nodes think. Edges carry data. Code does the plumbing. Skeptics guard the gate. One strong model judges. The human decides.**

## 1. Draw it first
- A **node** is one bounded job: one agent call, explicit input, one validated output.
- An **edge** exists only when the next node reads the last node's output. "And then" is not an edge.
- Redraw every linear script: cut the arrows that carry no data. What is left is usually a few
  independent nodes feeding one node that needs them all.

## 2. Contracts
- Every agent node gets a JSON `schema`. The model retries on mismatch; you never parse free text.
- Pass inputs in the prompt. Never assume a node can see another node's context.
- Name an edge by the shape that crosses it, not by its order.

## 3. Edges are free
- Flatten, dedupe, filter, count, format: plain JavaScript inside the script, zero tokens.
- An agent whose only job is to reformat another tool's output is wiring that pays rent. Delete it.
- Scripts that need the file system (validators, quote checkers, test runs) are edges the orchestrator
  runs between two workflows. Workflow scripts cannot touch files.

## 4. Fan out, fan in
- `pipeline()` by default: each item flows through all stages on its own.
- `parallel()` is a barrier. Use it only when the next stage needs every result at once
  (cross-set dedupe, early exit on a zero total, "compare with the others").
- Failed agents come back as `null`. Filter them, and **log** what was dropped. No silent caps.

## 5. Shapes worth knowing
| Shape | Use | Template |
|---|---|---|
| Diamond: split, fan out, reduce, synthesize | research, audits, scans | `workflows/diamond.js` |
| Router: one node classifies, code picks the branch | light path vs full audit | an `if` on a schema field |
| Skeptic panel: N lenses try to refute, majority keeps | any claim before a human sees it | `workflows/skeptic-panel.js` |
| Loop until dry: repeat until K rounds find nothing new | bug hunts, unknown-size discovery | `workflows/loop-until-dry.js` |

Loop rule: dedupe against **everything seen**, not only confirmed results, or rejected finds come back
every round and the loop never ends.

## 6. Models and money
- Every `agent()` names its model. Without one it inherits the session model (usually the most
  expensive). The guard denies a model-less call.
- Cheap model for bounded, repetitive nodes (read, extract, classify, vote). Strong model only for the
  judgment node, and usually that node is the main session, not a sub-agent.
- Announce before every run: how many agents, which model, which job. Fan-out multiplies call sites.

## 7. What stays outside the graph
- **File edits:** one orchestrator edits; agents return text. Then no worktrees are needed. Use
  `isolation: 'worktree'` only when nodes must write files in parallel.
- **A writer with fix rounds:** a workflow cannot resume an agent. Keep the writer as a normal
  Agent call and resume it, so one voice survives the fixes.
- **The human review:** the graph ends with a table the human reads, never with an auto-commit.

## 8. Knowledge-graph audit (graphify)
A second kind of graph: the project's notes as entities and links (graphify), used to audit the knowledge,
not to run agents. Script: `scripts/graph_audit.py`. The graph **reads** the notes and never writes into them:
the note app (Obsidian or any folder of .md files) stays the place people write; no `--obsidian` / `--wiki` output.

Cycle (one command each; agents only in step 4):
1. `stage` - mirror the corpus to a folder outside the project.
2. `changed` - list notes changed since the last build (and save graphify's incremental state).
3. `ids <file> ...` - existing node ids of those notes, for the agent prompt.
4. Extraction agents (cheap model, 20-25 files each) write `graphify-out/.graphify_chunk_NN.json` in the staging root.
5. `merge` - safe merge into the old graph, refuse dangling ids, re-cluster, save the manifest.
6. `publish` - copy `graph.html` (open in a browser), `graph.json`, `GRAPH_REPORT.md` (readable in the note app) into the project.
7. `audit` - `[fix]` = a note is wrong: fix it in the notes through the normal pipeline; `[note]` = review list.

What it adds over the note app's own graph view: inferred edges with confidence, communities, and the audit.
Lessons from a 93-note vault (2026-10):
- **Audit, not search.** On a small corpus, search and RAG answer daily questions. The graph pays off as a
  periodic check after a batch of edits: unsourced links, legacy facts linked as current, one entity under
  several names, isolated notes, hub notes to review first (their errors spread furthest).
- **Private data stays local.** If notes hold prices, wages or client data, extract with your own sub-agents
  (cheap model, 20-25 files each), never with a hosted extraction backend, even when its API key is set.
- **Stage outside the project.** Copy the corpus elsewhere and run graphify there; a copy inside a note app's
  folder shows every note twice. Keep graphify's cache with the staging copy so `--update` stays cheap.
- **Shared ids.** Tell every extraction agent the same id scheme for cross-note entities (`course_<slug>`,
  `person_<slug>`, `note_<title slug>`, ...); per-file ids never merge, and the graph falls apart into islands.
- **Keep old ids on update.** An agent re-reading one file invents new ids and silently cuts edges from files it
  did not read. Run `graph_audit.py ids <file>` and paste the result into the update prompt.
- **Tell the agent your domain traps:** spelling of canonical names, scrambled PDF text layers, which
  sources are legacy (label them, never link them as current), and "no money amounts in labels".
- **Never trust graphify's incremental merge on shared ids.** `build_merge` drops every node a re-extracted file
  owned, so edges from UNCHANGED notes that pointed at it vanish (a hub note such as an index re-extracted = 268
  edges lost in one update). `graph_audit.py merge` keeps those nodes; compare edge counts before publishing.
- **Count the cost.** First build here: about 780k agent tokens for 93 files; a 3-file update about 120-160k.

## 9. Save what works
Good runs are saved in `.claude/workflows/<name>.js`, version-controlled and launched by name with
`args`. Change one, then re-run `scripts/check_workflow.js` before using it for real.
