---
name: Esper RPC Protocol
description: Always-on rule enforcing strict XML-based agent-to-agent communication
always_on: true
---
<esper_module type="rule">
  <title>Esper RPC (Remote Procedure Call) Protocol</title>
  <purpose>Enforce strict, standardized communication between parent and child agents to prevent semantic drift, normalize inputs/outputs, and guarantee interoperability.</purpose>
  
  <instructions>
    <item>Whenever you spawn a subagent or communicate with another agent, you MUST format your message using the strict XML `<esper_module type="rule">` schema below.</item>
    <item>Do not use unstructured natural language to assign tasks to subagents.</item>
    <item>The receiving agent MUST strictly conform its response to the JSON schema provided in the `expected_output_schema` property.</item>
  </instructions>

  <protocol_schema>
    <esper_module type="rule">
      <envelope>
        <sender_role>[Your Role]</sender_role>
        <performative>[REQUEST | INFORM | PROPOSE | ERROR]</performative>
        <task_id>[Unique Identifier]</task_id>
      </envelope>
      <payload>
        ```json
        {
          "objective": "[Specific task objective]",
          "constraints": [
            "[Constraint 1]",
            "[Constraint 2]"
          ],
          "expected_output_schema": {
            // Define the exact JSON schema you want the subagent to return
          }
        }
        ```
      </payload>
    </esper_module>
  </protocol_schema>

  <performatives_guide>
    <item><name>REQUEST</name> <usage>Ask a subagent to perform a task.</usage></item>
    <item><name>INFORM</name> <usage>Provide data or results back to the parent agent.</usage></item>
    <item><name>PROPOSE</name> <usage>Submit a plan for approval before execution.</usage></item>
    <item><name>ERROR</name> <usage>Report a failure or inability to complete the task.</usage></item>
  </performatives_guide>
</esper_module>
