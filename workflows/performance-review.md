---
name: Performance Review
---

<esper_module type="workflow">
<purpose>
Analyze performance characteristics systematically.
</purpose>
<when_to_use>
<item>profiling code</item>
<item>investigating latency issues</item>
<item>reviewing performance-sensitive changes</item>
</when_to_use>
<instructions>
<execution_steps>
<step>Understand the performance requirements and baseline.</step>
<step>Measure before assuming bottlenecks.</step>
<step>Evaluate the following systematically:</step>
- algorithmic complexity
- memory allocations
- I/O overhead
- concurrency and synchronization
- caching strategies
<step>Verify edge cases where performance might degrade non-linearly.</step>
<step>Surface assumptions and potential trade-offs (e.g., speed vs. memory).</step>
</execution_steps>
</instructions>
<dependencies>
<required>
<item>workflows/memory-management.md</item>
<item>checklists/cleanup.md</item>
<item>checklists/performance.md</item>
<item>checklists/self-review.md</item>
<item>workflows/revision.md</item>
</required>
<canonical_sources>
<item>principles/performance.md</item>
</canonical_sources>
</dependencies>
</esper_module>
