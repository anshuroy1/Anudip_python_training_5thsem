# Problem Statement 
# Monthly electricity consumption (units) is stored as: 
# units = { 
#     "House101": 320, 
#     "House102": 180, 
#     "House103": 510, 
#     "House104": 275, 
#     "House105": 150, 
#     "House106": 430, 
#     "House107": 220, 
#     "House108": 390, 
#     "House109": 145, 
#     "House110": 600 
# } 
# Tasks 
# 1. Display houses consuming more than 400 units.  
# 2. Find the highest-consuming house.  
# 3. Find the lowest-consuming house.  
# 4. Calculate total units consumed.  
# 5. Create lists:  
# o Low Consumption (< 200)  
# o Medium Consumption (200–400)  
# o High Consumption (> 400)  
# 6. Count houses eligible for an energy-saving campaign (consumption > 300). 

# creating a dictionary to store monthly electricity consumption (units) of different houses
units = {   
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
}   
#--------------------------------------------------

# to display houses consuming more than 400 units
print("Houses consuming more than 400 units : ")
for house, unit in units.items():
    if unit > 400:
        print(house)
#--------------------------------------------------

# to find the highest-consuming house
highest_house = ""
highest_unit = 0
for house, unit in units.items():
    if unit > highest_unit:
        highest_unit = unit
        highest_house = house
print(f"Highest-consuming house : {highest_house} ({highest_unit} units)")
#--------------------------------------------------

# to find the lowest-consuming house
lowest_house = ""   
lowest_unit = 0
for house, unit in units.items():
    if lowest_unit == 0 or unit < lowest_unit:
        lowest_unit = unit
        lowest_house = house
print(f"Lowest-consuming house : {lowest_house} ({lowest_unit} units)")
#--------------------------------------------------

# to calculate total units consumed
total_units = 0
for unit in units.values():
    total_units += unit
print("Total units consumed : ", total_units)
#--------------------------------------------------

# to create lists of low, medium, and high consumption
low_consumption = []
medium_consumption = []
high_consumption = []

for house, unit in units.items():
    if unit < 200:
        low_consumption.append(house)
    elif unit <= 400:
        medium_consumption.append(house)
    else:
        high_consumption.append(house)

print("Houses with low consumption (< 200 units):", low_consumption)
print("Houses with medium consumption (200-400 units):", medium_consumption)
print("Houses with high consumption (> 400 units):", high_consumption)
#--------------------------------------------------     


# to count houses eligible for energy-saving campaign (consumption > 300)
campaign_count = 0
for unit in units.values():
    if unit > 300:
        campaign_count += 1
print("Number of houses eligible for energy-saving campaign (consumption > 300 units) : ", campaign_count)




