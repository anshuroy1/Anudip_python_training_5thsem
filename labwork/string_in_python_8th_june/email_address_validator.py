# Problem Statement 
# A user enters an email address: 
# rahul.sharma2026@gmail.com 
# Tasks 
# Write a program to: 
# 1. Extract username.  
# 2. Extract domain name.  
# 3. Extract extension.  
# 4. Count digits present in username.  
# 5. Count special characters.  
# 6. Check whether:  
# o Exactly one '@' exists.  
# o At least one '.' exists after '@'.  
# 7. Display Valid Email or Invalid Email.

#Program for email address validator
email = "rahul.sharma2026@gmail.com"

#TASK 1. Extract username
parts = email.split("@")
username = parts[0]

#TASK 2. Extract domain name
domain_parts=parts[1].split(".")
domain=domain_parts[0]

#TASK 3. Extract extension
extension=domain_parts[1]

#TASK 4. Count digits in username
digit_count=0

for ch in username:
    if ch.isdigit():
        digit_count+=1

#TASK 5. Count special characters
special_count=0

for ch in email:
    if ch.isalpha()==False and ch.isdigit()==False:
        special_count+=1

#TASK 6. Validate Email
valid=False

if email.count("@")==1:
    at_pos=email.index("@")

    if "." in email[at_pos:]:
        valid = True

# Display Results
print("Email:", email)
print("Username:", username)
print("Domain Name:", domain)
print("Extension:", extension)
print("Digits in Username:", digit_count)
print("Special Characters:", special_count)

if valid==True:
    print("Valid Email")
else:
    print("Invalid Email")