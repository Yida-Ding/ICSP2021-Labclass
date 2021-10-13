class Hash_linearprobing:
    def __init__(self,p):
        self.p=p
        self.ht=[None]*p
    def insert(self,k):
        a=k%self.p
        i=0
        while(self.ht[(a+i)%self.p]!=None):
            if(i==self.p):
                print("Full")
                return 0
            i+=1
        self.ht[(a+i)%self.p]=k
    def search(self,k):
        a=k%self.p
        i=0
        while(self.ht[(a+i)%self.p]!=None and i!=self.p):
            if(self.ht[(a+i)%self.p]==k):
                return True
            i+=1
        return False
    def delete(self,k):
        p=self.p
        a=k%p
        i=0
        while(self.ht[(a+i)%self.p]!=None and i!=self.p):
            if(self.ht[(a+i)%self.p]==k):
                self.ht[(a+i)%self.p]="deleted"
            i+=1 
A=Hash_linearprobing(7)
for i in range(1,8):
    A.insert(5+7*i)
#A.insert(5)
#A.insert(12)
A.delete(40)
print(A.search(40))
                