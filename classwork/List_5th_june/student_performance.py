# List of student marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# Passed students (marks >= 40)
passed = []
failed_count = 0

for i in marks:
    if i >= 40:
        passed.append(i)
    else:
        failed_count += 1

# Find highest mark without max()
highest = marks[0]
for i in marks:
    if i > highest:
        highest = i

# Find lowest mark without min()
lowest = marks[0]
for i in marks:
    if i < lowest:
        lowest = i

# Create merit list (marks > 75)
merit = []
for i in marks:
    if i > 75:
        merit.append(i)

# Display results
print("Passed Students:", passed)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit)
