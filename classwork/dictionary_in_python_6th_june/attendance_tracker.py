# Attendance Dictionary

attendance = {}

# Input data for 30 students
for i in range(3):
    roll_no = int(input("Enter Roll Number: "))
    status = input("Enter Attendance (P/A): ")

    attendance[roll_no] = status

print("attendance of students :")
print(attendance)
# Display roll numbers of present students
print("\nPresent Students:")

for roll_no, status in attendance.items():
    if status.upper() == 'P':
        print(roll_no)