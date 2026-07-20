---
name: Security
keywords: [security, hack, exploit, auth, vulnerability, safe]
---

<esper_module type="principle">
<purpose>
Ensure software is resilient against malicious activity and data breaches.
</purpose>
<instructions>
Security should be considered by default rather than added later.
Prefer secure defaults.
Validate data at system boundaries.
Treat external input as untrusted.
Avoid leaking:
<item>secrets</item>
<item>credentials</item>
<item>internal implementation details</item>
<item>sensitive user information</item>
Apply the principle of least privilege.
Prefer defense in depth over relying on a single protective measure.
When reviewing security, prioritize practical risks over theoretical concerns.
</instructions>
<dependencies>
<canonical_sources>
<item>principles/engineering.md</item>
</canonical_sources>
</dependencies>
</esper_module>
