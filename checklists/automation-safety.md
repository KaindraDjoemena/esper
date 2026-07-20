---
name: Automation Safety
---

<esper_module type="checklist">
<purpose>
Provide strict quality gates before executing bulk transformations or automated mechanical refactorings.
</purpose>
<when_to_use>
<item>running automated refactoring scripts</item>
<item>applying bulk structural changes across the repository</item>
</when_to_use>
<checklist>
<item uncompleted="true">Has the target scope been explicitly constrained to prevent unintended modifications?</item>
<item uncompleted="true">Were the changes validated incrementally on a subset of the codebase before running the bulk operation?</item>
<item uncompleted="true">**CRITICAL HITL GOVERNANCE**: For any action flagged as high-risk by `scripts/policy_gate.py`, you MUST strictly use the native `ask_question` interactive modal tool to secure undeniable user approval *before* executing the action.</item>
<item uncompleted="true">Can the resulting changes be deterministically verified via the test suite or manual inspection?</item>
<item uncompleted="true">Is there a clear rollback strategy if the automation introduces regressions?</item>
</checklist>
<dependencies>
<canonical_sources>
<item>principles/automation-safety.md</item>
</canonical_sources>
</dependencies>
</esper_module>
