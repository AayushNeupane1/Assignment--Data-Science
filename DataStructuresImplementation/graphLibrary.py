import networkx as nx

graph=nx.Graph()

graph.add_edge(10,20)
graph.add_edge(30,40)
graph.add_edge(50,60)

print("Nodes:",graph.nodes())
print("Nodes:",graph.edges())



