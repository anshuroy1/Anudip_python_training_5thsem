#taking input of secret number
secret_number=int(input("enter the secret number"))

attempt=0

while (True):

    #taking guess number from the user 

    guess_number=int(input("enter the number you guess"))

    #increment attempt whenever new guess number entered

    attempt+=1

    #checking if the number is same or not 
    if(secret_number==guess_number):
        print("correct guess")
        break

    #giving clue to the user whether it is high or low 
    
    if(guess_number<secret_number):
        print("too low")
    else:
        print("too high")