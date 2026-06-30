from app.agents.dependency_graph_agent import build_dependency_edges
from app.agents.issue_triage_agent import load_issues
from app.agents.readiness_assessment_agent import assess_readiness
from app.agents.requirement_extraction_agent import extract_requirements
from app.services.file_loader import read_json, read_text


def test_readiness_scoring_is_deterministic():
    requirements = extract_requirements(read_text("sample_data/sample_rfq_package.md"))
    issues = load_issues(read_json("sample_data/sample_issues.json"))
    edges = build_dependency_edges(requirements)

    report = assess_readiness(requirements, issues, edges)

    assert report.total_requirements == 6
    assert report.open_gating_issues == 2
    assert report.open_sev1_issues == 1
    assert report.readiness_score == 9
    assert report.readiness_level == "Red"
