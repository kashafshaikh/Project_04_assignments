# Purpose: A simple number guessing game where the user thinks of a number between 1 and 100, and the computer tries to guess it.

import random  

print("🎮 Welcome to the 'Guess Your Number' Game! 🎮")
print("Think of a number between 1 and 100, and I will try to guess it! 😏")
print("Just tell me if my guess is (H)igh, (L)ow, or (C)orrect. 😉")
print("Let's get started!\n")

low = 1
high = 100
attempts = 0  

while True:
    try:
        guess = random.randint(low, high)
        attempts += 1
        print(f"🤔 My guess is: {guess}")

        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == 'h':
            high = guess - 1  
            print("😮 Oops! Too high. Let me try again!\n")
        elif feedback == 'l':
            low = guess + 1  
            print("😅 Too low! I'll increase my guess next time.\n")
        elif feedback == 'c':
            print(f"\n🎉 Yay! I guessed your number in {attempts} attempts! 🥳")
            print("I knew I could do it! 😎")
            break
        else:
            print("😕 Please enter a valid response (H, L, or C) only!\n")

    except ValueError:
        print("\n⚠️ Oops! It seems like your hints have confused me and made the range invalid.")
        print("Please restart the game and try giving correct feedback! 😊")
        break
    except Exception as e:
        print(f"\n⚠️ Unexpected error occurred: {e}")
        print("Please try again later.")
        break

print("\nThanks for playing! See you next time! 👋")

