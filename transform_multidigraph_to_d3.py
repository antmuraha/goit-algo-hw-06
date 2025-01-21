import networkx as nx
import json


def transform_multidigraph_to_d3(G: nx.MultiDiGraph):
    # Prepare the nodes data
    nodes = []
    for node in G.nodes:
        if "pos" in G.nodes[node]:
            x, y = G.nodes[node]["pos"]
            nodes.append({
                "id": node,
                # Random position (for demo purposes, adjust as needed)
                "x": x,
                "y": y,
            })
        else:
            print("NODE WITHOUT POS>", node, G[node])

    # Prepare the edges data
    edges = []
    for u, v, data in G.edges(data=True):
        edges.append({
            "source": u,
            "target": v,
        })

    # Return the transformed data in D3.js format (nodes and edges)
    return {
        "nodes": nodes,
        "links": edges
    }


if __name__ == "__main__":
    # Example usage:
    # Create a sample MultiDiGraph
    G = nx.MultiDiGraph()

    # Add nodes and edges to the graph
    G.add_node(1, x=1, y=1)
    G.add_node(2, x=2, y=2)
    G.add_node(3, x=3, y=3)
    G.add_edge(1, 2, key=0, weight=5)
    G.add_edge(1, 2, key=1, weight=10)
    G.add_edge(2, 3, key=0, weight=2)
    G.add_edge(3, 1, key=0, weight=8)

    # Transform to D3.js format
    d3_data = transform_multidigraph_to_d3(G)

    # Output the transformed data as JSON for use in D3.js
    print(json.dumps(d3_data, indent=2))
