from __future__ import annotations

from app.schemas.models import ReadinessReport


def generate_executive_summary(report: ReadinessReport) -> str:
    lines = [
        "# Executive Summary",
        "",
        f"Feature Complete readiness is **{report.readiness_level}** with a score of **{report.readiness_score}/100**.",
        "",
        "## Key Metrics",
        "",
        f"- Total requirements: {report.total_requirements}",
        f"- Blocked or high-risk requirements: {report.blocked_or_high_risk_requirements}",
        f"- Open gating issues: {report.open_gating_issues}",
        f"- Open Sev1 issues: {report.open_sev1_issues}",
        f"- Missing or external dependencies: {report.missing_dependencies}",
        "",
        "## Owner Risk",
        "",
    ]
    for risk in report.owner_risks:
        lines.append(
            f"- {risk.owner_team}: {risk.risk_level} "
            f"(high-risk req: {risk.high_risk_requirement_count}, "
            f"gating: {risk.open_gating_issue_count}, Sev1: {risk.open_sev1_issue_count})"
        )

    lines.extend(["", "## Recommended Next Actions", ""])
    for action in report.next_actions:
        lines.append(
            f"- [{action.priority}] {action.owner_team}: {action.action} "
            f"by {action.due_milestone}. Rationale: {action.rationale}"
        )
    return "\n".join(lines) + "\n"
