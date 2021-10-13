##Task 1
#def test_prime(n):
#    for i in range(2,n):
#        if n%i==0:
#            return False
#    return True
#
#def list_prime(i,j):
#    L=[]    
#    for k in range(i,j+1):
#        if test_prime(k) is True:
#            L.append(k)
#    return L
#print(list_prime(2,100))
#
##Task 2
#def recsum(n):
#    if n==1:
#        return 1
#    else:
#        return(recsum(n-1)+n)
#print(recsum(5))
#
##Task 3(1) Recursion
#def fibonacci(n):
#    if n==1 or n==2:
#        return 1
#    else:
#        return(fibonacci(n-1)+fibonacci(n-2))
#print(fibonacci(100))
#
##Task 3(2) Iteration
#def fibonacci(n):
#    a,b=1,1
#    if n==1 or n==2:
#        return 1
#    else:
#        for t in range (1,n-1):
#            c=a+b
#            a,b=b,c
#        return c
#print(fibonacci(1))
#
##Task 4(2)
#def pasco(n):
#    if n==1:
#        return [1]
#    else:
#        preL=pasco(n-1)
#        curL=[1]
#        for i in range(1,len(preL)):
#            curL.append(preL[i-1]+preL[i])
#        curL.append(1)
#        return curL
#        
#print(pasco(2))
#
#
#
##Task 6
#def test_prime(n):
#    for i in range (2,n):
#        if n%i==0:
#            return 'no'
#    return 'yes'
#
#def prime_dict():
#    dict_prime={}
#    for j in range (1,1001):
#        if test_prime(j)=='yes':
#            dict_prime[j]='yes'
#        else:
#            dict_prime[j]='no'
#    return dict_prime
#
#print(prime_dict())


#[[1]]
#[[1,2],[2,1]]
def Permutation(L):
    if len(L)==1:
        return [L]
    else:
        M=[]
        for subL in Permutation(L[0:len(L)-1]):
            for i in range(0,len(subL)+1):
                K=subL.copy()
                K.insert(i,L[-1])
                M.append(K)
        return M

print(Permutation([3,4,5]))


#
#
##Task 7 solution1
#def find_prime():
#    L=[]
#    for i in range (2,1000):
#        s=0
#        for j in range (2,i):
#            if i%j==0:
#                s+=1
#        if s==0:
#            L.append(i)
#    return(L)
#
#def conjecture():
#    for j in range (1,1001):
#        for p in find_prime():
#            for q in find_prime():
#                if j==p+q:
#                    print([j,p,q])
#
#conjecture()
#
#
#
##Task 7 solution2
#def test_prime(a):
#    if a<=1:
#        return False
#    s=0
#    for i in range (2,a):
#       if a%i==0:
#           s+=1
#    if s==0:
#        return True
#    else:
#        return False
#def find_prime():
#    L=[]
#    for i in range (2,1001):
#        if test_prime(i) is True:
#            L.append(i)
#    return(L)
#def conjecture():
#    for j in range (4,1001,2):
#        for p in find_prime():
#            if test_prime(j-p) is True:
#                print([j,p,j-p])
#                break            
#conjecture()
#
#
#
##Task 8
#def get_fibo(n):
#    a,b=1,1
#    if n==1 or n==2:
#        return 1
#    else:
#        for t in range (1,n-1):
#            c=a+b
#            a,b=b,c
#        return c
#    
#def test_fibo():
#    p=int(input('Please input the number:'))
#    n=1
#    while n>=1:
#        if get_fibo(n)==p:
#            return n
#        if get_fibo(n)<p<get_fibo(n+1):
#            return -1
#        n+=1
#print(test_fibo())
#
#def get_subset(L,n):
#    if n==1:
#        res=[]
#        for i in L:
#            res.append([i])
#        return res
#    else:
#        cur=get_subset(L,n-1)  #[[1],[2],[3]]
#        res=[]
#        for i in cur:
#            for val in L:
#                ii=i.copy()
#                ii.append(val)
#                if ii[-1]>ii[-2]:
#                    res.append(ii)
#        return res
#
#def isprime(L,n):
#    count=0
#    res=get_subset(L,n)
#    M=[]
#    for i in res:
#        M.append(sum(i))
#    for i in M:
#        c=0
#        for j in range(2,i):
#            if i%j==0:
#                c+=1
#        if c==0:
#           count+=1
#    return count
#                
#    
#print(isprime([3,7,12,19],3))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#    