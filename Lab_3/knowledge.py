#while/for loop
i=1
while i<=3:
    print("i=",i)
    i=i+1
print("Done")

for i in range(1,4):
    print("i=",i)
print("Done")







#global/local variable
a=5
def sum_with_b(x):
    b=3
    print(x+b)
sum_with_b(a)
print(b)














def sums(L):
    result=[]
    for i in L:
        for j in L:
            if i+j not in result:
                result.append(i+j)
    print(result)
    
def even(n):
    result=[]
    for i in range(0,n,2):
        result.append(i)
    sums(result)

even(10)









   
x='global'
def f1():
    x='local'
    print(x)
    return x
print(x)
f1()
x=f1()
print(x)   
    
    
    
    
    
    
    




#inside function- only in function






