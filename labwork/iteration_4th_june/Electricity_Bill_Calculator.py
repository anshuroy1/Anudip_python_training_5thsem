# Input units consumed
units = int(input("Enter units consumed: "))

# Calculate bill
if units <= 100:
    bill = units * 5
    category = "Low Consumption"

elif units <= 200:
    bill = units * 7
    category = "Medium Consumption"

else:
    bill = units * 10
    category = "High Consumption"

# Display result
print("Units Consumed =", units)
print("Total Bill = ₹", bill)
print("Category =", category)