import random
# defining roll function
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll
# validating number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players")
            # for integer input outside of 2-4
    else:
        print("Invalid input. Please enter the number of players 2-4")
        # for non-integer input

max_score = 50
player_scores = [0 for _ in range(players)]
# print(player_scores) shows [0, 0, 0, 0] for 4 players

while max(player_scores) < max_score:

    # for loop for each player's turn (separate from total score)
    for player_idx in range(players):
        print("\nPlayer ", player_idx + 1, "'s turn has just started!")
        print("Your total score is: ", player_scores[player_idx], "\n")
        current_score = 0
        # for while the player is selecting "y" to roll again or has not rolled a 1. Rolling a 1 or selecting "n" will end the turn.
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y": #converting input to lowercase and breaking if not "y"
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is: ", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("\n Player number", winning_idx + 1, " is the winner with a score of: ", max_score)