from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


OwnerTeam = Literal[
    "BIOS",
    "BMC",
    "EC",
    "Driver / OS",
    "Application",
    "Validation",
    "Factory / Diagnostics",
    "Program / Quality",
]


class Requirement(BaseModel):
    requirement_id: str
    title: str
    description: str
    owner_team: OwnerTeam
    impacted_teams: list[str] = Field(default_factory=list)
    upstream_dependencies: list[str] = Field(default_factory=list)
    downstream_dependencies: list[str] = Field(default_factory=list)
    milestone: str = "Unassigned"
    acceptance_criteria: list[str] = Field(default_factory=list)
    status: str = "Open"
    priority: str = "P2"
    risk_if_late: str = "Medium"
    confidence_score: float = Field(default=0.75, ge=0, le=1)
    routing_rationale: str = ""


class Issue(BaseModel):
    issue_id: str
    title: str
    severity: str
    milestone: str
    owner_team: str
    status: str
    gating: bool = False
    machine_available: bool = True
    reproducible: bool = True
    linked_requirement_ids: list[str] = Field(default_factory=list)
    notes: str = ""


class DependencyEdge(BaseModel):
    source: str
    target: str
    dependency_type: Literal["upstream", "downstream", "impacted_team"]
    rationale: str


class OwnerRisk(BaseModel):
    owner_team: str
    open_requirement_count: int = 0
    high_risk_requirement_count: int = 0
    open_gating_issue_count: int = 0
    open_sev1_issue_count: int = 0
    risk_level: Literal["Low", "Medium", "High"]


class NextAction(BaseModel):
    owner_team: str
    action: str
    due_milestone: str
    priority: str
    rationale: str


class ReadinessReport(BaseModel):
    readiness_score: int = Field(ge=0, le=100)
    readiness_level: Literal["Red", "Yellow", "Green"]
    total_requirements: int
    blocked_or_high_risk_requirements: int
    open_gating_issues: int
    open_sev1_issues: int
    missing_dependencies: int
    owner_risks: list[OwnerRisk] = Field(default_factory=list)
    next_actions: list[NextAction] = Field(default_factory=list)
    metrics: dict[str, Any] = Field(default_factory=dict)
