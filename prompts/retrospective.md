---
name: Retrospective
---

<esper_module type="prompt">
  <title>Retrospective Prompt</title>
  <purpose>Trigger a systemic self-evaluation of the agent's recent performance.</purpose>
  <instructions>
    <item>Review recent transcripts or scratchpads. Identify consistent failure modes, logic gaps, or hallucinations. Generate a report detailing the root causes and recommend structural updates to Esper's principles or checklists.</item>
  </instructions>
  <dependencies>
<required>
    <item>workflows/agent-communication.md</item>
    <item>workflows/revision.md</item>
    <item>templates/research-report.md</item>
  </required>
</dependencies>
</esper_module>
