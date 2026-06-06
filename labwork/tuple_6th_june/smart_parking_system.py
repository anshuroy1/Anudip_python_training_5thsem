# Problem Statement
# Parking slots are represented as:
# slots = [1, 0, 1, 1, 0, 0, 1, 0]
# Where:
# • 1 = Occupied 
# • 0 = Available 
# Write a program to:
# • Count occupied and available slots.
# • Find the first available slot. 
# • Display all available slot numbers. 
# • Check whether parking occupancy exceeds 75%.
# Smart Parking System

slots = [1, 0, 1, 1, 0, 0, 1, 0]

# 1. Count occupied and available slots
occupied = 0
available = 0

for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied Slots:", occupied)
print("Available Slots:", available)

# 2. Find the first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        print("\nFirst Available Slot:", i)
        break

# 3. Display all available slot numbers
print("\nAvailable Slot Numbers:")

for i in range(len(slots)):
    if slots[i] == 0:
        print(i)

# 4. Check whether parking occupancy exceeds 75%
occupancy = (occupied / len(slots)) * 100

print("\nOccupancy Percentage:", occupancy)

if occupancy > 75:
    print("Parking Occupancy Exceeds 75%")
else:
    print("Parking Occupancy Does Not Exceed 75%")