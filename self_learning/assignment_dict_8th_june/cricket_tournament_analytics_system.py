#  Cricket Tournament Analytics System
# Problem Statement
# Store statistics of at least 30 cricket players.
# Example Structure
# players = {
# "Virat": {
# "runs": 645,
# "matches": 12,
# "wickets": 0
# }
# }
# Requirements
# 1. Display all player statistics.
# 2. Find highest run scorer.
# 3. Find lowest run scorer.
# 4. Calculate average runs.
# 5. Find player with maximum wickets.
# 6. Find all-rounders (runs > 300 and wickets > 5).
# 7. Display players scoring above average.
# 8. Create categories:
# o Star Performer
# o Good Performer
# o Average Performer
# o Poor Performer
# 9. Generate team statistics.
# 10. Display top 5 batsmen.
# 11. Display top 5 bowlers.
# 12. Create a separate dictionary for award winners.


#-----------------------------------------
n=30     #minimum number of players


    #creating a dictionary
player={}

while True:
        
        #input name of the player
        name=input("Enter name of player : ")

        #validate player name
        if name in player:
            print("Player name already exists. Please enter a unique name.")
            continue

        elif not name.replace(" ","").isalpha():
            print("Invalid player name. Please enter a valid name.")
            continue

        runs=int(input("Enter runs of player : "))

        #validate runs
        if runs < 0:
            print("Invalid runs. Please enter a valid runs.")
            continue

        matches=int(input("Enter matches of player : "))

        #validate matches
        if matches < 0:
            print("Invalid matches. Please enter a valid matches.")
            continue

        wickets=int(input("Enter wickets of player : "))

        #validate wickets
        if wickets < 0:
            print("Invalid wickets. Please enter a valid wickets.")
            continue
        
        #store player statistics and structure of dictionary
        player[name] = {
            "runs" : runs,
            "matches" : matches,
            "wickets" : wickets
        }

         #check if number of students is equal to 30
        if len(player) < n:
             continue

        else:
        
          #ask user to continue or exit
          choice = input("Do you want to continue? (yes/no) : ")
          if choice.lower() != "yes":
            break


# 1. Display all player statistics.
print("\nAll player statistics:")
for name, stats in player.items():
    print(f"Name: {name}")
    print(f"Runs: {stats['runs']}")
    print(f"Matches: {stats['matches']}")
    print(f"Wickets: {stats['wickets']}")
    print("-----------------------------------------")


# 2. Find highest run scorer.
highest_run_scorer = (list(player.keys()))[0]
for name, stats in player.items():
    if stats["runs"] > player[highest_run_scorer]["runs"]:
        highest_run_scorer = name

print(f"\nHighest run scorer: {highest_run_scorer} with ({player[highest_run_scorer]['runs']} runs)")
print("-----------------------------------------")

# 3. Find lowest run scorer.
lowest_run_scorer = (list(player.keys()))[0]
for name, stats in player.items():
    if stats["runs"] < player[lowest_run_scorer]["runs"]:
        lowest_run_scorer = name

print(f"\nLowest run scorer: {lowest_run_scorer} with ({player[lowest_run_scorer]['runs']} runs)")
print("-----------------------------------------")

# 4. Calculate average runs.

total_runs = 0
for name, stats in player.items():
    total_runs += stats["runs"]

average_runs = total_runs / len(player)

print(f"\nAverage runs: {average_runs}")
print("-----------------------------------------")

# 5. Find player with maximum wickets.

#taking a variable maximum_wickets_taker that stores the name of the player with maximum wickets
maximum_wickets_taker = (list(player.keys()))[0]
for name, stats in player.items():
    if stats["wickets"] > player[maximum_wickets_taker]["wickets"]:
        maximum_wickets_taker = name

print(f"\nMaximum wickets taker: {maximum_wickets_taker} with ({player[maximum_wickets_taker]['wickets']} wickets)")
print("-----------------------------------------")

# 6. Find all-rounders (runs > 300 and wickets > 5).

all_rounders = []
for name, stats in player.items():
    if stats["runs"] > 300 and stats["wickets"] > 5:
        all_rounders.append(name)

print(f"\nAll-rounders: {all_rounders}")
print("-----------------------------------------")

# 7. Display players scoring above average.

players_above_average = []
for name, stats in player.items():
    if stats["runs"] > average_runs:
        players_above_average.append(name)

print(f"\nPlayers scoring above average: {players_above_average}")
print("-----------------------------------------")


# 8. Create categories:
# o Star Performer
# o Good Performer
# o Average Performer
# o Poor Performer

star_performer = []

good_performer = []

average_performer = []

poor_performer = []

for name, stats in player.items():
    if stats["runs"] > 200 or stats["wickets"] > 10:
        star_performer.append(name)
    elif stats["runs"] > 100 or stats["wickets"] > 5:
        good_performer.append(name)
    elif stats["runs"] > 50 or stats["wickets"] > 1:
        average_performer.append(name)
    else:
        poor_performer.append(name)

#displaying the categories
print(f"\nStar Performer: {star_performer}")
print(f"\nGood Performer: {good_performer}")
print(f"\nAverage Performer: {average_performer}")
print(f"\nPoor Performer: {poor_performer}")
print("-----------------------------------------")

#9. Generate team statistics.
# Total Players
# Total Runs
# Total Wickets
# Average Runs
# Highest Run Scorer
# Maximum Wickets Taker

print("\nTeam Statistics:")

#total players
print(f"Total players: {len(player)}")

total_runs = 0
total_wickets = 0
for name, stats in player.items():
    total_runs += stats["runs"]
    total_wickets += stats["wickets"]

#total runs
print(f"\nTotal runs: {total_runs}")

#total wickets
print(f"Total wickets: {total_wickets}")

#average runs
print(f"\nAverage runs: {average_runs}")

#highest run scorer
print(f"\nHighest run scorer: {highest_run_scorer}")

#maximum wickets taker
print(f"\nMaximum wickets taker: {maximum_wickets_taker}")

print("-----------------------------------------")

# 10. Display top 5 batsmen.
sorted_players = sorted(player.items(),key=lambda player_name:player_name[1]["runs"] ,reverse=True)

top_5_batsmen = sorted_players[:5]

for name, stats in top_5_batsmen:
    print(f"Name: {name}, Runs: {stats['runs']}")

print("-----------------------------------------")

# 11. Display top 5 bowlers.

sorted_players = sorted(player.items(),key=lambda player_name:player_name[1]["wickets"] ,reverse=True)

top_5_bowlers = sorted_players[:5]

for name, stats in top_5_bowlers:
    print(f"Name: {name}, Wickets: {stats['wickets']}")

print("-----------------------------------------")


# 12. Create a separate dictionary for award winners.

#for findding the best all_rounder

#validating the  best_all_rounder
if len(all_rounders) == 0:
    exit("No all-rounders found.")

best_all_rounder = all_rounders[0]
current_score = 0
best_score = 0

for name in all_rounders:
    
    current_score = (
        player[name]["runs"] +
        (player[name]["wickets"] * 10)
    )

    best_score = (
        player[best_all_rounder]["runs"] +
        (player[best_all_rounder]["wickets"] * 10)
    )

    if current_score > best_score:
        best_all_rounder = name

award_winners = {
    "highest_run_scorer": highest_run_scorer,
    "maximum_wickets_taker": maximum_wickets_taker,
    "best_all_rounder": best_all_rounder
}


print("\nAward Winners:")
for key, value in award_winners.items():
    print(f"{key}: {value}")