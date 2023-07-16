#Muhammad Rahmani
#SocialNetwork Pj6
#Session 8
import networkx as nx
import matplotlib.pyplot as plt

a = 100
b = 300
graph1 = nx.gnm_random_graph(a, b)

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(graph1)
nx.draw(graph1, pos, node_size=10, node_color='yellow', edge_color='black', alpha=0.7, with_labels=True)
plt.title("Rahndom Graph Erdős-Rényi (n=100، m=300)")
plt.show()

