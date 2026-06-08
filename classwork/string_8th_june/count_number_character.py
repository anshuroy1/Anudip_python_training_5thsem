#wap to input a sentence from user and count the number of characters in it.without using len() function.
sentance = input("Enter the sentance: ")
count = 0
for i in sentance:
    count = count + 1
print("Number of characters in the sentance : ", count)