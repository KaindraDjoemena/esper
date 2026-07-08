---
name: Severity Taxonomy
description: Defines consistent severity levels for engineering findings.
---

# Severity Taxonomy

## Critical

Immediate engineering action required.

Examples:

- security vulnerabilities
- data corruption
- irreversible data loss
- crashes blocking production
- release blockers

## High

Serious issues with significant user or engineering impact.

Examples:

- broken functionality
- major architectural flaws
- substantial performance regressions

## Medium

Important issues that should be addressed but are unlikely to block release.

Examples:

- maintainability problems
- incomplete abstractions
- unnecessary complexity

## Low

Minor issues.

Examples:

- documentation gaps
- small refactors
- API consistency improvements

## Nit

Cosmetic observations.

Examples:

- naming
- formatting
- wording
- stylistic consistency

## Guidance

Severity should reflect engineering impact—not implementation effort.