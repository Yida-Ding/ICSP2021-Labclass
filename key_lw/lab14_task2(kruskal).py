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
def kruskal(G):
    def quicksort(li,l=0,r=-100):
        if(r==-100):
            r=len(li)-1
        if(l>=r):
            return 
        else:
            mid,l1,r1=li[l][2]["weight"],l,r
            while(l1<r1):
                while(li[l1][2]["weight"]<=mid and l1<len(li)-1):
                    l1+=1
                while(li[r1][2]["weight"]>mid):
                    r1-=1
                if(l1<r1):
                    li[l1],li[r1]=li[r1],li[l1]
            li[l],li[r1]=li[r1],li[l]
            quicksort(li,l,r1-1)
            quicksort(li,l1,r)
            return li
    def checkset(i,j,B):
        while(B[i]!=None):
            i=B[i]
        while(B[j]!=None):
            j=B[j]
        if(j==i):
            return False
        else:
            return True
    A=[]
    B={}
    E=[]
    for i in G.nodes:
        B[i]=None
    E=quicksort(list(G.edges(data=True)))
    for i in E:
        if(checkset(i[0],i[1],B)):
            A.append(i)
            if(i[0]<i[1]):
                B[i[1]]=i[0]
            else:
                B[i[0]]=i[1]
    return A
print(kruskal(G))