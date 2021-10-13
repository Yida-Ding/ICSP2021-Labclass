# Return 

# Ex1
def addition(a,b):
    result=a+b
    return result

#(3)
RESULT=addition(1,1)
print(result)
#(4)
print(addition(1,1))


# Ex2
def subtraction(a,b):
    result=a-b
    print(result)

#(1)
subtraction(2,1)
#(2)
RESULT=subtraction(2,1)
print(RESULT)


# Ex3
def product(a,b):
    result=a*b
    return 

#(1)
product(1,5)
#(2)
print(result)
#(3)
print(product(1,5))


# Ex4
def loop_1(n):
    L=[]
    for i in range(n):
        L.append(i)
        return L
    print(666)

def loop_2(n):
    L=[]
    for i in range(n):
        L.append(i)
    return L
    print(666)

#(1)
print(loop(5))
#(2)
print(loop_2(5))


# Ex5
def sumup(n):
    if n==1:
        return 1
    else:
        return n+sumup(n-1)

sumup(2)

#(1) change: if n==2 return 3
#(2) remove: else
#(3) change: return->print

        




