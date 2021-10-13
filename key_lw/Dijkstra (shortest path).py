import networkx as nx
G=nx.Graph() 
G.add_edge('A','B',weight=6) 
G.add_edge('A','C',weight=2) 
G.add_edge('C','D',weight=1) 
G.add_edge('C','E',weight=7) 
G.add_edge('C','F',weight=9) 
G.add_edge('A','D',weight=3) 
G.add_edge('G','E',weight=7) 
G.add_edge('G','C',weight=4) 
G.add_edge('E','D',weight=5)
def initialize(G):
    parent={}
    d={}
    w={}
    for i in G.nodes:
        parent[i]=None
        d[i]=9999999
    for i in G.edges(data=True):
        w[i[0]+i[1]]=i[2]["weight"]
        w[i[1]+i[0]]=i[2]["weight"]
    return parent,d,w
def relax(u,v,G,parent,d,w):
    if(d[v]>d[u]+w[u+v]):
        d[v]=d[u]+w[u+v]
        parent[v]=u
def dijkstra(G,s):
    parent,d,w=initialize(G)
    S=[]
    Q=list(G.nodes)
    d[s]=0
    while(len(Q)>0):
        a=Q[0] #       here i use a list to store all nodes, which leads the runtime O(V^2). using min_heap will be faster
        for i in Q:
            if(d[i]<d[a]):
                a=i
        Q.remove(a)
        S.append(a)
        for j in G.adj[a]:
            relax(a,j,G,parent,d,w)
    return parent
print(dijkstra(G,'A'))