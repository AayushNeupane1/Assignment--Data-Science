
import networkx as nx

tree=nx.DiGraph()

tree.add_edge(100, 99)   
tree.add_edge(100, 101) 

print(tree.nodes)
print(tree.edges)