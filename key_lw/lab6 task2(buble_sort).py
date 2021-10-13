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
b=int(input())
l=[]
for i in range(0,b):
   l.append(random.randint(0,b))
start_time=time.time()
Bubble_sort(l)
end_time=time.time()
print("Execution time is %es" %(end_time - start_time))