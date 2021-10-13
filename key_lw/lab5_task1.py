def pri(b,a=2):
    if(b==2):
        return True
    if(a==b):
        return True
    elif(b>a):
        if(b%a==0):
            return False
        else:
            return pri(b,a+1)
print(pri(99))
        