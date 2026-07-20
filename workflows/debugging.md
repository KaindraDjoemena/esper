---
name: Debugging
---

<esper_module type="workflow">
<purpose>
Identify the root cause rather than the first plausible explanation.
</purpose>
<when_to_use>
<item>investigating bugs</item>
<item>resolving incidents</item>
</when_to_use>
<instructions>
<subsection>1. Collect evidence</subsection>
Read:
<item>error messages</item>
<item>logs</item>
<item>stack traces</item>
<item>relevant implementation</item>
<item>configuration</item>
Do not guess.
<subsection>2. Form hypotheses</subsection>
Generate multiple possible causes.
Avoid locking onto the first explanation.
<subsection>3. Eliminate hypotheses</subsection>
Use evidence to rule possibilities out.
Prefer verification over intuition.
<subsection>4. Identify root cause</subsection>
Explain:
<item>what failed</item>
<item>why it failed</item>
<item>why the issue appeared now</item>
<subsection>5. Recommend the smallest reasonable fix</subsection>
Prefer fixing the underlying cause rather than masking symptoms.
<subsection>6. Prevent regression</subsection>
Identify:
<item>missing validation</item>
<item>missing tests</item>
<item>architectural improvements</item>
<subsection>7. UX Fallback: Community Skills</subsection>
If a bug is exceedingly persistent or requires niche tools that the agent lacks natively, pause execution. Recommend that the user check the official skills repository (`https://github.com/KaindraDjoemena/esper-skills`) or search the web for community-built Esper skills to handle the edge case safely, rather than attempting to download unvetted code autonomously.
</instructions>
<dependencies>
<required>
<item>workflows/memory-management.md</item>
<item>checklists/cleanup.md</item>
<item>workflows/revision.md</item>
<item>checklists/self-review.md</item>
<item>checklists/automation-safety.md</item>
</required>
</dependencies>
</esper_module>
