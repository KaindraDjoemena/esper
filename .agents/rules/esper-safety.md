---
name: Esper Safety Gate
description: Enforces automation safety and explicit user approval before execution.
always_on: true
---
<esper_module type="rule">
  <metadata>
    <name>Safety Gate</name>
    <purpose>Ensures safe bulk operations by enforcing explicit user approvals before performing wide-sweeping or irreversible changes.</purpose>
  </metadata>
  <instructions>
    <execution_steps>
      <step>Intercept Execution: Pause execution before any destructive, bulk modification, or scaffolding operation.</step>
      <step>Present Plan: Provide the user with a clear, incremental plan or blueprint of the proposed changes based on C:/Users/KD/.gemini/esper/principles/automation-safety.md.</step>
      <step>Await Approval: Require explicit user confirmation before proceeding.</step>
      <step>Validation: Ensure changes are validated incrementally.</step>
    </execution_steps>
  </instructions>
</esper_module>
