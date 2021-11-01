#Players
player_1 = "Leo"
player_2 = "Pedro"

print("Game on!")
print(f"player 1: {player_1}")
print(f"player 2: {player_2}")
print("--------------------------") 

#Round
current_round = 1
print(f"Round {current_round}!")
player_1_score = 10
player_2_score = 13
print(f"{player_2} wins with {player_2_score} to {player_1_score}")
print("--------------------------") 

#Results
print(f"Round {current_round + 1}!")
player_1_score = 20
player_2_score = 5
print(f"{player_1} defeats {player_2} by {player_1_score - player_2_score} points")