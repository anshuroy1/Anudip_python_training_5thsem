#write a program to check whether the triangle is formed or not by the sides 
side1=int(input("enter the side1 (in cm)"))
if(side1<=0):
    exit("side1 cannot be negative")
side2=int(input("enter the side2 (in cm)"))
if(side2<=0):
    exit("side2 cannot be negative")
side3=int(input("enter the side3 (in cm)"))
if(side3<=0):
    exit("side3 cannot be negative")

#check wheher the traingle is formed using these sides or not
if((side1+side2)>side3 & (side1+side3)>side2 & (side2+side3)>side1):
    if(side1 == side2 and  side2 == side3):
     print("above sides form a equilateral triangle")
    elif(side1==side2 or side2==side3 or side1==side3):
     print("above sides form a isosceles triangle ")
    else:
       print("above sides form a scalene triangle")
else:
    print("triangle is not formed using these sides")