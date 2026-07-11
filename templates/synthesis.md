---
name: Synthesis Template
---

<esper_module type="template">
<purpose>
Synthesize multiple subagent reports into a single, cohesive master document.
</purpose>
<conflict_resolution>
When synthesizing subagent findings, if multiple subagents report opposing evidence on the same code path, explicitly document the contradiction in the "Subagent Findings" section and prioritize the finding with the most concrete code-path evidence. Do not drop contradictory findings.
</conflict_resolution>
<output_format>

## Structure
1. Methodology
2. Subagent Findings (Aggregated)
3. Overall Master Roadmap
4. Conclusion

</output_format>
<dependencies>
<canonical_sources>
<item>principles/reporting/report-structure.md</item>
<item>principles/reporting/findings.md</item>
</canonical_sources>
</dependencies>
</esper_module>
