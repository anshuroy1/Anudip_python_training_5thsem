# Attendance for 15 days is recorded as:
# attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
# Write a program to:
# • Count present and absent days. 
# • Calculate attendance percentage. 
# • Determine eligibility (minimum 75% attendance). 
# • Display positions where the student was absent.
# Student Attendance Tracker

attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# 1. Count Present and Absent days
present = 0
absent = 0

for status in attendance:
    if status == 'P':
        present += 1
    else:
        absent += 1

print("Present Days:", present)
print("Absent Days:", absent)

# 2. Calculate Attendance Percentage
percentage = (present / len(attendance)) * 100

print("\nAttendance Percentage:", percentage)

# 3. Find first absent day
for i in range(len(attendance)):
    if attendance[i] == 'A':
        print("\nFirst Absent Day:", i + 1)
        break

# 4. Check eligibility (75% attendance required)
if percentage >= 75:
    print("\nEligible for Exam")
else:
    print("\nNot Eligible for Exam")