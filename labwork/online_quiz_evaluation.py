# Correct answers:
# correct = ['A', 'C', 'B', 'D', 'A']
# Student answers:
# student = ['A', 'B', 'B', 'D', 'C']
# Write a program to:
# • Calculate score. 
# • Display incorrectly answered question numbers. 
# • Count correct and wrong answers. 
# • Determine pass/fail (minimum 60%).

# Correct answers
correct = ['A', 'C', 'B', 'D', 'A']

# Student answers
student = ['A', 'B', 'B', 'D', 'C']

score = 0
correct_count = 0
wrong_count = 0
wrong_questions = []

# Calculate score
for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1
        correct_count += 1
    else:
        wrong_count += 1

        # Display incorrectly answered question numbers
        wrong_questions.append(i + 1)

# Count correct and wrong answers
print("Correct Answers =", correct_count)
print("Wrong Answers =", wrong_count)

# Calculate score
print("Score =", score)

# Display incorrectly answered question numbers
print("Incorrect Question Numbers =", wrong_questions)

# Determine pass/fail (minimum 60%)
percentage = (score / len(correct)) * 100

if percentage >= 60:
    print("Pass")
else:
    print("Fail")