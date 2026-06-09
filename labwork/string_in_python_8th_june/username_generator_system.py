# Problem Statement 
# A student enters: 
# Rahul Sharma 
# Tasks 
# Generate a username using the rules: 
# 1. Remove spaces.  
# 2. Convert to lowercase.  
# 3. Append current year (2026).  
# 4. If username length exceeds 12, keep only first 12 characters.  
# 5. Count vowels in the generated username.  
# 6. Count consonants.  
# 7. Display username statistics.  

#Program for username generator system
name = "Rahul Sharma"

#TASK 1. Remove spaces
username=name.replace(" ", "")

#TASK 2. Convert to lowercase
username=username.lower()

#TASK 3. Append current year
username=username+"2026"

#TASK 4. Keep only first 12 characters if length exceeds 12
if len(username)>12:
    username=username[:12]

#TASK 5 & 6. Count vowels and consonants
vowels=0
consonants=0

for ch in username:
    if ch.isalpha():
        if ch in "aeiou":
            vowels+=1
        else:
            consonants+=1

#TASK 7. Display username statistics
print("Original Name:", name)
print("Generated Username:", username)
print("Username Length:", len(username))
print("Vowels:", vowels)
print("Consonants:", consonants)