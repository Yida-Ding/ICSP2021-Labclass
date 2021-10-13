def sorted(l):
    for i in range(0,len(l)-1):
        if(l[i]>l[i+1]):
            return False
    return True
