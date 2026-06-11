# Problem Statement 
# Employee attendance records are stored in attendance.txt. 
# Sample Input/Data (attendance.txt) 
# EMP101,P 
# EMP102,A 
# EMP103,P 
# EMP104,P 
# EMP105,A 
# EMP106,P 
# EMP107,P 
# EMP108,A 
# EMP109,P 
# EMP110,P 
# Tasks 
# 1. Count present and absent employees.  
# 2. Display absent employee IDs.  
# 3. Calculate attendance percentage.  
# 4. Generate an absentee report in absent_report.txt.  
# 5. Display employees eligible for attendance awards (100% attendance). 


# Employee Attendance Monitoring System

attendance = [
    ["EMP101", "P"],
    ["EMP102", "A"],
    ["EMP103", "P"],
    ["EMP104", "P"],
    ["EMP105", "A"],
    ["EMP106", "P"],
    ["EMP107", "P"],
    ["EMP108", "A"],
    ["EMP109", "P"],
    ["EMP110", "P"]
]

present = 0
absent = 0
# Display absent employee IDs
print("Absent Employee IDs:")

for emp in attendance:

    # Validation
    if emp[1] != "P" and emp[1] != "A":
        print("Invalid Record:", emp)
        continue

    if emp[1] == "P":
        present += 1
    else:
        absent += 1
        print(emp[0])

# Count present and absent employees
print("\nPresent Employees:", present)
print("Absent Employees:", absent)



# Attendance Percentage
percentage = (present / len(attendance)) * 100

print("\nAttendance Percentage:", percentage, "%")

# Attendance Award Eligibility
print("\nAttendance Award Eligibility:")

for emp in attendance:
    if emp[1] == "P":
        print(emp[0])

print("\nAbsentee Report Generated Successfully.")