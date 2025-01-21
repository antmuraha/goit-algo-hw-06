import networkx as nx


def dfs_search(G: nx.Graph, start_node: int, end_node: int) -> list[int]:
    dfs_path = nx.dfs_predecessors(G, source=start_node)
    dfs_full_path = reconstruct_path(dfs_path, start_node, end_node)
    return dfs_full_path


def reconstruct_path(predecessors, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = predecessors.get(current)
        if current is None:
            return None
    path.append(start)
    return path[::-1]
