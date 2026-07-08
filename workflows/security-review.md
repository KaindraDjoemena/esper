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

1. Identify the boundaries and threat model of the system.
2. Assume external input is untrusted and verify validation.
3. Systematically evaluate:
   - authentication mechanisms
   - authorization boundaries
   - data handling and transit
   - secrets management
   - attack surface minimization
4. Identify leaked credentials, secrets, or internal implementation details.
5. Provide actionable mitigation strategies for identified risks.

## Required Dependencies

- templates/security-review.md
- checklists/security.md
- checklists/self-review.md

## Canonical Sources

- principles/security.md
