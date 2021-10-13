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
def Prim(G,s):
    key={}
    parent={}
    w={}
    e={}
    for i in G.edges(data=True):
        w[i[0]+i[1]]=i[2]["weight"]
        w[i[1]+i[0]]=i[2]["weight"]
    for i in G.nodes:
        key[i]=9999999
        parent[i]=None
    key[s]=0
    V=list(G.nodes)
    while(len(V)>0):
        a=V[0]
        for i in V:
            if(key[i]<key[a]):
                a=i
        V.remove(a)
        if(parent[a]!=None):
            e[a+parent[a]]=key[a]
        for i in G.adj[a]:
            if (key[i]>w[i+a] and i in V):
                key[i]=w[i+a]
                parent[i]=a
    print(e)
Prim(G,"A")