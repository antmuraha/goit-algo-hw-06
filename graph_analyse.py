import networkx as nx


def graph_analyse(G):
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()

    # Average degree of vertices
    degree_sequence = [d for _, d in G.degree()]
    average_degree = sum(degree_sequence) / num_nodes

    # Basic characteristics of the graph
    print("Basic characteristics of the graph:")
    print(f"Number of vertices (nodes): {num_nodes}")
    print(f"Number of edges (edges): {num_edges}")
    print(f"Average degree of vertices: {average_degree:.2f}")

    # Check connectivity
    is_connected = nx.is_connected(G.to_undirected())
    print(f"The graph is connected: {'Yes' if is_connected else 'No'}")

    # Calculating the graph diameter (if it is connected)
    diameter = None
    if is_connected:
        diameter = nx.diameter(G.to_undirected())
        print(f"The diameter of the graph: {diameter}")
    else:
        print("The diameter of a graph cannot be calculated because the graph is disconnected.")

    # Centrality analysis
    degree_centrality = nx.degree_centrality(G)  # Degree centrality
    max_centrality_node = max(degree_centrality, key=degree_centrality.get)
    print(f"Vertex with maximum centrality: {max_centrality_node}")
    return {
        "num_nodes": num_nodes,
        "num_edges": num_edges,
        "average_degree": average_degree,
        "is_connected": is_connected,
        "max_centrality_node": max_centrality_node,
        "diameter": diameter
    }
