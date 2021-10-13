class Stack:
    def __init__(self):
        self.S=[]
    
    def isEmpty(self):
        if len(self.S)==0:
            return True
        else:
            return False
    
    def push(self,x):
        self.S.append(x)
    
    def pop(self):
        if self.isEmpty():
            return "Error"
        else:
            outer=self.S[-1]
            self.S=self.S[:-1]
            return outer
        
agent=Stack()
agent.push(1)
agent.push(2)
agent.push(2)
print(agent.pop())
print(agent.S)

class Queue:
    def __init__(self):
        self.Q=[]
    
    def isEmpty(self):
        if len(self.Q)==0:
            return True
        else:
            return False
        
    def insert(self,x):
        self.Q.append(x)
        
    def dequeue(self):
        if self.isEmpty():
            return "Error"
        else:
            outer=self.Q[0]
            self.Q=self.Q[1:]
            return outer
            
#agent=Queue()
#agent.insert(1)
#agent.insert(5)
#agent.insert(5)
#agent.insert(5)
#agent.insert(5)
#print(agent.dequeue())
#print(agent.dequeue())
#print(agent.dequeue())
#print(agent.Q)

    
    
    
    
    