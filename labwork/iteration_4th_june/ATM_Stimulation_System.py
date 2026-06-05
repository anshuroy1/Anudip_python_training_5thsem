# Initial account balance
balance = 10000

# Infinite loop to keep showing menu until user chooses Exit
while True:

    # Display ATM menu
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Take user's choice
    choice = int(input("Enter your choice: "))

    # Option 1: Check Balance
    if choice == 1:
        print("Current Balance =", balance)

    # Option 2: Deposit Money
    elif choice == 2:

        # Enter amount to deposit
        amount = float(input("Enter amount to deposit: "))

        # Add deposited amount to balance
        balance += amount

        print("Deposit Successful")
        print("Current Balance =", balance)

    # Option 3: Withdraw Money
    elif choice == 3:

        # Enter amount to withdraw
        amount = float(input("Enter amount to withdraw: "))

        # Check if sufficient balance is available
        if amount <= balance:

            # Deduct amount from balance
            balance -= amount

            print("Withdrawal Successful")
            print("Current Balance =", balance)

        else:
            # If withdrawal amount is greater than balance
            print("Insufficient Balance")

    # Option 4: Exit ATM
    elif choice == 4:
        print("Thank You for using ATM")

        # Terminate the loop
        break

    # Invalid choice handling
    else:
        print("Invalid Choice. Please select between 1 and 4.")