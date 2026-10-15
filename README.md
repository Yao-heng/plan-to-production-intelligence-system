# plan-to-production-intelligence-system

[![CI](https://github.com/Yao-heng/plan-to-production-intelligence-system/actions/workflows/ci.yml/badge.svg)](https://github.com/Yao-heng/plan-to-production-intelligence-system/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**AI-driven platform delivery governance from requirements to release readiness.**

An AI-driven intelligent management system that transforms fragmented requirements, cross-functional dependencies, validation issues, release risks, and production readiness signals into executable ownership, readiness intelligence, recovery plans, and production decision support.

This repository contains a working local **MVP prototype** (deterministic, no external APIs or API keys required) built from fictional sample data simulating an AI server platform program, plus the full concept documentation behind it.

## Quick Start

Requires Python 3.11+.

```bash
git clone https://github.com/Yao-heng/plan-to-production-intelligence-system.git
cd plan-to-production-intelligence-system

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt

# Run the full MVP workflow (reads sample_data/, writes 6 files to outputs/)
python -m app.main

# Run the test suite (7 tests)
python -m pytest

# Lint
pip install ruff
ruff check .
```

Expected console output from `python -m app.main`:

```text
MVP workflow completed. Generated outputs:
- outputs/feature_checklist.md
- outputs/dependency_graph.json
- outputs/dependency_graph.md
- outputs/issue_triage_report.md
- outputs/fc_readiness_report.json
- outputs/executive_summary.md
```

### What the MVP workflow does

1. Loads a fictional RFQ package from `sample_data/sample_rfq_package.md`
2. Extracts structured platform requirements
3. Routes requirements to functional owner teams
4. Detects cross-team dependencies
5. Generates function-level feature checklists
6. Loads sample validation issues from `sample_data/sample_issues.json`
7. Performs issue triage by severity, owner, milestone, and gating status
8. Generates a Feature Complete readiness assessment
9. Produces executive-level summary reports

### Generated outputs

Running the workflow (re)generates these artifacts under `outputs/`. The copies committed in this repo are the actual output of the commands above — re-running produces byte-identical files, because the pipeline is fully deterministic.

| File | Contents |
| --- | --- |
| `outputs/executive_summary.md` | Feature Complete readiness status, key metrics, owner risks, recommended next actions |
| `outputs/feature_checklist.md` | Function-level execution checklists across BIOS, BMC, EC, Driver / OS, Validation, Factory, and Program teams |
| `outputs/issue_triage_report.md` | Validation issues grouped by severity, gating status, owner, milestone impact, reproducibility, and machine availability |
| `outputs/dependency_graph.md` | Cross-functional upstream / downstream dependency table |
| `outputs/dependency_graph.json` | The same dependency edges in structured JSON (32 edges for the bundled sample data) |
| `outputs/fc_readiness_report.json` | Structured readiness data (score, level, owner risks, next actions) for dashboards, APIs, or future AI agents |

### Example output (actual, from the bundled sample data)

Excerpt from `outputs/executive_summary.md` after running the workflow:

```markdown
# Executive Summary

Feature Complete readiness is **Red** with a score of **9/100**.

## Key Metrics

- Total requirements: 6
- Blocked or high-risk requirements: 4
- Open gating issues: 2
- Open Sev1 issues: 1
- Missing or external dependencies: 9

## Owner Risk

- BIOS: High (high-risk req: 2, gating: 1, Sev1: 1)
- BMC: Medium (high-risk req: 0, gating: 1, Sev1: 0)
- Driver / OS: Low (high-risk req: 0, gating: 0, Sev1: 0)
- EC: Medium (high-risk req: 1, gating: 0, Sev1: 0)
- Factory / Diagnostics: Medium (high-risk req: 1, gating: 0, Sev1: 0)
```

## Project Structure

```text
app/
  main.py                  Entry point: runs the end-to-end MVP workflow
  agents/                  Requirement extraction, ownership routing, dependency
                           graph, feature checklist, issue triage, readiness
                           assessment, and executive report agents
  schemas/models.py        Pydantic models (Requirement, Issue, ReadinessReport, ...)
  services/file_loader.py  Sample-data / output file I/O helpers
sample_data/               Fictional RFQ package, platform schedule, and issues
schemas/                   JSON Schemas for issues, readiness, and requirements
tests/                     Pytest suite (unit tests + end-to-end workflow test)
outputs/                   Generated artifacts (committed examples = actual run output)
docs/                      Concept paper, pitch deck, architecture, roadmap, use cases
assets/screenshots/        Screenshots of the generated outputs
```

## Running Tests

```bash
python -m pytest        # 7 tests: unit tests per agent + test_main_workflow.py (end-to-end)
ruff check .            # lint (rules E/F/I/W, configured in pyproject.toml)
```

CI (GitHub Actions, [`.github/workflows/ci.yml`](.github/workflows/ci.yml)) runs ruff, the full pytest suite, and an MVP workflow smoke test on every push and pull request.

## Visual Demo

The MVP generates structured delivery intelligence from fictional RFQ, schedule, and issue data. The screenshots below show how fragmented project information is converted into executive summaries, function-level checklists, issue triage reports, and dependency intelligence.

### Executive Summary

![Executive Summary](assets/screenshots/executive_summary.png)

The executive summary provides a decision-ready view of Feature Complete readiness, gating issues, owner risks, schedule risks, and recommended next actions.

### Feature Checklist

![Feature Checklist](assets/screenshots/feature_checklist.png)

The feature checklist demonstrates how fragmented RFQ requirements are converted into function-level execution ownership across BIOS, BMC, EC, Driver / OS, Validation, Factory, and Program teams.

### Issue Triage Report

![Issue Triage Report](assets/screenshots/issue_triage_report.png)

The issue triage report groups validation issues by severity, gating status, owner, milestone impact, reproducibility, and machine availability.

### Dependency Graph

![Dependency Graph](assets/screenshots/dependency_graph.png)

The dependency graph shows upstream and downstream relationships that may affect Feature Complete, Pilot, Production Readiness, RFD, RTS, or Sustaining Handoff.

## Project Documents

This project is documented as both a formal concept paper and a pitch deck.

* [Download Concept Document](docs/Plan_to_Production_Intelligence_System_Concept_v2.docx)
* [Download Pitch Deck](docs/Plan_to_Production_Intelligence_System_Pitch_v2.pptx)

The concept document explains the full Plan-to-Production Intelligence System, including enterprise pain points, AI-driven process transformation, agentic loop design, requirement decomposition, ownership routing, dependency intelligence, validation issue convergence, production readiness, and sustaining handoff.

The pitch deck provides a concise executive-level overview for recruiters, hiring managers, product leaders, and engineering leaders.

See also [`docs/architecture.md`](docs/architecture.md), [`docs/concept.md`](docs/concept.md), [`docs/roadmap.md`](docs/roadmap.md), and [`docs/use-cases.md`](docs/use-cases.md).

## Portfolio Positioning

This project is not a generic chatbot or task tracker. It is a domain-driven AI system concept and MVP prototype focused on enterprise delivery governance.

The Plan-to-Production Intelligence System is designed for enterprises that want real process transformation from AI adoption: reduced meeting time, lower human coordination loading, better resource utilization, more controlled product quality, predictable schedules, improved production readiness, and higher production line utilization.

This project productizes senior platform delivery intelligence learned from complex hardware, firmware, software, validation, ODM/JDM, manufacturing, and sustaining environments.

Many companies want AI adoption that creates measurable operational improvement, not only text generation. This system targets the areas enterprises care about most:

* Reducing repetitive coordination meetings
* Lowering human loading across engineering, validation, quality, manufacturing, and program teams
* Improving ownership clarity and accountability
* Detecting cross-functional dependencies earlier
* Improving product quality and release readiness
* Making schedules more predictable
* Reducing late production surprises
* Improving production line utilization
* Helping leaders make faster go / no-go decisions with structured evidence

The core idea is to convert the experience of senior technical program leaders, platform delivery owners, SWDMs, STMs, LDs, and cross-functional engineering leaders into an AI-assisted Plan-to-Production governance system.

## Why enterprises need this now

Enterprises do not only need another PM dashboard. They need a process-level operating model that reduces repetitive meetings, lowers engineering coordination load, makes product quality and schedules more controllable, and improves production-line utilization by detecting blockers before build capacity is wasted.

## Core product thesis

Plan-to-Production Intelligence System converts fragmented requirements, engineering dependencies, validation issues, and release risks into executable ownership, readiness intelligence, recovery plans, and production decision support.

## Target business outcomes

- **Reduce meeting time:** AI-generated agendas, owner actions, readiness gaps, and decision summaries replace repetitive status collection.
- **Reduce manpower loading:** Automate requirement extraction, checklist creation, owner routing, duplicate issue detection, and executive reporting.
- **Improve product quality and schedule control:** Evidence-based FC, pilot, production, RFD/RTS, and sustain handoff readiness gates make risks visible earlier.
- **Increase production-line utilization:** Detect blockers before build exit, reduce late surprises, and align recovery plans before line capacity is wasted.
- **Scale process intelligence across industries:** Apply the same requirement-to-release governance pattern to AI servers, storage systems, automotive, medical devices, semiconductor validation, aerospace, and enterprise software.

## Agentic workflow

Observe → Reason → Act → Verify → Escalate → Learn

The system productizes senior SWDM / STM / LD execution logic into an AI-assisted governance loop, while keeping human approval gates for production, release, customer risk, and commercial trade-off decisions.

## Modules

1. RFQ Package Ingestion Agent
2. Requirement Extraction Agent
3. Function Ownership Router
4. Feature Checklist Generator
5. Dependency Graph Agent
6. FC Readiness Agent
7. Issue Triage Agent
8. Recovery Plan Agent
9. Sustain Handoff Agent
10. Executive Risk Report Agent

## MVP roadmap

- MVP 1: RFQ document ingestion and requirement extraction
- MVP 2: Function checklist generation and owner routing
- MVP 3: Dependency graph and FC readiness dashboard
- MVP 4: Issue triage and recovery recommendation
- MVP 5: Executive risk report and GitHub demo dataset

## Why These Outputs Matter

These outputs demonstrate how the system converts scattered project data into decision-ready delivery intelligence.

Instead of relying on repeated status meetings, manual spreadsheet tracking, and fragmented ownership discussions, the MVP shows how AI-assisted governance can generate structured checklists, owner visibility, dependency intelligence, issue triage, readiness scoring, and executive summaries.

This is the foundation for reducing meeting time, lowering human coordination load, improving product quality, controlling schedule risk, and improving production readiness.

## What This Demonstrates

This MVP demonstrates the first step toward an AI-driven Plan-to-Production governance system.

It shows how enterprises can reduce manual coordination effort, meeting preparation time, ownership ambiguity, issue tracking overhead, and release readiness uncertainty by converting fragmented project information into structured, decision-ready intelligence.

The current implementation is deterministic and does not require external APIs or API keys. Future versions can extend this foundation with LLM-based extraction, RAG, Jira integration, PLM integration, validation log ingestion, CI/CD data, and production readiness dashboards.

## License

MIT — see [LICENSE](LICENSE).
