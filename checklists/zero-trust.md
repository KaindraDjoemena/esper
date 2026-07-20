---
name: Zero Trust Agent Identity
---

<esper_module type="checklist">
<purpose>
Enforce strict role scopes and identity bounds for all subagents to maintain zero trust security.
</purpose>
<when_to_use>
<item>spawning or configuring subagents</item>
<item>designing multi-agent workflows</item>
</when_to_use>
<instructions>
<subsection>Role Scopes</subsection>
<item uncompleted="true">Assign the narrowest possible permissions for each subagent based on its role (e.g., Code Researcher gets read-only access).</item>
<item uncompleted="true">Verify that subagents do not inherit excessive privileges from their caller implicitly.</item>
<subsection>Default Identity Fallback</subsection>
<item uncompleted="true">**CRITICAL**: The default fallback role for undefined agents MUST be explicitly defined as **Read-Only** (they can see files but cannot modify them).</item>
<item uncompleted="true">Ensure any deviation from the Read-Only default is explicitly documented and authorized.</item>
</instructions>
</esper_module>
