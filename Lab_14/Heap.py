import random

class Heap:
    def __init__(self,L):
        self.A=[""]+L
        self.size=len(L)
        #heapify
        for i in range(self.size//2+1,0,-1):
            self.sinkdown(i)

    def sinkdown(self,i):
        if i*2<self.size:
            large_i=i*2
            large_v=self.A[i*2]
            if large_v<self.A[i*2+1]:
                large_i=i*2+1
                large_v=self.A[i*2+1]
                
            if self.A[i]<large_v:
                self.A[i],self.A[large_i]=self.A[large_i],self.A[i]
                self.sinkdown(large_i)
                
        if i*2==self.size:
            if self.A[i]<self.A[i*2]:
                self.A[i],self.A[i*2]=self.A[i*2],self.A[i]
                
    def heappop(self):
        if self.size<1:
            return "Already empty"
        else:
            self.size-=1
            outer=self.A[1]
            self.A[1]=self.A[self.size+1]
            self.sinkdown(1)
            self.A=self.A[0:self.size+1]
            return outer
        
    def heappush(self,x):
        #a naive way
        self.A.append(x)
        self.size+=1
        #heapify
        for i in range(self.size//2+1,0,-1):
            self.sinkdown(i)
        return self.A
                                
    def heapsort(self):
        while self.size>1:
            self.A[1],self.A[self.size]=self.A[self.size],self.A[1]
            self.size-=1
            self.sinkdown(1)
        return self.A
    

#L=[26,24,20]
#H=Heap(L)
#H.heappush(5)
#H.heappush(5)
#print(H.heappop())
#print(H.A)
#print(H.heapsort())






def test(i,curset,L,k):
    if sum(curset)==k:
        print(curset)
    elif i!=len(L):
        test(i+1,curset+[L[i]],L,k)
        test(i+1,curset,L,k)

L=[21,10,34,12,1,17,6]
k=22
test(0,[],L,k)

        
    
    
    







                        

