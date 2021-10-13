def prime(n):
    for i in range (2,n):
        if(n%i==0):
            return 0
    return n
a=[]
for i in range(2,1001):
    if(prime(i)!=0):
        a.append(i)
print(a)
