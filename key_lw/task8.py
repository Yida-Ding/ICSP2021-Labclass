a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if(a!=0 and (b**2-(4*a*c))>0):
    print("x=",((-1)*b+(b**2-(4*a*c))**(1/2))/(2*a))
    print("or x=",((-1)*b-(b**2-(4*a*c))**(1/2))/(2*a))
elif(a!=0 and (b**2-(4*a*c))==0):
    print("x=",((-1)*b+(b**2-(4*a*c))**(1/2))/(2*a))
elif(a==0):
    print("x=",(-1)*c/b)
else:
    print("no real root")
    