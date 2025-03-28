# Description: A simple Hangman game implementation in Python with hints.

import random
from words import words_with_hints  # Import words dictionary from words.py

# Random word selection
word, hint = random.choice(list(words_with_hints.items()))  # Select word and hint
word = word.lower()  # Ensure lowercase for consistency
word_length = len(word)

# Game variables
guessed_letters = set()
lives = 8
hints_used = 0
display_word = ["_" for _ in word]

print("\n🎮 Welcome to Hangman! 🎮")
print(f"I have chosen a word. It has {word_length} letters.")
print(" ".join(display_word))  # Initial display

# Game loop
while lives > 0 and "_" in display_word:
    guess = input("\nGuess a letter or type 'hint' for a clue: ").lower().strip()

    # Handle hint request
    if guess == "hint":
        if hints_used == 0:  # Allow only one hint per game
            print(f"💡 Hint: {hint}")
            hints_used += 1
            lives -= 1  # Deduct one life for using a hint
            print(f"⚠️ You lost one life for using a hint! Lives left: {lives}")
        else:
            print("⚠️ You've already used your hint!")
        continue

    # Input validation
    if not guess:
        print("⚠️ Please enter a letter!")
        continue
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Invalid input! Enter a single letter (a-z).")
        continue
    if guess in guessed_letters:
        print(f"⚠️ You already guessed '{guess}'. Try another letter!")
        continue

    # Store guessed letter
    guessed_letters.add(guess)

    # Check if letter is in word
    if guess in word:
        print(f"✅ Good job! '{guess}' is in the word.")
        for index, letter in enumerate(word):
            if letter == guess:
                display_word[index] = guess
    else:
        lives -= 1
        print(f"❌ Wrong guess! '{guess}' is not in the word. {lives} lives left.")

    # Show updated word progress
    print(" ".join(display_word))

# Game result
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word correctly!")
else:
    print(f"\n😔 You lost! The word was: '{word}'")

print("Thanks for playing Hangman! 😊")
