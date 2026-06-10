# Classwork : To read the data from file and display the following:
# 1. No. of Vowels in file.
# 2. No. of characters into the file.
# 3. No. of lines into the file.

f = open("classwork/file_handling_10th_june/sentence.txt", "r")
data = f.read()
print(data)
f.close()

# to find the number of vowels in the file
vowels = "aeiouAEIOU"
vowel_count = 0
for char in data:
    if char in vowels:
        vowel_count += 1
print("Number of vowels in the file : ", vowel_count)

# to find the number of characters in the file
char_count = 0
for char in data:
    char_count += 1
print("Number of characters in the file : ", char_count)

# to find the number of lines in the file
line_count = 0
for char in data:
    if char == "\n":
        line_count += 1
print("Number of lines in the file : ", line_count)

