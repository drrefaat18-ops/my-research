# 📋 CLAUDE_EXECUTION_PLAN: Generic Academic Research Swarm & Vault Template
> **Target Executor:** Claude Code (Anthropic) / Ruflo Swarm  
> **Directive Authority:** Autonomous Master's Thesis Directives & Multi-Agent Swarm  
> **Mission:** Build a clean, domain-agnostic, production-ready research vault and multi-agent swarm template (`research-swarm-template/`) ready to be given to an academic researcher in ANY field.

---

## 🎯 Executive Overview & Architectural Contract

You (Claude Code) are instructed to execute the creation of a generic, turn-key research vault and autonomous multi-agent swarm template located at:
`d:\vault\my research\research-swarm-template/`

### Critical Guardrails:
1. **Zero Domain Contamination**: The resulting template must be **100% free** of personal and domain-specific data:
   - NO mentions of: `Refaat`, `Dr. Refaat`, `Port Said University`, `Pharmacology`, `Toxicology`, `Ahmed Mourad`, `m-PEA`, `PEA`, `Prednisolone`, `CFA`, `Adjuvant Arthritis`, `Wistar rats`, `Tacrolimus`, `Baricitinib`.
   - NO local institutional frictions (e.g. self-funded low-budget constraint for rat kits, lack of liquid nitrogen at Port Said).
2. **Preserve the Full Multi-Agent Swarm Engine**:
   - Ruflo V3 / Claude-Flow configuration (`.claude/`, `.claude-flow/`, `.mcp.json`).
   - The complete catalog of **470+ Agency Agents** in `.claude/agents/*.md`.
   - All 316 cataloged skills in `skills_manifest.csv`.
   - The 8 core Claude skills in `.claude/skills/`.
   - The Obsidian configuration in `.obsidian/` (including the `Retroma` theme, core plugins, and graph view).
3. **Universal 7-Pillar Research Topology**:
   - `00-Sources/`
   - `01 - Rationale & Research Questions/`
   - `02 - Theoretical Framework & Mechanics/`
   - `03 - Collective Literature Matrix/`
   - `04 - Methodology & Protocols/`
   - `05 - Benchmarks & Comparisons/`
   - `06 - Thesis Defense & Publishing/`
   - `07 - Automated QC & Audits/`
4. **Configurable Research Operating Directives**:
   Replace the hardcoded pharmacology budget constraint with a flexible **Research Feasibility & Rigor Framework** that accommodates 3 research profiles:
   - *Profile A: Self-Funded / Resource-Constrained Research* (Zero-spend filters, open-source tools, maximal data extraction).
   - *Profile B: Grant-Funded / Laboratory-Based Research* (Commercial kits, equipment protocols, grant milestones).
   - *Profile C: Computational / Theoretical / Data-Driven Research* (GPU/compute budgets, dataset provenance, simulation reproducibility).
5. **Turn-key Automation Suite**:
   - `scripts/init_research.py`: Interactive onboarding wizard for the friend to configure their name, field, topic, and research questions in 30 seconds.
   - `scripts/sync_agency_agents_to_ruflo.py`: Pre-installed agent synchronizer.
   - `scripts/run_qc_audit.py`: Universal 4-gate academic QC engine (Data parity, Link integrity, Epistemic tagging, Preliminary data quarantine).
   - `scripts/fix_broken_links.py`: Automated Zettelkasten link fixer.
   - `scripts/package_template.py`: 1-click zip bundler.

---

## 🛠️ Step-by-Step Execution Phases

### Phase 1: Directory Scaffold & Obsidian Visuals
- [ ] Create root directory: `research-swarm-template/`
- [ ] Create the 7 functional pillar directories:
  ```bash
  mkdir -p "research-swarm-template/00-Sources/literature"
  mkdir -p "research-swarm-template/00-Sources/data"
  mkdir -p "research-swarm-template/01 - Rationale & Research Questions"
  mkdir -p "research-swarm-template/02 - Theoretical Framework & Mechanics"
  mkdir -p "research-swarm-template/03 - Collective Literature Matrix/Studies"
  mkdir -p "research-swarm-template/04 - Methodology & Protocols/Protocols"
  mkdir -p "research-swarm-template/05 - Benchmarks & Comparisons"
  mkdir -p "research-swarm-template/06 - Thesis Defense & Publishing"
  mkdir -p "research-swarm-template/07 - Automated QC & Audits"
  mkdir -p "research-swarm-template/scripts"
  ```
- [ ] Copy `.obsidian` directory preserving:
  - `appearance.json` (`"cssTheme": "Retroma"`)
  - `themes/Retroma/` (Theme styling)
  - `core-plugins.json` (Optimized academic plugin configuration)
  - `graph.json` (Graph visualization parameters)
  - Clean `app.json`

---

### Phase 2: Agent Architecture, Ruflo V3 & Agency Swarm (470+ Agents)
- [ ] Copy `.claude/` directory to `research-swarm-template/.claude/`:
  - `settings.json`: Configured with Claude Flow V3, Agent Teams, Mesh Swarm, and Memory management.
  - `proven-config.json`: Ruflo configuration.
  - `agents/`: Copy all 745 markdown agent definition files (covering all 470 agency agents) from `d:\vault\my research\.claude\agents/`.
  - `skills/`: Copy all 8 core Claude skills (`hooks-automation`, `pair-programming`, `skill-builder`, `sparc-methodology`, `stream-chain`, `swarm-advanced`, `swarm-orchestration`, `verification-quality`).
- [ ] Copy `.claude-flow/` directory:
  - `config.yaml`: RuFlo V3 mesh swarm configuration.
  - `CAPABILITIES.md`: Complete swarm capability catalog.
  - `agents/store.json`: Pre-registered Agency Agents database.
- [ ] Copy `.agents/` directory:
  - `rules/research_rigor_and_methodology.md`: Domain-agnostic research rigor directives.
  - `skills/ruflo/SKILL.md`: Autonomous multi-agent orchestration skill with Agency Swarm documentation.
- [ ] Copy `skills_manifest.csv` (316 cataloged skills).
- [ ] Create `research-swarm-template/.mcp.json` with Ruflo V3 MCP server config.
- [ ] Create `research-swarm-template/.gitignore` (academic gitignore).

---

### Phase 3: Universal Agent Directives & Navigation Documents
- [ ] Create `research-swarm-template/AGENTS.md`:
  - Prime directive for academic rigor and reproducibility.
  - 4-Tier Epistemic claim tagging standard (`[Fact]`, `[Hypothesis]`, `[Planned]`, `[Interpretation]`).
  - Preliminary / pilot data quarantine rules (`#pilot`, `#preliminary`).
  - Luhmann Zettelkasten bidirectional linking standard ($\ge 2$ links per note, 0 orphan notes).
  - Configurable resource profile (Profiles A, B, C).
- [ ] Create `research-swarm-template/CLAUDE.md`:
  - Ruflo V3 + Claude Code instructions.
  - Swarm coordination via `SendMessage`, agent routing matrix (including full Agency Swarm dispatch).
  - 3-tier model routing (Deterministic / Haiku / Sonnet & Opus).
  - CLI quick reference (`npx ruflo init`, `npx ruflo swarm init`, `npx ruflo doctor`).
- [ ] Create `research-swarm-template/GEMINI.md`:
  - Deep analysis, multi-agent coordination, and methodological verification directives for Google DeepMind / Antigravity / Gemini.
- [ ] Create `research-swarm-template/_CLAUDE.md` & `_AGENTS.md`:
  - Detailed operating manual with template placeholders (`{{RESEARCHER_NAME}}`, `{{INSTITUTION}}`, `{{RESEARCH_TOPIC}}`, `{{DEGREE_LEVEL}}`).
- [ ] Create `research-swarm-template/AGENT_NAVIGATION_GUIDE.md` & `AGENT_NAVIGATION_GUIDE.json`:
  - Universal machine and human readable guide giving any LLM instant situational awareness of the vault's structure and rules.
- [ ] Create `research-swarm-template/Home-Index.md`:
  - Central Obsidian navigation dashboard linking all 7 MOC pillars with visual ASCII map and status badges.
- [ ] Create `research-swarm-template/README.md`:
  - Complete, user-friendly onboarding guide for the researcher friend:
    1. Opening the vault in Obsidian.
    2. Running the 30-second setup wizard (`python scripts/init_research.py`).
    3. Activating agents in Claude Code, Cursor, Antigravity, or Gemini.
    4. Swarm commands and Agency Agents usage.
    5. Running automated QC audits.

---

### Phase 4: Maps of Content (MOCs) & Template Notes
Create clean, template-ready Map of Content notes demonstrating proper Zettelkasten bidirectional links:
- [ ] `01 - Rationale & Research Questions/01-MOC-Rationale.md`
  - Links to: `[[Home-Index]]`, `[[Research-Problem-Statement]]`, `[[Core-Hypotheses-and-Objectives]]`
  - Contains template notes:
    - `Research-Problem-Statement.md`
    - `Core-Hypotheses-and-Objectives.md`
- [ ] `02 - Theoretical Framework & Mechanics/02-MOC-Theoretical-Framework.md`
  - Links to: `[[Home-Index]]`, `[[Theoretical-Framework-Core-Axis]]`, `[[Key-Variables-and-Mechanisms]]`
  - Contains template notes:
    - `Theoretical-Framework-Core-Axis.md`
    - `Key-Variables-and-Mechanisms.md`
- [ ] `03 - Collective Literature Matrix/03-MOC-Literature-Matrix.md`
  - Links to: `[[Home-Index]]`, `[[Master-Literature-Synthesis-Table]]`
  - Contains template note:
    - `Master-Literature-Synthesis-Table.md` (Universal 5-question comparison table template)
    - `Studies/Study-01-Template.md` (Atomic paper review note with 5-question framework)
- [ ] `04 - Methodology & Protocols/04-MOC-Methodology.md`
  - Links to: `[[Home-Index]]`, `[[Standard-Operating-Protocol-Template]]`, `[[Preliminary-Trial-Quarantine-Protocol]]`
  - Contains template notes:
    - `Protocols/Standard-Operating-Protocol-Template.md`
    - `Preliminary-Trial-Quarantine-Protocol.md` (Demonstrating `#pilot` quarantine)
- [ ] `05 - Benchmarks & Comparisons/05-MOC-Benchmarks.md`
  - Links to: `[[Home-Index]]`, `[[State-of-the-Art-Benchmark-Matrix]]`
  - Contains template note:
    - `State-of-the-Art-Benchmark-Matrix.md`
- [ ] `06 - Thesis Defense & Publishing/06-MOC-Defense-and-Publishing.md`
  - Links to: `[[Home-Index]]`, `[[Manuscript-Draft-Outline]]`, `[[Defense-Slides-Structure]]`
  - Contains template notes:
    - `Manuscript-Draft-Outline.md`
    - `Defense-Slides-Structure.md`
- [ ] `07 - Automated QC & Audits/07-MOC-QC-and-Audits.md`
  - Links to: `[[Home-Index]]`, `[[agency_agents_full_registry.json]]`
  - Copy `agency_agents_full_registry.json` from main repo.

---

### Phase 5: Python Tooling Suite (`scripts/`)
- [ ] `scripts/init_research.py`:
  - Interactive CLI wizard prompting for:
    - Researcher Name
    - University / Institution
    - Degree / Level (Master's, PhD, Postdoc, Journal Paper)
    - Research Discipline & Title
    - Core Hypotheses & Research Questions
    - Resource Profile (A, B, or C)
  - Updates `Home-Index.md`, `AGENT_NAVIGATION_GUIDE.md`, `AGENT_NAVIGATION_GUIDE.json`, `AGENTS.md`, and `CLAUDE.md` dynamically.
  - Supports non-interactive `--preset` mode.
- [ ] `scripts/sync_agency_agents_to_ruflo.py`:
  - Re-syncs agent definitions into `.claude/agents/` and `.swarm/memory.db`.
- [ ] `scripts/run_qc_audit.py`:
  - Universal 4-Gate Academic QC:
    - Gate 1: Data & note parity.
    - Gate 2: Graph & link integrity (zero dead wikilinks, $\ge 2$ links/note).
    - Gate 3: Epistemic claim tagging.
    - Gate 4: Preliminary / pilot quarantine.
- [ ] `scripts/fix_broken_links.py`:
  - Scans for broken `[[wikilinks]]` and resolves or reports them.
- [ ] `scripts/gap_audit.py`:
  - Scans vault for incomplete notes or missing sections.
- [ ] `scripts/setup_manifest_swarm.py` & `scripts/execute_manifest_swarm.py`:
  - Universal swarm orchestration script across the 10 academic roles.
- [ ] `scripts/package_template.py`:
  - Packs `research-swarm-template/` into `research-swarm-template.zip` excluding `.git`, `__pycache__`, and temporary logs.

---

### Phase 6: Automated Verification Gates
Execute the following verification commands to ensure production readiness:
1. **Zero-Leakage Regex Audit**:
   ```bash
   python -c "
   import re, os
   banned = ['Refaat', 'Port Said', 'Pharmacology', 'Toxicology', 'Ahmed Mourad', 'm-PEA', 'Prednisolone', 'CFA', 'Adjuvant Arthritis', 'Wistar', 'Tacrolimus', 'Baricitinib']
   root = 'research-swarm-template'
   leaks = []
   for r, d, files in os.walk(root):
       if '.git' in r: continue
       for f in files:
           if f.endswith(('.md', '.json', '.py', '.yaml')):
               fp = os.path.join(r, f)
               text = open(fp, encoding='utf-8', errors='ignore').read()
               for b in banned:
                   if re.search(r'\b' + re.escape(b) + r'\b', text, re.IGNORECASE):
                       leaks.append((fp, b))
   if leaks:
       print('FAIL: Found leaks:', leaks[:10])
       exit(1)
   else:
       print('PASS: Zero domain/personal leaks!')
   "
   ```
2. **Link Integrity Audit**:
   ```bash
   python research-swarm-template/scripts/fix_broken_links.py
   python research-swarm-template/scripts/run_qc_audit.py
   ```
   (Must report 0 broken links and 100% passing gates).
3. **Agency Swarm Count Check**:
   Confirm that `research-swarm-template/.claude/agents/` contains $\ge 470$ agent definitions.
4. **Packaging Test**:
   ```bash
   python research-swarm-template/scripts/package_template.py
   ```
   (Verify `research-swarm-template.zip` is created cleanly).

---

## 🏁 Final Hand-off Report
Upon completion, Claude Code should summarize the created template, the total agent count, the QC test results, and provide the command for Dr. Refaat to package or share the template with his friend.
