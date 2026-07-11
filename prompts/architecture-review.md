---
name: Architecture Review
---

<esper_module type="prompt">
  <title>Architecture Review Prompt</title>
  <purpose>Evaluate architectural quality.</purpose>
  <when_to_use>
    <item>conducting architecture reviews</item>
    <item>evaluating system design</item>
  </when_to_use>
  <instructions>
    <item>Review the implementation from an architectural perspective.</item>
    <item>Follow the Architecture Review workflow.</item>
    <item>Use the Architecture Review template.</item>
  </instructions>
  <dependencies>
<required>
    <item>workflows/agent-communication.md</item>
    <item>workflows/architecture-review.md</item>
    <item>workflows/revision.md</item>
    <item>templates/architecture-review.md</item>
  </required>
  <optional>
    <item>workflows/delegation.md</item> <!-- for broad systems requiring partitioned review -->
  </optional>
</dependencies>
</esper_module>
