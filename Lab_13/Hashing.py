class Hashing:
    def __init__(self,size):
        self.size=size
        self.table=[""]*self.size
        self.nval=0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    def linear_insert(self,value):
        loc=value%self.size
        loc_origin=loc
        n=1
        while self.table[loc]!="" and self.table[loc]!="*":
            loc=(value+n)%self.size
            n+=1
            if loc==loc_origin:
                print("Full")
                return
        else:
            self.table[loc]=value
            return
    
    def linear_search(self,value):
        loc=value%self.size
        loc_origin=loc
        n=1
        if self.table[loc]=="":
            return False
        while self.table[loc]!=value:
            loc=(value+n)%self.size
            n+=1
            if loc==loc_origin:
                return False
        else:
            return True
        
    def linear_delete(self,value):
        loc=value%self.size
        loc_origin=loc
        n=1
        if self.table[loc]=="":
            return "Miss"
        while self.table[loc]!=value:
            loc=(value+n)%self.size
            n+=1
            if loc==loc_origin:
                return "Miss"
        else:
            self.table[loc]="*"
            return
        
    def quadratic_insert(self,value):
        loc=value%self.size
        loc_origin=loc
        n=1
        while self.table[loc]!="" and self.table[loc]!="*":
            loc=(value+n**2)%self.size
            n+=1
            if loc==loc_origin:
                print('Fail')
                return
        self.table[loc]=value
        return
        
    def quadratic_search(self,value):
        loc=value%self.size
        loc_origin=loc
        n=1
        if self.table[loc]=="":
            return False
        while self.table[loc] != value:
            loc=(value+n**2)%self.size
            n+=1
            if loc==loc_origin:
                return False
        else:
            return True
        
    def quadratic_delete(self,value):
        loc=value%self.size
        loc_origin=loc
        n=1
        if self.table[loc]=="":
            return "Miss"
        while self.table[loc] != value:
            loc=(value+n**2)%self.size
            n+=1
            if loc==loc_origin:
                return "Miss"
        else:
            self.table[loc]="*"
            return
        
    def rehash_insert(self,val_L):
        for value in val_L:
            loc=value%self.size
            n=1
            if (self.nval+1)/self.size>=0.5:
                print("Current Table:",self.table)
                self.size*=2                        
                self.table=[""]*self.size
                self.nval=0
                self.rehash_insert(val_L)           
                return
            else:
                while self.table[loc]!="" and self.table[loc]!="*":
                    loc=(value+n)%self.size
                    n+=1
                else:
                    self.table[loc]=value
                    self.nval+=1
        return

    def str_linear_insert(self,word):
        word_val=sum([ord(char) for char in word])
        #linear insert
        loc=word_val%self.size
        loc_origin=loc
        n=1
        while self.table[loc]!="" and self.table[loc]!="*":
            loc=(word_val+n)%self.size
            n+=1
            if loc==loc_origin:
                print("Full")
                return
        else:
            self.table[loc]=word
            return

"""******************************************"""
Hash=Hashing(7)
print(Hash.rehash_insert([1,2,34,5,6,78,90,3,23,132,4567,3432,2,35]))    
   
    
    
    
        
        
        
        
        
        
      



    