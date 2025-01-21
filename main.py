import networkx as nx
import matplotlib.pyplot as plt
import search
from collections import deque
from custom.dijkstra import dijkstra
from generage_network import generate_network
from graph_analyse import graph_analyse
from dfs_graph import dfs_graph
from bfs_graph import bfs_graph
from transform_multidigraph_to_d3 import transform_multidigraph_to_d3
from write_json_data import write_json_data

# Generate network from OpenStreetMap
G = generate_network()


fig, ax = plt.subplots(figsize=(10, 10))
theme = ("white", "grey", "blue")
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=16,
        node_color="black", edge_color="blue", font_size=8)
edge_labels = nx.get_edge_attributes(
    G, 'weight')  # Get weights as a dictionary
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_labels, font_size=10, font_color="red")
plt.show()

meta = graph_analyse(G)
d3_data = transform_multidigraph_to_d3(G)
d3_data["meta"] = meta
write_json_data("cache/d3_data.json", d3_data)

# ======== DFS
start_node = 405614573
dfs_visited_nodes = []
dfs_graph(G, start_node, dfs_visited_nodes)

write_json_data("cache/dfs_visited_nodes.json",
                {
                    "title": "DFS Algorithm Visualization",
                    "data": dfs_visited_nodes
                })

print(
    f"DFS traversal order starting from node {start_node} ({len(dfs_visited_nodes)} steps)")

# ======== BFS
bfs_visited_nodes = []
bfs_graph(G, deque([start_node]), bfs_visited_nodes)

write_json_data("cache/bfs_visited_nodes.json",
                {
                    "title": "BFS Algorithm Visualization",
                    "data": bfs_visited_nodes
                })

print(
    f"BFS traversal order starting from node {start_node} ({len(bfs_visited_nodes)} steps)")

# Finding a path between two graph points
end_node = 1302669431
dfs_path = search.dfs(G, start_node=start_node, end_node=end_node)
bfs_path = search.bfs(G, start_node=start_node, end_node=end_node)
print("dfs_path", dfs_path)
print(f"Found the path DFS (len={len(dfs_path)}):", dfs_path)
print(f"Found the path BFS (len={len(bfs_path)}):", bfs_path)

print(f"Function call for vertex {start_node}", list(
    dijkstra(G, start_node).values())[:5], "...")
print(f"Function call for vertex {end_node}", list(
    dijkstra(G, end_node).values())[:5], "...")
