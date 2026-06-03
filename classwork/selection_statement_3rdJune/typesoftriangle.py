angle1 = int(input("enter the first angle"))
if(angle1 <= 0):
    exit("angle1 cannot be negative")
angle2 = int(input("enter the second angle"))
if(angle2 <= 0):
    exit("angle2 cannot be negative")
angle3 = int(input("enter the third angle"))
if(angle3 <= 0):
    exit("angle3 cannot be negative")

#check whether these three angle form a triangle or not
if((angle1 + angle2 + angle3)==180):
    if(angle1 < 90 and angle2 < 90 and angle3 < 90):
        print("above angles form acute angled triangle")
    elif(angle1 == 90 or angle2 == 90 or angle3 == 90):
        print("above angles forms right angled triangled")
    else:
        print("above angles form obtuse angled triangle")
else:
    print("above angle do not form any triangle")
