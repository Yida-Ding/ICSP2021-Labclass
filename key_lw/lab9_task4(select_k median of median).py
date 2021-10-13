import random
import time
import matplotlib.pyplot as plt
def mergesort(l):
    if(len(l)<=1):
        return l
    else:
        mid=len(l)//2
        left=l[0:mid]
        right=l[mid:len(l)]
        l=mergesort(left)
        r=mergesort(right)
        s=[]
        l1=0
        r1=0
        while(l1<=len(l) or r1<=len(r)):
            if(l1==len(l)):
                for i in range(r1,len(r)):
                    s.append(r[i])
                break
            if(r1==len(r)):
                for i in range(l1,len(l)):
                    s.append(l[i])
                break
            if(l[l1]<r[r1]):
                s.append(l[l1])
                l1=l1+1
            else:
                s.append(r[r1])
                r1=r1+1
        return s
def select_pivot(lis):
    if(len(lis)<=5):
        return mergesort(lis)[len(lis)//2]
    re=[]
    for i in range(0,len(lis)//5*5,5):
        re.append(mergesort(lis[i:i+5])[2])
    return select_k(re,len(re)//2)
def select_k(lis,k):
    if(len(lis)<=1):
        return lis[0]
    if(len(lis)<200):
        mid=lis[0]
    else:
        mid=select_pivot(lis)
    left=[]
    right=[]
    for i in lis:
        if(i<=mid):
            left.append(i)
        elif(i>mid):
            right.append(i)
    left.remove(mid)
    if(k<=len(left)):
        return select_k(left,k)
    if(k==len(left)+1):
        return mid
    if(k>len(left)+1):
        return select_k(right,k-len(left)-1)
n=10000
x=1
nl=[]
tl=[]
l=[]
while(len(l)<100001):
    a=random.randint(1,n)
    if (a not in l):
        l.append(a)
while(n<=100000):
    s=time.time()
    select_k(l,random.randint(1,n))
    e=time.time()
    nl.append(n)
    tl.append(e-s)
    n=n+10000
plt.plot(nl,tl)
plt.show()