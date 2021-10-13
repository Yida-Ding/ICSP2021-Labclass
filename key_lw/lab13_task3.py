import networkx as nx
import matplotlib.pyplot as plt
A=nx.Graph()
A.add_edge(1,2)
A.add_edge(4,2)
A.add_edge(3,2)
A.add_edge(3,5)
nx.draw(A)
plt.show()
#print(A.node)
#print(A.edges)
#print(A.degree())
#print(list(A.adj[2]))
#print(nx.shortest_path(A,1,5))
def DFS(s):
    