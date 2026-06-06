# Attendance for 15 days is recorded as:
# attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
# Write a program to:
# • Count present and absent days. 
# • Calculate attendance percentage. 
# • Determine eligibility (minimum 75% attendance). 
# • Display positions where the student was absent.
# Problem 6: Student Attendance Tracker

# attendance touple
attendance = ('P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P')

present = 0
absent = 0
absent_positions = []

#count present and absent days
for i in range(len(attendance)):
    if attendance[i] == 'P':
        present += 1
    else:
        absent += 1
        absent_positions.append(i + 1)

#calculate attendance percentage
percentage = (present / len(attendance)) * 100

print("Present Days:", present)
print("Absent Days:", absent)
print("Attendance Percentage:", percentage)

#check eligibility
if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

#display absent positions
print("Absent Positions:", absent_positions)