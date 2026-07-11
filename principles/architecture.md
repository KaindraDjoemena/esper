---
name: Architecture
---

<esper_module type="principle">
<purpose>
Guide system design to be maintainable, cohesive, and resilient to change.
</purpose>
<instructions>
Architecture exists to make change easier.
Prefer designs that:
<item>separate responsibilities clearly</item>
<item>reduce coupling</item>
<item>increase cohesion</item>
<item>improve maintainability</item>
<item>make dependencies explicit</item>
Favor extending existing architecture over replacing it.
Introduce new abstractions only when they clearly simplify the system or solve repeated problems.
Avoid unnecessary layers whose primary purpose is theoretical flexibility.
</instructions>
<dependencies>
<canonical_sources>
<item>principles/engineering.md</item>
</canonical_sources>
</dependencies>
</esper_module>
