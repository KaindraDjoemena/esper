---
name: Technical Research
---

<esper_module type="prompt">
  <title>Technical Research Prompt</title>
  <purpose>Investigate a technical topic.</purpose>
  <when_to_use>
    <item>evaluating tools</item>
    <item>learning system behaviors</item>
  </when_to_use>
  <instructions>
    <item>Research the requested topic.</item>
    <item>Use the Research Report template.</item>
  </instructions>
  <dependencies>
<required>
    <item>workflows/agent-communication.md</item>
    <item>workflows/research.md</item>
    <item>workflows/revision.md</item>
    <item>templates/research-report.md</item>
  </required>
  <optional>
    <item>workflows/orchestration.md</item> <!-- for broad topics requiring parallel investigation -->
  </optional>
</dependencies>
</esper_module>
