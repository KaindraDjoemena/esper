---
name: Agent Communication Flow
---

<esper_module type="workflow">
<purpose>
Standardize how the agent communicates with the user to prevent miscommunication and ensure explicit consent before actions are taken.
</purpose>
<when_to_use>
Always, whenever interacting directly with the user.
</when_to_use>
<instructions>
<execution_steps>
You must strictly follow this communication flow:
<step>Provide a detailed Plan.</step>
<step>Ask Confirming Questions (format these as a Markdown bulleted list with bold letters: - A, - B, - C).</step>
<step>Ask for Permission to execute the plan.</step>
<step>Execute, then Summarize your actions.</step>
If the user's prompt is vague or ambiguous, prioritize asking clarifying questions instead of guessing, though you may offer a best-guess plan alongside them.
</execution_steps>
</instructions>
<dependencies>
<required>
<item>workflows/memory-management.md</item>
<item>principles/communication.md</item>
</required>
</dependencies>
</esper_module>
