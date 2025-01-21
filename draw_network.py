import matplotlib.pyplot as plt
import osmnx as ox
import networkx as nx
# import osmnx as ox


def draw_network(G):
    # ox.plot_graph(G)
    # G = nx.Graph()

    # G.add_node("A")
    # G.add_nodes_from(["B", "C", "D"])

    # G.add_edge("A", "B")
    # G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

    # num_nodes = G.number_of_nodes()  # 4
    # num_edges = G.number_of_edges()  # 4
    # is_connected = nx.is_connected(G)  # True

    # G = nx.complete_graph(8)
    # nx.draw(G, with_labels=True)
    # plt.show()
                # pos = nx.spring_layout(G)  # Layout for nodes
                # nx.draw(G, pos, with_labels=True, arrows=True)
                # labels = nx.get_node_attributes(G, "label")
                # nx.draw_networkx_labels(
                #     G, pos, labels=labels,
                #     font_size=6,  # Font size
                #     font_color="red",  # Font color
                #     font_family="serif",  # Font family (e.g., serif, sans-serif)
                #     font_weight="bold",  # Font weight (e.g., bold, normal)
                # )
                # # nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
                # plt.show()
    ox.plot_graph(G)
