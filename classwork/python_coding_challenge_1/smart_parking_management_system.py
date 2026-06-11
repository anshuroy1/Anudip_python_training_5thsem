# The parking status of vehicles in a mall is maintained as follows. 
# Sample Data 
# parking_slots = [ 
#     "Occupied", "Vacant", "Occupied", "Vacant", 
#     "Occupied", "Occupied", "Vacant", "Occupied", 
#     "Vacant", "Occupied" 
# ] 
# Tasks 
# 1. Display vacant parking slot numbers.  
# 2. Count occupied and vacant slots.  
# 3. Allocate the first vacant slot to a new vehicle.  
# 4. Calculate parking occupancy percentage.  
# 5. Store updated parking information in parking.txt. 

parking_slots = ["Occupied", "Vacant", "Occupied", "Vacant", "Occupied", "Occupied", "Vacant", "Occupied", "Vacant", "Occupied"]

# 1. Display vacant parking slot numbers
print("Vacant Parking Slot Numbers:")
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        print("Vacant slot number:", i + 1)

# 2. Count occupied and vacant slots
occupied_slots = 0
vacant_slots = 0
for slot in parking_slots:
    if slot == "Occupied":
        occupied_slots += 1
    elif slot == "Vacant":
        vacant_slots += 1

print("Number of occupied slots:", occupied_slots)
print("Number of vacant slots:", vacant_slots)

# 3. Allocate the first vacant slot to a new vehicle
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        print("First vacant slot allocated to a new vehicle:", i + 1)
        break

# 4. Calculate parking occupancy percentage
occupied = 0 

for i in range(len(parking_slots)):
    if parking_slots[i] == "Occupied":
        occupied += 1

occupancy_percentage = (occupied / len(parking_slots)) * 100
print("Parking occupancy percentage:", occupancy_percentage, "%")

# 5. Store updated parking information in parking.txt



print("parking information stored in parking.txt")