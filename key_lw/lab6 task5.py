def f(x):
    return 3*x**2+x-2
def di(a,b):
    if(b-a<0.001):
        print("(",a,",",b,")")
    else:
        c=(a+b)/2
        if(f(c)==0):
            print(c)
        elif(f(a)*f(c)<0):
            di(a,c)
        else:
            di(c,b)
di(0,1)