---
name: Testing
---

<esper_module type="workflow">
<purpose>
Evaluate confidence in the implementation.
</purpose>
<when_to_use>
<item>writing new tests</item>
<item>reviewing existing test suites</item>
</when_to_use>
<instructions>
Review:
<item>existing tests</item>
<item>missing coverage</item>
<item>edge cases</item>
<item>failure scenarios</item>
Recommend tests that meaningfully increase confidence.
Avoid suggesting tests with little practical value.
</instructions>
<dependencies>
<required>
<item>checklists/cleanup.md</item>
<item>checklists/testing.md</item>
</required>
<canonical_sources>
<item>principles/testing.md</item>
</canonical_sources>
</dependencies>
</esper_module>
