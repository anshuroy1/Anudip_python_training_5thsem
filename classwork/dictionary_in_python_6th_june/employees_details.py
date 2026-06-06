# Employee ID as key and Salary as value

employees = {}

# Input records of 10 employees
for i in range(10):
    emp_id = input("Enter Employee ID: ")
    salary = int(input("Enter Salary: "))

    employees[emp_id] = salary

count = 0

# Find total employees having salary greater than 30000
for emp_id, salary in employees.items():
    if salary > 30000:
        count += 1

print("Employees with salary > 30000 =", count)

# Display employees whose salary is below 20000
print("Employees with salary < 20000:")

for emp_id, salary in employees.items():
    if salary < 20000:
        print(emp_id)