import networkx as nx


def bfs_search(G: nx.Graph, start_node: int, end_node: int) -> list[int]:
    bfs_path = nx.shortest_path(G, source=start_node, target=end_node)
    return bfs_path
