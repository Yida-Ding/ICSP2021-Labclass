def main():
    left=[None]*1000000
    right=[None]*100000
    l=[2,1,5,7,3]
    def sortt(l):
        for i in l:
            a=l[0]
            j=-1
            while(a!=None):
                if(i<a):
                    b=a
                    a=left[a]
                    j=0
                elif(i>a):
                    b=a
                    a=right[a]
                    j=1
                elif(i==a):
                    break
            if(j==0):
                left[b]=i
            elif(j==1):
                right[b]=i
    def printt(a):
        if(a==None):
            return 0
        elif(left[a]==None and right[a]==None):
            print(a)
        else:
            printt(left[a])
            print(a)
            printt(right[a])
    sortt(l)
    printt(l[0])
main()
                