# Product IDs and quality status:
# products = [
#  (101, "Pass"),
#  (102, "Fail"),
#  (103, "Pass"),
#  (104, "Fail"),
#  (105, "Pass")
# ]
# Write a program to:
# • Display failed product IDs. 
# • Count passed and failed products. 
# • Calculate pass percentage. 
# • Stop checking if 3 failures are found.

# Product IDs and quality status
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

pass_count = 0
fail_count = 0
fail_ids = []


# Display failed product IDs
for pid, status in products:
    if status == "Fail":
        fail_ids.append(pid)

print("Failed Product IDs:", fail_ids)

# Count passed and failed products
for pid, status in products:
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("Passed Products =", pass_count)
print("Failed Products =", fail_count)

# Calculate pass percentage
pass_percentage = (pass_count / len(products)) * 100
print("Pass Percentage =", pass_percentage)

# Stop checking if 3 failures are found
fail_found = 0

for pid, status in products:
    if status == "Fail":
        fail_found += 1

    if fail_found == 3:
        print("3 failures found. Stopping check.")
        break