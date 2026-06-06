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
correct = ('A', 'C', 'B', 'D', 'A')

# Student answers
student = ('A', 'B', 'B', 'D', 'C')

score = 0
correct_count = 0
wrong_count = 0
wrong_questions = []

# Compare answers
for i in range(len(correct)):

    # If answer is correct
    if correct[i] == student[i]:
        score += 1
        correct_count += 1

    # If answer is wrong
    else:
        wrong_count += 1
        wrong_questions.append(i + 1)

# Calculate percentage
percentage = (score / len(correct)) * 100

# Display results
print("Score:", score)
print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)
print("Incorrect Question Numbers:", wrong_questions)

# Check pass/fail
if percentage >= 60:
    print("Pass")
else:
    print("Fail")