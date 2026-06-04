# Input a number
n = int(input("Enter a number: "))

# Store original number
temp = n

# Initialize sum
sum = 0

# Find sum of factorials of digits
while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    temp = temp // 10

# Check Strong Number
if sum == n:
    print(n, "is a Strong Number")
else:
    print(n, "is not a Strong Number")