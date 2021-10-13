import time
def sortt(list):
    print(len(list))
    if(len(list)<=1):
        return list
    mid=[]
    mid.append(list[0])
    #print(mid)
    del list[0]
    left=[]
    right=[]
    for i in list:
        if(i<=mid[0]):
            left.append(i)
        else:
            right.append(i)
    return sortt(left)+mid+sortt(right)
#b=int(input())
b=10
l=[i for i in range(b,0,-1)]
s=time.time()
print(sortt(l))
e=time.time()
print("Execution time is %es" %(e - s))
