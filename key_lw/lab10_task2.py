import copy
class Node:
    def __init__(self,data=None,left=None,right=None,parent=None,layer=0):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent
        self.layer=layer
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
    def insert(self,k,layer=0):
        if (self==None):
            self=Node(k)
        else:
            if(k<self.data):
                layer=layer+1
                if(self.left==None):
                    self.left=Node(k)
                    self.left.parent=self
                    self.left.layer=layer
                else:
                    self.left.insert(k,layer)
            elif(k>self.data):
                layer=layer+1
                if(self.right==None):
                    self.right=Node(k)
                    self.right.parent=self
                    self.right.layer=layer
                else:
                    self.right.insert(k,layer)
          
    def printtree(self,re=None):
        if(re==None):
            re=[]
        if(self.left!=None):
            self.left.printtree(re)
        re.append(self.data)
        if(self.right!=None):
            self.right.printtree(re)
        s=copy.deepcopy(re)
        re=[]
        return s
    def printleaf(self,leaf=None):
        if(leaf==None):
            leaf=[]
        if(self.left!=None):
            leaf=self.left.printleaf(leaf)
        if(self.left==None and self.right==None):
            leaf.append(self.data)
        if(self.right!=None):
            leaf=self.right.printleaf(leaf)
        return leaf
    def finddeep(self,deep=0):
        if(self.left!=None):
            deep=self.left.finddeep(deep)
        if(self.left==None and self.right==None):
            if(deep<self.layer):
                deep=self.layer
        if(self.right!=None):
            deep=self.right.finddeep(deep)
        return deep
    def buildtree(self,l):
        for i in l:
            self.insert(i)
    def checktree(self):
        li=self.printtree([])
        print(li)
        for i in range(1,len(li)):
            if (li[i]<li[i-1]):
                return False
        return True
    def printlongestpath(self,deep):
        if(self.left!=None):
            self.left.printlongestpath(deep)
        if(self.left==None and self.right==None):
            if(self.layer==deep):
                a=self
                re=[]
                while(a!=None):
                    re.append(a.data)
                    a=a.parent
                print(re)
        if(self.right!=None):
            self.right.printlongestpath(deep)
    def longestpath(self):
        deep=self.finddeep()
        self.printlongestpath(deep)
    def test(self):
        di=0
        a=self
        re=[]
        while(a!=None):
            print(a.data)
            if(di<=1):
                if(a.left==None and a.right==None):
                    c=[]
                    b=a
                    while(b!=None):
                        c.append(b.data)
                        b=b.parent
                    re.append(c)
                    if(a==a.parent.left):
                        di=1
                    elif(a==a.parent.right):
                        di=2
                    a=a.parent
                elif(di==0):
                    if(a.left!=None):
                        a=a.left
                        di=0
                    elif(a.left==None):
                        di+=1
                elif(di==1):
                    if(a.right!=None):
                        a=a.right
                        di=0
                    elif(a.right==None):
                        di+=1
            elif(di>1):
                if(a.parent!=None):
                    if(a==a.parent.left):
                        di=1
                    elif(a==a.parent.right):
                        di=2
                a=a.parent
        print(re)
    def findnode(self,k):
        if(self.data==k):
            return self
        elif(k<self.data and self.left is not None):
            return self.left.findnode(k)
        elif(k>self.data and self.right is not None):
            return self.right.findnode(k)
        else:
            return False
    def delete(self,k):
        a=self.findnode(k)
        if(a.left==None and a.right==None):
            if(a.parent.left==a):
                a.parent.left=None
            if(a.parent.right==a):
                a.parent.right=None
        elif(a.left==None and a.right!=None):
            if(a.parent.left==a):
                a.parent.left=a.right
                a.right.parent=a.parent
            if(a.parent.right==a):
                a.parent.right=a.right
                a.right.parent=a.parent
        elif(a.left!=None and a.right==None):
            if(a.parent.left==a):
                a.parent.left=a.left
                a.left.parent=a.parent
            if(a.parent.right==a):
                a.parent.right=a.left
                a.left.parent=a.parent
        else:
            b=a
            b=b.right
            while(b!=None):
                c=b
                b=b.left
            if(a.right==c):
                if(a.parent!=None):
                    c.parent=a.parent
                elif(a.parent==None):
                    print("you cannot delete the root")
                elif(a.parent.left==a):
                    a.parent.left=c
                elif(a.parent.right==a):
                    a.parent.right=c
                c.left=a.left
                a.left.parent=c
            else:
                if(c.right!=None):
                    c.right.parent=c.parent
                    c.parent.left=c.right
                else:
                    c.parent.left=None
                c.right=a.right
                a.right.parent=c
                c.left=a.left
                a.left.parent=c
                if(a.parent==None):
                    print("you cannot delete the root")
                elif(a.parent.left==a):
                    a.parent.left=c
                else:
                    a.parent.right=c
                if(a.parent!=None):
                    c.parent=a.parent
#    def delete(self,k):
#        a=self
#        while(a!=None):
#            if(a.data==k):
#                break
#            if(di<=1):
#                if(a.left==None and a.right==None):        
#                    di=2
#                elif(di==0):
#                    if(a.left!=None):
#                        a=a.left
#                        di=0
#                    elif(a.left==None):
#                        di+=1
#                elif(di==1):
#                    if(a.right!=None):
#                        a=a.right
#                        di=0
#                    elif(a.right==None):
#                        di+=1
#            elif(di>1):
#                if(a.parent!=None):
#                    if(a==a.parent.left):
#                        di=1
#                    elif(a==a.parent.right):
#                        di=2
#                a=a.parent
#        if(a.left==None and a.right==None):
#            a=None
#        if(a.left==None and a.right!=None):
#            if(a.parent.left==a):
#                a.parent.left=a.
A=Node(10)
A.insert(9)
A.insert(11)
#print(A.search(8))
#print(A.findchildren(9))
l=[2,6,4,8,1,15,12,20]
A.buildtree(l)
#print(A.printleaf())
#print(A.printtree([]))
# =============================================================================
# print(A.finddeep())
#A.longestpath()
A.delete(9)
#print(A.printtree())
# =============================================================================
#print(A.checktree())
#A.test()                                