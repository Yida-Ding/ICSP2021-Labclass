def recsum(n,total=0):
    if(n==0):
        print(total)
    else:
        recsum(n-1,total+n)
n=int(input())
recsum(n)