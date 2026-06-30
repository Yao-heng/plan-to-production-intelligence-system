from app.agents.requirement_extraction_agent import extract_requirements
from app.services.file_loader import read_text


def test_extract_requirements_from_sample_rfq():
    requirements = extract_requirements(read_text("sample_data/sample_rfq_package.md"))

    assert len(requirements) == 6
    assert requirements[0].requirement_id == "BIOS-REQ-001"
    assert requirements[0].owner_team == "BIOS"
    assert "VAL-REQ-001" in requirements[0].downstream_dependencies
    assert requirements[0].confidence_score > 0.6
