#Program for employee id validation and analysis system
emp_id = "EMP2026ANUJ458"

#TASK 1. Count uppercase letters
upper_count = 0
for ch in emp_id:
    if ch.isupper():
        upper_count += 1

#TASK 2. Count digits
digit_count = 0
for ch in emp_id:
    if ch.isdigit():
        digit_count += 1

#TASK 3. Extract joining year
year = emp_id[3:7]

#TASK 4. Extract employee name
name = emp_id[7:-3]

#TASK 5. Validate ID
valid = True

#Check if it starts with EMP
if emp_id.startswith("EMP") == False:
    valid = False

# Check if year contains 4 digits
if emp_id[3:7].isdigit() == False:
    valid = False

# Check if last 3 characters are digits
if emp_id[-3:].isdigit() == False:
    valid = False

if valid == True:
    print("Valid ID")
else:
    print("Invalid ID")

#TASK 6. Create list of all digits
digit_list = []
for ch in emp_id:
    if ch.isdigit():
        digit_list.append(int(ch))

#TASK 7. Sum of all digits
digit_sum = sum(digit_list)

#TASK 8. Display results
print("Employee ID:", emp_id)
print("Uppercase Letters:", upper_count)
print("Digits:", digit_count)
print("Joining Year:", year)
print("Employee Name:", name)
print("Digit List:", digit_list)
print("Sum of Digits:", digit_sum)

if valid:
    print("Employee ID is VALID")
else:
    print("Employee ID is INVALID")