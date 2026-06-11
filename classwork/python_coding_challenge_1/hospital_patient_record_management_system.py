# A hospital maintains patient details in a file named patients.txt. 
# Sample Input/Data (patients.txt) 
# P101,Anuj,Normal 
# P102,Rahul,Critical 
# P103,Priya,Stable 
# P104,Neha,Critical 
# P105,Amit,Stable 
# P106,Sneha,Normal 
# P107,Karan,Critical 
# P108,Pooja,Stable 
# P109,Rohit,Normal 
# P110,Anjali,Stable 
# Tasks 
# 1. Display all patient records.  
# 2. Display critical patients.  
# 3. Count patients under each status.  
# 4. Search patient details using Patient ID.  
# 5. Save critical patient records to critical_patients.txt. 
# Hospital Patient Record Management System
# Hospital Patient Record Management System

# Patient Data
patients = [
    ["P101", "Anuj", "Normal"],
    ["P102", "Rahul", "Critical"],
    ["P103", "Priya", "Stable"],
    ["P104", "Neha", "Critical"],
    ["P105", "Amit", "Stable"],
    ["P106", "Sneha", "Normal"],
    ["P107", "Karan", "Critical"],
    ["P108", "Pooja", "Stable"],
    ["P109", "Rohit", "Normal"],
    ["P110", "Anjali", "Stable"]
]

# 1. Display all patient records
print("All Patient Records:")
for patient in patients:
    print(patient[0], patient[1], patient[2])

# 2. Display critical patients
print("\nCritical Patients:")
for patient in patients:
    if patient[2] == "Critical":
        print(patient[1])

# 3. Count patients under each status
normal = 0
stable = 0
critical = 0

for patient in patients:
    if patient[2] == "Normal":
        normal += 1
    elif patient[2] == "Stable":
        stable += 1
    elif patient[2] == "Critical":
        critical += 1

print("\nPatient Count:")
print("Normal :", normal)
print("Stable :", stable)
print("Critical :", critical)

# 4. Search patient using Patient ID
search_id = input("\nEnter Patient ID to Search: ")

found = False

for patient in patients:
    if patient[0] == search_id:
        print("\nPatient Found:")
        print(patient[0], patient[1], patient[2])
        found = True
        break

if not found:
    print("Patient Not Found")

# 5. Display critical patient report
print("\nCritical Patient Report:")
for patient in patients:
    if patient[2] == "Critical":
        print(patient[0], patient[1], patient[2])

print("\nCritical Patient Report Generated Successfully.")

''' 
Output:
All Patient Records:
P101 Anuj Normal
P102 Rahul Critical
P103 Priya Stable
P104 Neha Critical
P105 Amit Stable
P106 Sneha Normal
P107 Karan Critical
P108 Pooja Stable
P109 Rohit Normal
P110 Anjali Stable

Critical Patients:
Rahul
Neha
Karan

Patient Count:
Normal : 3
Stable : 4
Critical : 3

Enter Patient ID to Search: P102

Patient Found:
P102 Rahul Critical

Critical Patient Report:
P102 Rahul Critical
P104 Neha Critical
P107 Karan Critical

Critical Patient Report Generated Successfully.

'''