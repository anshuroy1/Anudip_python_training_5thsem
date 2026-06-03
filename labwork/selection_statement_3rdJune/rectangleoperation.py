length = int(input("enter the length side(in cm):"))
if(length < 0):
    exit("length cannot be negative")
breadth = int(input("enter the breadth side(in cm):"))
if(breadth < 0):
    exit("breadth cannot be negative")

    #lenght and breadth of rectangle
print("length of rectangle:",length,"cm")
print("breadth of rectangle:",breadth,"cm")

#area and perimeter 
print("Area:",length*breadth,"sq. cm")
print("perimeter:",2*(length+breadth),"cm")
