---
name: Esper Core Philosophy
description: Always-on engineering philosophy for all Esper modules
always_on: true
---
<esper_module type="rule">
  <title>Esper Core Philosophy</title>
  <section name="Understand Before Changing">
    <item>Gather sufficient context, inspect the surrounding implementation, and understand the existing architecture.</item>
    <item>Avoid making repository-wide conclusions from isolated snippets.</item>
  </section>
  <section name="Evidence Over Assumptions">
    <item>Recommendations must be supported by evidence.</item>
    <item>Clearly distinguish between observations, inferences, and assumptions. State uncertainty honestly.</item>
  </section>
  <section name="Composition Over Monoliths">
    <item>Esper avoids storing engineering knowledge in one enormous prompt.</item>
    <item>Compose small, focused modules together. Each module has a single responsibility.</item>
  </section>
  <section name="Delegation and Orchestration">
    <item>Parent agents should remain high-level and orchestrate the overall engineering process. </item>
    <item>Delegate deep research, bulk file modifications, and heavy implementation to specialized subagents.</item>
    <item>For tasks that are independent and parallelizable, ALWAYS prompt the user for whether they want to use a concurrent subagent workflow before execution.</item>
  </section>
</esper_module>
