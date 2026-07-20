---
name: Refactoring
---

<esper_module type="workflow">
<purpose>
Improve code quality while preserving behavior.
</purpose>
<when_to_use>
<item>cleaning up code</item>
<item>paying down technical debt</item>
<item>preparing for a new feature</item>
</when_to_use>
<instructions>
<item>Understand the existing implementation.</item>
<item>Preserve observable behavior.</item>
<item>Prefer incremental improvements.</item>
<item>Avoid mixing feature work with refactoring.</item>
<item>Reduce complexity without introducing unnecessary abstraction.</item>
<item>Keep changes easy to review.</item>
<item>CRITICAL: Draft a refactoring plan and ask the user for confirmation BEFORE executing any code changes.</item>
</instructions>
<dependencies>
<required>
<item>workflows/memory-management.md</item>
<item>checklists/cleanup.md</item>
<item>checklists/self-review.md</item>
<item>checklists/automation-safety.md</item>
<item>workflows/revision.md</item>
</required>
<canonical_sources>
<item>principles/refactoring.md</item>
</canonical_sources>
</dependencies>
</esper_module>
