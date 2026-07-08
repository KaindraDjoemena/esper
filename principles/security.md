---
name: Security
---

# Security Principles

## Purpose

Ensure software is resilient against malicious activity and data breaches.

## Principles

Security should be considered by default rather than added later.
Prefer secure defaults.
Validate data at system boundaries.
Treat external input as untrusted.

Avoid leaking:
- secrets
- credentials
- internal implementation details
- sensitive user information

Apply the principle of least privilege.
Prefer defense in depth over relying on a single protective measure.
When reviewing security, prioritize practical risks over theoretical concerns.

## Canonical Sources

- principles/engineering.md
