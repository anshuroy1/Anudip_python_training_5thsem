# A vehicle number plate is entered: 
# MH12AB4589 
# Tasks 
# Write a program to: 
# 1. Extract state code.  
# 2. Extract district code.  
# 3. Extract vehicle series.  
# 4. Extract vehicle number.  
# 5. Count letters and digits separately.  
# 6. Verify:  
# o First 2 characters must be alphabets.  
# o Next 2 must be digits.  
# o Next 2 must be alphabets.  
# o Last 4 must be digits.  
# 7. Display whether the number plate is valid. 

#Program to vehicle number plate verification
plate = "MH12AB4589"

#TASK 1. Extract state code
state_code=plate[0:2]

#TASK 2. Extract district code
district_code=plate[2:4]

#TASK 3. Extract vehicle series
vehicle_series=plate[4:6]

#TASK 4. Extract vehicle number
vehicle_number=plate[6:10]

#TASK 5. Count letters and digits
letters=0
digits=0

for ch in plate:
    if ch.isalpha():
        letters+=1
    elif ch.isdigit():
        digits+=1

#TASK 6. Verify format
valid=False

if (plate[0:2].isalpha() and
    plate[2:4].isdigit() and
    plate[4:6].isalpha() and
    plate[6:10].isdigit()):

    valid=True

#TASK 7. Display results
print("Vehicle Number Plate:", plate)
print("State Code:", state_code)
print("District Code:", district_code)
print("Vehicle Series:", vehicle_series)
print("Vehicle Number:", vehicle_number)
print("Total Letters:", letters)
print("Total Digits:", digits)

if valid==True:
    print("Number Plate is VALID")
else:
    print("Number Plate is INVALID")

'''OUTPUT
Vehicle Number Plate: MH12AB4589
State Code: MH
District Code: 12
Vehicle Series: AB
Vehicle Number: 4589
Total Letters: 4
Total Digits: 6
Number Plate is VALID
'''