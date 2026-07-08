---
name: Performance Review
---

# Performance Review Workflow

## Purpose

Analyze performance characteristics systematically.

## When to Use

- profiling code
- investigating latency issues
- reviewing performance-sensitive changes

## Workflow

1. Understand the performance requirements and baseline.
2. Measure before assuming bottlenecks.
3. Evaluate the following systematically:
   - algorithmic complexity
   - memory allocations
   - I/O overhead
   - concurrency and synchronization
   - caching strategies
4. Verify edge cases where performance might degrade non-linearly.
5. Surface assumptions and potential trade-offs (e.g., speed vs. memory).

## Required Dependencies

- checklists/performance.md
- checklists/self-review.md
- workflows/revision.md

## Canonical Sources

- principles/performance.md
