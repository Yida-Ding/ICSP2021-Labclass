def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return f(n-1)+f(n-2)+f(n-3)
    
#print(f(3))

def GCD(m,n):
    r=m%n
    if r==0:
        return n
    else:
        return GCD(n,r)

#print(GCD(16*2,16*7))

def g(x):
    return 2*(x**2)+x-2

def dichotomy_loop(a,b,e):
    while abs(a-b)>=e:
        mid=(a+b)/2
        if g(a)*g(mid)<0:
            a,b=a,mid
        else:
            a,b=mid,b
    return a,b

def dichotomy_recursion(a,b,e):
    if abs(a-b)<e:
        return a,b
    else:
        mid=(a+b)/2
        if g(a)*g(mid)<0:
            return dichotomy_recursion(a,mid,e)
        else:
            return dichotomy_recursion(mid,b,e)

def getMaximum(L):
    maxi=-float("inf")
    for e in L:
        if e>maxi:
            maxi=e
    return maxi
    
def checkDivision(n):
    if n<=0:
        return False
    else: 
        flag=False
        for i in range(2,n,2):
            if (n/i)%2==0:
                flag=True
        return flag
    
print(checkDivision(18))
            
        
    
    
    
    
    
    
    











