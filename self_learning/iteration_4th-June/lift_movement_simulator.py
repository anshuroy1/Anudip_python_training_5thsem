# ---------------------------------------------------------
# Program: Lift Movement Simulation
#
# Lift starts from floor 0.
#
# User enters destination floors repeatedly.
# Stop when user enters -1.
#
# Display:
# 1. Floors travelled in each trip
# 2. Total floors travelled
# ---------------------------------------------------------


current_floor = 0
total_travelled = 0

while True:

    destination = int(input("Enter Destination Floor (-1 to stop): "))

    if destination == -1:
        break

    travelled = abs(destination - current_floor)

    print("Travelled:", travelled, "floors")

    total_travelled += travelled

    current_floor = destination

print("Total Travelled:", total_travelled, "floors")