import copy
#def mergesort(l):
#    if(len(l)<=1):
#        return l
#    else:
#        mid=len(l)//2
#        left=mergesort(l[0:mid])
#        right=mergesort(l[mid:len(l)])
#        result=[]
#        l,r=0,0
#        while(len(left)>l and len(right)>r):
#            if(left[l]<right[r]):
#                result.append(left[l])
#                l+=1
#            else:
#                result.append(right[r])
#                r+=1
#        return result+right[r:len(right)]+left[l:len(left)]
#print(mergesort([5,2,7,8,3,1,99,34]))
##############################################################################
#def multiply(a,b):
#    if(len(str(a))<=1 or len(str(b))<=1):
#        return int(a)*int(b)
#    elif(len(str(a))>0 and len(str(b))>0):
#        a=str(a)
#        b=str(b)
#        while(len(a)>len(b)):
#            b="0"+b
#        while(len(b)>len(a)):
#            a="0"+a
#        a1=a[0:len(a)//2]
#        a2=a[len(a)//2:len(a)]
#        b1=b[0:len(b)//2]
#        b2=b[len(b)//2:len(b)]
#        a1b1=multiply(a1,b1)
#        a2b2=multiply(a2,b2)
#        c=multiply((int(a1)+int(a2)),(int(b1)+int(b2)))-int(a1b1)-int(a2b2)
#        return int(a1b1)*10**(len(a2)+len(b2))+int(c)*10**(len(a2))+int(a2b2)
#print(multiply(29400005,105012345))
################################################################################
#def select_k(l,k):
#    def median(l):
#        re=[]
#        for i in range(0,(len(l)//5)*5,5):
#            ls=mergesort(l[i:i+5])
#            re.append(ls[2])
#        return selectk(re,len(re)//2)
#    def selectk(l,k):
#        if(len(l)<=1):
#            return l[0]
#        if(len(l)<200):
#            med=l[0]
#        else:
#            med=median(l)
#        left=[]
#        right=[]
#        for i in l:
#            if(i<med):
#                left.append(i)
#            else:
#                right.append(i)
#        right.remove(med)
#        if(k<=len(left)):
#            return selectk(left,k)
#        elif(k==len(left)+1):
#            return med
#        else:
#            return selectk(right,k-1-len(left))
#    return selectk(l,k)
#print(select_k([1,2,3,4,5],2))
#################################################################################
#class bts:
#    def __init__(self,data):
#        self.data=data
#        self.left=None
#        self.right=None
#        self.parent=None
#    def insert(self,k):
#        if(k==self.data):
#            return
#        elif(k<self.data):
#            if(self.left!=None):
#                self.left.insert(k)
#            else:
#                self.left=bts(k)
#                self.left.parent=self.left
#        elif(k>self.data):
#            if(self.right!=None):
#                self.right.insert(k)
#            else:
#                self.right=bts(k)
#                self.right.parent=self.right
#    def creat(self,l):
#        for i in l:
#            self.insert(i)
#    def pt(self):
#        if(self.left!=None):
#            self.left.pt()
#        print(self.data)
#        if(self.right!=None):
#            self.right.pt()
#    def allpath(self,l=[]):
#        if(self.left==None and self.right==None):
#            print(l+[self.data])
#        if(self.right!=None):
#            self.right.allpath(l+[self.data])
#        if(self.left!=None):
#            self.left.allpath(l+[self.data])
#    def longestpath(self,l=[]):
#        if(self.left==None and self.right==None):
#            return [1,[self.data]]
#        elif(self.left==None):
#            return [self.right.longestpath()[0]+1,self.right.longestpath()[1]+[self.data]]
#        elif(self.right==None):
#            return [self.left.longestpath()[0]+1,self.left.longestpath()[1]+[self.data]]
#        else:
#            if(self.left.longestpath()[0]>self.right.longestpath()[0]):
#                return [self.left.longestpath()[0]+1,self.left.longestpath()[1]+[self.data]]
#            else:
#                return [self.right.longestpath()[0]+1,self.right.longestpath()[1]+[self.data]]
#a=bts(10)
#a.creat([4,14,2,5,11,15])
##a.allpath()
#print(a.longestpath())
################################################################################      
#class Hash:
#    def __init__(self,size=7):
#        self.table=[None for i in range(size)]
#        self.size=size   
#        self.doublehash=13
#        self.num=0
#    def insert_linearProbing(self,data):
#        l=data%self.size
#        p=l
#        while(self.table[p]!=None):
#            p=(p+1)%self.size
#            if(p==l):
#                return False
#        self.table[p]=data
#    def creat(self,l):
#        for i in l:
#            if(i!=None):
#                self.insert_doublehashing(i)
#            print(self.table)
#    def insert_quadraticProbing(self,data):
#        l=data%self.size
#        p=l
#        i=1
#        while(self.table[p]!=None):
#            p=(p+i**2)%self.size
#            i=i+1
#            if(p==l):
#                return False
#        self.table[p]=data
#    def insert_doublehashing(self,data):
#        l=data%self.size
#        p=l
#        i=1
#        re=self.doublehash-data%self.doublehash
#        while(self.table[p]!=None):
#            p=(p+i*re)%self.size
#            i=i+1
#            if(p==l):
#                return False
#        self.table[p]=data
#        self.num+=1
#        if(self.num/self.size>0.7):
#            self.rehash()
#    def rehash(self):
#        def prim(k):
#            for i in range(2,k):
#                if k%i==0:
#                    return False
#            return True
#        n=2*self.size
#        while(not prim(n)):
#            n=n-1
#        reh=Hash(n)
#        reh.creat(self.table)
#        self.size=n
#        self.table=copy.deepcopy(reh.table)
#    def transform(self,l):
#        li=[0 for i in range(len(l))]
#        for i in range(len(l)):
#            for j in l[i]:
#                li[i]+=ord(j)
#        return li
#                
#a=Hash()
#a.creat([44,56,2,78,123,1235,127,34748,2456,2929,5634,452536])
#print(a.transform(["asd","louis"])
##############################################################################
#class maxheap:
#    def __init__(self):
#        self.l=[None]
#        self.num=0
#    def insert(self,k):
#        self.num+=1
#        self.l.append(k)
#        p=self.num//2
#        i=self.num
#        while(self.l[p]!=None and k>self.l[p]):
#            self.l[p],self.l[i]=k,self.l[p]
#            i=p
#            p=p//2
#    def creat(self,l):
#        for i in l:
#            self.insert(i)
#    def sinkdown(self,i):
#        if(i*2<=self.num):
#            s=self.l[i*2]
#            skey=i*2
#            if(i*2+1<=self.num):
#                if(self.l[i*2+1]>self.l[i*2]):
#                    s=self.l[i*2+1]
#                    skey=i*2+1
#            if(self.l[i]<self.l[skey]):
#                self.l[i],self.l[skey]=self.l[skey],self.l[i]
#                self.sinkdown(skey)
#    def heapsort(self):
#        while(self.num>0):
#            print(self.l)
#            self.l[1],self.l[self.num]=self.l[self.num],self.l[1]
#            self.num-=1
#            self.sinkdown(1)
#a=maxheap()
#a.creat([6,3,8,45,20,1234,167,34,2,5])
#a.heapsort()
###############################################################################
import networkx as nx
G=nx.Graph()
G1=nx.Graph()
G2=nx.DiGraph()
G3=nx.DiGraph()
G.add_edge('A','B',weight=6) 
G.add_edge('A','C',weight=2) 
G.add_edge('C','D',weight=1) 
G.add_edge('C','E',weight=7) 
G.add_edge('C','F',weight=9) 
G.add_edge('A','D',weight=3) 
G.add_edge('G','E',weight=7) 
G.add_edge('G','C',weight=4) 
G.add_edge('E','D',weight=5)
G1.add_edge("A","B")
G1.add_edge("A","C")
G1.add_edge("B","D")
G1.add_edge("B","G")
G1.add_edge("B","F")
G1.add_edge("D","E")
G1.add_edge("F","E")
G1.add_edge("G","E")
G2.add_edge("undershorts","pants")
G2.add_edge("undershorts","shoes")
G2.add_edge("pants","shoes")
G2.add_edge("pants","belt")
G2.add_edge("shirt","belt")
G2.add_edge("shirt","tie")
G2.add_edge("tie","jacket")
G2.add_edge("belt","jacket")
G2.add_edge("socks","shoes")
G3.add_edge("a","b")
G3.add_edge("b","c")
G3.add_edge("c","d")
G3.add_edge("d","c")
G3.add_edge("d","h")
G3.add_edge("g","h")
G3.add_edge("c","g")
G3.add_edge("f","g")
G3.add_edge("g","f")
G3.add_edge("b","f")
G3.add_edge("b","e")
G3.add_edge("e","a")
G3.add_edge("h","h")
def BFS1(s,G):
    n=[]
    n.append(s)
    s={}
    p={}
    for i in G.nodes:
        s[i]="unvisited"
    while(len(n)>0):
        s[n[0]]="visited"
        for i in G.adj[n[0]]:
            if(s[i]=="unvisited"):
                n.append(i)
                s[i]="visited"
                p[i]=n[0]
        del n[0]
    return p
def BFS2(st,G):
    s={}
    l=[[]for b in range(len(G.nodes))]
    for a in G.nodes:
        s[a]="unvisited"
    s[st]="visited"
    l[0].append(st)
    for i in range(len(G.nodes)):
        for j in l[i]:
            for k in G.adj[j]:
                if(s[k]=="unvisited"):
                    l[i+1].append(k)
                    s[k]="visited"
    return l
def DFS(G):
    s={}
    l=[]
    stime={}
    for i in G.nodes:
        s[i]="unvisited"
    def dfss(st,time):
        s[st]="visited"
        time=time+1
        l.append(st)
        stime[st]=[time]
        for i in G.adj[st]:
            if(s[i]=="unvisited"):
                time=dfss(i,time)
        time=time+1
        stime[st]+=[time]
        return time
    for i in G.nodes:
        if(s[i]=="unvisited"):
            dfss(i,-1)
    return l,stime
#print(topological_sort(G))
#print(DFS(G))
def topological_sort(G):
    s={}
    l=[]
    stime={}
    for i in G.nodes:
        s[i]="unvisited"
    def dfss(st,time):
        s[st]="visited"
        time=time+1
        stime[st]=[time]
        for i in G.adj[st]:
            if(s[i]=="unvisited"):
                time=dfss(i,time)
        time=time+1
        stime[st]+=[time]
        l.append(st)
        return time
    for i in G.nodes:
        if(s[i]=="unvisited"):
            dfss(i,-1)
    l.reverse()
    return l,stime
def stronglyConnectedComponent(G):
    li,stime=topological_sort(G)
    Gt=nx.DiGraph()
    for i in G.edges(data=True):
        Gt.add_edge(i[1],i[0])
    def DFS2(G):
        s={}
        l=[]
        stime={}
        for i in G.nodes:
            s[i]="unvisited"
        def dfss(st,time):
            s[st]="visited"
            time=time+1
            l.append(st)
            stime[st]=[time]
            for i in G.adj[st]:
                if(s[i]=="unvisited"):
                    time=dfss(i,time)
            time=time+1
            stime[st]+=[time]
            return time
        for i in li:
            if(s[i]=="unvisited"):
                dfss(i,-1)
        return l,stime
    return DFS2(Gt)
print(stronglyConnectedComponent(G3))
#class Min_Heap:
#    def __init__(self,d):
#        self.ht=[]
#        self.size=0
#        self.d=d
#    def sinkdown(self,i):
#        if(i*2>self.size):
#            return 0
#        elif(i*2==self.size):
#            if(self.d[self.ht[i]]>self.d[self.ht[i*2]]):
#                self.ht[i],self.ht[i*2]=self.ht[i*2],self.ht[i]
#        else:
#            p=self.d[self.ht[i*2]]
#            pi=i*2
#            if(p>self.d[self.ht[i*2+1]]):
#                pi=i*2+1
#                p=self.d[self.ht[i*2+1]]
#            if(self.d[self.ht[i]]>p):
#                self.ht[i],self.ht[pi]=p,self.ht[i]
#                self.sinkdown(pi)
#    def creatheap(self,l):
#        self.size=len(l)
#        self.ht=[None]+l
#        for i in range(self.size,0,-1):
#            self.sinkdown(i)
#    def delete(self):
#        if(self.size>=1):
#            self.size-=1
#        else:
#            print("empty")
#            return 0
#        self.ht[1]=self.ht[self.size+1]
#        self.sinkdown(1)
#        self.ht=self.ht[0:self.size+1]
#    def heapsort(self):
#        while(self.size>1):
#            self.ht[1],self.ht[self.size]=self.ht[self.size],self.ht[1]
#            self.size-=1
#            self.sinkdown(1)
def shortest_path(G,s):
    def relax(u,v,w,p,d):
        if(d[v]>d[u]+w[u+v]):
            d[v]=d[u]+w[u+v]
            p[v]=u
    def initial(G):
        d={}
        p={}
        w={}
        for i in G.edges(data=True):
            d[i[0]]=9999999
            p[i[0]]=None
            d[i[1]]=9999999
            p[i[1]]=None
            w[i[0]+i[1]]=i[2]["weight"]
            w[i[1]+i[0]]=i[2]["weight"]
        return d,p,w
    d,p,w=initial(G)
    l=list(G.nodes)
    d[s]=0
#    print(d,p,w)
    while(len(l)>0):
        a=l[0]
        for k in l:
            if(d[k]<d[a]):
                a=k
        for j in G.adj[a]:
            relax(a,j,w,p,d)
        l.remove(a)
    return p
#print(shortest_path(G,'A'))
def MST(G):
    def mergesort(l):
        if(len(l)<=1):
            return l
        else:
            mid=len(l)//2
            left=mergesort(l[0:mid])
            right=mergesort(l[mid:len(l)])
            re=[]
            l,r=0,0
            while(l<len(left) and r<len(right)):
                if(left[l][2]["weight"]<right[r][2]["weight"]):
                    re.append(left[l])
                    l=l+1
                else:
                    re.append(right[r])
                    r=r+1
            return re+left[l:]+right[r:]
    def initial(G):
        d={}
        p={}
        w={}
        for i in G.edges(data=True):
            d[i[0]]=9999999
            p[i[0]]=None
            d[i[1]]=9999999
            p[i[1]]=None
            w[i[0]+i[1]]=i[2]["weight"]
            w[i[1]+i[0]]=i[2]["weight"]
        return d,p,w
    d,p,w=initial(G)
    def check(u,v,p):
        while(p[u]!=None):
            u=p[u]
        while(p[v]!=None):
            v=p[v]
        if(u==v):
            return False
        else:
            return True
    E=mergesort(list(G.edges(data=True)))
    re=[]
    while(len(E)>0):
        if(check(E[0][0],E[0][1],p)):
            re.append(E[0])
            if(E[0][0]>E[0][1]):
                p[E[0][0]]=E[0][1]
            else:
                p[E[0][1]]=E[0][0]
        del E[0]
    return re
#print(MST(G))        
    
G.add_node('A')
G.add_edge("A","B",weight=100)  
G.nodes
G.edges(data=True)
        
        
        
        
        
        
        
        
        
        
        
        
        