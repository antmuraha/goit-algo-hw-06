import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import search
from collections import deque
from geopy.distance import geodesic  # To calculate geographical distance
from custom.dijkstra import dijkstra
from generage_network import generate_network
from load_network import load_network
from draw_network import draw_network
from graph_analyse import graph_analyse
from dfs_graph import dfs_graph
from bfs_graph import bfs_graph
from dfs_recursive import dfs_recursive
from transform_multidigraph_to_d3 import transform_multidigraph_to_d3
from write_json_data import write_json_data

# G = load_network()
G = generate_network()
# print("LEN_1", len(G), G)

# Remove duplicated edges (keeping only one edge for each pair of nodes)
# seen_edges = set()  # To track seen edges
# edges_to_remove = []  # List of edges to remove

# # seen_edges.add((1,2))
# # if (1,2) in seen_edges:
# #     print("1111111")


# for u, v in list(G.edges()):
#     # print("====", u, v)
#     if (u, v) in seen_edges or (v, u) in seen_edges:
#         edges_to_remove.append((u, v))
#     else:
#         seen_edges.add((u, v))  # Add the edge pair to the seen set

# print("seen_edges", len(seen_edges))
# print("edges_to_remove", len(edges_to_remove))
# # # Remove duplicated edges
# G.remove_edges_from(edges_to_remove)


# G = nx.Graph(G)
# G = nx.DiGraph(G)
# print("LEN_2", len(G), G)

# highways_to_keep = ['primary']
# H = nx.MultiDiGraph()
# for u, v, attr in G.edges(data=True):
#     if attr['highway'] in highways_to_keep:
#         # print("HHHHHHHH")
#         H.add_edge(u, v, attr_dict=attr)
#         # H.nodes[u] = G.nodes[u]
#         # H.nodes[v] = G.nodes[v]
#         H.add_node(u, x=u, **attr)
#         H.add_node(v, y=v, **attr)

# if "crs" not in H.graph:
#     # Assign the EPSG:4326 CRS (WGS 84)
#     H.graph["crs"] = "EPSG:4326"

# draw_network(G)


# Step 2: Define a function to compute the Euclidean distance (or geographical distance)
# def calculate_distance(node1, node2):
#     # Extract coordinates from geometry
#     point1 = G.nodes[node1]
#     point2 = G.nodes[node2]
#     # print("CALCULATE", point1["y"], point2)
#     # Using geodesic for geographical distance
#     return geodesic((point1["y"], point1["x"]), (point2["y"], point2["x"])).meters


# Step 3: Define a distance threshold (in meters)
# distance_threshold = 50  # Distance in meters

# Step 4: Create a list of close nodes based on distance threshold
# edges_to_add = []

# for node1, data1 in G.nodes(data=True):
#     # if 'geometry' not in data1:
#     #     continue  # Skip nodes without geometry

#     for node2, data2 in G.nodes(data=True):
#         if node1 == node2:
#             print("EQUAL", node1)
#             continue  # Skip the same node or nodes without geometry

#         # Calculate the distance between nodes
#         dist = calculate_distance(node1, node2)
#         # print("DSIT", dist, node1, node2)
#         # If the distance is less than the threshold, add an edge between these nodes
#         if dist < distance_threshold:
#             # Add a new edge (optionally, set attributes like weight, distance, etc.)
#             edges_to_add.append(
#                 (node1, node2, {'weight': dist, 'distance': dist}))

# print("ADDED", len(edges_to_add))
# Step 5: Add the new edges to the graph
# G.add_edges_from(edges_to_add)
# G = G.to_directed()

# ox.plot_graph(G, node_size=5, edge_color="blue", bgcolor="white", node_color="black")
# plt.show()


# Step 3: Plot the graph with arrows
fig, ax = plt.subplots(figsize=(10, 10))

# themes = [
#     ("white", "grey", "blue"),
#     ("lightgray", "darkblue", "yellow"),
#     ("black", "white", "cyan"),
#     ("midnightblue", "lightgray", "orange"),
#     ("beige", "brown", "darkgreen"),
#     ("mintcream", "teal", "darkred"),
#     ("lavender", "purple", "gold"),
#     ("ivory", "darkgreen", "blueviolet"),
#     ("aliceblue", "cornflowerblue", "deeppink"),
#     ("gainsboro", "dimgray", "limegreen"),
# ]
theme = ("white", "grey", "blue")

# Use OSMnx to plot the base graph (without arrows)
# ox.plot_graph(G, ax=ax, node_size=10,  edge_linewidth=1,
#               show=False, bgcolor=theme[0], edge_color=theme[1], edge_alpha=0.5, node_color=theme[2])

# print(G[450862239])
pos = nx.get_node_attributes(G, 'pos')
# nx.draw_networkx(G, pos=pos,
#                  node_size=16,
#                  node_color="black",
#                  edge_color="blue",
#                  font_size=8,
#                  with_labels=True
#                  )
nx.draw(G, pos, with_labels=True, node_size=16,
        node_color="black", edge_color="blue", font_size=8)

# Add edge labels (weights)
edge_labels = nx.get_edge_attributes(
    G, 'weight')  # Get weights as a dictionary
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_labels, font_size=10, font_color="red")


# pos = ox.graph_to_gdfs(G, nodes=False, edges=True).iloc(1)
# pos =nx.spring_layout(G)
# print("IIIIIIIII", pos)
# print("PPPPPPPP", pos)
# # Step 4: Manually add arrows on the directed edges
# # Draw directed edges with arrows
# nx.draw_networkx_edges(G, pos=pos,
#                        edgelist=G.edges(), width=1.0, alpha=0.5, edge_color='blue',
#                        arrows=True, ax=ax)

# Step 5: Add labels or additional customization (optional)
# You can add node labels, edge labels, etc. here if desired
# nx.draw_networkx_labels(G, pos=ox.graph_to_gdfs(G, nodes=False, edges=True)[1], ax=ax)

# Show the plot
plt.show()

print(list(G[335301767]))
# exit()


meta = graph_analyse(G)
# print(list(G.edges)[:5])

# print(G.nodes[start_node][])
# exit(0)

# print("IS_CONNECTED", nx.is_weakly_connected(G))
d3_data = transform_multidigraph_to_d3(G)
# print(data)
# meta["title"] = "DFS Algorithm Visualization"
# filename_visited_nodes = "dfs_visited_nodes"
d3_data["meta"] = meta
write_json_data("cache/d3_data.json", d3_data)

# ======== DFS
start_node = 405614573
end_node = None
dfs_visited_nodes = []
dfs_graph(G, start_node, dfs_visited_nodes, end_node)

write_json_data("cache/dfs_visited_nodes.json",
                {
                    "title": "DFS Algorithm Visualization",
                    "data": dfs_visited_nodes
                })
# dfs_recursive(G, start_node, visited_nodes)
print(
    f"DFS traversal order starting from node {start_node} ({len(dfs_visited_nodes)} steps)")

# ======== BFS
bfs_visited_nodes = []
bfs_graph(G, deque([start_node]), bfs_visited_nodes, end_node)

write_json_data("cache/bfs_visited_nodes.json",
                {
                    "title": "BFS Algorithm Visualization",
                    "data": bfs_visited_nodes
                })
# dfs_recursive(G, start_node, visited_nodes)
print(
    f"BFS traversal order starting from node {start_node} ({len(bfs_visited_nodes)} steps)")

# Finding the path from 'start' to 'end' using DFS and BFS
end_node = 454336375
dfs_search_visited_nodes = []
dfs_graph(G, start_node, dfs_search_visited_nodes, end_node)

write_json_data("cache/dfs_search_visited_nodes.json",
                {
                    "title": "DFS Algorithm Visualization",
                    "data": dfs_search_visited_nodes
                })
# dfs_recursive(G, start_node, visited_nodes)
print(
    f"DFS traversal order starting from node {start_node} ({len(dfs_search_visited_nodes)} steps)")

# ======== BFS
bfs_search_visited_nodes = []
bfs_graph(G, deque([start_node]), bfs_search_visited_nodes, end_node)

write_json_data("cache/bfs_search_visited_nodes.json",
                {
                    "title": "BFS Algorithm Visualization",
                    "data": bfs_search_visited_nodes
                })
# dfs_recursive(G, start_node, visited_nodes)
print(
    f"BFS traversal order starting from node {start_node} ({len(bfs_search_visited_nodes)} steps)")


# =================================================================
# Пошук конкретного шляху за допомогою DFS і BFS
# dfs_path = nx.dfs_predecessors(G, source=start_node)  # Отримання попередників DFS
# bfs_path = nx.shortest_path(G, source=start_node, target=end_node)  # Найкоротший шлях (BFS)

# # Відновлення шляху з DFS (відслідковуючи попередників)
# def reconstruct_path(predecessors, start, end):
#     path = []
#     current = end
#     while current != start:
#         path.append(current)
#         current = predecessors.get(current)
#         if current is None:  # Якщо шлях недоступний
#             return None
#     path.append(start)
#     return path[::-1]

# dfs_full_path = reconstruct_path(dfs_path, start_node, end_node)
dfs_path = search.dfs(G, start_node=start_node, end_node=end_node)
bfs_path = search.bfs(G, start_node=start_node, end_node=end_node)

print(f"Path DFS (len={len(dfs_path)}):", dfs_path)
print(f"Path BFS (len={len(bfs_path)}):", bfs_path)

print(f"Function call for vertex {start_node}", dijkstra(G, start_node))
print(f"Function call for vertex {end_node}", dijkstra(G, end_node))
