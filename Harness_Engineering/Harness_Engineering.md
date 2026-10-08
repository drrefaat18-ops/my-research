# Harness Engineering: How to Build AI Workflows That Never Fall Apart

**Author:** mirku ([@mirku21](https://x.com/mirku21))  
**Published:** 12 Sep 2026  
**Original post:** https://x.com/mirku21/status/2098836008468992471

Most people respond to a broken AI output by rewriting the prompt.

Then they switch models.

Then they upgrade to a larger context window.

The model still forgets instructions.

It still recommends the wrong tool.

It still skips verification.

It still claims success on broken work.

The problem sits outside the model weights.

The problem sits in the execution environment.

That environment is the harness.

Designing it is harness engineering.

Dario Amodei explained this directly during the launch of Claude Code:

> "Of course, you need an interface, you need a harness to use them"

The model acts as a reasoning engine.

A model can predict the next logical step.

It cannot build a stable operating system on its own.

The harness controls what the model reads, what tools it can trigger, what data survives context resets, and when the execution must halt.

Prompt engineering adjusts the wording.

Harness engineering builds the infrastructure where that wording executes.

Put a frontier model in an empty chat box, and it generates casual prose.

Put that identical model in a repository with terminal access, automated test suites, project maps, and isolated workspaces, and it ships working software.

The weights stay identical.

The harness changes everything.

OpenAI recorded the identical pattern when training agents on Codex.

Their early runs failed because the environment was underspecified.

The engineering team avoided asking the model to try harder.

They built explicit capability checks and mechanical boundaries.

When an agent fails repeatedly, stop editing adjectives in the system prompt.

Inspect the operating system around the model.

## The Three Layers of a Reliable AI System

Builders often treat prompt chains, agent loops, and multi-agent graphs as competing ideas.

They represent three distinct layers of one system.

### 1. The Harness Layer (Environment and Memory)

The harness consists of everything existing outside model weights.

It manages filesystem access, environment variables, authentication tokens, and durable files.

Andrej Karpathy established the defining mental model:

> The model is the CPU.  
> The context window is the RAM.

A raw CPU without storage or an operating system crashes instantly.

When users dump twenty pages of background text into a single prompt, they flood the RAM.

The model loses attention on critical rules.

A clean harness stores project knowledge in external markdown files.

It loads only the exact snippet needed for the immediate step.

### 2. The Loop Layer (Evidence and Convergence)

A model outputting code or text needs automated validation.

Asking the model "Are you sure this is right?" creates a circular hallucination loop.

The model evaluates its own probabilistic prediction and confirms its initial bias.

The loop layer introduces objective sensors:

- Test runners (`pytest`, `vitest`, `cargo test`)
- Format validators (JSON schema checkers, linters)
- Execution budgets (maximum four attempts before human review)

The model suggests the correction.

The harness runs the test and supplies the raw terminal output.

Execution continues only when mechanical evidence confirms the fix.

### 3. The Graph Layer (Work Allocation)

Long tasks crumble when forced into a single endless conversation thread.

The graph layer distributes work across isolated execution contexts.

One worker analyzes the task and writes an implementation blueprint.

A second worker writes the code in an isolated directory branch.

A third adversarial worker reviews the diff against project requirements.

Context stays clean.

No single prompt carries the burden of the entire project lifecycle.

## The 5 Core Jobs of a Personal AI Harness

You do not need a massive enterprise platform to apply harness engineering.

A personal harness requires five mechanical rules in your everyday workflows.

### 1. Turn Every Request into a Bounded Contract

Conversational prompts allow models to silently redefine success.

When an ambiguous prompt encounters friction, the model solves an easier adjacent task and reports victory.

A production contract sets hard boundaries before generation starts:

- **Deliverable:** Exact file name and format
- **Constraints:** Dependencies allowed, style requirements, token budget
- **Non-Goals:** Explicit list of items the model must avoid touching
- **Acceptance Criteria:** The exact condition required to close the task

Without an explicit contract, the model decides when it finishes.

With a contract, the criteria decides when the model finishes.

### 2. Provide a Map, Not an Encyclopedia

Context degradation strikes every frontier model over long horizons.

Dumping an entire project documentation file into chat burns tokens and dilutes focus.

Elite builders create a compact root map.

The map outlines where documentation, schemas, and source files live.

The model scans the map, selects the single relevant file, and reads that file alone.

A compact map preserves working memory.

A giant prompt dump exhausts it.

### 3. Externalize Memory into Durable Files

Chat history serves as temporary scratch space.

The conversation thread is not a database.

When a session runs long, attention fades and context windows fill up.

Store architecture decisions, user preferences, and unresolved bugs in a dedicated project file.

In Claude Code and Cursor, this file is `CLAUDE.md` or `.cursorrules`.

When starting a fresh session, the model reads the file and resumes immediately.

The work survives chat wipes, rate limits, and model switches.

### 4. Build Sensors Before Granting Autonomy

An agent cannot repair errors it cannot observe.

Telling a model "write bug-free code" changes nothing.

Providing a command that outputs exit code zero or a stack trace gives the model ground truth.

Sensors turn subjective quality into verifiable evidence:

- Compilers and type checkers that fail on syntax errors
- Automated test scripts that verify data transformations
- Checklist validators that confirm all required fields exist

The model creates the artifact.

The sensor generates the evidence.

The harness decides if the run passes.

### 5. Apply the Dual-Encoding Rule

Writing a rule in plain English leaves room for probabilistic failure.

The model reads the instruction, parses twenty other constraints, and skips the rule under load.

Dual-encoding solves this permanently:

First, explain the rule in text so the model understands the goal.

Second, place a mechanical gate that blocks execution if the rule breaks.

If an agent must avoid deleting files, tell it in the prompt.

Then restrict its terminal permissions so `rm -rf` throws an operating system error.

The prompt guides the intention.

The mechanical gate protects the system.

## How to Set Up a Personal Micro-Harness

Here is a five-minute harness structure you can paste into any repository, Claude Project, or Cursor workspace.

Save this content as `HARNESS.md` in your project root:

```markdown
# Project Operating Contract

## Operating Boundaries
- Allowed scope: Modify only files explicitly assigned in the current task
- Forbidden actions: Never delete existing tests, never add unverified dependencies

## Project Map
- /src: Application source code
- /tests: Validation test suites
- /docs/decisions.md: Durable log of accepted architectural choices

## Verification Protocol
Before marking any task complete, run these checks in order:
1. Run local linter: `npm run lint`
2. Run test suite: `npm test`
3. Verify output format matches the requested schema

## Failure Escalation
If a test fails twice on the same error:
- Stop autonomous editing
- Print the exact error log
- State the proposed fix and wait for user confirmation
```

This short file replaces twenty lines of repetitive prompting in every chat.

It establishes project scope, controls file access, and forces mechanical verification.

## The Two-Pass Prompting Workflow

When working on difficult reasoning tasks in standard chat interfaces, use a two-pass harness loop.

Most users ask for an answer and accept the first draft.

Production workflows split generation and critique into separate passes.

### Pass 1: The Execution Pass

```markdown
Draft the technical specification for [Feature X].
Follow the constraints listed in HARNESS.md.
Do not evaluate your own output yet.
Output the raw draft and state all assumptions made.
```

### Pass 2: The Adversarial Review Pass

```markdown
Review the draft above as a skeptical senior reviewer.
Check against these specific failure points:
1. Are edge cases handled when input arrays are empty?
2. Does the logic introduce extra dependencies?
3. Does the solution violate any constraint from HARNESS.md?

List every failure point found.
Then output the revised version fixing those gaps.
```

Separating the creator role from the reviewer role cuts hallucinated claims in half.

The model cannot defend its own errors when explicitly instructed to attack them.

## Why the Harness Compounds

Models update every few months.

Prompts that work today often produce different outputs on the next model checkpoint.

Harness engineering preserves your engineering effort.

When Anthropic releases an updated Claude or OpenAI launches a new reasoning model, your prompts might require minor adjustments.

Your test suites, project maps, permission boundaries, and durable state files remain intact.

They work on the new model immediately.

The model provides raw cognitive compute.

The harness provides the rails that turn compute into reliable execution.

Stop tweaking adjectives in your prompts.

Start building the harness around them.
