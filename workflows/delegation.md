---
name: Delegation
---

<esper_module type="workflow">
<purpose>
Coordinate complex engineering tasks by planning, decomposing, delegating, and integrating work across multiple agents.
</purpose>
<when_to_use>
<item>implementing large features</item>
<item>performing broad architectural reviews</item>
<item>conducting extensive parallel research</item>
<item>executing multi-phase implementation plans</item>
</when_to_use>
<instructions>
<subsection>1. Plan and Decompose</subsection>
Identify if the task is too large for sequential execution or consists of independent, parallelizable components. The parent agent must remain high-level, orchestrating the effort and synthesizing results. Always delegate 'dirty work' (like deep research, sweeping directories, bulk file editing, or heavy implementation) to specialized subagents to keep the main chat context clean.
CRITICAL: For tasks that are independent and parallelizable, you must ALWAYS prompt the user to confirm whether they want to use a concurrent subagent workflow before proceeding.
Decompose the task into independent, non-overlapping subtasks. Assign Specialized Roles by providing each subagent with a specific prompt as its entry point (e.g., assign `prompts/research.md` to create a Researcher, or `prompts/code-review.md` to create a Reviewer).
<subsection>2. Package Context</subsection>
For each subtask, prepare the specific context the subagent will need:
<item>The exact objective</item>
<item>The required dependencies (workflows, templates)</item>
<item>Existing evidence and constraints</item>
Exclude unnecessary context to preserve reasoning quality.
<subsection>3. Delegate and Execute</subsection>
Invoke the subagents with their partitioned tasks and packaged context. Ensure each subagent has a clear, isolated responsibility.
<subsection>4. Validate</subsection>
When a subagent completes its task, validate its output:
<item>Are the conclusions supported by evidence?</item>
<item>Were the constraints respected?</item>
<item>Are there any new assumptions or unresolved questions introduced?</item>
<subsection>5. Integrate and Review</subsection>
Synthesize the validated findings or code from all subagents into the primary task using a clear Merge Strategy:
<item>For code: Ensure that merged changes from different agents do not create logical contradictions, syntax errors, or overlapping modifications.</item>
<item>For reports: Synthesize findings into a single, unified narrative. Do not simply append subagent reports together.</item>
Perform a final review to ensure the integrated result forms a cohesive, working solution that satisfies the original intent.
</instructions>
<dependencies>
<required>
<item>checklists/cleanup.md</item>
<item>checklists/delegation.md</item>
<item>workflows/revision.md</item>
<item>checklists/automation-safety.md</item>
</required>
<canonical_sources>
<item>principles/delegation.md</item>
</canonical_sources>
</dependencies>
</esper_module>
