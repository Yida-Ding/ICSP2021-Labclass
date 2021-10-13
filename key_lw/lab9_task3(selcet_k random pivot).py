import random
def select_pivot(lis):
    x=random.randint(0,len(lis)-1)
    return x
def partitioning(lis,x):
    left,right=[],[]
    for i in lis:
        if(i<=x):
            left.append(i)
        else:
            right.append(i)
    return left,right
def select_k(lis,k):
    if(len(lis)<=1):
        return lis[0]
    x=select_pivot(lis)
    m=lis[x]
    del lis[x]
    left,right=partitioning(lis,m)
    if(k<=len(left)):
        return select_k(left,k)
    if(k==len(left)+1):
        return m
    if(k>len(left)+1):
        return select_k(right,k-len(left)-1)
l=[]
while(len(l)<100):
    a=random.randint(1,100)
    if (a not in l):
        l.append(a)
print(select_k(l,56))