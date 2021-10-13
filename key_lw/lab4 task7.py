def main():
    def f(n):
        for i in range (2,n):
            if(n%i==0):
                return 0
        return 1
    l=[]
    for i in range(2,999):
        if(f(i)==1):
            l.append(i)
    for i in range(3,1000):
        if(i%2==0):
            s=''
            for j in l:
                if(i-j in l):
                    s=s+" "+str(j)
                    s=s+" "+str(i-j)
                    print(s)
                    break
main()
        