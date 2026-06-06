# Problem Statement
# A batsman's scores in different matches are stored in a list.
# scores = [45, 78, 12, 100, 67, 8, 90, 55]
# Write a program to:
# • Count half-centuries and centuries. 
# • Find the highest score. 
# • Display all scores below 20. 
# • Calculate the average score.
# Cricket Tournament Scorecard

scores = [45, 78, 12, 100, 67, 8, 90, 55]

# 1. Count half-centuries and centuries
half_century = 0
century = 0

for score in scores:
    if score >= 100:
        century += 1
    elif score >= 50:
        half_century += 1

print("Half-Centuries:", half_century)
print("Centuries:", century)

# 2. Find the highest score
highest = scores[0]

for score in scores:
    if score > highest:
        highest = score

print("\nHighest Score:", highest)

# 3. Display all scores below 20
print("\nScores Below 20:")

for score in scores:
    if score < 20:
        print(score)

# 4. Calculate the average score
total = 0

for score in scores:
    total += score

average = total / len(scores)

print("\nAverage Score:", average)