#class Rational:
#    def __init__(self,n,d):
#        self.n=n
#        self.d=d
#        
#    def __str__(self):
#        return '%d/%d'%(self.n,self.d)
#        
#    def __add__(self,other):
#        new_n=self.n*other.d+self.d*other.n
#        new_d=self.d*other.d
#        return Rational(new_n,new_d)
#    
#    def __sub__(self,other):
#        new_n=self.n*other.d-self.d*other.n
#        new_d=self.d*other.d
#        return Rational(new_n,new_d)
#    
#    def __mul__(self,other):
#        return Rational(self.n*other.n,self.d*other.d)
#         
#    def __truediv__(self,other):
#        return Rational(self.n*other.d,self.d*other.n)
#    
#    def simplify(self):
#        #compute GCD
#        m,n=max([self.n,self.d]),min([self.n,self.d])
#        r=m%n
#        m=n
#        n=r
#        while r!=0:
#            r=m%n
#            m=n
#            n=r    
#        
#        return Rational(int(self.n/m),int(self.d/m))
#        
#r1=Rational(1,2)
#r2=Rational(3,4)
#r3=Rational(5,6)
#r4=Rational(7,8)
#r5=Rational(9,10)
#
#r1+r2
#
#r=(r1+r2-r3)*r4/r5
#print(r)
#print(r.simplify())






def checkPrime(data,n=2):
    if data==1:
        return False
    elif data==n:
        return True
    else:
        if data%n!=0:
            checkPrime(data,n-1)
        return False
        
print(checkPrime(2))


class Dog:
    def __init__(self,sex):
        self.eaten_food=0
        self.walk_time=0
        self.mood=None
        self.day=0
        self.sex=sex
    
    def feed(self):
        self.eaten_food+=1
        print("Feed to",self.eaten_food)
    
    def walk(self):
        self.walk_time+=1
        print("Walk to",self.walk_time)
        
    def check_mood(self):
        if self.eaten_food<3 or self.walk_time<1:
            self.mood="angry"
        else:
            self.mood="happy"
    
    def next_day(self):
        self.walk_time=0
        self.eaten_food=0
        self.mood=None
        self.day+=1
                
        
    
            
        
    
    
    
    
        
    
    
    
    









