from __future__ import annotations

import re

from app.agents.ownership_router import route_requirement
from app.schemas.models import Requirement


BLOCK_RE = re.compile(r"^##\s+(?P<id>[A-Z]+-REQ-\d+):\s+(?P<title>.+)$", re.MULTILINE)


FIELD_ALIASES = {
    "Description": "description",
    "Owner Team": "owner_team",
    "Impacted Teams": "impacted_teams",
    "Upstream Dependency": "upstream_dependencies",
    "Upstream Dependencies": "upstream_dependencies",
    "Downstream Dependency": "downstream_dependencies",
    "Downstream Dependencies": "downstream_dependencies",
    "Milestone": "milestone",
    "Acceptance Criteria": "acceptance_criteria",
    "Status": "status",
    "Priority": "priority",
    "Risk If Late": "risk_if_late",
}


def _split_list(value: str) -> list[str]:
    if value.strip().lower() in {"", "none", "n/a", "na"}:
        return []
    normalized = value.replace(";", ",")
    return [part.strip() for part in normalized.split(",") if part.strip()]


def _parse_fields(block: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in block.splitlines():
        match = re.match(r"^-\s+\*\*(?P<key>[^*]+)\*\*:\s*(?P<value>.*)$", line.strip())
        if match:
            fields[match.group("key").strip()] = match.group("value").strip()
    return fields


def extract_requirements(markdown: str) -> list[Requirement]:
    matches = list(BLOCK_RE.finditer(markdown))
    requirements: list[Requirement] = []

    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        block = markdown[start:end].strip()
        raw_fields = _parse_fields(block)
        data: dict[str, object] = {
            "requirement_id": match.group("id"),
            "title": match.group("title").strip(),
            "description": raw_fields.get("Description", ""),
            "owner_team": raw_fields.get("Owner Team", "Program / Quality"),
            "impacted_teams": _split_list(raw_fields.get("Impacted Teams", "")),
            "upstream_dependencies": _split_list(
                raw_fields.get("Upstream Dependency", raw_fields.get("Upstream Dependencies", ""))
            ),
            "downstream_dependencies": _split_list(
                raw_fields.get("Downstream Dependency", raw_fields.get("Downstream Dependencies", ""))
            ),
            "milestone": raw_fields.get("Milestone", "Unassigned"),
            "acceptance_criteria": _split_list(raw_fields.get("Acceptance Criteria", "")),
            "status": raw_fields.get("Status", "Open"),
            "priority": raw_fields.get("Priority", "P2"),
            "risk_if_late": raw_fields.get("Risk If Late", "Medium"),
        }

        routing_text = " ".join(
            [
                str(data["requirement_id"]),
                str(data["title"]),
                str(data["description"]),
                " ".join(data["impacted_teams"]),  # type: ignore[arg-type]
            ]
        )
        decision = route_requirement(routing_text)
        data["owner_team"] = decision.owner_team
        data["confidence_score"] = decision.confidence_score
        data["routing_rationale"] = decision.rationale
        requirements.append(Requirement(**data))

    return requirements
