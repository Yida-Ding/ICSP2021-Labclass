import time
import random
def insertion_sort(l):
    for i in range(len(l)-1,0,-1):
        j=i
        a=l[i-1]
        while(j<=len(l)-1 and a>l[j]):
            l[j-1]=l[j]
            j=j+1
        l[j-1]=a
    return l
b=int(input())
l=[]
for i in range(0,b):
   l.append(random.randint(0,b))
   l.append(b-i)
start_time=time.time()
print(insertion_sort(l))
end_time=time.time()
print("Execution time is %es" %(end_time - start_time))