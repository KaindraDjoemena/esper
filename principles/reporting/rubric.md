---
name: Report Quality Rubric
description: Defines the canonical rubric and qualities for evaluating engineering reports.
---

<esper_module type="principle">
<purpose>
A high-quality engineering report enables another engineer to make informed decisions with minimal additional investigation. This rubric provides a standardized method for evaluating engineering reports, ensuring they meet Esper's standards for clarity, rigor, and professionalism.
</purpose>
<characteristics_of_good_reports>
A good report is: evidence-driven, actionable, prioritized, balanced, transparent, technically precise, and honest about uncertainty.
Avoid reports that are: vague, repetitive, unsupported, overly speculative, excessively summarized, lacking prioritization, or missing implementation guidance.
</characteristics_of_good_reports>
<evaluation_criteria>
<subsection>1. Completeness</subsection>
<item>Is the scope explicitly defined?</item>
<item>Are all user requirements or initial prompts addressed?</item>
<item>Is the context gathered documented transparently?</item>
<subsection>2. Evidence Quality</subsection>
<item>Are claims supported by concrete evidence (e.g., code snippets, logs, documentation)?</item>
<item>Are observations clearly distinguished from inferences and assumptions?</item>
<item>Is speculation avoided or explicitly labeled?</item>
<subsection>3. Prioritization</subsection>
<item>Are findings prioritized by engineering impact rather than implementation effort?</item>
<item>Is there a clear roadmap for addressing the most critical issues first?</item>
<item>Are nits and minor issues separated from critical blocking concerns?</item>
<subsection>4. Actionability</subsection>
<item>Do recommendations provide clear, next-step guidance?</item>
<item>Can another engineer begin implementation with minimal clarification?</item>
<item>Are the technical consequences of the findings explained?</item>
<subsection>5. Clarity</subsection>
<item>Is the language concise and technically precise?</item>
<item>Is the report structured logically, making it easy to scan?</item>
<item>Does it avoid generic statements and repetitive phrasing?</item>
<subsection>6. Confidence Communication</subsection>
<item>Is uncertainty stated honestly using the confidence taxonomy (Confirmed, Likely, Speculative)?</item>
<item>Is the overall confidence in the assessment communicated clearly?</item>
<subsection>7. Balanced Assessment</subsection>
<item>Are architectural and engineering strengths identified and documented?</item>
<item>Does the report recognize good decisions worth preserving?</item>
</evaluation_criteria>
<usage>
Use this rubric when reviewing, editing, or producing any engineering deliverable to ensure it reflects the communication standards of a senior engineer. Deliverables should be validated using `checklists/self-review.md`.
</usage>
</esper_module>
