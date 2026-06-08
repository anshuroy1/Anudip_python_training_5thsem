# Accept employee details

employee_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

# Calculate HRA (20% of Basic Salary)
hra = basic_salary * 20 / 100

# Calculate DA (10% of Basic Salary)
da = basic_salary * 10 / 100

# Calculate PF Deduction (12% of Basic Salary)
pf = basic_salary * 12 / 100

# Calculate Gross Salary
# Gross Salary = Basic Salary + HRA + DA
gross_salary = basic_salary + hra + da

# Calculate Net Salary
# Net Salary = Gross Salary - PF
net_salary = gross_salary - pf

# Determine Employee Grade
if net_salary > 50000:
    grade = "Senior Grade"

elif net_salary > 30000:
    grade = "Mid Grade"

else:
    grade = "Junior Grade"

# Display Payroll Details
print("\n========== PAYROLL DETAILS ==========")

print("Employee Name :", employee_name)
print("Basic Salary  :", basic_salary)

print("\nAllowances and Deductions")
print("HRA (20%)     :", hra)
print("DA (10%)      :", da)
print("PF (12%)      :", pf)

print("\nSalary Details")
print("Gross Salary  :", gross_salary)
print("Net Salary    :", net_salary)

print("\nEmployee Grade :", grade)