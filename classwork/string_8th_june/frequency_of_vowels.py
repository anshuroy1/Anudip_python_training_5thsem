#wap to find the frequency of vowels in a given sentance.ignoring case
sentance = input("Enter the sentance: ")
# to find the frequency of vowels in the sentance
sentance= sentance.lower() # to ignore case
vowels = "aeiou"
frequency = {}
for char in sentance:
    if char in vowels:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print("Frequency of vowels in the sentance : ", frequency)