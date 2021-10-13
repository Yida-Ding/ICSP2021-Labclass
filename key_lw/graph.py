class graph:
    def __init__(self):
        self.l={}
    def add_node(self,n):
        self.l[n]=[None]
    def add_edge(self,s,e):
        if(s not in self.l):
            self.l[s]=[e]
        else:
            self.l[s].append(e)
        if(e not in self.l):
            self.l[e]=[s]
        else:
            self.l[e].append(s)
    def getnode(self):
        l=[]
        for i in self.l:
            l.append(i)
        return l
    def getedge(self):
        l=[]
        for i in self.l:
            for j in self.l[i]:
                if(i<j):
                    l.append((i,j))
        return l
    def getdegree(self,n):
        return len(self.l[n])
    def getneighbor(self,n):
        return self.l[n]
    def DFS_loop(self):
        st={}               # state
        fr={}               # from
        for i in self.l:
            st[i]="unvisited"
            fr[i]=None
        di=0                #direction
        print(i)             # above this line is the preparation for DFS
        while(i!=None):
            st[i]="visited"
            if(di>=len(self.l[i])):
                i,di=fr[i],0
                print(i)
            elif(st[self.l[i][di]]=="unvisited"):
                fr[self.l[i][di]],i=i,self.l[i][di]
                st[i],di="visited",0
                print(i)
            elif(st[self.l[i][di]]=="visited"):
                di+=1
    def DFS_recursion(self):
        st={}
        for i in self.l:
            st[i]="unvisited"
        def DFS_recursion2(i):
            print(i)
            st[i]="visited"
            for j in self.l[i]:
                if(st[j]=="unvisited"):
                    DFS_recursion2(j)
        DFS_recursion2(i)
    def BFS(self):
        st={}
        l=[]
        for i in self.l:
            st[i]="unvisited"
            l.append([])
        l[0].append(i)
        st[i]="visited"
        j=0
        for j in range(0,len(self.l)):
            for k in l[j]:
                for h in self.l[k]:
                    if(st[h]=="unvisited"):
                        l[j+1].append(h)
                        st[h]="visited"
        return l
A=graph()
A.add_edge(1,2)
A.add_edge(4,2)
A.add_edge(3,2)
A.add_edge(3,5)
#print(A.getnode())       
#print(A.getedge())       
#print(A.getdegree(3))       
#print(A.getneighbor(3))
#A.DFS_loop()     
#A.DFS_recursion()
#print(A.BFS())
