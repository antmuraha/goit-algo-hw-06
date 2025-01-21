
def dfs_recursive(graph, vertex, visited_order: list[int] = [], visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    # print(vertex, end=' ')  # Відвідуємо вершину
    visited_order.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:

            dfs_recursive(graph, neighbor, visited_order, visited=visited)


if __name__ == "__main__":
    import networkx as nx
    import matplotlib.pyplot as plt
    # Представлення графа за допомогою списку суміжності
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Виклик функції DFS
    start_node = 'A'
    visited_order = []
    dfs_recursive(graph, start_node, visited_order)
    # nx.draw_networkx(graph)
    # plt.show()
    print(
        f"DFS traversal order starting from node {start_node} ({len(visited_order)} steps): {visited_order}")
