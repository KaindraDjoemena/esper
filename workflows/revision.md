---
name: Revision
---

<esper_module type="workflow">
<purpose>
Enforce a rigorous, observable self-improvement loop. The agent must draft, critique, and verify its own work in an explicit scratchpad before presenting the final deliverable to the user, mimicking how an experienced engineer rigorously reviews a design document before publishing.
</purpose>
<when_to_use>
<item>prior to finalizing any major report, plan, or review</item>
<item>when compiling final recommendations</item>
<item>when accuracy and exhaustiveness are critical</item>
</when_to_use>
<instructions>
<subsection>1. The Scratchpad</subsection>
You must conduct your drafting and verification inside a `<scratchpad>` XML block. Do not attempt to do this "mentally" or implicitly.
<subsection>2. Exploration / Thinking</subsection>
Before drafting, use the `<scratchpad>` to think out loud. Deconstruct the problem context unconditionally, consider edge cases, and organize your thoughts without worrying about formal formatting.
<subsection>3. Draft</subsection>
Still inside the `<scratchpad>`, formulate your initial findings, code, or recommendations based on your exploration. Ensure you are following all explicit exhaustiveness constraints (do not artificially limit your findings).
<subsection>4. Chain-of-Verification (CoVe)</subsection>
Perform a strict verification pass on your draft:
<item>Extract Claims: List the factual claims and technical assertions made in your draft.</item>
<item>Formulate Verification Questions: For each extracted claim, explicitly write a question to test its validity (e.g., "Does `foo.py` actually contain function `bar()`?").</item>
<item>Verify: Answer your verification questions by checking against the source context and codebase.</item>
<item>Mandate Citations: If a claim cannot be backed up by explicit evidence or context, flag it for removal.</item>
<subsection>5. Critique</subsection>
Evaluate your verified draft against the `self-review.md` checklist. Actively look for:
<item>Omissions: What information, edge cases, or perspectives are missing from the baseline draft? (Counteract omission bias).</item>
<item>Contradictions: Are there any logical inconsistencies?</item>
<item>Actionability: Are the recommendations actionable and justified?</item>
<subsection>6. Revise</subsection>
Adjust your draft based on the CoVe and Critique passes.
<item>Downgrade confidence where evidence is weak.</item>
<item>Eliminate unverifiable claims.</item>
<item>Expand the draft to include any flagged omissions.</item>
<item>Prioritize the most critical findings.</item>
<subsection>7. Finalize</subsection>
Close the `</scratchpad>`. Only after the critique and revision passes are complete, structure the final deliverable according to the designated template and present it to the user.
</instructions>
<dependencies>
<required>
<item>workflows/memory-management.md</item>
<item>checklists/cleanup.md</item>
<item>checklists/self-review.md</item>
</required>
<canonical_sources>
<item>principles/reporting/rubric.md</item>
</canonical_sources>
</dependencies>
</esper_module>
