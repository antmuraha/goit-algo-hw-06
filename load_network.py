import json
import osmnx as ox
import networkx as nx
from shapely.geometry import LineString


def load_network():
    with open("cache/graph.json", "r") as f:
        data = json.load(f)

    # Реконструкція графу
    G = nx.MultiDiGraph()

    # Додавання вузлів
    for node in data["nodes"]:
        node_id = node.pop("id")
        G.add_node(node_id, **node)

    # Додавання ребер
    for edge in data["edges"]:
        source = edge.pop("source")
        target = edge.pop("target")

        # Відновлення геометрії з координат, якщо є
        if "geometry" in edge:
            edge["geometry"] = LineString(edge["geometry"])

        G.add_edge(source, target, **edge)

    print("Граф успішно відновлено!", G)
    # Перевірка кількості вузлів та ребер
    print("Кількість вузлів:", G.number_of_nodes())
    print("Кількість ребер:", G.number_of_edges())
    # G = nx.Graph(G)
    # ox.simplification.simplify_graph()

    highways_to_keep = ['primary']
    H = nx.MultiDiGraph()
    for u,v,attr in G.edges(data=True):
        if attr['highway'] in highways_to_keep:
            # print("HHHHHHHH")
            H.add_edge(u,v,attr_dict=attr)
            # H.nodes[u] = G.nodes[u]
            # H.nodes[v] = G.nodes[v]

    if "crs" not in H.graph:
    # Assign the EPSG:4326 CRS (WGS 84)
        H.graph["crs"] = "EPSG:4326"

    return H


if __name__ == "__main__":
    load_network()
