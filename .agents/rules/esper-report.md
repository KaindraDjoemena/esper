---
name: Esper Reporting Taxonomy
description: Formats outputs using Esper's unified reporting taxonomy.
always_on: true
---
<esper_module type="rule">
  <metadata>
    <name>Reporting Taxonomy</name>
    <purpose>Standardizes reporting formats across all Esper agents to ensure consistent taxonomy (Severity, Confidence) and structural schemas.</purpose>
  </metadata>
  <instructions>
    <execution_steps>
      <step>Analyze Input: Receive raw findings or data from other skills.</step>
      <step>Apply Taxonomy: Categorize findings using the official Severity scale (Critical, High, Medium, Low, Nit) and Confidence scale (Confirmed, Likely, Speculative) according to C:/Users/KD/.gemini/esper/principles/reporting/taxonomy.md.</step>
      <step>Format Output: Structure the final artifact using the canonical reporting schemas.</step>
    </execution_steps>
  </instructions>
</esper_module>
