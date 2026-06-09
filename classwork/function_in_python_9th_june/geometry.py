#module to calculate area and perimeter of 2D figures
#for calculating area and perimeter of rectangle
def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)   

#for calculating area and perimeter of square
def square_area(side):
    return side * side

def square_perimeter(side):
    return 4 * side

#for calculating area and perimeter of circle
def circle_area(radius):    
    pi = 3.14159
    return pi * radius * radius

def circle_perimeter(radius):
    pi = 3.14159
    return 2 * pi * radius
