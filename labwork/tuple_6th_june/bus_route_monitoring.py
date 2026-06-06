# Passenger count at each stop:
# passengers = [12, 18, 25, 30, 28, 15, 8]
# Write a program to:
# • Find the busiest stop. 
# • Display stops with fewer than 10 passengers. 
# • Calculate average passengers. 
# • Determine whether any stop exceeded 25 passengers.
# Passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Find the busiest stop
max_passengers = max(passengers)
busiest_stop = passengers.index(max_passengers) + 1

print("Busiest Stop:", busiest_stop)
print("Passengers at Busiest Stop:", max_passengers)

# Display stops with fewer than 10 passengers
print("Stops with fewer than 10 passengers:")
for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1)

# Calculate average passengers
average = sum(passengers) / len(passengers)
print("Average Passengers:", average)

# Determine whether any stop exceeded 25 passengers
found = False

for count in passengers:
    if count > 25:
        found = True
        break

if found:
    print("Yes, a stop exceeded 25 passengers")
else:
    print("No stop exceeded 25 passengers")