import time
import random
import copy
def insertion_sort(l):
    for i in range(0,len(l)-1):
        j=i
        a=l[i+1]
        while(j>=0 and a<l[j]):
            l[j+1]=l[j]
            j=j-1
        l[j+1]=a
    return l
start_time=time.time()
insertion_sort(l)
end_time=time.time()
etime=-1
le=5000
while(not (etime<5.4 and etime>5.3)):
    start_time=time.time()
    l=[]
    for j in range(le,0,-1):
        l.append(j)
    insertion_sort(l)
    end_time=time.time()
    etime=end_time-start_time
    if(etime<5.3):
        le=le+100
    if(etime>5.4):
        le=le-100
print(le)