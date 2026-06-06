# Employee data is stored as tuples:
# employees = [
#  ("Rahul", 35000),
#  ("Priya", 55000),
#  ("Amit", 42000),
#  ("Neha", 65000)
# ]
# Write a program to:
# • Display employees earning above ₹50,000. 
# • Find the highest-paid employee. 
# • Calculate total salary expenditure. 
# • Count employees earning below ₹40,000.
# Employee Salary Processing

employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# 1. Display employees earning above ₹50,000
print("Employees Earning Above ₹50,000:")

for employee in employees:
    if employee[1] > 50000:
        print(employee[0], employee[1])

# 2. Find the highest-paid employee
highest = employees[0]

for employee in employees:
    if employee[1] > highest[1]:
        highest = employee

print("\nHighest Paid Employee:")
print(highest[0], highest[1])

# 3. Calculate total salary expenditure
total = 0

for employee in employees:
    total += employee[1]

print("\nTotal Salary Expenditure:", total)

# 4. Count employees earning below ₹40,000
count = 0

for employee in employees:
    if employee[1] < 40000:
        count += 1

print("\nEmployees Earning Below ₹40,000:", count)