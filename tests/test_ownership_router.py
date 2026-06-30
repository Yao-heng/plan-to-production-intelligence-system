from app.agents.ownership_router import route_requirement


def test_route_requirement_uses_domain_keywords():
    decision = route_requirement("UEFI BIOS Secure Boot TPM measurements")

    assert decision.owner_team == "BIOS"
    assert decision.confidence_score >= 0.8
    assert "BIOS" in decision.rationale


def test_route_requirement_defaults_to_program_quality():
    decision = route_requirement("Customer schedule risk needs ownership clarification")

    assert decision.owner_team == "Program / Quality"
