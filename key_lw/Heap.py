import random
class Max_Heap:
    def __init__(self):
        self.ht=[]
        self.size=0
    def sinkdown(self,i):
        if(i*2>self.size):
            return 0
        elif(i*2==self.size):
            if(self.ht[i]<self.ht[i*2]):
                self.ht[i],self.ht[i*2]=self.ht[i*2],self.ht[i]
        else:
            p=self.ht[i*2]
            pi=i*2
            if(p<self.ht[i*2+1]):
                pi=i*2+1
                p=self.ht[i*2+1]
            if(self.ht[i]<p):
                self.ht[i],self.ht[pi]=p,self.ht[i]
                self.sinkdown(pi)
    def creatheap(self,l):
        self.size=len(l)
        self.ht=[None]+l
        for i in range(self.size,0,-1):
            self.sinkdown(i)
    def delete(self):
        if(self.size>=1):
            self.size-=1
        else:
            print("empty")
            return 0
        self.ht[1]=self.ht[self.size+1]
        self.sinkdown(1)
        self.ht=self.ht[0:self.size+1]
    def heapsort(self):
        while(self.size>1):
            self.ht[1],self.ht[self.size]=self.ht[self.size],self.ht[1]
            self.size-=1
            self.sinkdown(1)
            
l=[random.randint(1,100) for i in range(1,6)]
A=Max_Heap()
A.creatheap(l)
print(A.ht)
A.delete()
A.delete()
print(A.hts)