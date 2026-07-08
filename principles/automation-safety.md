---
name: Automation Safety
---

# Automation Safety Principles

## Purpose

Establish safety constraints for bulk codebase transformations.

## Principles

When performing bulk transformations or mechanical refactoring:
- Validate changes incrementally rather than relying entirely on bulk execution.
- Require explicit user approval before performing irreversible operations.
- Ensure that the final result is verified through tests or manual validation.
- Avoid wide-sweeping automated refactorings without strong evidence of safety.

## Canonical Sources

- principles/engineering.md
