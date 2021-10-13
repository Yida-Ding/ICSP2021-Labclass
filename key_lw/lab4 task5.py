def f(n,L):
    if len(L)<n:
        X=[1]*(len(L)+1)
        for i in range(0,len(L)-1):
            X[i+1]=2*(L[i]+L[i+1])
        f(n,X)
    print (L)
f(4,[1])