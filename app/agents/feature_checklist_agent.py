from __future__ import annotations

from collections import defaultdict

from app.schemas.models import Requirement


CHECKLIST_TEAMS = [
    "BIOS",
    "BMC",
    "EC",
    "Driver / OS",
    "Validation",
    "Factory / Diagnostics",
]


def generate_feature_checklist(requirements: list[Requirement]) -> str:
    grouped: dict[str, list[Requirement]] = defaultdict(list)
    for requirement in requirements:
        grouped[requirement.owner_team].append(requirement)

    lines = ["# Feature Checklist", ""]
    for team in CHECKLIST_TEAMS:
        lines.extend([f"## {team} Checklist", ""])
        team_requirements = grouped.get(team, [])
        if not team_requirements:
            lines.extend(["- [ ] Confirm no committed RFQ items for this domain.", ""])
            continue
        for requirement in team_requirements:
            criteria = "; ".join(requirement.acceptance_criteria) or "Acceptance criteria pending."
            lines.append(
                f"- [ ] {requirement.requirement_id} - {requirement.title} "
                f"({requirement.milestone}, {requirement.priority}): {criteria}"
            )
        lines.append("")
    return "\n".join(lines)
