import osmnx as ox
from generage_network import generate_network
from load_network import load_network
from draw_network import draw_network

G = load_network()
# G = generate_network()
print("LEN", len(G))
# draw_network(G)

from keplergl import KeplerGl

# # Create a Kepler map with a dataset
# map_1 = KeplerGl()
# map_1.save_to_html(file_name="kepler_transport_network.html")
# Step 2: Set CRS for the graph (WGS 84, EPSG:4326)
# G = ox.project_graph(G, to_crs="ANN401")
if "crs" not in G.graph:
    # Assign the EPSG:4326 CRS (WGS 84)
    G.graph["crs"] = "EPSG:4326"
# G = ox.get_undirected(G)
nodes, edges = ox.graph_to_gdfs(G)

# Step 3: Create GeoJSON for nodes and edges
nodes_geojson = nodes.to_json()
edges_geojson = edges.to_json()

# Step 4: Initialize Kepler.gl Map
map_1 = KeplerGl(height=600)

# Step 5: Load the GeoJSON data into Kepler.gl
map_1.add_data(data=nodes_geojson, name="Nodes")
map_1.add_data(data=edges_geojson, name="Edges")

# Step 6: Display the map
map_1.save_to_html(file_name="sf_transport_network.html")

# import folium
# import numpy as np
# import requests
# import shapely
# from shapely.geometry import LineString

# for u, v, data in G.edges(data=True):
#     print("DATA", data['attr_dict']['geometry'])
#     # Get the coordinates of the start and end nodes
#     start_node = G.nodes[u]
#     end_node = G.nodes[v]
#     print("start_node", u, start_node)
#     print("end_node", v, end_node)
#     # Create a LineString geometry based on node coordinates
#     line = LineString([(start_node['x'], start_node['y']), (end_node['x'], end_node['y'])])
    
#     # Assign this geometry to the edge data
#     data['geometry'] = line


            # print(G.graph)
            # # G = G.to_undirected()
            # # Step 2: Check if CRS is assigned, and assign it if necessary
            # if "crs" not in G.graph:
            #     # Assign the EPSG:4326 CRS (WGS 84)
            #     G.graph["crs"] = "EPSG:4326"


            # x_vals = []
            # y_vals = []
            # nodes = G.nodes
            # for node, data in nodes(data=True):
            #     print("DDDDDDD", node)
            #     break
            #     # If coordinates are stored in the 'geometry' field (Shapely Point)
            #     if 'geometry' in data:
            #         point = data['geometry']
            #         x_vals.append(point.x)
            #         y_vals.append(point.y)

            # # Step 4: Compute the mean of x and y values
            # mean_x = np.mean(x_vals)
            # mean_y = np.mean(y_vals)
            # # Step 2: Get the positions (coordinates) of the nodes
            # # OSMnx provides node data in the form of 'x' and 'y' attributes
            # # Step 3: Convert the graph to GeoDataFrames (nodes and edges)
            # # G = ox.get_undirected(G)
            # # print("convert.to_digraph", G)
            # nodes, edges = ox.graph_to_gdfs(G, node_geometry=False, fill_edge_geometry=False)
            # # nodes = G.nodes
            # # edge = G.edges



            # # Step 4: Create a Folium Map centered around the average coordinates of the nodes
            # m = folium.Map(location=[mean_y, mean_x], zoom_start=12)

            # print("Y:", nodes)

            # # Step 4: Create a Folium Map centered around the average coordinates of the nodes
            # m = folium.Map(zoom_start=12)


            # for u, v, data in G.edges(data=True):
            #     print(f"Edge from {u} to {v}, geometry: {data.get('geometry')}")

            # # Step 5: Add edges (roads) to the Folium map
            # # Loop through each edge and add it to the map as a polyline
            # for _, edge in edges.iterrows():
            #     try:
            #         print("00000000000", edge['attr_dict'])
            #         print("111111", edge['attr_dict']['geometry'])
            #         # coords = list(edge['geometry'].coords)  # Extract coordinates of edge geometry
            #         coords = edge['attr_dict']['geometry'].coords
            #         print("222222", coords)
            #         start = [coords[0][1], coords[0][0]]  # (latitude, longitude) for start
            #         end = [coords[-1][1], coords[-1][0]]  # (latitude, longitude) for end
                    
            #         folium.PolyLine([start, end], color="blue", weight=2.5, opacity=1).add_to(m)
            #     except Exception as e:
            #         print("Error EDGE", e)

            # # Step 6: Add nodes (junctions) to the Folium map
            # # Loop through each node and add it to the map as a circle marker
            # # for _, node in nodes.iterrows():
            #     # print("node", node)
            #     # folium.CircleMarker(
            #     #     location=[node.geometry.y, node.geometry.x],  # (latitude, longitude)
            #     #     radius=3,  # Size of the circle marker
            #     #     color="red",
            #     #     fill=True,
            #     #     fill_color="red",
            #     #     fill_opacity=0.6,
            #     # ).add_to(m)

            # # m = folium.Map(tiles="cartodbpositron")

            # # geojson_data = requests.get(
            # #     "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/world_countries.json"
            # # ).json()

            # # folium.GeoJson(geojson_data, name="hello world").add_to(m)

            # # folium.LayerControl().add_to(m)
            # # folium.Html.save(outfile="map.html")
            # m.save("transport_network.html")
