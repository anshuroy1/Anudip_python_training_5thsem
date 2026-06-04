#write a program to validate the pin
valid_pin="1234"
attempt=0
while(True):
# tracking input from user

 pin = input("enter pin:")

#validate the pin
 if(pin==valid_pin):
    print("access granted")
    break
 else:
 # checking the pin is four digit or not
 
  if(len(pin)!= 4):
    print("pin is not acceptable")
    continue
  else:
    print("incorrectPIN:Try Again")
    attempt +=1

print("Total failed attempt:",attempt)