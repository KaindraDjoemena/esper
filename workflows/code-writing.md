---
name: Code Writing
---

# Code Writing Workflow

## Purpose

Produce code that integrates naturally into the existing project.

## When to Use

- implementing features
- writing scripts
- modifying existing code

## Workflow

### 1. Understand the task

Clarify:
- what problem is being solved
- expected behavior
- constraints
- success criteria

### 2. Gather context

Read:
- related implementation
- interfaces
- shared utilities
- surrounding architecture
- existing patterns

Do not begin designing until sufficient context has been gathered.

### 3. Identify conventions

Reuse:
- naming
- folder organization
- architecture
- abstractions
- error handling
- dependency injection
- testing patterns

Consistency is generally preferable to novelty.

### 4. Design

- Generate alternative solutions before committing to an approach.
- Explain trade-offs between approaches.
- Verify assumptions against existing code.

Prefer:
- minimal changes
- localized modifications
- readable implementations
- reusable components

Avoid speculative abstractions.

### 5. Validate mentally

Before presenting code, verify:
- edge cases
- failure paths
- nullability
- async behavior
- error handling
- compatibility with surrounding code

### 6. Ask for Confirmation

Before executing any changes, present your proposed design and implementation plan to the user.
**Stop and wait for explicit confirmation from the user before writing any code.**

### 7. Execute and Summarize

Once approved, execute the plan.
Explain:
- what was changed
- why the implementation fits
- tradeoffs
- assumptions

If uncertain, state the uncertainty.

## Required Dependencies

- workflows/revision.md
- checklists/feature.md

## Canonical Sources

- principles/engineering.md
