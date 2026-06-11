#design a python program to calculate area of triangle using heron's formula.

try:
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter third side: "))

    #check for zer0 or negative 
    if side1 <=0 or side2 <= 0 or side3 <= 0:
        print("triangle side must be greater than zero")

    #check three sides can form a triangle or not
    #by triangle inequality theorem
    elif (side1 + side2 <= side3) or (side2 + side3 <= side1) or (side1 + side3 <= side2):
        print("cannot form a valid triangle")

    else:
        #heron's formula
        s = (side1 + side2 + side3)/2
        area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
        print("Area of triangle is: ", area)

except ValueError:
    print("non numeric value entered. please enter numeric value")

finally:
    print("triangle area calculaation completed")