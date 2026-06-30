# Plan-to-Production Intelligence System

A local MVP prototype for turning RFQ content, issue data, and schedule signals into ownership routing, dependency visibility, feature checklists, issue triage, and Feature Complete readiness reporting.

## MVP Prototype

This first prototype runs locally with deterministic Python logic. It does not call external APIs and does not require API keys.

```powershell
pip install -r requirements.txt
python app/main.py
pytest
```

Generated artifacts are written to `outputs/`:

- `feature_checklist.md`
- `dependency_graph.json`
- `dependency_graph.md`
- `issue_triage_report.md`
- `fc_readiness_report.json`
- `executive_summary.md`
