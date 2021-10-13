import random
p=0
n=1
while(p<0.5):
    x=0
    for i in range(1,101):
        a=[0]*366
        for j in range(0,n):
            te=random.randint(1,365)
            a[te]+=1
        for k in a:
            if(k>=2):
                x=x+1
                break
    n=n+1
    p=x/100
print(n)