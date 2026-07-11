---
name: Automation Safety
---

<esper_module type="principle">
<purpose>
Establish safety constraints for bulk codebase transformations.
</purpose>
<instructions>
When performing bulk transformations or mechanical refactoring:
<item>Validate changes incrementally rather than relying entirely on bulk execution.</item>
<item>Require explicit user approval before performing irreversible operations.</item>
<item>Ensure that the final result is verified through tests or manual validation.</item>
<item>Avoid wide-sweeping automated refactorings without strong evidence of safety.</item>
</instructions>
<dependencies>
<canonical_sources>
<item>principles/engineering.md</item>
</canonical_sources>
</dependencies>
</esper_module>
