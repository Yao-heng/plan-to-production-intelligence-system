from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT_PATH = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT_PATH))

from app.agents.dependency_graph_agent import (
    build_dependency_edges,
    build_graph,
    dependency_edges_to_markdown,
)
from app.agents.executive_report_agent import generate_executive_summary
from app.agents.feature_checklist_agent import generate_feature_checklist
from app.agents.issue_triage_agent import issue_triage_to_markdown, load_issues, triage_issues
from app.agents.readiness_assessment_agent import assess_readiness
from app.agents.requirement_extraction_agent import extract_requirements
from app.services.file_loader import PROJECT_ROOT, read_json, read_text, write_json, write_text


def run_workflow() -> list[str]:
    rfq_markdown = read_text("sample_data/sample_rfq_package.md")
    requirements = extract_requirements(rfq_markdown)

    dependency_edges = build_dependency_edges(requirements)
    build_graph(requirements, dependency_edges)

    issues = load_issues(read_json("sample_data/sample_issues.json"))
    triage = triage_issues(issues)
    readiness = assess_readiness(requirements, issues, dependency_edges)

    generated = [
        write_text("outputs/feature_checklist.md", generate_feature_checklist(requirements)),
        write_json("outputs/dependency_graph.json", [edge.model_dump() for edge in dependency_edges]),
        write_text("outputs/dependency_graph.md", dependency_edges_to_markdown(dependency_edges)),
        write_text("outputs/issue_triage_report.md", issue_triage_to_markdown(triage)),
        write_json("outputs/fc_readiness_report.json", readiness.model_dump()),
        write_text("outputs/executive_summary.md", generate_executive_summary(readiness)),
    ]
    return [str(path.relative_to(PROJECT_ROOT)) for path in generated]


def main() -> None:
    generated = run_workflow()
    print("MVP workflow completed. Generated outputs:")
    for path in generated:
        print(f"- {path}")


if __name__ == "__main__":
    main()
