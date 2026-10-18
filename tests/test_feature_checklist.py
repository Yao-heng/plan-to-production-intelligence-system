"""Unit tests for the feature checklist generator.

Pins the grouping contract: requirements land under their owner team's
section in the fixed CHECKLIST_TEAMS order, teams without requirements
get the placeholder confirmation line, and acceptance criteria fall back
to an explicit "pending" marker instead of a blank.
"""

from app.agents.feature_checklist_agent import CHECKLIST_TEAMS, generate_feature_checklist
from app.schemas.models import Requirement


def requirement(req_id: str, team: str, **overrides: object) -> Requirement:
    data: dict = {
        "requirement_id": req_id,
        "title": f"Title {req_id}",
        "description": "desc",
        "owner_team": team,
    }
    data.update(overrides)
    return Requirement(**data)


def section_body(checklist: str, team: str) -> str:
    """Return the lines under one team's '## <team> Checklist' heading."""
    marker = f"## {team} Checklist"
    start = checklist.index(marker) + len(marker)
    rest = checklist[start:]
    next_heading = rest.find("\n## ")
    return rest if next_heading == -1 else rest[:next_heading]


def test_requirements_are_grouped_under_owner_team_sections() -> None:
    checklist = generate_feature_checklist(
        [
            requirement("BIOS-REQ-1", "BIOS"),
            requirement("BMC-REQ-1", "BMC"),
            requirement("BIOS-REQ-2", "BIOS"),
        ]
    )

    bios = section_body(checklist, "BIOS")
    assert "BIOS-REQ-1" in bios
    assert "BIOS-REQ-2" in bios
    assert "BMC-REQ-1" not in bios
    assert "BMC-REQ-1" in section_body(checklist, "BMC")


def test_team_sections_follow_fixed_order() -> None:
    checklist = generate_feature_checklist([requirement("EC-REQ-1", "EC")])

    positions = [checklist.index(f"## {team} Checklist") for team in CHECKLIST_TEAMS]
    assert positions == sorted(positions)


def test_empty_teams_get_placeholder_line() -> None:
    checklist = generate_feature_checklist([requirement("BIOS-REQ-1", "BIOS")])

    for team in CHECKLIST_TEAMS:
        if team == "BIOS":
            continue
        assert "Confirm no committed RFQ items for this domain." in section_body(checklist, team)


def test_acceptance_criteria_rendering_and_fallback() -> None:
    checklist = generate_feature_checklist(
        [
            requirement(
                "BIOS-REQ-1",
                "BIOS",
                milestone="EVT",
                priority="P1",
                acceptance_criteria=["POST passes", "Boot time < 20s"],
            ),
            requirement("BIOS-REQ-2", "BIOS"),
        ]
    )

    bios = section_body(checklist, "BIOS")
    assert "POST passes; Boot time < 20s" in bios
    assert "(EVT, P1)" in bios
    assert "Acceptance criteria pending." in bios


def test_empty_requirements_still_emit_all_sections() -> None:
    checklist = generate_feature_checklist([])

    assert checklist.startswith("# Feature Checklist")
    for team in CHECKLIST_TEAMS:
        assert f"## {team} Checklist" in checklist
