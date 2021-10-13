import random
import numpy as np
import math
import matplotlib.pyplot as plt

#Task 1
def expandArctan(x,Nterms):
    seriesSum=0
    for i in range(Nterms):
        n=2*i+1
        seriesSum+=((-1)**(i))*(x**n)/n
    return seriesSum

res=expandArctan(1,1000)
print("The Pi calculaiton of programme:",res*4)
print("The real Pi:",np.pi)


#Task 2
def getDistanceFromOrigin(x,y):
    dis=math.sqrt(x**2+y**2)
    return dis

def generatePoints(N):
    Ninside=0
    for i in range(N):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        dis=getDistanceFromOrigin(x,y)
        if dis<=1:
            Ninside+=1
    return Ninside

def approximatePi(Ninside,N):
    pi=Ninside/N*4
    return pi

N=10000
Ninside=generatePoints(N)
pi=approximatePi(Ninside,N)
print(pi)
    
    
#Extra
def generateData(N):
    xin,yin,xout,yout=[],[],[],[]
    for i in range(N):
        x,y=random.uniform(0,1),random.uniform(0,1)
        if getDistanceFromOrigin(x,y)<=1:
            xin.append(x)
            yin.append(y)
        else:
            xout.append(x)
            yout.append(y)
    return xin,yin,xout,yout

def plotData(Ns):
    fig,axes=plt.subplots(2,2,figsize=(10,8))
    for i in range(2):
        for j in range(2):
            xin,yin,xout,yout=generateData(Ns[i][j])
            axes[i][j].scatter(xin,yin,c='orange',s=5)
            axes[i][j].scatter(xout,yout,c='blue',s=5)
            pi=approximatePi(len(xin),len(xin)+len(xout))
            axes[i][j].set_title("Pi:%f"%pi)
    plt.show()
        
plotData([[100,1000],[10000,100000]])

    




