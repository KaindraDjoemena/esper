---
name: Architecture Review
---

# Architecture Review

## Purpose

Evaluate how well an implementation aligns with the existing architecture and identify opportunities for improvement.

## When to Use

- architecture review
- design review
- refactoring discussion
- large feature implementation

## Deliverable Structure

Follow the canonical Report Structure.

Include the following architecture-specific sections:

### Architectural Strengths

Identify design decisions that positively contribute to:
- maintainability
- extensibility
- readability
- testability
- separation of concerns

Explain *why* they are effective.

### Dependency Analysis

Evaluate:
- dependency direction
- unnecessary dependencies
- circular dependencies
- hidden coupling
- opportunities for simplification

### Consistency

Evaluate whether the implementation follows existing project conventions.
If it intentionally deviates, explain whether the deviation appears justified.

### Long-Term Considerations

Discuss:
- maintainability
- extensibility
- operational complexity
- future development cost

Avoid speculative concerns that are unsupported by the implementation.

## Canonical Sources

- principles/reporting/report-structure.md
- principles/reporting/findings.md

