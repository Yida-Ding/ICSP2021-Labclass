import time
import random
def Bubble_sort(l):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if(l[j]<l[i]):
                c=l[i]
                l[i]=l[j]
                l[j]=c
    return l
def select_k(l,k):
    return Bubble_sort(l)[k-1]
print(select_k([3,2,1,4,5],3))