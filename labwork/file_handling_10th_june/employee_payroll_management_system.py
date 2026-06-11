# Problem Statement 
# A company stores employee details in a text file named employees.txt. 
# File Format 
# EMP101,Anuj,45000 
# EMP102,Rahul,52000 
# EMP103,Priya,38000 
# EMP104,Neha,61000 
# EMP105,Amit,29000 
# EMP106,Sneha,55000 
# EMP107,Karan,47000 
# EMP108,Pooja,72000 
# EMP109,Rohit,33000 
# EMP110,Anjali,68000 
# Requirements 
# Create a menu-driven program to: 
# 1. Display all employee records.  
# 2. Search employee details using Employee ID.  
# 3. Calculate the average salary.  
# 4. Find the highest-paid and lowest-paid employee.  
# 5. Display employees earning above ₹50,000.  
# 6. Add a new employee record to the file.  
# 7. Generate salary categories:  
# o High (₹60,000 and above)  
# o Medium (₹40,000–₹59,999)  
# o Low (below ₹40,000)


#employee payroll management system

def display_records():
    file = open("employees.txt", "r")
    data = file.readlines()

    print("\nEmployee Records")
    for line in data:
        print(line.strip())

    file.close()


def search_employee():
    emp_id = input("Enter Employee ID: ")

    file = open("employees.txt", "r")
    found = False

    for line in file:
        record = line.strip().split(",")

        if record[0] == emp_id:
            print("\nEmployee Found")
            print("ID :", record[0])
            print("Name :", record[1])
            print("Salary :", record[2])
            found = True
            break

    if not found:
        print("Employee not found")

    file.close()


def average_salary():
    file = open("employees.txt", "r")

    total = 0
    count = 0

    for line in file:
        record = line.strip().split(",")

        total += int(record[2])
        count += 1

    if count > 0:
        print("Average Salary =", total / count)

    file.close()


def highest_lowest_salary():

    file = open("employees.txt", "r")

    records = file.readlines()

    highest = records[0].strip().split(",")
    lowest = records[0].strip().split(",")

    for line in records:

        record = line.strip().split(",")

        if int(record[2]) > int(highest[2]):
            highest = record

        if int(record[2]) < int(lowest[2]):
            lowest = record

    print("\nHighest Paid Employee")
    print(highest)

    print("\nLowest Paid Employee")
    print(lowest)

    file.close()


def salary_above_50000():

    file = open("employees.txt", "r")

    print("\nEmployees earning above 50000")

    for line in file:

        record = line.strip().split(",")

        if int(record[2]) > 50000:
            print(line.strip())

    file.close()


def add_employee():

    emp_id = input("Enter Employee ID : ")
    name = input("Enter Name : ")
    salary = int(input("Enter Salary : "))

    file = open("employees.txt", "a")

    file.write(f"\n{emp_id},{name},{salary}")

    file.close()

    print("Employee Added Successfully")


def salary_categories():

    file = open("employees.txt", "r")

    high = []
    medium = []
    low = []

    for line in file:

        record = line.strip().split(",")

        salary = int(record[2])

        if salary >= 60000:
            high.append(record[1])

        elif salary >= 40000:
            medium.append(record[1])

        else:
            low.append(record[1])

    print("\nHigh Category")
    print(high)

