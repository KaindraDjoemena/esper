---
name: Code Review
---

<esper_module type="prompt">
  <title>Code Review Prompt</title>
  <purpose>Review recent code changes for correctness, maintainability, and security.</purpose>
  <when_to_use>
    <item>peer code review</item>
    <item>pull request review</item>
  </when_to_use>
  <instructions>
    <item>Perform a comprehensive review.</item>
    <item>Follow the Code Review workflow.</item>
    <evaluate>
      <item>correctness</item>
      <item>security</item>
      <item>maintainability</item>
      <item>performance</item>
      <item>API design</item>
      <item>project consistency</item>
    </evaluate>
    <item>Use the Code Review template.</item>
  </instructions>
  <dependencies>
<required>
    <item>workflows/agent-communication.md</item>
    <item>workflows/code-review.md</item>
    <item>templates/code-review.md</item>
  </required>
</dependencies>
</esper_module>
