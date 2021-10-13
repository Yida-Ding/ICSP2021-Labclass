a=[78, 83, 95, 92, 61, 50, 83, 79, 71, 99]
j=0
for i in a:
    if(i<60):
        print("GP=0")
    elif(i>=60 and i<69):
        print("GP=1")
    elif(i>=70 and i<79):
        print("GP=2")
    elif(i>=80 and i<=84):
        print("GP=3")
        j=j+1
    elif(i>=85 and i<=100):
        print("GP=4")
print(j)