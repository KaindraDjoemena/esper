---
name: Audit Report
---

<esper_module type="template">
<purpose>
Provide a comprehensive review of code changes or system state, highlighting risks, strengths, and recommendations.
</purpose>
<when_to_use>
<item>code audit</item>
<item>pull request review</item>
<item>security review</item>
</when_to_use>
<output_format>

## Deliverable Structure

Follow the canonical Report Structure.

Ensure exhaustive coverage of the reviewed scope. Do not artificially limit the findings section to a small list.

When documenting findings, consider these audit-specific categories:

- Correctness
- Security
- Performance
- Maintainability
- API Design
- Testing

</output_format>
<dependencies>
<canonical_sources>
<item>principles/reporting/report-structure.md</item>
<item>principles/reporting/findings.md</item>
<item>principles/reporting/rubric.md</item>
</canonical_sources>
</dependencies>
</esper_template>
