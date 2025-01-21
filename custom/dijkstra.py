import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(G: nx.Graph, start):
    distances = {vertex: float('infinity') for vertex in G}
    distances[start] = 0
    unvisited = list(G.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, data in G[current_vertex].items():
            weight = data["weight"]
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


def all_pairs_shortest_path(G: nx.Graph):
    all_distances = {}

    for vertex in G:
        all_distances[vertex] = dijkstra(G, vertex)

    return all_distances


if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (1, 2, {"weight": 10}),
        (1, 3, {"weight": 15}),
        (2, 4, {"weight": 8}),
        (3, 4, {"weight": 11}),
        (4, 5, {"weight": 17}),
        (5, 1, {"weight": 21}),
        (3, 6, {"weight": 12}),
        (2, 6, {"weight": 19})
    ])

    print("Cross check:")
    shortest_paths = all_pairs_shortest_path(G)
    for start in shortest_paths:
        print(f"Path from {start}: {shortest_paths[start]}")

    nx.draw_networkx(G)
    plt.show()
