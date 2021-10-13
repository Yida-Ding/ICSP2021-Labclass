def fibo(n):
    print(fibo(n))
    if(n==1 or n==2):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input())
fibo(n)
    
    