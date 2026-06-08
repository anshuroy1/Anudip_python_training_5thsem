# Runs scored by players in a tournament: 
# runs = { 
#     "Virat": 645, 
#     "Rohit": 512, 
#     "Gill": 698, 
#     "Rahul": 435, 
#     "Hardik": 278, 
#     "Pant": 534, 
#     "Surya": 389, 
#     "Jadeja": 301, 
#     "Iyer": 455, 
#     "KL": 410 
# } 
# Tasks 
# 1. Display players scoring more than 500 runs.  
# 2. Find the Orange Cap winner.  
# 3. Find the lowest scorer.  
# 4. Calculate total runs scored.  
# 5. Create a list of players scoring below 400.  
# 6. Count players scoring between 400 and 600 runs. 

# creating a dictionary to store runs scored by players in a tournament
runs = {    
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
}   
#--------------------------------------------------
# to display players scoring more than 500 runs
print("Players scoring more than 500 runs : ")
for player, run in runs.items():
    if run > 500:
        print(player)
#--------------------------------------------------

# to find the Orange Cap winner
orange_cap_winner = ""  
highest_runs = 0
for player, run in runs.items():
    if run > highest_runs:
        highest_runs = run
        orange_cap_winner = player
print(f"Orange Cap winner : {orange_cap_winner} ({highest_runs} runs)")
#-------------------------------------------------- 

# to find the lowest scorer
lowest_scorer = ""
lowest_runs = 0
for player, run in runs.items():
    if lowest_runs == 0 or run < lowest_runs:
        lowest_runs = run
        lowest_scorer = player
print(f"Lowest scorer : {lowest_scorer} ({lowest_runs} runs)")

#--------------------------------------------------
# to calculate total runs scored
total_runs = 0
for run in runs.values():
    total_runs += run

print("Total runs scored : ", total_runs)
#--------------------------------------------------

# to create a list of players scoring below 400
players_below_400 = []              
for player, run in runs.items():
    if run < 400:
        players_below_400.append(player)
print("Players scoring below 400 runs : ", players_below_400)
#--------------------------------------------------

# to count players scoring between 400 and 600 runs
count = 0
for run in runs.values():
    if 400 <= run <= 600:
        count += 1
print("Number of players scoring between 400 and 600 runs : ", count)

'''
Output:
Players scoring more than 500 runs :
Virat
Rohit
Gill
Pant
Orange Cap winner : Gill (698 runs)
Lowest scorer : Hardik (278 runs)
Total runs scored :  4657
Players scoring below 400 runs :  ['Hardik', 'Surya', 'Jade
Number of players scoring between 400 and 600 runs :  5
'''

