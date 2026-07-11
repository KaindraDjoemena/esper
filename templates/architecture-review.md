---
name: Architecture Review
---

<esper_module type="template">
<purpose>
Evaluate how well an implementation aligns with the existing architecture and identify opportunities for improvement.
</purpose>
<when_to_use>
<item>architecture review</item>
<item>design review</item>
<item>refactoring discussion</item>
<item>large feature implementation</item>
</when_to_use>
<output_format>

## Deliverable Structure

Follow the canonical Report Structure.

Include the following architecture-specific sections:

### Architectural Strengths

Identify design decisions that positively contribute to:

- maintainability
- extensibility
- readability
- testability
- separation of concerns

Explain *why* they are effective.

### Dependency Analysis

Evaluate:

- dependency direction
- unnecessary dependencies
- circular dependencies
- hidden coupling
- opportunities for simplification

### Consistency

Evaluate whether the implementation follows existing project conventions.

If it intentionally deviates, explain whether the deviation appears justified.

### Long-Term Considerations

Discuss:

- maintainability
- extensibility
- operational complexity
- future development cost

Avoid speculative concerns that are unsupported by the implementation.

</output_format>
<dependencies>
<canonical_sources>
<item>principles/reporting/report-structure.md</item>
<item>principles/reporting/findings.md</item>
</dependencies>
</canonical_sources>
</esper_module>
