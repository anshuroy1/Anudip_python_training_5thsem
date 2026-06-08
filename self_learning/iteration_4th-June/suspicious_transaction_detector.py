# ---------------------------------------------------------
# Program: Suspicious Transaction Detector
#
# Accept transaction amounts continuously.
# Stop when user enters -1.
#
# Count:
# 1. Transactions above 50000
# 2. Transactions below 1000
# 3. Total transaction amount
# ---------------------------------------------------------

high_count = 0
low_count = 0
total_amount = 0

while True:

    amount = int(input("Enter Transaction Amount (-1 to stop): "))

    # Stop condition
    if amount == -1:
        break
   
    # Negative transactions not allowed
    if amount < 0:
        print("Amount cannot be negative.")
        continue

    total_amount += amount

    if amount > 50000:
        high_count += 1

    if amount < 1000:
        low_count += 1

# Display results
print("\nTransactions Above ₹50,000 :", high_count)
print("Transactions Below ₹1,000 :", low_count)
print("Total Transaction Amount :", total_amount)