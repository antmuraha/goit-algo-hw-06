import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def bfs_graph(G: nx.Graph, queue: deque, visited_order: list[int], parent=None, visited=None):
    """
    Custom Breadth-First Search (BFS) implementation for a Graph
    with memorization of steps for visualization of the algorithm.

    Parameters:
        graph (nx.Graph): The directed graph to traverse.
        start_node: The starting node for the BFS traversal.
    """
    # queue = deque([start_node])
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    # print("0000_vertex", vertex)
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        # print(">>>", vertex)
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        sibling = set(G[vertex])
        new_set = sibling - visited
        for n in new_set:
            visited_order.append({"nodeId": vertex,
                                  "edges": [
                                      {"source": vertex, "target": n}]})
        # print("NEW_SET", set(G[vertex]), new_set)
        queue.extend(new_set)

    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    if len(queue):
        next_node = queue[0]
        parent_node = parent or vertex
        # print("====queue", len(queue), parent_node, next_node)

        bfs_graph(G, queue, visited_order, vertex, visited)
    # if visited is None:
    #     visited = set()
    # visited.add(start_node)
    # # print(start_node, end=';')  # Відвідуємо вершину

    # for neighbor in G[start_node]:
    #     visited_order.append({"nodeId": start_node,
    #                           "edges": [
    #                               {"source": start_node, "target": neighbor}]})
    #     if neighbor not in visited:
    #         bfs_graph(G, neighbor, visited_order, visited=visited)


# Example usage
if __name__ == "__main__":
    # Create a Graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4),
                     (4, 5), (5, 1), (3, 6), (2, 6)])
    print(G.edges)
    # Perform BFS starting from node 1
    start_node = 1
    visited_order = []
    bfs_graph(G, deque([start_node]), visited_order)

    print(
        f"BFS traversal order starting from node {start_node} ({len(visited_order)} steps): {visited_order}")
    nx.draw_networkx(G)
    plt.show()
