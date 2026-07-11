---
name: Retrieval Philosophy
---

<esper_module type="principle">
<purpose>
Define how engineering knowledge should be discovered, retrieved, and composed by agents to minimize context overhead.
</purpose>
<core_philosophy>
Esper scales through retrieval, not accumulation. Context should be earned, not assumed.
</core_philosophy>
<instructions>
<execution_steps>
<step>Knowledge is Discoverable, Not Preloaded: Agents should discover knowledge via `routing.md` and explicit module relationships. Never load the entire workspace eagerly.</step>
<step>Context is Earned: Do not load modules "just in case." Only load a module when there is concrete evidence that the task requires it.</step>
<step>Incremental Discovery: Start with the absolute minimum set of required modules. Expand context iteratively as the investigation uncovers new requirements or complexities.</step>
<step>Progressive Disclosure: Read interfaces, signatures, and documentation first. Only read deep implementations if the interface is insufficient to answer the current question.</step>
<step>Retrieval Stopping Conditions: Stop gathering context as soon as you have enough evidence to formulate a testable hypothesis or a viable alternative. Only resume retrieval if the hypothesis is disproven.</step>
<step>Context Pruning: Actively discard or deprioritize information that proves irrelevant during investigation to avoid polluting reasoning.</step>
<step>Canonical Sources: Do not duplicate definitions. If a module requires understanding a concept (like "Severity"), it should reference the canonical source. Load the canonical source only if you actually need to apply that concept.</step>
<step>Minimize Overhead: Favor modular composition over monolithic context. The smaller the active context, the sharper the reasoning.</step>
<step>Maximum Traversal Depth: Establish a strict maximum depth for dependency traversal (e.g., do not follow links deeper than 2 or 3 levels from the entry point) to prevent transitive context bloat.</step>
</execution_steps>
</instructions>
<dependencies>
<canonical_sources>
<item>principles/engineering.md</item>
</canonical_sources>
</dependencies>
</esper_module>
