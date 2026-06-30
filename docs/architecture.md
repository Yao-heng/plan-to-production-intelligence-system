# Architecture

The MVP uses a deterministic local pipeline:

1. File loader reads sample RFQ markdown and issue JSON.
2. Requirement extraction parses RFQ requirement blocks into Pydantic models.
3. Ownership router applies keyword rules and records confidence and rationale.
4. Dependency graph agent creates dependency edges and a NetworkX directed graph.
5. Checklist and issue triage agents write portfolio-friendly Markdown reports.
6. Readiness assessment calculates a simple Feature Complete score.
7. Executive report agent summarizes risk, readiness, and next actions.

This version intentionally avoids external APIs, model calls, credentials, and non-deterministic behavior.
