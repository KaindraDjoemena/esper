---
name: Architecture Review
---

<esper_module type="workflow">
<purpose>
Evaluate how well the implementation fits the project's architecture.
</purpose>
<when_to_use>
<item>conducting architecture reviews</item>
<item>evaluating system design</item>
</when_to_use>
<instructions>
<item>Understand the existing architecture before recommending changes.</item>
<item>Use the `esp-rag` skill for text retrieval and the `esp-graph` skill for relationship traversal to map out architectural dependencies (implementing the GraphRAG paradigm).</item>
<item>Identify architectural boundaries.</item>
<item>Evaluate cohesion and coupling.</item>
<item>Look for unnecessary abstractions.</item>
<item>Consider scalability, extensibility, and maintainability.</item>
<item>Generate alternative architectural approaches and analyze their trade-offs.</item>
<item>Actively search for contradictions or evidence that challenges your initial assessment.</item>
<item>Explain tradeoffs rather than declaring one solution universally correct.</item>
<item>Recommend architectural changes only when they provide clear long-term value.</item>
</instructions>
<dependencies>
<required>
<item>workflows/memory-management.md</item>
<item>checklists/cleanup.md</item>
<item>checklists/architecture.md</item>
</required>
<canonical_sources>
<item>principles/architecture.md</item>
</canonical_sources>
</dependencies>
</esper_module>
