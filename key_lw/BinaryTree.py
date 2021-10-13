class Node:
    def __init__(self,data,left=None,right=None,parent=None):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent
    def search(self,k):
        if(self.data==k):
            return True
        elif(k<self.data and self.left is not None):
            return self.left.search(k)
        elif(k>self.data and self.right is not None):
            return self.right.search(k)
        else:
            return False
    def findparent(self,k):
        if(self.data==k):
            return self.parent.data
        elif(k<self.data and self.left is not None):
            return self.left.findparent(k)
        elif(k>self.data and self.right is not None):
            return self.right.findparent(k)
        else:
            return False
    def findchildren(self,k):
        if(self.data==k):
            if(self.left!=None and self.right!=None):
                return self.left.data , self.right.data
            elif(self.left==None and self.right!=None):
                return None , self.right.data
            elif(self.left!=None and self.right==None):
                return self.left.data , None
            elif(self.left==None and self.right==None):
                return None, None
        elif(k<self.data and self.left is not None):
            return self.left.findchildren(k)
        elif(k>self.data and self.right is not None):
            return self.right.findchildren(k)
        else:
            return False
    def insert(self,k):
        if (self==None):
            self=Node(k)
        else:
            if(k<self.data):
                if(self.left==None):
                    self.left=Node(k)
                    self.left.parent=self
                else:
                    self.left.insert(k)
            elif(k>self.data):
                if(self.right==None):
                    self.right=Node(k)
                    self.right.parent=self
                else:
                    self.right.insert(k)
    def printtree(self):
        if(self.left!=None):
            self.left.printtree()
        print(self.data)
        if(self.right!=None):
            self.right.printtree()
A=Node(10)
A.insert(9)
A.insert(8)
print(A.search(8))
print(A.findchildren(10))

            
                    