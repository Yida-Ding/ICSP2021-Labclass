def main():
    def transformLtostr(L):
        result=''
        for i in L:
            result=result+' '+str(i)
        return result
    def c(m,n):
        if(m==n or n==0):
            return 1
        else:
            return c(m-1,n-1)+c(m-1,n)
    n=int(input())
    for i in range(1,n+1):
        l=[]
        for j in range(0,i+1):
            l.append(c(i,j))
        print(transformLtostr(l))
main()