def mergesort(l):
    if(len(l)<=1):
        return l
    else:
        mid=len(l)//2
        left=l[0:mid]
        right=l[mid:len(l)]
        l=mergesort(left)
        r=mergesort(right)
        s=[]
        l1=0
        r1=0
        while(l1<=len(l) or r1<=len(r)):
            if(l1==len(l)):
                for i in range(r1,len(r)):
                    s.append(r[i])
                break
            if(r1==len(r)):
                for i in range(l1,len(l)):
                    s.append(l[i])
                break
            if(l[l1]<r[r1]):
                s.append(l[l1])
                l1=l1+1
            else:
                s.append(r[r1])
                r1=r1+1
        return s
def k_selection(list,k):
    li=mergesort(list)
    return li[k-1]
print(select_k([3,2,1,4,5],3))
