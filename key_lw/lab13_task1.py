class graph:
    def __init__(self):
        self.l=[]
    def add_node(self,n):
        self.l.append([n])
    def add_undirectedge(self,s,e): 
        a=0
        b=0
        for i in range(0,len(self.l)):
             if(self.l[i][0]==s):
                 a+=1
             if(self.l[i][0]==e):
                 b+=1
        if(a==0):
            self.add_node(s)
        if(b==0):
            self.add_node(e)
        for i in range(0,len(self.l)):
            if(self.l[i][0]==s):
                self.l[i].append(e)
                a+=1
            if(self.l[i][0]==e):
                self.l[i].append(s)
                b+=1
    def getnode(self):
        l=[]
        for i in range(0,len(self.l)):
            l.append(self.l[i][0])
        return l
    def getedge(self):
        l=[]
        for i in range(0,len(self.l)):
            for j in range(1,len(self.l[i])):
                if(self.l[i][0]<self.l[i][j]):
                    l.append([self.l[i][0],self.l[i][j]])
        return l
    def getdegree(self,n):
        for i in range(0,len(self.l)):
            if(self.l[i][0]==n):
                return len(self.l[i])-1
    def getneibour(self,n):
        for i in range(0,len(self.l)):
            if(self.l[i][0]==n):
                return self.l[i][1:]
    def findnode(self,n):
        for i in range(0,len(self.l)):
            if(self.l[i][0]==n):
                return i
    def DFS(self):
        st=["unvisited"]*(len(self.l)+1)
        fr=[None]*(len(self.l)+1)
        i=0
        di=1
        while(i!=None):
            st[self.l[i][0]]="visited"
            if(di>=len(self.l[i])):
                i=fr[self.l[i][0]]
                di=1
                if(i!=None):
                    print(self.l[i][0])
            elif(st[self.l[i][di]]=="unvisited"):
                fr[self.l[i][di]]=i
                i=self.findnode(self.l[i][di])
                st[self.l[i][0]]="visited"
                print(self.l[i][0])
                di=1
            elif(st[self.l[i][di]]=="visited"):
                di+=1
A=graph()
A.add_undirectedge(1,2)
A.add_undirectedge(4,2)
A.add_undirectedge(3,2)
A.add_undirectedge(3,5)
#print(A.getnode())
#print(A.getneibour(3))
#print(A.l)
A.DFS()