# Employee records stored as tuples
 #Tasks
#Write a Python program to:
#1. Display details of employees scoring 80 or above. 
#2. Count the number of employees who need improvement (score below 60). 
#3. Find the employee with the highest score. 
#4. Create a list containing the names of all employees scoring above 75. 
#5. Display the performance category for each employee: 
#o 90 and above → Excellent 
#o 75 to 89 → Good 
#o 60 to 74 → Average 
#o Below 60 → Needs Improv 
 
employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# 1. Display employees scoring 80 or above
print("Employees Scoring 80 or Above:")
for emp in employees:
    if emp[2] >= 80:   # score is at index 2
        print(emp[0], emp[1], emp[2])
        

# 2. Count employees needing improvement (score below 60)
count = 0
for emp in employees:
    if emp[2] < 60:
        count += 1

print("\nEmployees Needing Improvement:", count)

# 3. Find employee with highest score
highest = employees[0]   # assume first employee has highest score

for emp in employees:
    if emp[2] > highest[2]:
        highest = emp

print("\nHighest Performer:")
print(highest[0], highest[1], highest[2])

# 4. Create list of employees scoring above 75
high_performers = []

for emp in employees:
    if emp[2] > 75:
        high_performers.append(emp[1])  # add employee name

print("\nHigh Performers:")
print(high_performers)

# 5. Display performance category for each employee
print("\nPerformance Categories:")

for emp in employees:
    score = emp[2]

    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(emp[1], "->", category)#employee record stored in tuple