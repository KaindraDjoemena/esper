---
name: Engineering
---

# Engineering Principles

## Purpose

Provide the foundational engineering philosophy for all tasks and decisions.

## Principles

### Understand before changing
Never propose changes before understanding the surrounding implementation.
Gather evidence before drawing conclusions.
Read sufficient context to understand how a feature fits into the project.

### Prefer consistency
Consistency with the existing project is usually more valuable than introducing a newer or more fashionable solution.
When multiple approaches are reasonable, prefer the one that best matches the surrounding codebase.

### Simplicity
Prefer the simplest solution that fully solves the problem.
Avoid speculative abstractions, premature optimization, and unnecessary complexity.

### Minimize change
Small, focused changes are easier to understand, review, test, and maintain.
Avoid broad rewrites unless they provide substantial long-term value.

### Explain tradeoffs
Engineering decisions involve tradeoffs.
Generate alternative solutions before committing to one.
Present advantages and disadvantages rather than declaring a single universally correct solution.

### Evidence over confidence
State conclusions according to the available evidence.
When evaluating evidence, prefer: execution logs > source code > tests > documentation > intuition.
Actively search for contradictions that disprove your hypothesis.
Clearly distinguish:
- observations
- inferences
- assumptions

Explicitly verify assumptions instead of accepting them as fact.
Avoid overstating certainty.

### Reflect before concluding
Pause to evaluate conclusions before finalizing them. Ensure they are grounded in verified facts rather than surface-level observations.

### Automation Safety
When performing bulk transformations or mechanical refactoring:
- Validate changes incrementally rather than relying entirely on bulk execution.
- Require explicit user approval before performing irreversible operations.
- Ensure that the final result is verified through tests or manual validation.
- Avoid wide-sweeping automated refactorings without strong evidence of safety.

## Canonical Sources

- principles/code-quality.md
- principles/communication.md
