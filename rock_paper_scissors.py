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

def get_valid_player_choice():
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice in ['rock', 'paper', 'scissors']:
            return player_choice
        else:
            print("Invalid choice! Please try again.")

def play_game():
    # Second pass - handle input validation and player exit option
    while True:
        player_choice = get_valid_player_choice()
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
