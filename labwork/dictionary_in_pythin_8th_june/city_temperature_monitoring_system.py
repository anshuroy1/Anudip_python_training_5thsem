# Problem Statement 
# Daily temperatures of different cities are stored as: 
# temperature = { 
#     "Delhi": 41, 
#     "Mumbai": 33, 
#     "Chennai": 37, 
#     "Kolkata": 39, 
#     "Bengaluru": 28, 
#     "Pune": 30, 
#     "Jaipur": 42, 
#     "Lucknow": 40, 
#     "Hyderabad": 35, 
#     "Ahmedabad": 43 
# } 
# Tasks 
# 1. Display cities having temperature above 40°C.  
# 2. Find the hottest city.  
# 3. Find the coolest city.  
# 4. Calculate average temperature.  
# 5. Create a list of pleasant cities (temperature < 35°C).  
# 6. Count cities with temperature between 35°C and 40°C. 
#
# creating a dictionary to store daily temperatures of different cities
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}
#--------------------------------------------------

# to display cities having temperature above 40°C
print("Cities having temperature above 40°C : ")
for city, temp in temperature.items():
    if temp > 40:
        print(city)
#--------------------------------------------------

# to find the hottest city
hottest_city = ""
highest_temp = 0
for city, temp in temperature.items():
    if temp > highest_temp:
        highest_temp = temp
        hottest_city = city
print(f"Hottest city :  {hottest_city} ({highest_temp}°C)")
#--------------------------------------------------


# to find the coolest city
coolest_city = ""
lowest_temp = 0
for city, temp in temperature.items():
    if lowest_temp == 0 or temp < lowest_temp:
        lowest_temp = temp
        coolest_city = city
print(f"Coolest city : {coolest_city} ({lowest_temp}°C)")
#--------------------------------------------------


# to calculate average temperature
total_temp = 0
for temp in temperature.values():
    total_temp += temp  
average_temp = total_temp / len(temperature)
print("Average temperature : ", average_temp)
#--------------------------------------------------

# to create a list of pleasant cities (temperature < 35°C)
pleasant_cities = []
for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)
print("Pleasant cities (temperature < 35°C) : ", pleasant_cities)
#--------------------------------------------------

# to count cities with temperature between 35°C and 40°C
count = 0
for temp in temperature.values():
    if 35 <= temp <= 40:
        count += 1
print("Number of cities with temperature between 35°C and 40°C : ", count)

'''
Output:
Cities having temperature above 40°C :
Delhi
Jaipur
Ahmedabad

Hottest city :  Ahmedabad (43°C)
Coolest city :  Bengaluru (28°C)
Average temperature :  36.8
Pleasant cities (temperature < 35°C) :  ['Mumbai', 'Bengaluru', 'Pune']

Number of cities with temperature between 35°C and 40°C :  4
'''
