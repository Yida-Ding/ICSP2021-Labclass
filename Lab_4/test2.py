
L=[4,7,2,5,6]
def g(L):
    if len(L)==1:
        return L[0]
    else:
        i=max(L[0],g(L[1:]))
        return i
print(g(L))


