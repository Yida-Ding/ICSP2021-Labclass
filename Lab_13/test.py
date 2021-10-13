import random 

L=[1,2,3,3,5]
for e in L.copy():
    if e==3:
        L.remove(e)
print(L)

#class Hashing:
#    def __init__(self,size):
#        self.size=size
#        self.table=[""]*self.size
#        self.nval=0
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
#    def linear_insert(self,value):
#        loc=value%self.size
#        loc_origin=loc
#        n=1
#        while self.table[loc]!="" and self.table[loc]!="*":
#            loc=(value+n)%self.size
#            n+=1
#            if loc==loc_origin:
#                print("Full")
#                return
#        self.table[loc]=value
#        return
#    
#    def linear_search(self,value):
#        loc=value%self.size
#        loc_origin=loc
#        n=1
#        if self.table[loc]=="":
#            return False
#        while self.table[loc]!=value:
#            loc=(value+n)%self.size
#            n+=1
#            if loc==loc_origin:
#                return False
#        else:
#            return True
#        
#    def linear_delete(self,value):
#        loc=value%self.size
#        loc_origin=loc
#        n=1
#        if self.table[loc]=="":
#            return "Miss"
#        while self.table[loc]!=value:
#            loc=(value+n)%self.size
#            n+=1
#            if loc==loc_origin:
#                return "Miss"
#        else:
#            self.table[loc]="*"
#            return
#
#    def quadratic_insert(self,value):
#        loc=value%self.size
#        loc_origin=loc
#        n=1
#        while self.table[loc]!="" and self.table[loc]!="*":
#            loc=(value+n**2)%self.size
#            n+=1
#            if loc==loc_origin:
#                print('Fail')
#                return
#        else:
#            self.table[loc]=value
#            return
#
#        
#Hash=Hashing(20)
#Hash.quadratic_insert(5)
#Hash.quadratic_insert(10)
#Hash.quadratic_insert(11)
#Hash.quadratic_insert(12)
#Hash.quadratic_insert(13)
#Hash.quadratic_insert(14)
#Hash.quadratic_insert(14)
#Hash.quadratic_insert(14)
#Hash.quadratic_insert(13)
#Hash.quadratic_insert(14)
#Hash.quadratic_insert(14)
##Hash.quadratic_insert(14)
#
#print(Hash.table)
#
#
