import time
import matplotlib.pyplot as plt

def GCD(m,n):
    r=m%n
    if r==0:
        return n
    else:
        return GCD(n,r)

print(GCD(16*2,16*7))

def getPrimeNumbers(N):
    res=[]
    for i in range(2,N+1):
        isPrime=True
        for j in range(2,i):
            if i%j==0:
                isPrime=False
        if isPrime==True:
            res.append(i)
    return res


def getPrimeNumbers_improved(N):
    res=[]
    for i in range(2,N+1):
        isPrime=True
        for j in range(2,int((i**0.5)+1)):
            if i%j==0:
                isPrime=False
        if isPrime==True:
            res.append(i)
    return res

def visualizeRuntime():
    Ns,T1,T2=[],[],[]
    for N in range(100,10000,1000):
        t1=time.time()
        getPrimeNumbers(N)
        t2=time.time()
        getPrimeNumbers_improved(N)
        t3=time.time()
        Ns.append(N)
        T1.append(t2-t1)
        T2.append(t3-t2)
        
    fig,ax=plt.subplots(1,1,figsize=(10,8),dpi=100)
    ax.plot(Ns,T1,label="Original")
    ax.plot(Ns,T2,label="Improved")
    ax.set_xlabel("N")
    ax.set_ylabel("Runtime(s)")
    ax.set_ylim(0,3)
    ax.set_xlim(0,10000)
    ax.set_title("Runtime Comparision")
    ax.legend()

visualizeRuntime()





    
    


