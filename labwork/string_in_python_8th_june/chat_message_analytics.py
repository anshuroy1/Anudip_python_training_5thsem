# A chat application stores a message: 
# Python is awesome and Python is easy to learn 
# Tasks 
# Write a program to: 
# 1. Count total characters.  
# 2. Count total words.  
# 3. Find the longest word.  
# 4. Find the shortest word.  
# 5. Count how many times the word "Python" appears.  
# 6. Create a list of words having more than 4 characters.  
# 7. Display all words starting with a vowel.  
# 8. Count the number of vowels and consonants. 

#Program for chat  message analytics
message="Python is awesome and Python is easy to learn"

#TASK 1. Count total characters
char_count=len(message)

#TASK 2. Count total words
words=message.split()
word_count=len(words)

#TASK 3. Find longest word
longest=words[0]

for word in words:
    if len(word)>len(longest):
        longest=word

#TASK 4. Find shortest word
shortest=words[0]

for word in words:
    if len(word)<len(shortest):
        shortest=word

#TASK 5. Count occurrences of Python
python_count=0

for word in words:
    if word=="Python":
        python_count+=1

#TASK 6. List of words having more than 4 characters
more_than_4=[]

for word in words:
    if len(word)>4:
        more_than_4.append(word)

#TASK 7. Display words starting with a vowel
vowel_words=[]

for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

#TASK 8. Count vowels and consonants
vowels=0
consonants=0

for ch in message:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1

# Display Results
print("Message:", message)
print("Total Characters:", char_count)
print("Total Words:", word_count)
print("Longest Word:", longest)
print("Shortest Word:", shortest)
print("Python Appears:", python_count, "times")
print("Words with more than 4 characters:", more_than_4)
print("Words starting with vowels:", vowel_words)
print("Vowels:", vowels)
print("Consonants:", consonants)

'''OUTPUT
Message: Python is awesome and Python is easy to learn
Total Characters: 45
Total Words: 9
Longest Word: awesome
Shortest Word: is       
Python Appears: 2 times
Words with more than 4 characters: ['Python', 'awesome', 'Python', 'learn']
Words starting with vowels: ['is', 'awesome', 'and', 'is', 'easy']

vowels = 14
consonants = 23
'''