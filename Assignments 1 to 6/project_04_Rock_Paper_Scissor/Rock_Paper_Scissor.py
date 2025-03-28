# Description: A simple Rock, Paper, Scissors game in Python

import random  # Importing random module to make computer's choice random

# Possible choices for the game
choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors Game! 🎮")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to stop the game.\n")

# Loop to keep the game running until the user decides to quit
while True:
    try:
        # Taking input from the user, removing spaces, and converting it to lowercase
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\nGame interrupted! Exiting...")
        break

    # If the user types 'quit', the game will end
    if user_choice == "quit":
        break

    # Checking if the user entered a valid choice
    if user_choice not in choices:
        print("❌ Invalid choice, try again!\n")
        continue  # Go back to the beginning of the loop to take input again

    # Computer randomly selects a choice
    computer_choice = random.choice(choices)
    print(f"💻 Computer chose: {computer_choice}")

    # Checking if it's a tie
    if user_choice == computer_choice:
        print("🤝 It's a tie!\n")

    # Checking winning conditions for the user
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You win!\n")  # User wins in these cases

    # If it's not a tie and user doesn't win, computer wins
    else:
        print("💻 Computer wins!\n")  # Computer wins in remaining cases

# Message displayed when the game ends
print("\nThanks for playing! 😊")

