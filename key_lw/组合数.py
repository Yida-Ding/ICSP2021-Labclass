def c(m,n):
    if(m==n):
        return 1
    if(n==0):
        return 1
    return c(m-1,n-1)+c(m-1,n)
a=int(input())
b=int(input())
print(c(a,b))