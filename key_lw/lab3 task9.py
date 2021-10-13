def f(n):
    return 2*(n**2)+n-2
def dec(a,b):
    if((b-a)<0.001):
        return (a+b)/2
    c=float((a+b)/2)
    if(f(c)==0):
        return c
    elif(f(a)*f(c)<0):
        return dec(a,c)
    elif(f(b)*f(c)<0):
        return dec(c,b)
print(dec(0,1))
    