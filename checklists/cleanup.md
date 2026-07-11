---
name: Cleanup
---

<esper_module type="checklist">
<purpose>
Ensure the workspace remains pristine by enforcing a strict cleanup protocol for temporary files, diagnostic scripts, and scratchpads generated during an engineering task.
</purpose>
<when_to_use>
<item>At the conclusion of any workflow that generates temporary or diagnostic files.</item>
</when_to_use>
<instructions>
<execution_steps>
<step>Location Restriction: All temporary files, scratchpads, and diagnostic scripts MUST be created exclusively within the `.esper/shared_context/scratch/` directory. Do not pollute the main codebase directory.</step>
<step>Mandatory Deletion: Before completing your task, you MUST delete all files you created in `.esper/shared_context/scratch/`.</step>
<step>Utility Preservation: If you believe a diagnostic script or utility file you wrote would be highly valuable for the user in the future (e.g., a complex debugging script or a custom repository visualization tool):</step>
- Do NOT delete it immediately.
- Explicitly prompt the user explaining why it is useful.
- Ask for permission to keep it.
- If the user agrees, move the file into the `.esper/utils/` directory.
<step>Final Check: Validate that no stray files were left behind in the project working tree before summarizing your work.</step>
</execution_steps>
</instructions>
</esper_module>
