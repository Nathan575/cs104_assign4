import random

def greet_user():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")

def get_user_choice():
    return input("Enter your choice (rock, paper, or scissors): ").strip().lower()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])




def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"





def main():
    print("Welcome to the game!")

if __name__ == "__main__":
    main()
