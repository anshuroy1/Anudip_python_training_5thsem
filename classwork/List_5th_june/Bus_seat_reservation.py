# Bus seats
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

booked = 0
available = 0
available_seats = []

for i in range(len(seats)):
    if seats[i] == 1:
        booked += 1
    else:
        available += 1
        available_seats.append(i + 1)   # Seat number starts from 1

# First available seat
for i in range(len(seats)):
    if seats[i] == 0:
        first_available = i + 1
        break

# Occupancy percentage
occupancy = (booked / len(seats)) * 100

print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seats)
print("Bus Occupancy:", occupancy, "%")

if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")