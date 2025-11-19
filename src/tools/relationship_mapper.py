"""Relationship Mapper Tool for visualizing campaign element connections."""

import json
from typing import Any, Dict, List, Optional, Type

import networkx as nx
from crewai_tools import BaseTool
from pydantic import BaseModel, Field


class RelationshipMapperInput(BaseModel):
    """Input schema for RelationshipMapper."""

    elements: str = Field(
        ...,
        description="JSON string of campaign elements with their relationships",
    )
    output_format: str = Field(
        default="json",
        description="Output format: 'json', 'graphml', or 'analysis'",
    )


class RelationshipMapperTool(BaseTool):
    """
    Tool for creating and analyzing relationship networks between campaign elements.

    Creates network graphs showing connections between NPCs, factions, locations,
    and events. Identifies key nodes, clusters, and orphaned elements.
    """

    name: str = "Relationship Mapper"
    description: str = (
        "Maps relationships between campaign elements (NPCs, factions, locations, events). "
        "Creates network graphs and identifies key connections, isolated elements, "
        "and central figures. Input should be JSON with elements and their relationships."
    )
    args_schema: Type[BaseModel] = RelationshipMapperInput

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.graph = nx.Graph()

    def _run(self, elements: str, output_format: str = "json") -> str:
        """
        Map relationships between campaign elements.

        Args:
            elements: JSON string of elements and relationships
            output_format: Desired output format

        Returns:
            Relationship analysis or graph data
        """
        try:
            data = json.loads(elements)
            self._build_graph(data)

            if output_format == "analysis":
                return self._analyze_graph()
            elif output_format == "graphml":
                return self._export_graphml()
            else:
                return self._export_json()

        except json.JSONDecodeError as e:
            return f"Error parsing JSON: {str(e)}"
        except Exception as e:
            return f"Error mapping relationships: {str(e)}"

    def _build_graph(self, data: Dict[str, Any]):
        """Build network graph from campaign data."""
        self.graph.clear()

        # Add nodes for each element
        for category, items in data.items():
            if isinstance(items, list):
                for item in items:
                    if isinstance(item, dict) and "name" in item:
                        node_id = f"{category}:{item['name']}"
                        self.graph.add_node(
                            node_id,
                            category=category,
                            name=item["name"],
                            **{k: v for k, v in item.items() if k != "name"},
                        )

        # Add edges based on relationships
        for category, items in data.items():
            if isinstance(items, list):
                for item in items:
                    if isinstance(item, dict) and "name" in item:
                        source_id = f"{category}:{item['name']}"

                        # Look for relationship fields
                        relationship_fields = [
                            "allies",
                            "enemies",
                            "members",
                            "locations",
                            "npcs",
                            "factions",
                            "connections",
                            "related_to",
                        ]

                        for field in relationship_fields:
                            if field in item and isinstance(item[field], list):
                                for related in item[field]:
                                    # Try to find matching node
                                    for node in self.graph.nodes():
                                        if related.lower() in node.lower():
                                            edge_type = field
                                            self.graph.add_edge(
                                                source_id,
                                                node,
                                                relationship=edge_type,
                                            )
                                            break

    def _analyze_graph(self) -> str:
        """Analyze the relationship graph."""
        if len(self.graph.nodes()) == 0:
            return json.dumps({"error": "No nodes in graph"})

        analysis = {
            "statistics": {
                "total_nodes": self.graph.number_of_nodes(),
                "total_edges": self.graph.number_of_edges(),
                "density": nx.density(self.graph),
                "is_connected": nx.is_connected(self.graph),
            },
            "central_figures": [],
            "isolated_elements": [],
            "clusters": [],
            "recommendations": [],
        }

        # Find central nodes (high degree)
        if len(self.graph.nodes()) > 0:
            degree_dict = dict(self.graph.degree())
            sorted_nodes = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)
            analysis["central_figures"] = [
                {"name": node, "connections": degree} for node, degree in sorted_nodes[:5]
            ]

        # Find isolated nodes (no connections)
        isolated = list(nx.isolates(self.graph))
        analysis["isolated_elements"] = isolated

        if isolated:
            analysis["recommendations"].append(
                f"Found {len(isolated)} isolated elements with no connections. "
                "Consider adding relationships to integrate them into the campaign."
            )

        # Find communities/clusters
        if nx.is_connected(self.graph):
            # Use community detection if graph is connected
            try:
                communities = nx.community.greedy_modularity_communities(self.graph)
                analysis["clusters"] = [
                    {"cluster_id": i, "members": list(community)}
                    for i, community in enumerate(communities)
                ]
            except Exception:
                pass
        else:
            # List connected components
            components = list(nx.connected_components(self.graph))
            analysis["clusters"] = [
                {"component_id": i, "members": list(component)}
                for i, component in enumerate(components)
            ]

        # Recommendations
        if analysis["statistics"]["density"] < 0.1:
            analysis["recommendations"].append(
                "Graph density is low. Consider adding more connections between elements "
                "to create a more interconnected world."
            )

        if not analysis["statistics"]["is_connected"]:
            analysis["recommendations"].append(
                "Graph has disconnected components. Consider adding bridges between "
                "different parts of your campaign world."
            )

        return json.dumps(analysis, indent=2)

    def _export_json(self) -> str:
        """Export graph as JSON."""
        data = nx.node_link_data(self.graph)
        return json.dumps(data, indent=2)

    def _export_graphml(self) -> str:
        """Export graph as GraphML (for tools like Gephi, yEd)."""
        try:
            import io

            buffer = io.BytesIO()
            nx.write_graphml(self.graph, buffer)
            return buffer.getvalue().decode("utf-8")
        except Exception as e:
            return f"Error exporting GraphML: {str(e)}"

    def identify_key_nodes(self, top_n: int = 5) -> List[str]:
        """Identify the most connected/central nodes."""
        centrality = nx.degree_centrality(self.graph)
        sorted_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
        return [node for node, _ in sorted_nodes[:top_n]]

    def find_shortest_path(self, source: str, target: str) -> List[str]:
        """Find shortest path between two elements."""
        try:
            return nx.shortest_path(self.graph, source, target)
        except nx.NetworkXNoPath:
            return []
        except nx.NodeNotFound:
            return []
