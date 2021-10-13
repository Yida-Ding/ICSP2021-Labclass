def CheckPrime(n):
    for j in range(2,n):
        if n%j==0:
            return False
    return True

def Listprime(a):
    PrimeL=[]
    for i in range(2,a+1):
        if CheckPrime(i)==True:
            PrimeL.append(i)
    return PrimeL

def FindSum(k):
    D=set(Listprime(k))
    for i in D:
        j=k-i
        if j in D:
            print(i,"+",j,"=",k)
            return
                
#FindSum(8)    
    
    
#tupl=(1,2)
#tupl[1]=3
#print(tupl)
#a=[0]*2
#print([a* for i in range(2)])

def f(n):
    return [1,n]

print(f(2)[0])




#import copy
#L=[[1,2],[3,4]]
#R=copy.deepcopy(L)
#R[0][0]=999
#print(L)





    
