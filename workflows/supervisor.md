---
name: Supervisor Architecture
---

<esper_module type="workflow">
<purpose>
Instructs the parent agent to act as a Supervisor, decoupling planning from execution using a Graph-based state machine and A2A JSON contracts.
</purpose>
<when_to_use>
<item>complex operations requiring plan-and-execute decoupling</item>
<item>workflows demanding strict state checkpointing and graph routing</item>
</when_to_use>
<instructions>
<subsection>1. Plan Phase</subsection>
The Supervisor must decompose the user request into a strict plan of execution steps. Each step must be formatted into the Agent-to-Agent (A2A) data contract specified in `templates/a2a-contract.json`.
<subsection>2. Route Tasks</subsection>
Use the deterministic state machine defined in `scripts/workflow_engine.py` to route tasks. Pass the A2A JSON payloads to the engine for state management.
<subsection>3. Execute Phase</subsection>
Delegate the execution of each step to specialized subagents. The subagents will receive the `payload` from the A2A contract and return their results in the same structured format.
<subsection>4. State Checkpointing</subsection>
Ensure the `workflow_engine.py` saves the state to `.esper/shared_context/checkpoints/` after each node execution to maintain determinism and allow for recovery.
<subsection>5. Synthesis</subsection>
Once the execution graph terminates successfully (without hitting infinite loops), synthesize the final outputs from the A2A contracts and present them to the user.
</instructions>
<dependencies>
<required>
<item>checklists/zero-trust.md</item>
<item>workflows/orchestration.md</item>
<item>templates/a2a-contract.json</item>
<item>workflows/evaluator.md</item>
</required>
</dependencies>
</esper_module>
