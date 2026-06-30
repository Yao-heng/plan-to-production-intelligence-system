from __future__ import annotations

from collections import defaultdict

from app.schemas.models import DependencyEdge, Issue, NextAction, OwnerRisk, ReadinessReport, Requirement


HIGH_RISK_VALUES = {"high", "critical"}
BLOCKED_VALUES = {"blocked", "at risk", "delayed"}


def _is_open_issue(issue: Issue) -> bool:
    return issue.status.lower() not in {"closed", "resolved", "verified"}


def assess_readiness(
    requirements: list[Requirement],
    issues: list[Issue],
    dependencies: list[DependencyEdge],
) -> ReadinessReport:
    blocked_or_high_risk = [
        req
        for req in requirements
        if req.risk_if_late.lower() in HIGH_RISK_VALUES or req.status.lower() in BLOCKED_VALUES
    ]
    open_issues = [issue for issue in issues if _is_open_issue(issue)]
    open_gating = [issue for issue in open_issues if issue.gating]
    open_sev1 = [issue for issue in open_issues if issue.severity.upper() == "SEV1"]
    missing_dependencies = [
        edge
        for edge in dependencies
        if edge.source.startswith("External:") or edge.target.startswith("External:")
    ]

    score = 100
    score -= len(blocked_or_high_risk) * 8
    score -= len(open_gating) * 10
    score -= len(open_sev1) * 12
    score -= len(missing_dependencies) * 3
    readiness_score = max(0, min(100, score))
    readiness_level = "Green" if readiness_score >= 85 else "Yellow" if readiness_score >= 65 else "Red"

    owner_risks = _build_owner_risks(requirements, open_gating, open_sev1)
    next_actions = _build_next_actions(blocked_or_high_risk, open_gating, open_sev1, missing_dependencies)

    return ReadinessReport(
        readiness_score=readiness_score,
        readiness_level=readiness_level,
        total_requirements=len(requirements),
        blocked_or_high_risk_requirements=len(blocked_or_high_risk),
        open_gating_issues=len(open_gating),
        open_sev1_issues=len(open_sev1),
        missing_dependencies=len(missing_dependencies),
        owner_risks=owner_risks,
        next_actions=next_actions,
        metrics={
            "scoring_model": "100 - 8*blocked/high-risk req - 10*gating issue - 12*sev1 issue - 3*missing dependency",
            "dependency_edges": len(dependencies),
        },
    )


def _build_owner_risks(
    requirements: list[Requirement],
    open_gating: list[Issue],
    open_sev1: list[Issue],
) -> list[OwnerRisk]:
    requirement_count: dict[str, int] = defaultdict(int)
    high_risk_count: dict[str, int] = defaultdict(int)
    gating_count: dict[str, int] = defaultdict(int)
    sev1_count: dict[str, int] = defaultdict(int)

    for req in requirements:
        requirement_count[req.owner_team] += 1
        if req.risk_if_late.lower() in HIGH_RISK_VALUES or req.status.lower() in BLOCKED_VALUES:
            high_risk_count[req.owner_team] += 1
    for issue in open_gating:
        gating_count[issue.owner_team] += 1
    for issue in open_sev1:
        sev1_count[issue.owner_team] += 1

    owners = sorted(set(requirement_count) | set(gating_count) | set(sev1_count))
    risks: list[OwnerRisk] = []
    for owner in owners:
        pressure = high_risk_count[owner] + gating_count[owner] + sev1_count[owner]
        risk_level = "High" if pressure >= 2 else "Medium" if pressure == 1 else "Low"
        risks.append(
            OwnerRisk(
                owner_team=owner,
                open_requirement_count=requirement_count[owner],
                high_risk_requirement_count=high_risk_count[owner],
                open_gating_issue_count=gating_count[owner],
                open_sev1_issue_count=sev1_count[owner],
                risk_level=risk_level,
            )
        )
    return risks


def _build_next_actions(
    blocked_or_high_risk: list[Requirement],
    open_gating: list[Issue],
    open_sev1: list[Issue],
    missing_dependencies: list[DependencyEdge],
) -> list[NextAction]:
    actions: list[NextAction] = []
    for req in blocked_or_high_risk[:5]:
        actions.append(
            NextAction(
                owner_team=req.owner_team,
                action=f"Close risk plan for {req.requirement_id}: {req.title}",
                due_milestone=req.milestone,
                priority=req.priority,
                rationale=f"Requirement is {req.status} with {req.risk_if_late} late risk.",
            )
        )
    for issue in (open_sev1 + open_gating)[:5]:
        actions.append(
            NextAction(
                owner_team=issue.owner_team,
                action=f"Resolve {issue.issue_id}: {issue.title}",
                due_milestone=issue.milestone,
                priority=issue.severity,
                rationale="Open Sev1 or gating issue impacts Feature Complete readiness.",
            )
        )
    if missing_dependencies:
        actions.append(
            NextAction(
                owner_team="Program / Quality",
                action="Confirm external dependency owners and committed delivery dates.",
                due_milestone="Feature Complete",
                priority="P1",
                rationale=f"{len(missing_dependencies)} dependency edges point to external or unresolved items.",
            )
        )
    return actions
