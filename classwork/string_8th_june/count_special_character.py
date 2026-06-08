
#count the number of special characters in the sentance.
sentance = input("Enter the sentance: ")
special_char = 0
for i in sentance:
    if not i.isalnum() :
        special_char += 1       
print("Number of special characters in the sentance : ", special_char)