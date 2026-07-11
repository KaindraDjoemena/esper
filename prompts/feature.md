---
name: Feature Implementation
---

<esper_module type="prompt">
  <title>Feature Implementation Prompt</title>
  <purpose>Plan and implement a new feature while respecting the existing architecture.</purpose>
  <when_to_use>
    <item>implementing new features</item>
    <item>extending existing functionality</item>
  </when_to_use>
  <instructions>
    <item>Implement the requested feature.</item>
    <item>Follow the Code Writing workflow.</item>
    <item>If requirements are ambiguous, identify the ambiguity before proposing an implementation.</item>
    <item>Use the Implementation Plan template when the feature is non-trivial.</item>
  </instructions>
  <dependencies>
<required>
    <item>workflows/agent-communication.md</item>
    <item>workflows/code-writing.md</item>
    <item>templates/implementation-plan.md</item>
  </required>
  <optional>
    <item>workflows/delegation.md</item> <!-- for large features requiring parallel execution -->
  </optional>
</dependencies>
</esper_module>
