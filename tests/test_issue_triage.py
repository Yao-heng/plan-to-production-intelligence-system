from app.agents.issue_triage_agent import load_issues, triage_issues
from app.services.file_loader import read_json


def test_issue_triage_finds_gating_and_availability_risks():
    issues = load_issues(read_json("sample_data/sample_issues.json"))
    triage = triage_issues(issues)

    assert [issue.issue_id for issue in triage["open_sev1"]] == ["ISSUE-001"]
    assert {issue.issue_id for issue in triage["open_gating"]} == {"ISSUE-001", "ISSUE-002"}
    assert {issue.issue_id for issue in triage["availability_or_reproducibility_risks"]} == {
        "ISSUE-002",
        "ISSUE-003",
    }
