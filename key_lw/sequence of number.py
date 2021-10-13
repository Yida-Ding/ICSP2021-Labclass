def f(l,li,x):
    if(x==len(li)):
        print(li)
    else:
        if(len(li)==0):
            for i in range(1,len(l)):
                li=[]
                li.append(l[i-1])
                f(l,li,x,)
        else:
            for i in range(li[len(li)-1],len(l)):
                r=li.copy()
                r.append(l[i])
                f(l,r,x,)
x=int(input())
y=int(input())#x>y is required
f(range(1,x+1),[],y)