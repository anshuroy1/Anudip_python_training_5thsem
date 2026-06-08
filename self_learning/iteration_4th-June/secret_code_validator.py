# ---------------------------------------------------------
# Program: Secret Code Validator
#
# A code is valid if:
# 1. It contains exactly 6 digits.
# 2. Sum of first 3 digits equals sum of last 3 digits.
# ---------------------------------------------------------

# Accept code from user
code = input("Enter a 6-digit code: ")

# Validate input
if not code.isdigit():
    print("Invalid Input! Digits only.")

elif len(code) != 6:
    print("Invalid Input! Code must contain exactly 6 digits.")

else:

    # Calculate sum of first three digits
    first_sum = int(code[0]) + int(code[1]) + int(code[2])

    # Calculate sum of last three digits
    last_sum = int(code[3]) + int(code[4]) + int(code[5])

    # Check validity
    if first_sum == last_sum:
        print("Valid Code")
    else:
        print("Invalid Code")