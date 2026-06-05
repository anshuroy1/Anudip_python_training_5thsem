player_score = []
#input of score from user
for i in range(11): 
    score = int(input("Enter the score of player {}:".format(i+1)))
    player_score.append(score)
#display the score of player
print("player scores")
print("score of 11 players:",player_score)
#finding highest score
max_score = player_score[0]
for index in range(1,len(player_score)):
    if player_score[index] > max_score:
        max_score = player_score[index]
print("The highest score is: ", max_score)