total_students = 30
attendance_count = 1
present_count = 0
while(attendance_count <= 30):
    print("student",attendance_count)
    #input for student present or not
    student_present = input("attendance:")
    #count the present student 

    if(student_present.lower()=="present"):
         
         present_count += 1
    attendance_count += 1
print("No of student:",present_count)
print("No of absent:", (total_students - present_count))

