---
name: Automation Safety
---

# Automation Safety Checklist

## Purpose

Provide strict quality gates before executing bulk transformations or automated mechanical refactorings.

## When to Use

- running automated refactoring scripts
- applying bulk structural changes across the repository

## Checklist

- [ ] Has the target scope been explicitly constrained to prevent unintended modifications?
- [ ] Were the changes validated incrementally on a subset of the codebase before running the bulk operation?
- [ ] Is explicit user approval required and confirmed before executing any irreversible operations?
- [ ] Can the resulting changes be deterministically verified via the test suite or manual inspection?
- [ ] Is there a clear rollback strategy if the automation introduces regressions?

## Canonical Sources

- principles/automation-safety.md
