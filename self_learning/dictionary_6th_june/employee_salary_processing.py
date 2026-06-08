# • Display employees earning above ₹60,000.
# • Count employees earning below ₹40,000.
# • Find the highest-paid employee.
# • Create a list of employees eligible for a bonus (salary > ₹50,000).
# • Calculate the average salary.

# Employee Salary Processing

salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Employees earning above 60000
print("Employees earning above 60000:")

for emp, sal in salary.items():
    if sal > 60000:
        print(emp, ":", sal)

# Count employees earning below 40000
count = 0

for sal in salary.values():
    if sal < 40000:
        count += 1

print("\nEmployees earning below 40000:", count)

# Highest paid employee
highest_emp = ""
highest_salary = 0

for emp, sal in salary.items():
    if sal > highest_salary:
        highest_salary = sal
        highest_emp = emp

print("\nHighest Paid Employee:", highest_emp)
print("Salary:", highest_salary)

# Employees eligible for bonus
bonus_list = []

for emp, sal in salary.items():
    if sal > 50000:
        bonus_list.append(emp)

print("\nBonus Eligible Employees:")
print(bonus_list)

# Average salary
total = 0

for sal in salary.values():
    total += sal

average = total / len(salary)

print("\nAverage Salary:", average)