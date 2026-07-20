---
name: Code Writing
---

<esper_module type="workflow">
<purpose>
Produce code that integrates naturally into the existing project.
</purpose>
<when_to_use>
<item>implementing features</item>
<item>writing scripts</item>
<item>modifying existing code</item>
</when_to_use>
<instructions>
<subsection>1. Understand the task</subsection>
Clarify:
<item>what problem is being solved</item>
<item>expected behavior</item>
<item>constraints</item>
<item>success criteria</item>
<subsection>2. Gather context</subsection>
Read:
<item>related implementation</item>
<item>interfaces</item>
<item>shared utilities</item>
<item>surrounding architecture</item>
<item>existing patterns</item>
Do not begin designing until sufficient context has been gathered.
<subsection>3. Identify conventions</subsection>
Reuse:
<item>naming</item>
<item>folder organization</item>
<item>architecture</item>
<item>abstractions</item>
<item>error handling</item>
<item>dependency injection</item>
<item>testing patterns</item>
Consistency is generally preferable to novelty.
<subsection>4. Design</subsection>
<item>Generate alternative solutions before committing to an approach.</item>
<item>Explain trade-offs between approaches.</item>
<item>Verify assumptions against existing code.</item>
Prefer:
<item>minimal changes</item>
<item>localized modifications</item>
<item>readable implementations</item>
<item>reusable components</item>
Avoid speculative abstractions.
<subsection>5. Validate mentally</subsection>
Before presenting code, verify:
<item>edge cases</item>
<item>failure paths</item>
<item>nullability</item>
<item>async behavior</item>
<item>error handling</item>
<item>compatibility with surrounding code</item>
<subsection>6. Ask for Confirmation</subsection>
Before executing any changes, present your proposed design and implementation plan to the user.
Stop and wait for explicit confirmation from the user before writing any code.
<subsection>7. Execute and Summarize</subsection>
Once approved, execute the plan.
Explain:
<item>what was changed</item>
<item>why the implementation fits</item>
<item>tradeoffs</item>
<item>assumptions</item>
If uncertain, state the uncertainty.
</instructions>
<dependencies>
<required>
<item>workflows/memory-management.md</item>
<item>checklists/cleanup.md</item>
<item>workflows/revision.md</item>
<item>checklists/feature.md</item>
<item>checklists/automation-safety.md</item>
</required>
<canonical_sources>
<item>principles/engineering.md</item>
</canonical_sources>
</dependencies>
</esper_module>
