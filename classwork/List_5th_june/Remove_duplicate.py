# program to remove duplicate enteries of given numbers
# Create an empty list to store numbers
numbers = []
print("enter any 20 numbers:")
# Input 20 numbers
for x in range(20):
    num = int(input())
#append into list

    numbers.append(num)
    print("..........")
element = int(input("enter any number to remove its duplicate:"))
#......
#finding the frequency of given number
frequency = numbers.count(element)
if frequency == 0:
    print("element not found")
elif frequency == 1:
    print("no duplicates found")
else:
    #reversing the list
    numbers.reverse()
    for i in range(1, frequency):
        numbers.remove(element)
#reversing the list again
numbers.reverse()
print("After removing duplicates")
print(numbers)