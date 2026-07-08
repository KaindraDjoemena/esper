---
name: Code Review
---

# Code Review Workflow

## Purpose

Produce a review that is accurate, well-supported, and grounded in the implementation rather than assumptions.

## When to Use

- peer code review
- pull request review

## Workflow

### 1. Gather context

Before reviewing:
- Inspect the Git diff.
- Read every changed file.
- Read directly related files that provide necessary context.
- Read relevant tests when they exist.
- Read relevant documentation if it affects the change.

Never review isolated snippets when surrounding context is readily available.

### 2. Understand before evaluating

Identify:
- the purpose of the change
- the design being implemented
- the surrounding architecture
- dependencies
- existing project conventions

Avoid judging code before understanding its intent.

### 3. Review from multiple perspectives

Evaluate:
- correctness
- security
- maintainability
- performance
- API design
- readability
- testability
- project consistency

Not every category will apply.

### 4. Prioritize findings

Only report findings that provide meaningful value.
Avoid nitpicks unless they significantly improve readability or maintainability.
When something is well-designed, explicitly acknowledge it.

### 5. Report findings

Report findings using the canonical Finding schema.
Only report findings that provide meaningful value.
Separate confirmed issues from hypotheses.

### Context Gathered

For substantial reviews, begin with:
- Git information reviewed
- Files reviewed
- Tests reviewed
- Documentation reviewed

This demonstrates the evidence used to reach conclusions.

## Required Dependencies

- templates/code-review.md
- checklists/code-review.md
