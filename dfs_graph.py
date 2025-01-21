import networkx as nx
import matplotlib.pyplot as plt


def dfs_graph(G: nx.Graph, start_node, visited_order: list[int], visited=None):
    """
    Custom Depth-First Search (DFS) implementation for a Graph
    with memorization of steps for visualization of the algorithm.

    Parameters:
        graph (nx.Graph): The directed graph to traverse.
        start_node: The starting node for the DFS traversal.
    """

    if visited is None:
        visited = set()
    visited.add(start_node)
    for neighbor in G[start_node]:
        visited_order.append({"nodeId": start_node,
                              "edges": [
                                  {"source": start_node, "target": neighbor}]})

        if neighbor not in visited:
            dfs_graph(G, neighbor, visited_order, visited=visited)


# Example usage
if __name__ == "__main__":
    # Create a Graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4),
                     (4, 5), (5, 1), (3, 6), (2, 6)])
    start_node = 1
    visited_order = []
    dfs_graph(G, start_node, visited_order)
    print(
        f"DFS traversal order starting from node {start_node} ({len(visited_order)} steps): {visited_order}")
    nx.draw_networkx(G)
    plt.show()
