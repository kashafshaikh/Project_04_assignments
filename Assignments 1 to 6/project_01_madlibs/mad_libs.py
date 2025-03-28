# Title: Coding Mad Libs CLI Game
# Description: A CLI-based game that creates a fun coding-related story based on user input.

def main():
    print("🎉 Welcome to the Coding Mad Libs Game! 🎉\nFill in the blanks to generate your coding story:\n")

    # Inputs from the user
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    language = input("Enter a programming language: ")
    noun = input("Enter a noun (related to tech): ")
    verb = input("Enter a verb: ")
    snack = input("Enter your favorite snack while coding: ")
    famous_dev = input("Enter a famous developer or tech personality: ")

    # Coding story madlib
    story = f"""
Late at night, in a {adj1} room filled with glowing screens, I sat down to code in {language}.
The {noun} on my desk blinked {adj2} as I tried to {verb} my bug-filled code.
Suddenly, I realized I hadn't eaten anything — so I grabbed my favorite snack, {snack}, and got back to work.
Just when I was about to give up, a video popped up on YouTube by {famous_dev}, saying:
"Don't quit! Every bug is a lesson."  
I took a deep breath, fixed the issue, and finally my code ran successfully.  
And that's how coding turned into my favorite {noun} adventure!
"""

    # Print story
    print("\n💻✨ Your Coding Mad Lib Story ✨💻")
    print(story)
    print("Keep coding and stay inspired! 🚀")

if __name__ == '__main__':
    main()



# Example Output

# 🎉 Welcome to the Coding Mad Libs Game! 🎉
# Fill in the blanks to generate your coding story:

# Enter an adjective: quiet
# Enter another adjective: blinking
# Enter a programming language: Python
# Enter a noun (related to tech): keyboard
# Enter a verb: debug
# Enter your favorite snack while coding: chips
# Enter a famous developer or tech personality: Linus Torvalds

# 💻✨ Your Coding Mad Lib Story ✨💻

# Late at night, in a quiet room filled with glowing screens, I sat down to code in Python.
# The keyboard on my desk blinked blinking as I tried to debug my bug-filled code.
# Suddenly, I realized I hadn't eaten anything — so I grabbed my favorite snack, chips, and got back to work.
# Just when I was about to give up, a video popped up on YouTube by Linus Torvalds, saying:
# "Don't quit! Every bug is a lesson."  
# I took a deep breath, fixed the issue, and finally my code ran successfully.  
# And that's how coding turned into my favorite keyboard adventure!

# Keep coding and stay inspired! 🚀
