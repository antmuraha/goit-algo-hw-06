import networkx as nx
import osmnx as ox

bbox_default = (33.384748, 47.902419, 33.397021, 47.923273)


def generate_network(bbox: str = bbox_default):
    """
    Generate network from OpenStreetMap
    default bbox: (33.384748, 47.902419, 33.397021, 47.923273)

    To search for bbox you can use  http://bboxfinder.com/ or similar.
    """
    G = ox.graph_from_bbox(bbox,  network_type="drive")

    # Preprocessing of graph data
    new_G = nx.Graph()
    edges = []
    remove_nodes = []
    for n, data in G.nodes(data=True):
        es = list(G[n])
        if es == 0:
            continue
        pos = [data["x"], data["y"]]
        new_G.add_node(n, pos=pos)

    weight_index = 1
    for e in G.edges(data=True):
        s, t, data = e
        new_G.add_edge(s, t, weight=weight_index)
        weight_index = weight_index + 1

    new_G.add_edges_from(edges)
    for n in remove_nodes:
        if n in new_G:
            new_G.remove_node(n)

    if "crs" not in new_G.graph:
        # Assign the EPSG:4326 CRS (WGS 84)
        new_G.graph["crs"] = "EPSG:4326"

    print("Generate graph:", new_G)
    return new_G


if __name__ == "__main__":
    G = generate_network()
    print(G)
