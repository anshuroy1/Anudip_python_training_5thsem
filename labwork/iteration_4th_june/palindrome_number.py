num = int(input("Enter a number: ")) #taking input of a number

temp = num     #copying a number 
reverse = 0    #iniliasation of reverse

while temp > 0: 

    digit = temp % 10
    reverse = reverse * 10 + digit    #reverse the number 

    temp = temp // 10

print("Reverse =", reverse)

if num == reverse:         #checking whether the number is palindrome or not
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")