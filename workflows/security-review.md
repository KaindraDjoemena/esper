---
name: Security Review
---

# Security Review Workflow

## Purpose

Systematically review system posture and identify security risks.

## When to Use

- security audits
- reviewing sensitive changes

## Workflow

1. Map the system's trust boundaries and document the security review scope.
2. Apply input validation principles: confirm all external data is sanitized at system boundaries.
3. Systematically evaluate:
   - authentication mechanisms
   - authorization boundaries
   - data handling and transit
   - secrets and credential hygiene
   - exposure surface reduction
4. Verify that secrets, credentials, and internal implementation details are not inadvertently disclosed.
5. Provide actionable remediation strategies for identified weaknesses.

## Required Dependencies

- checklists/security.md
- checklists/self-review.md
- workflows/revision.md

## Canonical Sources

- principles/security.md
