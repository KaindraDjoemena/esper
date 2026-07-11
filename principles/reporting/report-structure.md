---
name: Report Structure
description: Defines the canonical structure for engineering reports and review deliverables. Use when producing audits, code reviews, architecture reviews, security reviews, or any structured engineering assessment.
---

<esper_module type="principle">
<purpose>
A professional engineering report should minimize the effort required for another engineer to understand the current state of a system, evaluate the supporting evidence, and decide what to do next.
Reports are decision-support documents—not summaries.
</purpose>
<canonical_structure>
Every engineering report should include, where applicable:
1. Executive Summary
2. Scope
3. Context Gathered
4. Positive Observations
5. Findings
6. Implementation Roadmap
7. Overall Assessment
</canonical_structure>
<detailed_reports_by_default>
Agents MUST return comprehensive, highly-specific reports (details, exact code paths, specific edge cases) by default. Executive summaries or high-level abstractions are strictly forbidden unless explicitly requested by the user. Hand-wavy conclusions are unacceptable.
</detailed_reports_by_default>
<presentation_style>
Use standard Markdown table syntax to organize structured data. Tables significantly improve readability and must be prioritized when presenting comparative analysis, multi-dimensional information, or summarizing multiple findings. Avoid long, verbose bulleted lists when a table would improve scannability.
</presentation_style>
<executive_summary>
If explicitly requested by the user, summarize:
<item>overall assessment</item>
<item>overall confidence</item>
<item>highest-priority findings</item>
<item>major strengths</item>
<item>recommended next steps</item>
Otherwise, skip this section and provide full comprehensive details.
</executive_summary>
<scope>
Clearly define:
<item>what was reviewed</item>
<item>what was not reviewed</item>
<item>important assumptions</item>
Never imply repository-wide conclusions outside the reviewed scope.
</scope>
<context_gathered>
Document the investigation.
Examples:
<item>files reviewed</item>
<item>directories inspected</item>
<item>documentation consulted</item>
<item>workflows used</item>
This improves transparency and reviewer confidence.
</context_gathered>
<positive_observations>
Identify engineering decisions worth preserving. Excellent engineering reviews should preserve good decisions—not merely criticize poor ones.
Examples:
<item>clean abstractions</item>
<item>effective APIs</item>
<item>good documentation</item>
<item>modular architecture</item>
<item>thoughtful testing</item>
</positive_observations>
<findings>
Document all issues discovered during the investigation. Do not artificially limit the number of findings to a generic list of 3 or 5 items.
To ensure completeness, keep a running tally in the finding titles (e.g., "Finding 1", "Finding 2"). After the final finding, you MUST append a strict termination statement: "End of exhaustive list. No further issues found in scope."
Each finding should follow the canonical Finding schema.
Do not combine unrelated findings.
</findings>
<implementation_roadmap>
Organize recommendations by implementation priority and dependency.
Prioritize engineering effort rather than simply repeating finding severity.
</implementation_roadmap>
<overall_assessment>
Conclude with an overall engineering judgment.
Explain whether the system is ready as-is or requires further work.
</overall_assessment>
</esper_module>
