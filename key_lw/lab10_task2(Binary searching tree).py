import copy
class Node:
    def __init__(self,data=None,left=None,right=None,parent=None,layer=0):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent
        self.layer=layer
        self.root=self
    def search(self,k):
        if(self.data==k):
            return True
        elif(k<self.data and self.left is not None):
            return self.left.search(k)
        elif(k>self.data and self.right is not None):
            return self.right.search(k)
        else:
            return False
    def insert(self,k,layer=0):
        if (self==None):
            self=Node(k)
            a=self
            while(a.parent!=None):
                a=a.parent
            self.root=a
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
        return re
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
    def findshortest(self,deep=0):
        if(self.left!=None):
            deep=self.left.findshortest(deep)
        if(self.left==None and self.right==None):
            if(deep>self.layer):
                deep=self.layer
        if(self.right!=None):
            deep=self.left.findshortest(deep)
        return deep
    def checkbalanced(self):
        if(self.finddeep()-self.findshortest()<=1):
            return True
        else:
            return False
    def buildtree(self,l):
        for i in l:
            self.insert(i)
    def checktree(self):
        li=self.printtree([])
#        print(li)
        for i in range(1,len(li)):
            if (li[i]<li[i-1]):
                return False
        return True
    def sublayer(self):
        self.layer-=1
        if(self.left!=None):
            self.left.addlayer()
        if(self.right!=None):
            self.right.addlayer()
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
        a=self.root
        print("root",a.data)
        re=[]
        while(a!=None):
            if(a.parent!=None):
                print("data=",a.data,"parent",a.parent.data,"colour=",a.colour)
            else:
                print('data=',a.data,'parent',None,'colour=',a.colour)
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
#        print(re)
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
                a.right.sublayer()
            if(a.parent.right==a):
                a.parent.right=a.right
                a.right.parent=a.parent
                a.right.sublayer()
        elif(a.left!=None and a.right==None):
            if(a.parent.left==a):
                a.parent.left=a.left
                a.left.parent=a.parent
                a.left.sublayer
            if(a.parent.right==a):
                a.parent.right=a.left
                a.left.parent=a.parent
                a.left.sublayer
        else:
            b=a
            b=b.right
            while(b!=None):
                c=b
                b=b.left
            if(a.right==c):
                if(a.parent==None):
                    print("you cannot delete the root")
                elif(a.parent!=None):
                    c.parent=a.parent
                    if(a.parent.left==a):
                        a.parent.left=c
                    elif(a.parent.right==a):
                        a.parent.right=c
                    c.left=a.left
                    a.left.parent=c
                    c.layer=a.layer
            else:
                if(c.right!=None):
                    c.right.parent=c.parent
                    c.parent.left=c.right
                    c.right.layer-=1
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
                c.layer=a.layer
class RBT(Node):
    def __init__(self,data=None,left=None,right=None,parent=None,layer=None,colour=0):#0 is black,1 is red
        super().__init__(data,left,right,parent,layer)
        self.colour=colour
    def checkcolour(self):
        if(self.left!=None):
            if(self.left.checkcolour()==False):
                return False
        if(self.colour==1):
           if(self.left!=None and self.left.colour==1):
               return False
           if(self.right!=None and self.right.colour==1):
               return False
        if(self.right!=None):
            if(self.right.checkcolour()==False):
                return False
        return True
    def checktree(self):
        res=[]
        def checkpath(a):
            if(a.left!=None):
                checkpath(a.left)
            if(a.left==None and a.right==None):
                print(a.data)
                b=a
                re=[]
                while(b!=None):
                    if(b.colour==0):
                        re.append(b.data)
                    b=b.parent
                res.append(re)
            if(a.right!=None):
                checkpath(a.right)
        checkpath(self.root)
        print(res)
        def checkpath2(l):
            for i in range(0,len(l)-1):
                if(len(l[i])!=len(l[i+1])):
                    return False
            return True
        return checkpath2(res) and self.checkcolour() and self.root.colour==0
    def rightrotate(self,x):
#        print("rightrotate")
        if(x.parent.parent!=None):
            pp=x.parent.parent
            if(x.parent==x.parent.parent.left):
                a=1
            else:
                a=2
            x.parent.parent=x
            x.parent.left=x.right
            x.right=x.parent
            if(x.parent.left!=None):
                x.parent.left.parent=x.parent
            x.parent=pp
            if(a==1):
                pp.left=x
            else:
                pp.right=x
        else:
            x.parent.parent=x
            x.parent.left=x.right
            x.right=x.parent
            if(x.parent.left!=None):
                x.parent.left.parent=x.parent
            x.parent=None
            self.root=x
#            print("--",self.root.data)
    def leftrotate(self,x):
#        print('leftrotate')
        if(x.parent.parent!=None):
#            print('i.data=',x.data)
            pp=x.parent.parent
            if(x.parent==x.parent.parent.left):
                a=1
#                print('a=1','pp',pp.data)
            else:
                a=2
            x.parent.parent=x
            x.parent.right=x.left
            x.left=x.parent
            if(x.parent.right!=None):
                x.parent.right.parent=x.parent
            x.parent=pp
            if(a==1):
                pp.left=x
            else:
                pp.right=x
        else:
            x.parent.parent=x
            x.parent.right=x.left
            x.left=x.parent
            if(x.parent.right!=None):
                x.parent.right.parent=x.parent
            x.parent=None
            self.root=x
    def insert(self,x,layer=0):
        i=RBT(x)
        i.colour=1
        a=self
        while(a!=None):
            temp=a
            if(x<a.data):
                a=a.left
            elif(x>a.data):
                a=a.right
            elif(x==a.data):
                break
        p=temp
#        print("temp=",temp.data)
        if(x==p.data):
            return
        elif(x<p.data):
            p.left=i
        elif(x>p.data):
            p.right=i
        i.parent=p
        self.recolourRBT(i)
    def recolourRBT(self,i):
        p=i.parent
        if(p.colour==0):
            return
        else:
            pp=i.parent.parent
#            print(pp.left.data)
            if(i.parent==pp.left):
                u=pp.right
            else:
                u=pp.left
            if(u==None):
                if(i==p.left and p==pp.left):
                    self.rightrotate(p)
                    p.colour=0
                    i.colour=1
                    pp.colour=1
                elif(i==p.right and p==pp.left):
                    self.leftrotate(i)
                    self.recolourRBT(p)
                elif(i==p.right and p==pp.right):
                    self.lefttrotate(p)#self.rightrotate(p)
                    p.colour=0
                    pp.colour=1
                elif(i==p.left and p==pp.right):
                    self.rightrotate(i)
                    self.recolourRBT(p)
            elif(u.colour==1):
                p.colour=0
                u.colour=0
                pp.colour=1
                if(pp.parent==None):
                    pp.colour=0
                else:
                    self.recolourRBT(pp)
            elif(u.colour==0):
                if(p==pp.left):
                    self.rightrotate(p)
                elif(p==pp.right):
                    self.leftrotate(p)
                pp.colour=1
                p.colour=0
                i.colour=0    
#A=Node(10)
#A.insert(9)
#A.insert(11)
#A.insert(12)
#print(A.checkbalanced())
#l=[2,6,4,8,1,15,12,20]
#A.buildtree(l)
#A.test()
#A.delete(9)   
B=RBT(10)
l2=[2,1,5,9]
B.buildtree(l2)
print(B.checktree())
#B.insert(2)
#B.insert(1)
#B.insert(5)
#print("-----------------------------------")
#B.insert(9)
#print(B.root.printtree())
B.test()
#print(B.data,B.colour)
#print(B.data)
#B.rightrotate(B.left)
#print(B.printtree())          
#B.leftrotate(B)
#B.test()