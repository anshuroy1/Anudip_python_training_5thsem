# • Display students scoring 15 or above.
# • Count students scoring below 10.
# • Find the top performer.
# • Create a list of students who passed (≥ 10 marks).
# • Calculate the class average

# Online Quiz Performance

quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Students scoring 15 or above
print("Students Scoring 15 or Above:")

for student, marks in quiz_scores.items():
    if marks >= 15:
        print(student, ":", marks)

# Count students scoring below 10
count = 0

for marks in quiz_scores.values():
    if marks < 10:
        count += 1

print("\nStudents Scoring Below 10:", count)

# Top performer
top_student = ""
highest_marks = 0

for student, marks in quiz_scores.items():
    if marks > highest_marks:
        highest_marks = marks
        top_student = student

print("\nTop Performer:", top_student)
print("Marks:", highest_marks)

# Passed students (10 or more)
passed = []

for student, marks in quiz_scores.items():
    if marks >= 10:
        passed.append(student)

print("\nPassed Students:")
print(passed)

# Class average
total = 0

for marks in quiz_scores.values():
    total += marks

average = total / len(quiz_scores)

print("\nClass Average:", average)