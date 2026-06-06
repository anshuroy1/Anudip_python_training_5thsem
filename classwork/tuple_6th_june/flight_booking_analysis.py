# • Passenger ID 
# • Destination 
# • Booking Status

# Write a Python program to:
# 1. Display all passengers whose booking status is Confirmed. 
# 2. Count the number of passengers travelling to Delhi. 
# 3. Count Confirmed, Waiting, and Cancelled bookings separately. 
# 4. Create a list containing passenger IDs with Waiting status. 
# 5. Determine which destination has the highest number of bookings.

# Passenger records stored as tuples
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Display all confirmed passengers
print("Confirmed Passengers:")

for booking in bookings:
    if booking[2] == "Confirmed":
        print(booking[0], booking[1])

# 2. Count passengers travelling to Delhi
delhi_count = 0

for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count += 1

print("\nPassengers Travelling to Delhi:", delhi_count)

# 3. Count Confirmed, Waiting and Cancelled bookings
confirmed = 0
waiting = 0
cancelled = 0

for booking in bookings:
    if booking[2] == "Confirmed":
        confirmed += 1
    elif booking[2] == "Waiting":
        waiting += 1
    elif booking[2] == "Cancelled":
        cancelled += 1

print("\nConfirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

# 4. Create list of passenger IDs with Waiting status
waiting_list = []

for booking in bookings:
    if booking[2] == "Waiting":
        waiting_list.append(booking[0])

print("\nWaiting List:")
print(waiting_list)

# 5. Find destination with highest bookings
delhi = 0
mumbai = 0
chennai = 0

for booking in bookings:
    if booking[1] == "Delhi":
        delhi += 1
    elif booking[1] == "Mumbai":
        mumbai += 1
    elif booking[1] == "Chennai":
        chennai += 1

if delhi > mumbai and delhi > chennai:
    print("\nMost Booked Destination:")
    print("Delhi")
elif mumbai > delhi and mumbai > chennai:
    print("\nMost Booked Destination:")
    print("Mumbai")
else:
    print("\nMost Booked Destination:")
    print("Chennai")