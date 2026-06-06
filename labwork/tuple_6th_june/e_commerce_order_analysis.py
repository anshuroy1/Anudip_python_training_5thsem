# Problem Statement
# An online store records orders as:
# orders = [
#  ("Laptop", 55000),
#  ("Mouse", 800),
#  ("Keyboard", 1500),
#  ("Monitor", 12000),
#  ("Pen Drive", 600)
# ]
# Write a program to:
# • Display all products costing more than ₹1000. 
# • Find the most expensive product. 
# • Calculate the total order value. 
# • Count products costing below ₹1000.
# Order details stored in a list of tuples
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# 1. Display products costing more than ₹1000
print("Products Costing More Than ₹1000:")
for order in orders:
    if order[1] > 1000:
        print(order[0], order[1])

# 2. Find the most expensive product
expensive = orders[0]

for order in orders:
    if order[1] > expensive[1]:
        expensive = order

print("\nMost Expensive Product:")
print(expensive[0], expensive[1])

# 3. Calculate total order value
total = 0

for order in orders:
    total += order[1]

print("\nTotal Order Value:", total)

# 4. Count products costing below ₹1000
count = 0

for order in orders:
    if order[1] < 1000:
        count += 1

print("\nProducts Costing Below ₹1000:", count)