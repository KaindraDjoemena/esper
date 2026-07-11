---
name: Reporting Taxonomy
description: Defines consistent severity levels and confidence scales for engineering findings.
---

<esper_module type="principle">
<severity>
Severity should reflect engineering impact—not implementation effort.
<subsection>Critical</subsection>
Immediate engineering action required.
Examples: security vulnerabilities, data corruption, release blockers.
<subsection>High</subsection>
Serious issues with significant user or engineering impact.
Examples: broken functionality, major architectural flaws, performance regressions.
<subsection>Medium</subsection>
Important issues that should be addressed but are unlikely to block release.
Examples: maintainability problems, incomplete abstractions, unnecessary complexity.
<subsection>Low</subsection>
Minor issues.
Examples: documentation gaps, small refactors, API consistency improvements.
<subsection>Nit</subsection>
Cosmetic observations.
Examples: naming, formatting, wording, stylistic consistency.
---
</severity>
<confidence>
Confidence reflects the strength of the supporting evidence—not the importance of the finding.
Prefer lower confidence over overstating certainty. Separate observations from inferences.
<subsection>Confirmed</subsection>
Directly supported by evidence.
Examples: observed code, failing tests, documented behavior.
<subsection>Likely</subsection>
Strong evidence exists, but some assumptions remain.
Further verification is recommended.
<subsection>Speculative</subsection>
Limited evidence.
Present as a hypothesis rather than a conclusion. Never present speculation as fact.
</confidence>
</esper_module>
