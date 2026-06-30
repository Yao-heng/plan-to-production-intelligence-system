from __future__ import annotations

import networkx as nx

from app.schemas.models import DependencyEdge, Requirement


def build_dependency_edges(requirements: list[Requirement]) -> list[DependencyEdge]:
    requirement_ids = {requirement.requirement_id for requirement in requirements}
    edges: list[DependencyEdge] = []

    for requirement in requirements:
        for dependency in requirement.upstream_dependencies:
            source = dependency if dependency in requirement_ids else f"External:{dependency}"
            edges.append(
                DependencyEdge(
                    source=source,
                    target=requirement.requirement_id,
                    dependency_type="upstream",
                    rationale=f"{requirement.requirement_id} lists upstream dependency {dependency}.",
                )
            )
        for dependency in requirement.downstream_dependencies:
            target = dependency if dependency in requirement_ids else f"External:{dependency}"
            edges.append(
                DependencyEdge(
                    source=requirement.requirement_id,
                    target=target,
                    dependency_type="downstream",
                    rationale=f"{requirement.requirement_id} lists downstream dependency {dependency}.",
                )
            )
        for team in requirement.impacted_teams:
            edges.append(
                DependencyEdge(
                    source=requirement.requirement_id,
                    target=f"Team:{team}",
                    dependency_type="impacted_team",
                    rationale=f"{team} is listed as an impacted team.",
                )
            )

    return edges


def build_graph(requirements: list[Requirement], edges: list[DependencyEdge]) -> nx.MultiDiGraph:
    graph = nx.MultiDiGraph()
    for requirement in requirements:
        graph.add_node(requirement.requirement_id, owner_team=requirement.owner_team, milestone=requirement.milestone)
    for edge in edges:
        graph.add_edge(edge.source, edge.target, dependency_type=edge.dependency_type, rationale=edge.rationale)
    return graph


def dependency_edges_to_markdown(edges: list[DependencyEdge]) -> str:
    lines = [
        "# Dependency Graph",
        "",
        "| Source | Target | Type | Rationale |",
        "| --- | --- | --- | --- |",
    ]
    for edge in edges:
        lines.append(f"| {edge.source} | {edge.target} | {edge.dependency_type} | {edge.rationale} |")
    return "\n".join(lines) + "\n"
