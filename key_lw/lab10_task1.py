def countingsort(l,k):
    c=[0]*(k+1)
    r=[]
    for i in l:
        c[i]=c[i]+1
    for i in range(0,k+1):
        r=r+[i]*c[i]
    return r
print(countingsort([2,5,3,0,2,3,0,3],6))