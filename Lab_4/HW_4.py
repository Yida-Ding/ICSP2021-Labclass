#Task1
def hanoi(n,x,y,z):
    if n==1:
        print("Move disk from",x,"to",z)
    else:
        hanoi(n-1,x,z,y)
        print(x,y,z)
        hanoi(1,x,y,z)
        hanoi(n-1,y,x,z)

hanoi(2,'a','b','c')

#(1)
#change: line7 -> hanoi(1,x,y,z)
#(2)
#add: line6/7/8 -> print(x,y,z)
#(3)
#add: line6/8 -> return
#print(hanoi(2,'a','b','c'))

l=[4,7,2,5,6]
def g(l):
    if len(l)==1:
        return l[0]
    else:
        i=max(l[0],g(l[1:]))
        print(i)
        return i
g(l)
#Task (2)
def F(n):
    if n==1:
        return 1
    else:
        return 2*F(n-1)+1


#Task (3)
def G(n):
    if n==1:
        return 1
    elif n==2:
        return 3
    else:
        minStep=float("inf")
        for x in range(1,n):
            temp=2*G(x)+2**(n-x)-1
            if temp<minStep:
                minStep=temp
        return minStep
        
#res=G(5)    
#print(res)    
        

def getSteps(N):
    L=[1,3]
    for n in range(3,N+1):
        min_step=float("inf")
        for x in range(1,n):
            step=2*L[x-1]+2**(n-x)-1
            if step<min_step:
                min_step=step
        L.append(min_step)
    return L

#print(getStep(5))


