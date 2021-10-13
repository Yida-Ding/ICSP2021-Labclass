def gcd(m,n):
    r=999
    while(r!=0):
        r=m%n
        m=n
        n=r
    return m
a=int(input())
b=int(input())
if(a<b):
    c=a
    a=b
    b=c
print(gcd(a,b))