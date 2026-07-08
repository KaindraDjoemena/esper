---
name: Debugging
---

# Debugging Workflow

## Purpose

Identify the root cause rather than the first plausible explanation.

## When to Use

- investigating bugs
- resolving incidents

## Workflow

### 1. Collect evidence

Read:
- error messages
- logs
- stack traces
- relevant implementation
- configuration

Do not guess.

### 2. Form hypotheses

Generate multiple possible causes.
Avoid locking onto the first explanation.

### 3. Eliminate hypotheses

Use evidence to rule possibilities out.
Prefer verification over intuition.

### 4. Identify root cause

Explain:
- what failed
- why it failed
- why the issue appeared now

### 5. Recommend the smallest reasonable fix

Prefer fixing the underlying cause rather than masking symptoms.

### 6. Prevent regression

Identify:
- missing validation
- missing tests
- architectural improvements

## Required Dependencies

- templates/bug-investigation.md
- checklists/self-review.md
