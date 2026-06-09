# 8. String-Based Attendance Tracker 
# Problem Statement 
# Attendance of a student for 15 days is represented as: 
# PPAPPPAAPPPPAPP 
# Where: 
# • P = Present  
# • A = Absent  
# Tasks 
# Write a program to: 
# 1. Count Present and Absent days.  
# 2. Calculate attendance percentage.  
# 3. Find the longest consecutive streak of Presence.  
# 4. Find the longest consecutive streak of Absence.  
# 5. Determine whether attendance is below 75%. 

#Program for string based attendence tracker
attendance = "PPAPPPAAPPPPAPP"

#TASK 1. Count Present and Absent days
present=0
absent=0

for ch in attendance:
    if ch=='P':
        present+=1
    else:
        absent+=1

#TASK 2. Calculate attendance percentage
total_days=len(attendance)
percentage=(present/total_days)*100

#TASK 3. Find longest consecutive streak of Presence
current_p=0
longest_p=0

for ch in attendance:
    if ch=='P':
        current_p+=1

        if current_p>longest_p:
            longest_p=current_p
    else:
        current_p=0

# TASK 4. Find longest consecutive streak of Absence
current_a=0
longest_a=0

for ch in attendance:
    if ch=='A':
        current_a+=1

        if current_a>longest_a:
            longest_a=current_a
    else:
        current_a=0

#TASK 5. Check attendance below 75%
below_75=False

if percentage<75:
    below_75=True

# Display Results
print("Attendance Record:", attendance)
print("Present Days:", present)
print("Absent Days:", absent)
print("Attendance Percentage:", percentage)
print("Longest Presence Streak:", longest_p)
print("Longest Absence Streak:", longest_a)

if below_75==True:
    print("Attendance is below 75%")
else:
    print("Attendance is 75% or above")

'''
output:
Attendance Record: PPAPPPAAPPPPAPP
Present Days: 11
Absent Days: 4
Attendance Percentage: 73.33333333333333
Longest Presence Streak: 4
Longest Absence Streak: 2
Attendance is below 75%

'''