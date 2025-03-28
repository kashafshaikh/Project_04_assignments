# Title: Guess My Number
# Description: A simple number guessing game where the user has to guess a number between 1 and 99.

import random  # Import random module to generate a random number

def main():
    secret_number = random.randint(1, 99)  # Generate a secret number between 1 and 99

    # Instructions for the player
    print("I am thinking of a number between 1 and 99...")
    print("Type 'c' to exit anytime.")
    print("Type 'hint' if you want a hint!\n")

    guess_count = 0  # Keep track of number of guesses
    first_try = True  # Flag to check if it's the first guess

    while True:
        # Show different prompts: first guess vs. next guesses
        if first_try:
            user_input = input("Enter a guess: ").strip()  # First attempt prompt
            first_try = False  # After first input, flag becomes False
        else:
            user_input = input("Enter a new guess: ").strip()  # Subsequent attempts prompt

        # Check if user wants to exit
        if user_input.lower() == 'c' or user_input == '':
            print("\nGame exited by user. The secret number was:", secret_number)
            print(f"You tried {guess_count} times.")
            break

        # Check if user asked for a hint
        if user_input.lower() == 'hint':
            # Provide hint if number is above or below 50
            if secret_number > 50:
                print("Hint: The secret number is greater than 50!\n")
            else:
                print("Hint: The secret number is less than or equal to 50!\n")
            continue  # Skip to next iteration after giving hint

        try:
            guess = int(user_input)  # Convert user input to integer
            guess_count += 1  # Increment guess count after valid number

            # Validate range of guess
            if guess < 1 or guess > 99:
                print("Please enter a number between 1 and 99.\n")
                continue

            # Compare guess with the secret number and respond
            if guess < secret_number:
                print("Your guess is too low.\n")
            elif guess > secret_number:
                print("Your guess is too high.\n")
            else:
                # Correct guess message
                print(f"🎉 Congrats! The number was: {secret_number}")
                print(f"You guessed it in {guess_count} tries! 🎯")
                break  # Exit loop when guessed correctly

        except ValueError:
            # Handle invalid input that is not a number, 'hint' or 'c'
            print("Invalid input! Please enter a number, 'hint' or 'c' to exit.\n")

# Run the main function when the script is executed
if __name__ == '__main__':
    main()


