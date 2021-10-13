#def BubbleSort1(L):
#    for n in range(len(L)-1,-1,-1):
#        for i in range(0,n):
#            if L[i]>L[i+1]:
#                L[i],L[i+1]=L[i+1],L[i]
#    return L
#
#def BubbleSort2(L):
#    for n in range(len(L)-1,-1,-1):
#        flag=True
#        for i in range(0,n):
#            if L[i]>L[i+1]:
#                L[i],L[i+1]=L[i+1],L[i]
#                flag=False
#        if flag==True:
#            return L
#    return L
#
##print(BubbleSort2([5,4,3,2,1]))
#
#def EquationCount(n,t):
#    if n==0:
#        return 0
#    elif n==1 or t==1:
#        return 1
#    elif n==t:
#        return 1+EquationCount(n,n-1)
#    elif n>t:
#        return EquationCount(n,t-1)+EquationCount(n-t,t)
#    else:
#        return EquationCount(n,n)
#    
#res=EquationCount(3,3)
#print(res)
#
##Merge Sort
#def Merge(L,R):
#    res=[]
#    while len(L)>0 and len(R)>0:
#        if L[0]<R[0]:
#            res.append(L[0])
#            L.remove(L[0])
#        else:
#            res.append(R[0])
#            R.remove(R[0])
#    res=res+L+R
#    return res
#
#def MergeSort(lst):
#    if len(lst)==1:
#        return lst
#    else:
#        L=lst[0:len(lst)//2]
#        R=lst[len(lst)//2:len(lst)]
#        return Merge(MergeSort(L),MergeSort(R))
#print(MergeSort([1,3,5,2,4,6]))
##time complexity=O(nlogn)
    
    






















    
    




