import random
import time

def naive_multiple(a,b):
    if len(a)==1 and len(b)==1:
        return(int(a)*int(b))
    i=int(len(a)/2)
    a1=a[:i]
    a2=a[i:]
    b1=b[:i]
    b2=b[i:]
    k1=10**len(a)
    k2=10**(0.5*len(a))
    return(naive_multiple(a1,b1)*k1+
           (naive_multiple(a1,b2)+ naive_multiple(b1,a2))*k2+
           naive_multiple(a2,b2))
    
start=time.time()
print(naive_multiple(12,24))
end=time.time()
print('run_time=%es'%(end-start))

#def get_randlist(start,end,length):
#    res=[]
#    for i in range(length):
#        res.append(random.randint(start,end))
#    return(res)
#def find_smallest(l):
#    res=l[0]
#    for i in range(len(l)):
#        if l[i]<res:
#            res=l[i]
#    return(res)
#def naive_select(l,k):
#    for i in range(k-1):
#        l.remove(find_smallest(l))
#    return(find_smallest(l))
#print(naive_select(get_randlist(102,2292,1000),283))


