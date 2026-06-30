from app.agents.dependency_graph_agent import build_dependency_edges, build_graph
from app.agents.requirement_extraction_agent import extract_requirements
from app.services.file_loader import read_text


def test_dependency_edges_include_upstream_and_team_edges():
    requirements = extract_requirements(read_text("sample_data/sample_rfq_package.md"))
    edges = build_dependency_edges(requirements)
    graph = build_graph(requirements, edges)

    assert any(edge.source == "BIOS-REQ-001" and edge.target == "VAL-REQ-001" for edge in edges)
    assert any(edge.target == "Team:Validation" for edge in edges)
    assert graph.has_node("BIOS-REQ-001")
    assert graph.number_of_edges() == len(edges)
