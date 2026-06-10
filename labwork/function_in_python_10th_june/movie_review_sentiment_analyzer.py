# roblem Statement 
# Movie reviews are stored as follows: 
# reviews = [ 
#     "excellent movie", 
#     "average story", 
#     "excellent acting", 
#     "poor direction", 
#     "excellent visuals", 
#     "poor screenplay", 
#     "good music", 
#     "excellent climax", 
#     "average performance", 
#     "good cinematography" 
# ] 
# Requirements 
# Create the following functions: 
# 1. count_sentiments(reviews) 
# Counts: 
# • Excellent  
# • Good  
# • Average  
# • Poor reviews  
# 2. most_common_word(reviews) 
# Returns the most frequently occurring word. 
# 3. longest_review(reviews) 
# Returns the review containing the maximum number of characters.
# 4. reviews_with_keyword(reviews, keyword) 


# Displays all reviews containing a given keyword
reviews = [ 
    "excellent movie", 
    "average story", 
    "excellent acting", 
    "poor direction", 
    "excellent visuals", 
    "poor screenplay", 
    "good music", 
    "excellent climax", 
    "average performance", 
    "good cinematography" 
] 
# creating a function to count sentiments
def count_sentiments(reviews):
    
        excellent = 0
        good = 0
        average = 0
        poor = 0
        for review in reviews:
            if "excellent" in review:
                excellent += 1
            elif "good" in review:
                good += 1
            elif "average" in review:
                average += 1
            elif "poor" in review:
                poor += 1
        
        return excellent, good, average, poor

# creating a function to find the most common word
def most_common_word(reviews):
    word_count = {}
    for review in reviews:
        words = review.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    most_common = max(word_count, key=word_count.get)
    return most_common

# creating a function to find the longest review
def longest_review(reviews):
    longest = ""
    for review in reviews:
        if len(review) > len(longest):
            longest = review
    return longest

# creating a function to find reviews with a given keyword
def reviews_with_keyword(reviews, keyword): 
    return [review for review in reviews if keyword in review]      

# Display Results
excellent, good, average, poor = count_sentiments(reviews)
print("Sentiments:")
print("Excellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Poor:", poor)
print("Most Common Word:", most_common_word(reviews))
print("Longest Review:", longest_review(reviews))
print("Reviews containing 'excellent':", reviews_with_keyword(reviews, "excellent"))