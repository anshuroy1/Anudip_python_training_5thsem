# Write a program to determine whether the password is Strong, Medium, or Weak. 
# Rules: 
# • Minimum length 8  
# • Contains at least:  
# o 1 uppercase letter  
# o 1 lowercase letter  
# o 1 digit  
# o 1 special character  
# Additionally: 
# 1. Count uppercase letters.  
# 2. Count lowercase letters.  
# 3. Count digits.  
# 4. Count special characters.  
# 5. Display all digits separately.  
# 6. Display all special characters separately. 

#Program for password strength analyzer
password = "Python@2026!"

upper=0
lower=0
digit=0
special=0

digits_list=[]
special_list=[]

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
        digits_list.append(ch)
    else:
        special += 1
        special_list.append(ch)

# Check password strength
if len(password)>=8 and upper>=1 and lower>=1 and digit>=1 and special>=1:
    strength="Strong"

elif len(password)>=8 and (upper>=1 or lower>=1) and digit>=1:
    strength ="Medium"

else:
    strength="Weak"

# Display results
print("Password:",password)
print("Uppercase Letters:",upper)
print("Lowercase Letters:",lower)
print("Digits:",digit)
print("Special Characters:",special)
print("Digits Present:",digits_list)
print("Special Characters Present:",special_list)
print("Password Strength:",strength)


'''OUTPUT
Password: Python@2026!
Uppercase Letters: 1
Lowercase Letters: 5
Digits: 4
Special Characters: 1
Digits Present: ['2', '0', '2', '6']
Special Characters Present: ['@']
Password Strength: Strong

'''