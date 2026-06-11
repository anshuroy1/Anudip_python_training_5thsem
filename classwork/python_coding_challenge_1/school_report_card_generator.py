# Problem Statement 
# Student marks are stored in marks.txt. 
# Sample Input/Data (marks.txt) 
# S101,Anuj,92 
# S102,Rahul,76 
# S103,Priya,88 
# S104,Neha,45 
# S105,Amit,58 
# S106,Sneha,95 
# S107,Karan,81 
# S108,Pooja,73 
# S109,Rohit,39 
# S110,Anjali,90 
# Tasks 
# 1. Calculate grades for all students.  
# 2. Generate a report card file report_card.txt.  
# 3. Display topper details.  
# 4. Count pass and fail students.  
# 5. Display students eligible for merit certificates (marks ≥ 90). 

# School Report Card Generator

students = [
    ["S101", "Anuj", 92],
    ["S102", "Rahul", 76],
    ["S103", "Priya", 88],
    ["S104", "Neha", 45],
    ["S105", "Amit", 58],
    ["S106", "Sneha", 95],
    ["S107", "Karan", 81],
    ["S108", "Pooja", 73],
    ["S109", "Rohit", 39],
    ["S110", "Anjali", 90]
]

# 1. Calculate grades
print("Student Grades:")

for student in students:
    marks = student[2]

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    print(student[1], "-", grade)

# 2. Find topper
topper = students[0]

for student in students:
    if student[2] > topper[2]:
        topper = student

print("\nTopper:")
print(topper[1], "(", topper[2], ")")

# 3. Count pass and fail students
passed = 0
failed = 0

for student in students:
    if student[2] >= 40:
        passed += 1
    else:
        failed += 1

print("\nPassed Students:", passed)
print("Failed Students:", failed)

# 4. Merit certificate students (marks >= 90)
print("\nStudents Eligible for Merit Certificate:")

for student in students:
    if student[2] >= 90:
        print(student[1], "-", student[2])

print("\nReport Card Generated Successfully.")