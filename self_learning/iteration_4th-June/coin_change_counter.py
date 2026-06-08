# ---------------------------------------------------------
# Program: Coin Change Counter
#
# Find minimum notes required using:
# 500, 200, 100, 50, 20, 10
# ---------------------------------------------------------

amount = int(input("Enter amount: "))

# Validate input
if amount <= 0:
        print("Amount must be greater than 0.")

else:

        # 500 Notes
        notes500 = amount // 500
        amount = amount % 500

        # 200 Notes
        notes200 = amount // 200
        amount = amount % 200

        # 100 Notes
        notes100 = amount // 100
        amount = amount % 100

        # 50 Notes
        notes50 = amount // 50
        amount = amount % 50

        # 20 Notes
        notes20 = amount // 20
        amount = amount % 20

        # 10 Notes
        notes10 = amount // 10
        amount = amount % 10

        # Display Notes
        if notes500 > 0:
            print("500 x", notes500)

        if notes200 > 0:
            print("200 x", notes200)

        if notes100 > 0:
            print("100 x", notes100)

        if notes50 > 0:
            print("50 x", notes50)

        if notes20 > 0:
            print("20 x", notes20)

        if notes10 > 0:
            print("10 x", notes10)

        # Remaining amount
        if amount > 0:
            print("Remaining Amount:", amount)