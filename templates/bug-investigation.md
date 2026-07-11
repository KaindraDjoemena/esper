---
name: Bug Investigation
---

<esper_module type="template">
<purpose>
Document the root cause of a bug, the evidence supporting the conclusion, and the recommended fix.
</purpose>
<when_to_use>
<item>debugging</item>
<item>incident response</item>
<item>bug fixing</item>
</when_to_use>
<output_format>

## Deliverable Structure

### Problem

Describe the reported issue.

### Evidence

- Error messages
- Logs
- Stack traces
- Relevant code

### Root Cause

Explain what actually caused the issue.

### Why It Happened

Describe the sequence of events.

### Recommended Fix

Explain the preferred solution.

### Regression Prevention

Suggest:

- tests
- validation
- architectural improvements

</output_format>
<dependencies>
<canonical_sources>
<item>principles/reporting/findings.md</item>
<item>principles/reporting/taxonomy.md</item>
<item>principles/reporting/rubric.md</item>
</canonical_sources>
</dependencies>
</esper_module>
