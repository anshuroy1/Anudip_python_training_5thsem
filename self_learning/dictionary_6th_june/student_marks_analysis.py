# Display students scoring 80 or above.
# • Count the number of students who failed (marks < 40).
# • Find the highest scorer.
# • Create a list of students scoring between 60 and 75.
# • Assign grades:
  #  A: ≥ 90
  #  B: 75–89
  #  C: 50–74
  #  F: < 50


# Program: Student Marks Analysis using Dictionary


# Dictionary containing student names and marks
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}


# 1. Display students scoring 80 or above


print("Students scoring 80 or above:")

for name, score in marks.items():

    if score >= 80:
        print(name, ":", score)


# 2. Count failed students (marks < 40)


fail_count = 0

for score in marks.values():

    if score < 40:
        fail_count += 1

print("\nNumber of Failed Students:", fail_count)


# 3. Find highest scorer


highest_student = ""
highest_marks = 0

for name, score in marks.items():

    if score > highest_marks:
        highest_marks = score
        highest_student = name

print("\nHighest Scorer:", highest_student)
print("Marks:", highest_marks)


# 4. Create list of students scoring between 60 and 75


students_60_75 = []

for name, score in marks.items():

    if score >= 60 and score <= 75:
        students_60_75.append(name)

print("\nStudents scoring between 60 and 75:")
print(students_60_75)

# 5. Assign Grades


print("\nStudent Grades:")

for name, score in marks.items():

    if score >= 90:
        grade = "A"

    elif score >= 75:
        grade = "B"

    elif score >= 50:
        grade = "C"

    else:
        grade = "F"

    print(name, ":", grade)