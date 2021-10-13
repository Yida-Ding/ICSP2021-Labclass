#Input
cs_score=int(input("Please enter ICSP score:"))
cs_credit=int(input("Please enter ICSP credit:"))
la_score=int(input("Please enter LA score:"))
la_credit=int(input("Please enter LA credit:"))

#Task1
if 60<=cs_score<=100:
    cs_gp=4-3*((100-cs_score)**2)/1600
elif cs_score<60:
    cs_gp=0    
    
if 60<=la_score<=100:
    la_gp=4-3*((100-la_score)**2)/1600
elif la_score<60:
    la_gp=0
print("The grade point of ICSP is",cs_gp,"The grade point of LA is",la_gp)


#Task2
gpa=(cs_gp*cs_credit+la_gp*la_credit)/(cs_credit+la_credit)
print("The GPA of Peter is ",gpa)


#Task3
if gpa>3.5 and la_score>=60 and cs_score>=60:
    scholarship=3000
elif gpa>3 and (la_score>=60 or cs_score>=60):
    scholarship=1000
elif gpa<=3:
    scholarship=0
print("The scholarship of Peter is",scholarship)



#Function
def f(score):
    if 60<=score<=100:
        gp=4-3*((100-score)**2)/1600
    elif score<60:
        gp=0
    return gp

cs_gp=f(cs_score)
la_gp=f(la_score)
print("The grade point of ICSP is",cs_gp,"The grade point of LA is",la_gp)



















