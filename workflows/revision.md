---
name: Revision
---

# Revision Workflow

## Purpose

Enforce a rigorous, observable self-improvement loop. The agent must draft, critique, and verify its own work in an explicit scratchpad before presenting the final deliverable to the user, mimicking how an experienced engineer rigorously reviews a design document before publishing.

## When to Use

- prior to finalizing any major report, plan, or review
- when compiling final recommendations
- when accuracy and exhaustiveness are critical

## Workflow

### 1. The Scratchpad
You must conduct your drafting and verification inside a `<scratchpad>` XML block. Do not attempt to do this "mentally" or implicitly.

### 2. Exploration / Thinking
Before drafting, use the `<scratchpad>` to think out loud. Deconstruct the problem context unconditionally, consider edge cases, and organize your thoughts without worrying about formal formatting.

### 3. Draft
Still inside the `<scratchpad>`, formulate your initial findings, code, or recommendations based on your exploration. Ensure you are following all explicit exhaustiveness constraints (do not artificially limit your findings).

### 4. Chain-of-Verification (CoVe)
Perform a strict verification pass on your draft:
- **Extract Claims:** List the factual claims and technical assertions made in your draft.
- **Formulate Verification Questions:** For each extracted claim, explicitly write a question to test its validity (e.g., "Does `foo.py` actually contain function `bar()`?").
- **Verify:** Answer your verification questions by checking against the source context and codebase.
- **Mandate Citations:** If a claim cannot be backed up by explicit evidence or context, flag it for removal.

### 5. Critique
Evaluate your verified draft against the `self-review.md` checklist. Actively look for:
- **Omissions:** What information, edge cases, or perspectives are missing from the baseline draft? (Counteract omission bias).
- **Contradictions:** Are there any logical inconsistencies?
- **Actionability:** Are the recommendations actionable and justified?

### 6. Revise
Adjust your draft based on the CoVe and Critique passes.
- Downgrade confidence where evidence is weak.
- Eliminate unverifiable claims.
- Expand the draft to include any flagged omissions.
- Prioritize the most critical findings.

### 7. Finalize
Close the `</scratchpad>`. Only after the critique and revision passes are complete, structure the final deliverable according to the designated template and present it to the user.

## Required Dependencies

- checklists/self-review.md

## Canonical Sources

- principles/reporting/rubric.md
