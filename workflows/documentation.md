---
name: Documentation
---

<esper_module type="workflow">
<purpose>
Produce documentation that accurately reflects the implementation.
</purpose>
<when_to_use>
<item>writing documentation</item>
<item>reviewing documentation</item>
</when_to_use>
<instructions>
<subsection>1. Read implementation</subsection>
Read relevant source files before documenting behavior.
Documentation should describe reality.
<subsection>2. Separate facts</subsection>
Differentiate:
<item>observed behavior</item>
<item>inferred behavior</item>
<item>assumptions</item>
Never present assumptions as facts.
<subsection>3. Explain intent</subsection>
Focus on:
<item>why</item>
<item>when</item>
<item>constraints</item>
Avoid narrating obvious code.
<subsection>4. Use examples</subsection>
Whenever practical, derive examples from the implementation.
<subsection>5. Keep documentation maintainable</subsection>
Prefer concise explanations.
Avoid repeating information already expressed clearly in code.
</instructions>
<dependencies>
<required>
<item>workflows/memory-management.md</item>
<item>checklists/cleanup.md</item>
<item>checklists/documentation.md</item>
<item>workflows/revision.md</item>
</required>
</dependencies>
</esper_module>
