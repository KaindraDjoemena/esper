---
name: Report Structure
description: Defines the canonical structure for engineering reports and review deliverables. Use when producing audits, code reviews, architecture reviews, security reviews, or any structured engineering assessment.
---

# Report Structure

## Purpose

A professional engineering report should minimize the effort required for another engineer to understand the current state of a system, evaluate the supporting evidence, and decide what to do next.

Reports are decision-support documents—not summaries.

## Canonical Structure

Every engineering report should include, where applicable:

1. Executive Summary
2. Scope
3. Context Gathered
4. Positive Observations
5. Findings
6. Implementation Roadmap
7. Overall Assessment

## Detailed Reports by Default

Agents MUST return comprehensive, highly-specific reports (details, exact code paths, specific edge cases) by default. Executive summaries or high-level abstractions are strictly forbidden unless explicitly requested by the user. Hand-wavy conclusions are unacceptable.

## Executive Summary

If explicitly requested by the user, summarize:

- overall assessment
- overall confidence
- highest-priority findings
- major strengths
- recommended next steps

Otherwise, skip this section and provide full comprehensive details.

## Scope

Clearly define:

- what was reviewed
- what was not reviewed
- important assumptions

Never imply repository-wide conclusions outside the reviewed scope.

## Context Gathered

Document the investigation.

Examples:

- files reviewed
- directories inspected
- documentation consulted
- workflows used

This improves transparency and reviewer confidence.

## Positive Observations

Identify engineering decisions worth preserving. Excellent engineering reviews should preserve good decisions—not merely criticize poor ones.

Examples:

- clean abstractions
- effective APIs
- good documentation
- modular architecture
- thoughtful testing

## Findings

Document all issues discovered during the investigation. Do not artificially limit the number of findings to a generic list of 3 or 5 items.

To ensure completeness, keep a running tally in the finding titles (e.g., "Finding 1", "Finding 2"). After the final finding, you MUST append a strict termination statement: *"End of exhaustive list. No further issues found in scope."*

Each finding should follow the canonical Finding schema.

Do not combine unrelated findings.

## Implementation Roadmap

Organize recommendations by implementation priority and dependency.

Prioritize engineering effort rather than simply repeating finding severity.

## Overall Assessment

Conclude with an overall engineering judgment.

Explain whether the system is ready as-is or requires further work.

