y=int(input())
l=[1]*y
p=0
while(p>-1):
    if(l[p]>y):
        p-=1
    else:
        if(p==y-1):
            print(l)
        else:
            i=1
            while(i in l):
                i+=1
            l[p+1]=i-1
            p=p+1
    while(l[p]+1 in l):
        l[p]+=1
    l[p]+=1