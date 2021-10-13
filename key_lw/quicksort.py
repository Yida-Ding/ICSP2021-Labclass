def quicksort(li,l=0,r=-100):
    if(r==-100):
        r=len(li)-1
    if(l>=r):
        return 
    else:
        mid,l1,r1=li[l],l,r
        while(l1<r1):
            while(li[l1]<=mid ):
                l1+=1
            while(li[r1]>mid):
                r1-=1
            if(l1<r1):
                li[l1],li[r1]=li[r1],li[l1]
        li[l],li[r1]=li[r1],li[l]
        quicksort(li,l,r1-1)
        quicksort(li,l1,r)
        return li
l=[6,83,82,452,23,26,262,37,2,2,845,8,13,74171,1,8145842,84154588,1,81,38,837632,4513,7]
print(quicksort(l))
            