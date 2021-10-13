a=int(input())
if(a<60):
    b=0
elif(a>60 and a<=69):
    b=1
elif(a>=70 and a<=79):
    b=2
elif(a>=80 and a<=84):
    b=3
elif(a>=85 and a<=100):
    b=4
print("GP=",b)