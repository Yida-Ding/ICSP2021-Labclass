#Counting Sort
#inputL=[a3,a1,a2,a1,a4,a5]
#valueL=[a1,a2,a3,a4,a5]
#countL=[0,0,1,0,0]
#merge to a resL

def CountingSort(L,k):
    valueL=list(range(0,k+1))
    countL=[0 for i in range(0,k+1)]
    #count the times
    for i in range(len(L)):
        ind=valueL.index(L[i])
        countL[ind]+=1
    #return sorted list
    res=[]
    for i in range(len(valueL)):
        res+=[valueL[i]]*countL[i]
    return res
#print(CountingSort([5,7,2,8,4,3],8))



#BINARY SEARCH TREE
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        
    def infix_order_traversal(self):
        if self.left==None and self.right==None:
            return [self.data]
        else:
            res=[]
            if self.left!=None:
                res+=self.left.infix_order_traversal()
            res.append(self.data)
            if self.right!=None:
                res+=self.right.infix_order_traversal()
            return res
    
    def prefix_order_traversal(self):
        if self.left==None and self.right==None:
            return [self.data]
        else:
            res=[]
            res.append(self.data)
            if self.left!=None:
                res+=self.left.prefix_order_traversal()
            if self.right!=None:
                res+=self.right.prefix_order_traversal()
            return res
       
    def getAllLeaf(self):
        if self.left==None and self.right==None:
            return [self.data]
        else:
            res=[]
            if self.left!=None:
                res+=self.left.getAllLeaf()
            if self.right!=None:
                res+=self.right.getAllLeaf()
            return res
        
    def getAllLength(self):
        if self.left==None and self.right==None:
            return [1]
        else:
            res=[]
            if self.left!=None:
                res+=self.left.getAllLength()
            if self.right!=None:
                res+=self.right.getAllLength()
            return [x+1 for x in res]

    def getAllPaths(self):
        if self.left==None and self.right==None:
            return [[self.data]]
        else:
            res=[]
            if self.left!=None:
                res+=self.left.getAllPaths()
            if self.right!=None:
                res+=self.right.getAllPaths()
            return [p+[self.data] for p in res]
        
    def insert_data(self,k):
        if k<self.data and self.left is not None:
            self.left.insert_data(k)
        elif k>self.data and self.right is not None:
            self.right.insert_data(k)
        elif k<self.data and self.left is None:
            self.left=Node(k,None,None)
        elif k>self.data and self.right is None:
            self.right=Node(k,None,None)

    

Tree1=Node(7,Node(4,Node(2,Node(1),Node(3)),Node(5,Node(6))),Node(9,Node(8),Node(10)))
Tree2=Node(7,Node(4),Node(9))
print(Tree1.getAllLength())
        

