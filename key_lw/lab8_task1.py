import time
def pascal(n,line_i): 
   # print (line_i) 
    if len(line_i)<n: 
        line_ii=[1] 
        for i in range(len(line_i)-1): 
            line_ii.append(line_i[i]+line_i[i+1]) 
        line_ii.append(1) 
        pascal(n,line_ii)
n=int(input())
s=time.time()
pascal(n,[1])
d=time.time()
print(n,d-s)

