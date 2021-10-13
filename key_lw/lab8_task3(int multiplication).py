import time

def multiply(a,b):
    s=[0]*5
    a=str(a)
    b=str(b)
    if(len(a)==1 and len(b)==1):
        return int(a)*int(b)
    else:
        while(len(a)<len(b)):
            a="0"+a
        while(len(b)<len(a)):
            b="0"+b
        a1=a[0:len(a)//2]
        a2=a[(len(a)//2):len(a)]
        b1=b[0:len(b)//2]
        b2=b[len(b)//2:len(b)]
        s[1]=multiply(a1,b1)
        s[4]=multiply(a2,b2)
        for i in range(1,5):
            if(s[i]==None):
                s[i]=0
        s[3]=multiply(int(a1)+int(a2),int(b1)+int(b2))-s[1]-s[4]
        s[1]=s[1]*10**((len(a)-len(a)//2)+(len(b)-len(b)//2))
        s[3]=s[3]*10**(len(b)-len(b)//2)
        return s[1]+s[3]+s[4]
    
print(multiply('2222','1'))

   
        

