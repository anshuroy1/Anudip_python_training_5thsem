# Accept a number and check whether every digit is exactly 1 greater than its previous digit.
# Accept number as string
num = input("Enter a number: ")

# Assume number is consecutive initially
flag = True

# Traverse each digit except the last digit
for i in range(len(num) - 1):

    # Convert characters to integers and compare
    # Next digit should be exactly 1 greater
    if int (num[i + 1]) != int(num[i]) + 1:
        flag = False
        break

# Display result
if flag:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")