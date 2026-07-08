# Esper Routing Table

## Purpose

The Routing Table is the primary entry point for determining the correct module composition for any user request. It allows an agent to immediately map intent to the required modules without blindly exploring the workspace.

## How to Use

1. Identify the user's primary objective.
2. Find the corresponding **Task Type** in the map below.
3. Load the designated **Entry Point**.
4. The Entry Point will specify **Required Dependencies**. Load these.
5. Retrieve **Optional Dependencies** or **Canonical Sources** only when explicitly justified by context or as the task evolves.

## Routing Map

| Task Type | Entry Point (Load this first) |
|---|---|
| Reviewing System Architecture | `prompts/architecture-review.md` |
| Investigating a Bug / Issue | `prompts/bug-investigation.md` |
| Reviewing a Pull Request / Code | `prompts/code-review.md` |
| Writing or Reviewing Documentation | `prompts/documentation.md` |
| Explaining Existing Code | `prompts/explain.md` |
| Implementing a New Feature | `prompts/feature.md` |
| Creating an Implementation Plan | `prompts/feature.md` |
| Analyzing / Improving Performance | `prompts/performance-review.md` |
| Refactoring Code | `prompts/refactor.md` |
| Researching / Exploring | `prompts/research.md` |
| Reviewing Security | `prompts/security-review.md` |
| Coordinating Multiple Agents | `prompts/orchestration.md` |
| Systemic Retrospective | `prompts/retrospective.md` |

## Canonical Sources

- principles/retrieval.md

## Fallback & Overlapping Tasks

If the user's objective does not perfectly match a task type, select the closest match. Do not load multiple prompts simultaneously.

If a task spans multiple objectives (e.g., investigating a bug that might require refactoring), **start with the most constrained or immediate objective** (e.g., `bug-investigation.md`). 

However, because Esper relies on explicit user confirmation before execution, **default to Orchestration (`prompts/orchestration.md`)** and invoke subagents for any non-trivial task. Do not force a constrained single-agent workflow when parallel execution is possible. Always check if a relevant skill (e.g., `esp-*`) exists for the objective.
