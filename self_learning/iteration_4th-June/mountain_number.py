# ---------------------------------------------------------
# Program: Mountain Number Checker
#
# A Mountain Number is a number whose digits:
# 1. First strictly increase
# 2. Then strictly decrease
#
# Example:
# 12321 -> Mountain Number
# 12345 -> Not a Mountain Number
# 54321 -> Not a Mountain Number
# ---------------------------------------------------------

# Accept input from user
num = input("Enter a number: ")


# Input Validation


# Check if input contains only digits
if not num.isdigit():
    print("Invalid Input! Please enter digits only.")

# A mountain number needs at least 3 digits
elif len(num) < 3:
    print("Not a Mountain Number (must contain at least 3 digits).")

else:

    n = len(num)
    i = 0

    # Flags to check whether we have
    # both increasing and decreasing parts
    increasing = False
    decreasing = False

   
    
    # Increasing Part
  

    while i < n - 1 and num[i] < num[i + 1]:
        increasing = True
        i += 1


    # Decreasing Part
   

    while i < n - 1 and num[i] > num[i + 1]:
        decreasing = True
        i += 1

   
    # Final Check
   

    # A valid mountain number:
    # 1. Has an increasing part
    # 2. Has a decreasing part
    # 3. Reaches the last digit after both phases

    if increasing and decreasing and i == n - 1:
        print("Mountain Number")
    else:
        print("Not a Mountain Number")