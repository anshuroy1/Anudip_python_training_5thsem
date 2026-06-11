
# A railway reservation system stores the booking status of seats in a train coach. 
# Sample Data 
# seats = { 
#     1: "Booked", 
#     2: "Available", 
#     3: "Booked", 
#     4: "Available", 
#     5: "Booked", 
#     6: "Booked", 
#     7: "Available", 
#     8: "Booked", 
#     9: "Available", 
#     10: "Booked" 
# } 
# Tasks 
# 1. Display all available seat numbers.  
# 2. Count booked and available seats.  
# 3. Reserve the first available seat.  
# 4. Cancel booking for a given seat number.  
# 5. Store the updated reservation status in reservations.txt. 
 # 6Display occupancy percentage.  


seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
}

# 1 Display all available seat numbers
available_seats = []
# for count available seats
for seat_num, status in seats.items():
    if status == "Available":
        available_seats.append(seat_num)
print("Available seat numbers:", available_seats)


# 2 count booked and available seats
booked_seats = 0
available_seats = 0
for status in seats.values():
    if status == "Booked":
        booked_seats += 1
    else:
        available_seats += 1
print("Booked seats:", booked_seats)
print("Available seats:", available_seats)

# 3 reserve the first available seat
for seat_num, status in seats.items():
    if status == "Available":
        seats[seat_num] = "Booked"
        print("First available seat reserved:", seat_num)
        break

# 4 cancel booking for a given seat number
seat_to_cancel = int(input("Enter seat number to cancel: "))
seats[seat_to_cancel] = "Available"
print("Booking for seat", seat_to_cancel, "cancelled.")

# 5 store the updated reservation status in reservations.txt
with open("reservations.txt", "w") as file:
    for seat_num, status in seats.items():
        file.write(f"Seat {seat_num}: {status}\n")

print("Updated reservation status stored in reservations.txt")

 # 6 display occupancy percentage
total_seats = len(seats)
occupancy_percentage = (booked_seats / total_seats) * 100
print("Occupancy percentage:", occupancy_percentage, "%")
