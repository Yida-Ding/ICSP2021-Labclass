##Task1
#a=int(input('Please enter a number:'))
#b=a
#print(b)
#
##Task2
#print(int((8000.01+19)/37)*(15**2)-3861)

#Task3
print(5<6)
print(5<=6)
print(5==6)
print(5>=4)
print(5==6 or 6==6)
print(5==6 and 6==6)
print(not(5==6) and 6==6)

##Task4
#b=int(input('Please enter a number'))
#a=5
#if a<b:
#    a=a+2
#else:
#    a=a-1
#print(a)
#
##Task5
#grade=int(input('Please input your grade'))
#if grade<0 or grade>100:
#    print('Please enter it again')
#elif grade<60:
#    GP=0
#    print('Your GP is',GP)
#elif grade<70:
#    GP=1
#    print('Your GP is',GP)
#elif grade<80:
#    GP=2
#    print('Your GP is',GP)
#elif grade<85:
#    GP=3
#    print('Your GP is',GP)
#else:
#    GP=4
#    print('Your GP is',GP)
#
##Task6
#user_name=input('Please input your user name:')
#password=input('Please input your password:')
#while not(user_name=='User' and password=='123456'):
#    user_name=input('Please input your user name again:')
#    password=input('Please input your password again:')
#print('logged in')
#
##Task7
#a,b,c,d=int(input('Four numbers')),int(input('')),int(input('')),int(input(''))
#if a>b:
#    if a>c:
#        if a>d:
#            print(a)
#        else:
#            print(d)
#    else:
#        if c>d :
#            print(c)
#        else:
#            print(d)
#else:
#    if b>c:
#        if b>d:
#            print(b)
#        else:
#            print(d)
#    else:
#        if c>d:
#            print(c)
#        else:
#            print(d)
#
#
##Task9
#print('Please input 3 numbers')
#a,b,c=float(input('')),float(input('')),float(input(''))
#L=[a,b,c]
#for i in range(len(L)):
#    for j in range(i+1,len(L)):
#        if L[i]<L[j]:
#            L[i],L[j]=L[j],L[i]
#print(L)
#
#
##Task10
#import math
#print('Please input the coordinate of A')
#x1,y1=float(input('')),float(input(''))
#print('Please input the coordinate of B')
#x2,y2=float(input('')),float(input(''))
#print('Please input the coordinate of C')
#x3,y3=float(input('')),float(input(''))
#c_sqr=(x1-x2)**2+(y1-y2)**2
#b_sqr=(x3-x1)**2+(y3-y1)**2
#a_sqr=(x2-x3)**2+(y2-y3)**2
#c=math.sqrt(c_sqr)
#b=math.sqrt(b_sqr)
#a=math.sqrt(a_sqr)
#if c_sqr==max(c_sqr,b_sqr,a_sqr):
#    cos=(b_sqr+a_sqr-c_sqr)/(2*a*b)
#if b_sqr==max(c_sqr,b_sqr,a_sqr):
#    cos=(c_sqr+a_sqr-b_sqr)/(2*c*a)
#if a_sqr==max(c_sqr,b_sqr,a_sqr):
#    cos=(b_sqr+c_sqr-a_sqr)/(2*b*c)
#radian=math.acos(cos)
#degree=math.degrees(radian)
#if degree==180.0:
#    print("That can't be a triangle")
#print('The biggest angle is',degree)
#
#
#
#
#
#
#
#
#
#
#
#
#
