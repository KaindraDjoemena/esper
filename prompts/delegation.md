---
name: Orchestration
---

<esper_module type="prompt">
  <title>Orchestration Prompt</title>
  <purpose>Coordinate massive parallel operations across multiple agents.</purpose>
  <when_to_use>
    <item>massive repository audits</item>
    <item>parallel test generation</item>
    <item>architecture-wide refactoring</item>
  </when_to_use>
  <instructions>
    <item>As the parent agent, you must remain high-level and orchestrate the process. Delegate the 'dirty work'—such as deep research and detailed implementation—to specialized subagents.</item>
    <item>CRITICAL: Whenever tasks are independent and parallelizable, ALWAYS prompt the user first to ask if they want to use a concurrent subagent workflow.</item>
    <item>Define the mission and delegate it into mutually exclusive, collectively exhaustive sub-tasks. Spin up parallel subagents for each task. Aggregate their output using the Synthesis template.</item>
  </instructions>
  <dependencies>
<required>
    <item>workflows/agent-communication.md</item>
    <item>workflows/delegation.md</item>
    <item>templates/synthesis.md</item>
    <item>templates/shared-scratchpad.md</item>
    <item>checklists/automation-safety.md</item>
  </required>
</dependencies>
</esper_module>
