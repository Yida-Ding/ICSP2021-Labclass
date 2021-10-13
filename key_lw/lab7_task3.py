def sorted(l):
    for i in range(0,len(l)-1):
        if(l[i]>l[i+1]):
            return False
    return True
def f(l,li=[]):
    if(len(l)==len(li)):
        lis=[]
        for i in li:
            lis.append(l[i])
#        if(sorted(lis)):
        print(lis)
    else:
        if(len(li)==0):
            for i in range(0,len(l)):
                li=[]
                li.append(i)
                f(l,li)
        else:
            for i in range(0,len(l)):
                if(not( i in li)):
                    r=li.copy()
                    r.append(i)
                    f(l,r)
f([1,3,2])
    

     
