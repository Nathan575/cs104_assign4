import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'player'
    else:
        return 'computer'

def play_game():
    # First pass - handling rematch for ties
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = get_computer_choice()

        print(f"Computer chose: {computer_choice}")
        winner = get_winner(player_choice, computer_choice)

        if winner == 'tie':
            print("It's a tie! Rematch!")
        else:
            print(f"{winner.capitalize()} wins!")
            break

# Start the game
play_game()
