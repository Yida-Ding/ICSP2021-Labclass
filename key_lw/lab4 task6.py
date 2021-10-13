def main():
    def f(n):
        for i in range (2,n):
            if(n%i==0):
                return 0
        return 1
    dic={}
    dic[1]='no'
    for i in range(2,1001):
        if(f(i)==1):
            dic[i]='yes'
        else:
            dic[i]='no'
    print(dic)
main()