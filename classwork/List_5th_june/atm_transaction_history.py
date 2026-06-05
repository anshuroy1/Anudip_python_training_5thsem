# List of transactions
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Calculate current balance
balance = 0
for i in transactions:
    balance += i

# Create deposit and withdrawal lists
deposits = []
withdrawals = []

for i in transactions:
    if i > 0:
        deposits.append(i)
    else:
        withdrawals.append(i)

# Find largest deposit
largest_deposit = deposits[0]
for i in deposits:
    if i > largest_deposit:
        largest_deposit = i

# Find largest withdrawal
largest_withdrawal = withdrawals[0]
for i in withdrawals:
    if i < largest_withdrawal:
        largest_withdrawal = i

# Display results
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)