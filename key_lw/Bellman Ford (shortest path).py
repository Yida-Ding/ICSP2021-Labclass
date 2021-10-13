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
def Bellman(G,s):
    parent,d,w=initialize(G)
    d[s]=0
    for i in range(0,len(list(G.nodes))-1):
        for j in G.edges(data=True):
            relax(j[0],j[1],G,parent,d,w)
#    b="B"
#    while(b!=None):
#        print(b)
#        b=parent[b]
    for j in G.edges(data=True):
        if(d[j[1]]>d[j[0]]+w[j[0]+j[1]]):
            return False
    return True,parent  # the first parameter represent whether there is negative cycle, and parent store the path
print(Bellman(G,'A'))