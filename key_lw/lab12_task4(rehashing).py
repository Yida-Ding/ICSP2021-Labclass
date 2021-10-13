import random
import copy
class Hash_doublehashing:
    def __init__(self,p2=7,p=11):
        self.p2=p2
        self.p=p
        self.ht=[None]*p
        self.nu=0
    def insert(self,k): 
        if(self.nu>0.5*len(self.ht)):
            self.rehashing()
        a=k%self.p
        i=0
        co=self.p2-(k%self.p2)
        while(self.ht[(a+i*co)%self.p]!=None and self.ht[(a+i*co)%self.p]!="deleted"):
            print("a")
            i+=1
        self.ht[(a+i*co)%self.p]=k
        self.nu+=1
    def rehashing(self):
        p=self.p*2
        while(True):
            a=0
            for i in range(2,p):
                if(p%i==0):
                    a+=1
            if(a==0):
                break
            p=p+1
        A=Hash_doublehashing(self.p2,p)
        for i in self.ht:
            if(i!=None and i!="deleted"):
                A.insert(i)
        self.p=p
        self.ht=copy.deepcopy(A.ht)
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
A=Hash_doublehashing()
for i in range(1,100):
    A.insert(random.randint(1,1000))
print(A.ht)
#A.insert(5)
#A.insert(12)
#A.delete(40)