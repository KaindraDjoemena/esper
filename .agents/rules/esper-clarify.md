---
name: Esper Clarify
description: Human-in-the-Loop Clarification rule to resolve ambiguity safely.
always_on: true
---
<esper_module type="rule">
  <metadata>
    <name>Clarify</name>
    <purpose>To ensure explicit user permission and clarity before proceeding with any action, acting as a Human-in-the-Loop safeguard for Esper operations.</purpose>
  </metadata>
  <instructions>
    <execution_steps>
      <step>Detect Ambiguity: Monitor user prompts for vagueness, unspecified requirements, or ambiguous intent.</step>
      <step>Pause Execution: If ambiguity is detected or a significant, destructive, or complex action is requested without prior confirmation, immediately pause execution. Do not proceed with code changes.</step>
      <step>Generate Confirming Questions: Formulate concise, clear Confirming Questions to resolve the ambiguity. You MUST use the native `ask_question` interactive modal tool to format these questions.</step>
      <step>Wait for Permission: Do not proceed until explicit user confirmation and answers to the questions have been received.</step>
    </execution_steps>
  </instructions>
</esper_module>
