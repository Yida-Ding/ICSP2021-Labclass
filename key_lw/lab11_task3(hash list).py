class Hash_linearchain:
    def __init__(self,p):
        self.p=p
        self.ht=[]
        for i in range(p):
            self.ht.append([])
    def insert(self,k):
        a=k%self.p
        self.ht[a].append(k)
        print(self.ht)
    def search(self,x):
        a=x%self.p
        i=0
        while(i<len(self.ht[a])):
            if(self.ht[a][i]==x):
                return True
            i=i+1
        return False
    def delete(self,x):
        a=x%self.p
        if(self.search(x)):
            self.ht[a].remove(x)
A=Hash_linearchain(7)
A.insert(5)
print(A.search(5))
A.delete(5)
print(A.search(5))