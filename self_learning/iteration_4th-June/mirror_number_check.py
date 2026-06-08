# ---------------------------------------------------------
# Program: Number Mirror Check
#
# Check whether the left half of a number
# is identical to the right half.
#
# Example:
# 123123 -> Mirror Number
# 123456 -> Not a Mirror Number
# ---------------------------------------------------------

# Accept input
num = input("Enter a number: ")

# Validate input
if not num.isdigit():
    print("Invalid Input! Digits only.")

# Number should have even digits
elif len(num) % 2 != 0:
    print("Not a Mirror Number")

else:

    # Find middle position
    mid = len(num) // 2

    # Split into two halves
    left_half = num[:mid]
    right_half = num[mid:]

    # Compare halves
    if left_half == right_half:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")