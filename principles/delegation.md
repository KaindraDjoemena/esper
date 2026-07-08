---
name: Delegation
---

# Delegation Principles

## Purpose

Provide canonical guidance on when and how to delegate engineering tasks to subagents to execute complex work efficiently without duplicating effort or bloating context.

## Principles

### Decompose by Domain Boundaries
Partition tasks along natural architectural or functional boundaries. Delegate independent investigations, parallel research, or isolated component implementations. Avoid delegating highly coupled work where constant coordination is required.

### Inherit, Don't Bootstrap
A delegated agent should not have to rediscover the workspace. The primary agent must transfer the necessary context:
- The specific objective of the delegated task
- The active workflow and relevant principles
- Gathered evidence and constraints
- Known assumptions

### Strict Context Boundaries
Transfer only the context necessary for the subagent to succeed. 
- **Required Context**: Objective, constraints, and relevant evidence.
- **Optional Context**: Surrounding architecture if it impacts the implementation.
- **Disposable Context**: Early speculative hypotheses or unrelated project history should be omitted to minimize context window bloat.

### Avoid Duplicated Investigation
Ensure subagents have mutually exclusive responsibilities. Two subagents should not be asked to research the same codebase area or solve the same problem concurrently unless explicitly designed as a comparative exercise.

### Validate Before Integration
Never blindly accept a subagent's output. The primary agent is responsible for validating that the subagent's findings are supported by evidence, assumptions are documented, and unresolved questions are surfaced before integrating the work into the final deliverable.

### Conflict Resolution & Consensus
When subagents disagree (e.g., conflicting architectural or performance recommendations), the primary agent acts as the final decision-maker. The primary agent must evaluate the competing evidence, resolve the contradiction, and form a consensus rather than presenting conflicting options to the user.

### Shared Evidence
If multiple subagents require access to the same evolving information, establish a centralized shared artifact (e.g., a scratchpad) to collect and distribute evidence, preventing fragmented or duplicated research.

## Canonical Sources

- principles/engineering.md
