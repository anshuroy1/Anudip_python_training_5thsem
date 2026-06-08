# • Display players who scored 50 or more runs.
# • Count the number of centuries.
# • Find the player with the highest score.
# • Create a list of players scoring below 30 runs.
# • Determine how many players scored between 50 and 99.

# Cricket Scoreboard Analysis

scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Players scoring 50 or more
print("Players scoring 50 or more:")

for player, runs in scores.items():
    if runs >= 50:
        print(player, ":", runs)

# Count centuries
centuries = 0

for runs in scores.values():
    if runs >= 100:
        centuries += 1

print("\nNumber of Centuries:", centuries)

# Highest scorer
highest_player = ""
highest_score = 0

for player, runs in scores.items():
    if runs > highest_score:
        highest_score = runs
        highest_player = player

print("\nHighest Scorer:", highest_player)
print("Runs:", highest_score)

# Players scoring below 30
below_30 = []

for player, runs in scores.items():
    if runs < 30:
        below_30.append(player)

print("\nPlayers Scoring Below 30:")
print(below_30)

# Players scoring between 50 and 99
count = 0

for runs in scores.values():
    if runs >= 50 and runs <= 99:
        count += 1

print("\nPlayers Scoring Between 50 and 99:", count)