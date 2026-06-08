# ---------------------------------------------------------
# Program: Race Leader Tracker
#
# Input lap times of racers and display:
# 1. Fastest racer position
# 2. Slowest racer position
# 3. Difference between fastest and slowest time
# ---------------------------------------------------------

# Input number of racers
n = int(input("Enter number of racers: "))

lap_times = []

# Input lap times
for i in range(n):
    time = float(input(f"Enter lap time of Racer {i + 1}: "))
    lap_times.append(time)

# Assume first racer is fastest and slowest
fastest = lap_times[0]
slowest = lap_times[0]

fastest_pos = 1
slowest_pos = 1

# Find fastest and slowest racers
for i in range(len(lap_times)):

    if lap_times[i] < fastest:
        fastest = lap_times[i]
        fastest_pos = i + 1

    if lap_times[i] > slowest:
        slowest = lap_times[i]
        slowest_pos = i + 1

# Calculate difference
difference = slowest - fastest

# Display results
print("Fastest Racer Position :", fastest_pos)
print("Slowest Racer Position :", slowest_pos)
print("Time Difference :", difference)