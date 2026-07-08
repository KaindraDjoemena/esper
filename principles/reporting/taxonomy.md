---
name: Reporting Taxonomy
description: Defines consistent severity levels and confidence scales for engineering findings.
---

# Reporting Taxonomy

## Severity

Severity should reflect engineering impact—not implementation effort.

### Critical
Immediate engineering action required.
Examples: security vulnerabilities, data corruption, release blockers.

### High
Serious issues with significant user or engineering impact.
Examples: broken functionality, major architectural flaws, performance regressions.

### Medium
Important issues that should be addressed but are unlikely to block release.
Examples: maintainability problems, incomplete abstractions, unnecessary complexity.

### Low
Minor issues.
Examples: documentation gaps, small refactors, API consistency improvements.

### Nit
Cosmetic observations.
Examples: naming, formatting, wording, stylistic consistency.

---

## Confidence

Confidence reflects the strength of the supporting evidence—not the importance of the finding.
Prefer lower confidence over overstating certainty. Separate observations from inferences.

### Confirmed
Directly supported by evidence.
Examples: observed code, failing tests, documented behavior.

### Likely
Strong evidence exists, but some assumptions remain.
Further verification is recommended.

### Speculative
Limited evidence.
Present as a hypothesis rather than a conclusion. Never present speculation as fact.
