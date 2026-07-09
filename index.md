# Esper

> "Enhance."

Esper is a modular engineering operating system for AI coding assistants.

Rather than relying on a single monolithic system prompt, Esper decomposes engineering knowledge into small, focused modules with clearly defined responsibilities. These modules are composed together at runtime to guide reasoning, reduce oversight, and improve consistency across engineering tasks.

Esper is designed to be:

- Agent-agnostic
- Modular
- Composable
- Maintainable
- Evidence-driven

While originally developed for Gemini, Esper is intended to work with any capable coding assistant.

---

# Philosophy

Esper is built around four core ideas.

## Understand before changing

Engineering recommendations should be grounded in an understanding of the existing implementation.

Before proposing changes:

- gather sufficient context
- inspect the surrounding implementation
- understand existing architecture
- identify project conventions

Avoid making repository-wide conclusions from isolated snippets.

---

## Evidence over assumptions

Recommendations should be supported by evidence.

Clearly distinguish between:

- observations
- inferences
- assumptions

State uncertainty honestly.

---

## Composition over monoliths

Esper avoids storing engineering knowledge in one enormous prompt.

Instead, it composes small, focused modules together.

Each module has a single responsibility.

This keeps the system maintainable and easy to extend.

---

## Engineering over prompt engineering

Esper is intentionally designed like software.

Each document owns one responsibility.

Knowledge should live in exactly one place.

When guidance changes, it should only need to be updated once.

---

# Architecture

Esper is organized as a layered system.

```text
Human Request
        │
        ▼
Routing (Task Discovery)
        │
        ▼
Prompt Specification
        │
        ▼
Workflow (Delegation -> Scratchpads -> Synthesis)
        │
        ▼
Engineering Principles
        │
        ▼
Checklist
        │
        ▼
Template
        │
        ▼
Final Response
```

Each layer contributes something unique.

---

# Module Hierarchy and Responsibilities

Each module category has a strictly defined responsibility. Guidance should never cross these boundaries.

## `routing.md` (Discovery)

The central index that maps a user's request to the correct entry point. It prevents agents from eagerly loading the workspace and ensures context is built incrementally.

## `prompts/` (Intent)

Defines **what** the user is asking. Prompts act as entry points that translate user intent into Esper's architecture. 
They identify the task and declare **Required Dependencies** (workflows, templates). 
Prompts must not contain step-by-step instructions or formatting guidance.

## `workflows/` (Process)

Defines **how** an engineering task should be performed.
Workflows describe repeatable procedural steps (e.g., gathering context, understanding architecture, validating assumptions).
Workflows are strictly procedural and should not define output formatting or underlying engineering philosophy.

## `principles/` (Philosophy)

Defines **why** we make certain engineering choices, and establishes canonical standards.
Principles guide engineering judgment throughout a task (e.g., simplicity, consistency, maintainability).
They explain philosophy, not process.

## `checklists/` (Validation)

Defines **reminders** and quality gates.
Checklists exist to reduce oversight by reminding the assistant of commonly forgotten considerations (e.g., "Are failure paths handled?").
They supplement judgment and validate output quality before finalizing a task. They should not introduce new procedures.

## `templates/` (Structure)

Defines **deliverable format**.
Templates act as thin structural specifications for the final response. They define headers, layout, and presentation but rely on workflows for how to gather the data and `principles/reporting/` for how to format findings and scales.

## `shared_context/` (Memory)

Defines **persistent state**.
A designated directory for agents to store repository maps, scratchpads, and persistent notes so that knowledge persists between sessions.
- **Global Context** (`esper/shared_context/`): Used for meta-knowledge about the Esper framework itself.
- **Project Context** (`<project-root>/.esper/shared_context/`): Used for codebase-specific memories. Agents must gracefully create this if it does not exist and advise the user to update `.gitignore`.

## Skills (Extensions)

Defines **capabilities**.
Skills are optional, executable extensions that combine Esper's modules (prompts, workflows, checklists, templates) into highly specialized, automatable tasks (e.g., repository auditing, complex scaffolding). They exist outside the core repository to prevent bloat but are strictly governed by Esper's philosophy when invoked.

---

# Reporting Model

Esper uses a centralized reporting model to prevent duplication.

- **Canonical Schemas**: Definitions for findings, severity levels, confidence scales, and report structures live exclusively in `principles/reporting/`.
- **Thin Templates**: Deliverable templates (e.g., `audit-report.md`) do not redefine these scales. They simply reference the canonical schemas and define the domain-specific sections.
- **Review Quality**: Code review and architecture checklists enforce report-quality gates (e.g., ensuring scope and context are documented, findings are prioritized). This ensures the review itself is communicated effectively.

---

# Module Composition and Precedence

Esper composes small modules dynamically. When overlapping or conflicting guidance occurs, agents must resolve it deterministically using the following precedence (highest to lowest):

1. **Prompt Specification**: The user's explicit intent overrides general procedures.
2. **Workflow**: Procedural execution rules override general philosophy.
3. **Engineering Principles**: Canonical standards (including reporting) override structural templates.
4. **Checklist**: Quality gates that validate the result.
5. **Template**: Structural layout.

**Conflict Resolution:**
- If a Template defines a finding format that conflicts with `principles/reporting/`, the **Principle** wins.
- If a Workflow step contradicts an Engineering Principle (e.g., the workflow says "rewrite all", but the principle says "minimize change"), the **Workflow** takes precedence for that specific task.
- If an implicit assumption conflicts with an explicit checklist item, the **Checklist** requirement must be satisfied.

---

# Completion Criteria

An engineering task in Esper is considered complete only when the following criteria are met, regardless of the specific workflow:

1. **Context Validated**: Sufficient context was gathered and assumptions were explicitly verified against the codebase.
2. **Intent Satisfied**: The core objective defined by the prompt specification was achieved.
3. **Quality Gated**: All relevant checklist items for the task have been satisfied.
4. **Deliverable Structured**: The final output conforms to the designated template and adheres to reporting principles (if applicable).
5. **No Unwarranted Changes**: The solution minimizes unnecessary complexity and respects existing architectural boundaries.

---

# Cross-Reference Policy

Modules reference each other to form an interconnected graph, allowing discoverability without monolithic prompts. Context must be earned and retrieved incrementally.

**Dependency Types:**
- **Required Dependencies:** Modules strictly necessary to complete the task (e.g., core workflows, templates). Must be loaded. **If a Required Dependency is missing or fails to load, the agent must halt execution and notify the user to resolve the broken link before proceeding.**
- **Optional Dependencies:** Modules loaded only if justified by the evolving task context (e.g., retrieving security principles during a review).
- **Canonical Sources:** Definitional modules (e.g., severity scales). Load only if you explicitly need to apply the concept.

**Best Practices:**
- **Keep it shallow:** Only link to immediate, high-value dependencies. Avoid deep recursive linking to prevent context window bloat.
- **Directional referencing:** Prompts reference Workflows and Templates. Workflows reference Checklists and Principles. Templates reference Reporting Principles. Avoid circular dependencies.
- **Canonical sources:** Do not redefine concepts inline. If a module needs to describe "Severity", it must link to `principles/reporting/taxonomy.md`. Ensure you load foundational sources like `principles/retrieval.md` to guide context gathering.

---

# Directory Layout

```text
esper/
├── README.md
├── benchmarks/      # Performance and validation tests
├── bootstrap/       # Initial setup and installation templates
├── checklists/      # Quality gates and validation rules
├── principles/      # Engineering philosophy and canonical standards
├── prompts/         # Entry points defining what the user is asking
├── shared_context/  # Persistent state and scratchpads
├── templates/       # Deliverable formats and structural layouts
└── workflows/       # Procedural steps defining how a task is performed
```

Future modules should follow the same design philosophy:

- focused
- reusable
- composable
- maintainable

---

# Future Vision

Esper is intended to evolve alongside engineering practice.

New knowledge should be incorporated by adding or refining focused modules rather than expanding monolithic prompts.

The long-term goal is an engineering operating system that enables AI assistants to reason with the discipline, consistency, and evidence-based approach of experienced software engineers.

---

*"Enhance."*