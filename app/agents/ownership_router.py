from __future__ import annotations

from dataclasses import dataclass


KEYWORD_RULES: dict[str, list[str]] = {
    "BIOS": ["bios", "uefi", "boot", "secure boot", "tpm", "smbios", "acpi", "firmware"],
    "BMC": ["bmc", "redfish", "ipmi", "sel", "sensor", "telemetry"],
    "EC": ["ec", "embedded controller", "thermal table", "fan", "keyboard"],
    "Driver / OS": ["driver", "os", "linux", "windows", "kernel", "device manager"],
    "Application": ["application", "ui", "portal", "dashboard", "api"],
    "Validation": ["validation", "test", "qualification", "coverage", "stress"],
    "Factory / Diagnostics": ["factory", "manufacturing", "diagnostic", "mfg", "production line"],
    "Program / Quality": ["program", "quality", "schedule", "milestone", "risk", "customer"],
}


@dataclass(frozen=True)
class RoutingDecision:
    owner_team: str
    confidence_score: float
    rationale: str


def route_requirement(text: str) -> RoutingDecision:
    normalized = text.lower()
    scores = {
        team: sum(1 for keyword in keywords if keyword in normalized)
        for team, keywords in KEYWORD_RULES.items()
    }
    best_team, best_score = max(scores.items(), key=lambda item: item[1])

    if best_score == 0:
        return RoutingDecision(
            owner_team="Program / Quality",
            confidence_score=0.55,
            rationale="No strong domain keyword matched; routed to Program / Quality for ownership clarification.",
        )

    confidence = min(0.95, 0.62 + best_score * 0.11)
    matched = [keyword for keyword in KEYWORD_RULES[best_team] if keyword in normalized]
    return RoutingDecision(
        owner_team=best_team,
        confidence_score=round(confidence, 2),
        rationale=f"Matched {best_team} keywords: {', '.join(matched)}.",
    )
