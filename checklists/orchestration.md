---
name: Orchestration
description: A quality gate for validating and integrating work performed by delegated subagents.
---

<esper_module type="checklist">
<purpose>
Ensure that work produced by subagents is rigorously validated, properly integrated, and meets the quality standards of the primary agent before finalization.
</purpose>
<quality_gates>
Before integrating a subagent's deliverable, verify the following:
<item uncompleted="true">Evidence: Are the subagent's findings and implementations supported by documented evidence rather than assumptions?</item>
<item uncompleted="true">Scope: Did the subagent stay within its assigned context boundaries without performing duplicated or unauthorized work?</item>
<item uncompleted="true">Context Transfer: Were the subagent's assumptions and unresolved questions clearly surfaced to the primary agent?</item>
<item uncompleted="true">Integration: Does the delegated work integrate cleanly with the primary objective and other subagents' work?</item>
<item uncompleted="true">Conflict Resolution: Have all contradictions or disagreements between subagents been explicitly resolved into a single consensus?</item>
<item uncompleted="true">Confidence: Is the confidence level of the delegated work preserved and communicated in the final integration?</item>
<item uncompleted="true">Context Cleanliness: Were subagents used for 'dirty work' (like bulk file editing) or 'research' (like sweeping directories) to keep the main chat context clean?</item>
</quality_gates>
<dependencies>
<canonical_sources>
<item>principles/delegation.md</item>
</canonical_sources>
</dependencies>
</esper_module>
