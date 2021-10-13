a=int(input())
b=int(input())
if(a<b):
    c=a
    a=b
    b=c
if(a>0 and b>0):
    for i in range(a,a*b*5):
        if(i%a==0 and i%b==0):
            print(i)
    
