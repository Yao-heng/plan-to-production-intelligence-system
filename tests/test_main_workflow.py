"""End-to-end integration test for the MVP workflow in app.main.

Runs the full pipeline against the bundled sample data and verifies that all
six deliverables are generated. Tests in this repo assume the repository root
as the working directory (same convention as the other test modules).
"""
from pathlib import Path

from app.main import run_workflow

EXPECTED_OUTPUTS = {
    "outputs/feature_checklist.md",
    "outputs/dependency_graph.json",
    "outputs/dependency_graph.md",
    "outputs/issue_triage_report.md",
    "outputs/fc_readiness_report.json",
    "outputs/executive_summary.md",
}


def test_run_workflow_generates_all_outputs():
    generated = run_workflow()

    assert set(generated) == EXPECTED_OUTPUTS
    for relative_path in EXPECTED_OUTPUTS:
        path = Path(relative_path)
        assert path.is_file(), f"missing output: {relative_path}"
        assert path.stat().st_size > 0, f"empty output: {relative_path}"
