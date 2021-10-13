def main():
    def fibo(n):
        if(n==1 or n==2):
            return 1
        else:
            return fibo(n-1)+fibo(n-2)
    def index(x):
        i=1
        while(fibo(i)<=x):
            if(fibo(i)==x):
                return i
            else:
                i=i+1
        return -1
    x=int(input())
    print(index(x))
main()
        