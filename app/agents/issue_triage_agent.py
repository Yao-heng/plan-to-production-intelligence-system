from __future__ import annotations

from collections import defaultdict
from typing import Any

from app.schemas.models import Issue


def load_issues(raw_issues: list[dict[str, Any]]) -> list[Issue]:
    return [Issue(**issue) for issue in raw_issues]


def triage_issues(issues: list[Issue]) -> dict[str, Any]:
    def group_by(field: str) -> dict[str, list[str]]:
        grouped: dict[str, list[str]] = defaultdict(list)
        for issue in issues:
            grouped[str(getattr(issue, field))].append(issue.issue_id)
        return dict(grouped)

    open_issues = [issue for issue in issues if issue.status.lower() not in {"closed", "resolved", "verified"}]
    open_sev1 = [issue for issue in open_issues if issue.severity.upper() == "SEV1"]
    open_gating = [issue for issue in open_issues if issue.gating]
    availability_risks = [
        issue
        for issue in open_issues
        if not issue.machine_available or not issue.reproducible
    ]

    return {
        "by_severity": group_by("severity"),
        "by_milestone": group_by("milestone"),
        "by_owner": group_by("owner_team"),
        "by_gating_status": {
            "gating": [issue.issue_id for issue in issues if issue.gating],
            "non_gating": [issue.issue_id for issue in issues if not issue.gating],
        },
        "open_sev1": open_sev1,
        "open_gating": open_gating,
        "availability_or_reproducibility_risks": availability_risks,
    }


def issue_triage_to_markdown(triage: dict[str, Any]) -> str:
    lines = ["# Issue Triage Report", ""]
    for title, key in [
        ("Open Sev1 Issues", "open_sev1"),
        ("Open Gating Issues", "open_gating"),
        ("Machine Availability / Reproducibility Risks", "availability_or_reproducibility_risks"),
    ]:
        lines.extend([f"## {title}", ""])
        issues = triage[key]
        if not issues:
            lines.append("- None")
        for issue in issues:
            lines.append(
                f"- {issue.issue_id} [{issue.severity}] {issue.title} "
                f"- Owner: {issue.owner_team}, Milestone: {issue.milestone}, Status: {issue.status}"
            )
        lines.append("")

    lines.extend(["## Grouping Summary", ""])
    for label, key in [
        ("Severity", "by_severity"),
        ("Milestone", "by_milestone"),
        ("Owner", "by_owner"),
    ]:
        lines.append(f"### By {label}")
        for group, ids in triage[key].items():
            lines.append(f"- {group}: {', '.join(ids)}")
        lines.append("")
    return "\n".join(lines)
