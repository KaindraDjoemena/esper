---
name: Delegation
---

<esper_module type="principle">
<purpose>
Provide canonical guidance on when and how to delegate engineering tasks to subagents to execute complex work efficiently without duplicating effort or bloating context.
</purpose>
<instructions>
<subsection>Decompose by Domain Boundaries</subsection>
Partition tasks along natural architectural or functional boundaries. Delegate independent investigations, parallel research, or isolated component implementations. Avoid delegating highly coupled work where constant coordination is required.
<subsection>Inherit, Don't Bootstrap</subsection>
A delegated agent should not have to rediscover the workspace. The primary agent must transfer the necessary context:
<item>The specific objective of the delegated task</item>
<item>The active workflow and relevant principles</item>
<item>Gathered evidence and constraints</item>
<item>Known assumptions</item>
<subsection>Strict Context Boundaries</subsection>
Transfer only the context necessary for the subagent to succeed.
<item>Required Context: Objective, constraints, and relevant evidence.</item>
<item>Optional Context: Surrounding architecture if it impacts the implementation.</item>
<item>Disposable Context: Early speculative hypotheses or unrelated project history should be omitted to minimize context window bloat.</item>
<subsection>Avoid Duplicated Investigation</subsection>
Ensure subagents have mutually exclusive responsibilities. Two subagents should not be asked to research the same codebase area or solve the same problem concurrently unless explicitly designed as a comparative exercise.
<subsection>Validate Before Integration</subsection>
Never blindly accept a subagent's output. The primary agent is responsible for validating that the subagent's findings are supported by evidence, assumptions are documented, and unresolved questions are surfaced before integrating the work into the final deliverable.
<subsection>Conflict Resolution & Consensus</subsection>
When subagents disagree (e.g., conflicting architectural or performance recommendations), the primary agent acts as the final decision-maker. The primary agent must evaluate the competing evidence, resolve the contradiction, and form a consensus rather than presenting conflicting options to the user.
<subsection>Shared Evidence</subsection>
If multiple subagents require access to the same evolving information, establish a centralized shared artifact (e.g., a scratchpad) to collect and distribute evidence, preventing fragmented or duplicated research.
</instructions>
<dependencies>
<canonical_sources>
<item>principles/engineering.md</item>
</canonical_sources>
</dependencies>
</esper_module>
