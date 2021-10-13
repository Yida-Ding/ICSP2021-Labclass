#[[1]]
#[[1,2],[2,1]]
def Permutation(L):
    if len(L)==1:
        return [L]
    else:
        res=[]
        for subL in Permutation(L[0:len(L)-1]):
            for i in range(0,len(subL)+1):
                tempL=subL.copy()
                tempL.insert(i,L[-1])
                res.append(tempL)
        return res

print(Permutation([1,2,3]))

def reorder(sample,number):
    sample0=sample[:number]
    if number==1:
        return [sample0]
    L=[sample0]
    for entry in reorder(sample,number-1):
        for n in range(0,len(entry)+1):
            entry0=entry.copy()
            print(entry)
            entry0.insert(n,sample0[len(sample0)-1])
            if entry0 in L:
                L.remove(entry0)
            L.append(entry0)
    return L


b=1
a=b
print(a)




