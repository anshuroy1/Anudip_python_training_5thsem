# Problem Statement 
# A customer submits a review: 
# This product is excellent excellent excellent and very useful 
# Tasks 
# Write a program to: 
# 1. Count total words.  
# 2. Create a dictionary containing word frequencies.  
# 3. Find the most frequently used word.  
# 4. Find all words appearing only once.  
# 5. Count words having more than 5 characters.  
# 6. Display words in reverse order.  
# 7. Create a list of unique words. 
#Program for product review analyzer
review="This product is excellent excellent excellent and very useful"

# Convert review into list of words
words=review.split()

#TASK 1. Count total words
total_words=len(words)

#TASK 2. Create dictionary of frequency of words
freq={}

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

#TASK 3. Find most frequently used word
most_word = ""
max_count = 0

for word in freq:
    if freq[word]>max_count:
        max_count=freq[word]
        most_word=word

#TASK 4. Find words appearing only once
once_words =[]
for word in freq:
    if freq[word] == 1:
        once_words.append(word)

#TASK 5. Count words having more than 5 characters
count_more_5=0

for word in words:
    if len(word)>5:
        count_more_5+=1

#TASK 6. Display words in reverse order
reverse_words=words[::-1]

#TASK 7. Create list of unique words
unique_words=[]

for word in words:
    if word not in unique_words:
        unique_words.append(word)

# Display Results
print("Review:", review)
print("Total Words:", total_words)
print("Word Frequencies:", freq)
print("Most Frequent Word:", most_word)
print("Words Appearing Once:", once_words)
print("Words with More Than 5 Characters:", count_more_5)
print("Words in Reverse Order:", reverse_words)
print("Unique Words:", unique_words)

'''OUTPUT
Review: This product is excellent excellent excellent and very useful
Total Words: 9
Word Frequencies: {'This': 1, 'product': 1, 'is': 1, 'excellent': 3, 'and': 1, 'very': 1, 'useful': 1}
Most Frequent Word: excellent
Words Appearing Once: ['This', 'product', 'is', 'and', 'very', 'useful']
Words with More Than 5 Characters: 3
Words in Reverse Order: ['useful', 'very', 'and', 'excellent', 'excellent', 'excellent', 'is', 'product', 'This']
Unique Words: ['This', 'product', 'is', 'excellent', 'and', 'very', 'useful']
    '''