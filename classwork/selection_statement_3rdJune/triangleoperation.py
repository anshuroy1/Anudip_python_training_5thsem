 #program to calculate area and perimeter of triangle
#input of three sides
print("..........Triangle........")
side1 = int(input("Enter first side(in cm):"))
side2 = int(input("Enter second side(in cm):"))
side3 = int(input("Enter third side(in cm):"))
#.......
print("side of the triangle")
print("First side:",side1,"cm")
print("second side:",side2,"cm")
print("third side:",side3,"cm")
#to calculate perimeter
perimeter = side1 + side2 + side3
s = perimeter/2
print("Area:",(s*(s-side1)*(s-side2)*(s-side3))**0.5,"sq. cm")
print("perimeter:",perimeter,"cm")
