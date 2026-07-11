---
name: Code Review
---

<esper_module type="template">
<purpose>
Provide structured feedback on code changes to ensure correctness, security, performance, and maintainability.
</purpose>
<when_to_use>
<item>pull request reviews</item>
<item>peer reviews</item>
<item>code audits</item>
</when_to_use>
<output_format>

## Deliverable Structure

Follow the canonical Report Structure.

When documenting findings, consider these specific review areas:

### Correctness
Verify the logic meets requirements and handles edge cases.

### Security
Identify potential vulnerabilities or unsafe practices.

### Performance
Highlight inefficient algorithms or resource usage.

### Maintainability
Evaluate code clarity, coupling, and modularity.

### Testing
Ensure sufficient test coverage and quality.

</output_format>
<dependencies>
<canonical_sources>
<item>principles/reporting/report-structure.md</item>
<item>principles/reporting/findings.md</item>
</canonical_sources>
</dependencies>
</esper_module>
