# Problem Statement 
# A railway coach has seats represented as follows: 
# seats = [ 
#     "Booked", "Available", "Booked", "Booked", 
#     "Available", "Available", "Booked", "Available", 
#     "Booked", "Booked", "Available", "Booked" 
# ] 
# Requirements 
# Create the following functions: 
# 1. count_seats(seats) 
# Returns the number of booked and available seats. 
# 2. first_available(seats) 
# Returns the seat number of the first available seat. 
# 3. occupancy_percentage(seats) 
# Returns the percentage of occupied seats. 
# 4. display_available_seats(seats) 
# Displays all available seat numbers.

seats = ["Booked", "Available", "Booked", "Booked", "Available", "Available", "Booked", "Available", "Booked", "Booked", "Available", "Booked"]

#count_seats
def count_seats(seats):
    booked = 0
    available = 0
    for seat in seats:
        if seat == "Booked":
            booked += 1
        else:
            available += 1
    return booked, available

#first_available
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1
        
#occupancy_percentage
def occupancy_percentage(seats):
    booked, available = count_seats(seats)
    return (booked / (booked + available)) * 100

#display_available_seats
def display_available_seats(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1)

booked, available = count_seats(seats)
print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available(seats))
print("Occupancy:", occupancy_percentage(seats), "%")
print("Available Seat Numbers:")
display_available_seats(seats)