# Tasks
# • Display stops having more than 20 passengers.
# • Count stops with fewer than 10 passengers.
# • Find the busiest stop.
# • Create a list of stops requiring an extra bus (passengers > 25).
# • Calculate the average number of passengers.

# Bus Route Passenger Analysis

passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# Stops having more than 20 passengers
print("Stops Having More Than 20 Passengers:")

for stop, count in passengers.items():
    if count > 20:
        print(stop, ":", count)

# Count stops with fewer than 10 passengers
low_count = 0

for count in passengers.values():
    if count < 10:
        low_count += 1

print("\nStops With Fewer Than 10 Passengers:", low_count)

# Busiest stop
busy_stop = ""
max_passengers = 0

for stop, count in passengers.items():
    if count > max_passengers:
        max_passengers = count
        busy_stop = stop

print("\nBusiest Stop:", busy_stop)

# Stops requiring extra bus
extra_bus = []

for stop, count in passengers.items():
    if count > 25:
        extra_bus.append(stop)

print("\nStops Requiring Extra Bus:")
print(extra_bus)

# Average passengers
total = 0

for count in passengers.values():
    total += count

average = total / len(passengers)

print("\nAverage Passengers:", average)