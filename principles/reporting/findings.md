---
name: Finding Schema
description: Defines the canonical structure of engineering findings. Use whenever documenting bugs, architectural concerns, design feedback, security observations, or engineering recommendations.
---

<esper_module type="principle">
<purpose>
Every engineering finding should communicate enough information for another engineer to understand the issue, evaluate its importance, and decide on an appropriate action.
</purpose>
<canonical_fields>
<subsection>Title</subsection>
Short descriptive summary.
<subsection>Severity</subsection>
Use a level from the canonical [Severity Taxonomy](taxonomy.md).
<subsection>Category</subsection>
Examples:
<item>Correctness</item>
<item>Architecture</item>
<item>Security</item>
<item>Performance</item>
<item>Maintainability</item>
<item>Testing</item>
<item>Documentation</item>
<item>Developer Experience</item>
<subsection>Evidence</subsection>
Describe concrete observations.
Reference specific files, APIs, code, or documentation where appropriate.
Avoid unsupported claims.
<subsection>Impact</subsection>
Explain why the finding matters.
Describe technical consequences rather than generic statements.
<subsection>Recommendation</subsection>
Describe the preferred engineering action.
Recommendations should be actionable.
<subsection>Confidence</subsection>
Communicate certainty using the Confidence taxonomy.
</canonical_fields>
<guiding_questions>
Every finding should answer:
1. What is the issue?
2. Why does it matter?
3. How certain is the conclusion?
4. What should happen next?
</guiding_questions>
<instructions>
<item>One finding per issue.</item>
<item>Prefer evidence over speculation.</item>
<item>Recommendations should follow naturally from evidence.</item>
<item>Exhaustiveness: Document all discovered issues. Do not artificially limit the number of findings (e.g., stopping at 3 or 5 items).</item>
</instructions>
<dependencies>
<canonical_sources>
<item>principles/reporting/taxonomy.md</item>
</canonical_sources>
</dependencies>
</esper_module>
