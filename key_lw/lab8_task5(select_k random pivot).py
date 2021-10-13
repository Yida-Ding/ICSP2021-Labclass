import random
def select_k(lis,k):
    if(len(lis)<=1):
        return lis[0]
    mid=[]
    mid.append(lis[0])
    del lis[0]
    left=[]
    right=[]
    for i in lis:
        if(i<=mid[0]):
            left.append(i)
        else:
            right.append(i)
    if(k<=len(left)):
        return select_k(left,k)
    if(k==len(left)+1):
        return mid[0]
    if(k>len(left)+1):
        return select_k(right,k-len(left)-1)
l=[]
while(len(l)<100):
    a=random.randint(1,100)
    if (a not in l):
        l.append(a)
print(select_k(l,56))