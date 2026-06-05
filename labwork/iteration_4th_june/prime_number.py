n = int(input("Enter a number:"))
count = 0

print("Factors:", end=" ")

for i in range(1, (n//2) + 1):
    if n % i == 0:
        print(i, end=" ")
        count += 1
print()
if count == 2:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")