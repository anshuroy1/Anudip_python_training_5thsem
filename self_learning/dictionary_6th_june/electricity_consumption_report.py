# • Display houses consuming more than 300 units.
# • Count houses consuming less than 200 units.
# • Find the house with the highest consumption.
# • Create a list of houses eligible for an energy-saving awareness campaign (consumption > 400 units).
# • Categorize houses as:
   # o Low: < 200 units
   # o Medium: 200–350 units
   # o High: > 350 units

# Electricity Consumption Report

units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# Houses consuming more than 300 units
print("Houses Consuming More Than 300 Units:")

for house, unit in units.items():

    if unit > 300:
        print(house, ":", unit)

# Count houses consuming less than 200 units
count = 0

for unit in units.values():

    if unit < 200:
        count += 1

print("\nHouses Consuming Less Than 200 Units:", count)

# Highest consumption
highest_house = ""
highest_units = 0

for house, unit in units.items():

    if unit > highest_units:
        highest_units = unit
        highest_house = house

print("\nHighest Consumption:")
print(highest_house, ":", highest_units)

# Houses for awareness campaign
campaign = []

for house, unit in units.items():

    if unit > 400:
        campaign.append(house)

print("\nEnergy Saving Awareness Campaign:")
print(campaign)

# Categorize houses
print("\nHouse Categories:")

for house, unit in units.items():

    if unit < 200:
        category = "Low"

    elif unit <= 350:
        category = "Medium"

    else:
        category = "High"

    print(house, ":", category)