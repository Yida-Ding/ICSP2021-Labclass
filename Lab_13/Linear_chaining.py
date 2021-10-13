import random


#Birthday Paradox
def get_prob(n,Ntest):
    count=0
    for i in range(Ntest):
        L=[random.randint(1,365) for i in range(n)]
        L.sort()
        for j in range(len(L)-1):
            if L[j]==L[j+1]:
                count+=1
                break
    return count/Ntest

print(get_prob(30,10000))

class Linear_chaining:
    def __init__(self,size):
        self.size=size
        self.table=[[] for i in range(size)]
    
    def insert(self,value):
        loc=value%self.size
        self.table[loc].append(value)
        return self.table
    
    def search(self,value):
        loc=value%self.size
        for data in self.table[loc]:
            if data==value:
                return True
        return False
    
    def delete(self,value):
        loc=value%self.size
        for data in self.table[loc].copy():
            if data==value:
                self.table[loc].remove(value)
        return self.table
    
"""**************************************"""
chain=Linear_chaining(5)
print(chain.insert(5))
print(chain.insert(5))
print(chain.insert(4))
print(chain.delete(5))
print(chain.table)