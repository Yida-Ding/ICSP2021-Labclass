class Hash_doublehashing:
    def __init__(self,p,p2):
        self.p2=p2
        self.p=p
        self.ht=[None]*p
    def insert(self,k):
        a=k%self.p
        i=0
        co=k%self.p2
        while(self.ht[(a+i*co)%self.p]!=None):
            if(i==self.p):
                print("Full")
                return 0
            i+=1
        self.ht[(a+i*co)%self.p]=k
    def search(self,k):
        a=k%self.p
        i=0
        co=k%self.p2
        while(self.ht[(a+i*co)%self.p]!=None and i!=self.p):
            if(self.ht[(a+i*co)%self.p]==k):
                return True
            i+=1
        return False
    def delete(self,k):
        p=self.p
        a=k%p
        i=0
        co=k%self.p2
        while(self.ht[(a+i*co)%self.p]!=None and i!=self.p):
            if(self.ht[(a+i*co)%self.p]==k):
                self.ht[(a+i*co)%self.p]="deleted"
            i+=1 
A=Hash_doublehashing(7,11)
for i in range(1,2):
    A.insert(5+7*i)
#A.insert(5)
#A.insert(12)
#A.delete(40)
print(A.search(12))