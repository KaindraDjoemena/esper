---
name: Finding Schema
description: Defines the canonical structure of engineering findings. Use whenever documenting bugs, architectural concerns, design feedback, security observations, or engineering recommendations.
---

# Finding Schema

## Purpose

Every engineering finding should communicate enough information for another engineer to understand the issue, evaluate its importance, and decide on an appropriate action.

## Canonical Fields

### Title

Short descriptive summary.

### Severity

Use a level from the canonical [Severity Taxonomy](severity.md).

### Category

Examples:

- Correctness
- Architecture
- Security
- Performance
- Maintainability
- Testing
- Documentation
- Developer Experience

### Evidence

Describe concrete observations.

Reference specific files, APIs, code, or documentation where appropriate.

Avoid unsupported claims.

### Impact

Explain why the finding matters.

Describe technical consequences rather than generic statements.

### Recommendation

Describe the preferred engineering action.

Recommendations should be actionable.

### Confidence

Communicate certainty using the Confidence taxonomy.

## Guiding Questions

Every finding should answer:

1. What is the issue?
2. Why does it matter?
3. How certain is the conclusion?
4. What should happen next?

## Principles

- One finding per issue.
- Prefer evidence over speculation.
- Recommendations should follow naturally from evidence.
- Exhaustiveness: Document all discovered issues. Do not artificially limit the number of findings (e.g., stopping at 3 or 5 items).
## Canonical Sources

- principles/reporting/taxonomy.md
