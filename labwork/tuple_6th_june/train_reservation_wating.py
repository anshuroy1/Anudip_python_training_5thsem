# Passenger records:
# passengers = [
#  ("Anuj", "Confirmed"),
#  ("Rahul", "Waiting"),
#  ("Priya", "Confirmed"),
#  ("Amit", "Waiting"),
#  ("Neha", "Confirmed")
# ]
# Write a program to:
# • Display all waiting-list passengers. 
# • Count confirmed and waiting passengers. 
# • Find whether a specific passenger has a confirmed ticket. 
# • Create separate lists for confirmed and waiting passengers.
# Passenger records
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed_count = 0
waiting_count = 0
confirmed_list = []
waiting_list = []

# Display all waiting-list passengers
print("Waiting List Passengers:")
for name, status in passengers:
    if status == "Waiting":
        print(name)
        

# Count confirmed and waiting passengers
for name, status in passengers:
    if status == "Confirmed":
        confirmed_count += 1
    else:
        waiting_count += 1

print("Confirmed Passengers =", confirmed_count)
print("Waiting Passengers =", waiting_count)

# Find whether a specific passenger has a confirmed ticket
search_name = "Priya"

for name, status in passengers:
    if name == search_name:
        if status == "Confirmed":
            print(search_name, "has a Confirmed Ticket")
        else:
            print(search_name, "is in Waiting List")

# Create separate lists for confirmed and waiting passengers
for name, status in passengers:
    if status == "Confirmed":
        confirmed_list.append(name)
    else:
        waiting_list.append(name)

print("Confirmed List =", confirmed_list)
print("Waiting List =", waiting_list)