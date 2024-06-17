import itertools
import matplotlib.pyplot as plt
import networkx as nx
from netgraph import MultiGraph
import participantsColors as pc



G = nx.MultiGraph()

pos = {
    0: (0,0),
    1: (0, 1),
    2: (0,2),
    3: (1,0),
    4: (1,1),
    5: (1,2),
}

edge_to_weight = {
    ("C1", "C1", 2) : 2,
    ("C2", "C1", 3) : 3,
}

for edge, weight in edge_to_weight.items():
    G.add_edge(*edge, weight=weight)


MultiGraph(G, node_labels=True, edge_labels=edge_to_weight, edge_color='tab:blue')
plt.show()





# # Light 3 Nodes 

# # Creating Nodes
# # G = nx.MultiGraph()
# # # Define Number of Participants
# # colors = range(4)
# # pos = {
# #     0: (0,0),
# #     1: (0, 1),
# #     2: (0,2),
# #     3: (1,0),
# #     4: (1,1),
# #     5: (1,2),
# # }
# # G.add_nodes_from(pos.keys())
# # labels = {}
# # labels[0] = "C1"
# # labels[1] = "C2"
# # labels[2] = "C3"
# # labels[3] = "C1"
# # labels[4] = "C2"
# # labels[5] = "C3"

# # G.add_edges_from

# # # Define edges
# # p1 = [(2, 3)]
# # p2 = [(1,3), (2, 3)]

# # # nx.draw_networkx_edges(G, pos, edgelist=p1, edge_color=pc.colorsList[0])
# # # nx.draw_networkx_edges(G, pos, edgelist=p2, edge_color=pc.colorsList[1])
# # nx.draw(G, pos, labels)



# edge_to_weight = {
#     ("C3", "C1", 1) : 1,
#     ("C1", "C1", 2) : 2,
#     ("C2", "C1", 3) : 3,
# }

# G = nx.MultiGraph()

# G.add_edge(3,4)
# plt.show()


# from pyvis.network import Network

# net = Network()

# net.add_node(0, label="C1", group=1) 
# net.add_node(1, label="C2", group=1) 
# net.add_node(2, label="C3", group=1)
# net.add_node(3, label="C1", group=2)
# net.add_node(4, label="C2", group=2) 
# net.add_node(5, label="C3", group=2)

# net.add_edge(2,3, color= pc.colorsList[0], label="P1")
# net.add_edge(0,3, color = pc.colorsList[1], label="P2")
# net.add_edge(2,0, color = pc.colorsList[2], label="P3")
# net.add_edge(1,0, color = pc.colorsList[3], label = "P4")
# net.add_edge(2,0, color = pc.colorsList[3], label = "P4")
# net.write_html("basic.html")
