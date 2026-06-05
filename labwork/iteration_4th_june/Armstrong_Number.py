#input a number from user
n = int(input("enter a number: "))

#store original number
temp = n

#count the number of digits

digits = len(str(n))

#variable to store sum of powers
sum = 0

#calculate Armstrong sum
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10 
#check Armstrong or not
if sum == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not a Armstrong number")