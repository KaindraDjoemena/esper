---
name: Security Review
---

<esper_module type="workflow">
<purpose>
Systematically review system posture and identify security risks.
</purpose>
<when_to_use>
<item>security audits</item>
<item>reviewing sensitive changes</item>
</when_to_use>
<instructions>
<execution_steps>
<step>Map the system's trust boundaries and document the security review scope.</step>
<step>Apply input validation principles: confirm all external data is sanitized at system boundaries.</step>
<step>Systematically evaluate:</step>
- authentication mechanisms
- authorization boundaries
- data handling and transit
- secrets and credential hygiene
- exposure surface reduction
<step>Verify that secrets, credentials, and internal implementation details are not inadvertently disclosed.</step>
<step>Provide actionable remediation strategies for identified weaknesses.</step>
</execution_steps>
</instructions>
<dependencies>
<required>
<item>workflows/memory-management.md</item>
<item>checklists/cleanup.md</item>
<item>checklists/security.md</item>
<item>checklists/self-review.md</item>
<item>workflows/revision.md</item>
</required>
<canonical_sources>
<item>principles/security.md</item>
</canonical_sources>
</dependencies>
</esper_module>
