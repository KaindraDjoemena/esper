---
name: Explain
---

<esper_module type="workflow">
<purpose>
Produce a clear, accurate, and structured explanation of an implementation.
</purpose>
<when_to_use>
<item>explaining code</item>
<item>onboarding to a new codebase</item>
<item>understanding system architecture</item>
</when_to_use>
<instructions>
<execution_steps>
<step>Understand the Request: Identify what the user specifically wants to understand.</step>
<step>Gather Context: Read the relevant implementation, tests, and documentation. Do not assume behavior without evidence.</step>
<step>High-Level Overview: Summarize the purpose and architecture of the implementation.</step>
<step>Component Analysis: Identify and explain the most important components and their responsibilities.</step>
<step>Interaction Analysis: Explain how the components interact to achieve the overall goal.</step>
Focus on helping the reader build a mental model rather than providing a line-by-line translation of the code.
</execution_steps>
</instructions>
<dependencies>
<required>
<item>workflows/memory-management.md</item>
<item>checklists/cleanup.md</item>
<item>checklists/self-review.md</item>
<item>workflows/revision.md</item>
</required>
<canonical_sources>
<item>principles/communication.md</item>
</canonical_sources>
</dependencies>
</esper_module>
