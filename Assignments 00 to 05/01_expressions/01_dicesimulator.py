
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random  # Import random to simulate dice rolls

NUM_SIDES = 6  # Each die has 6 sides

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    Variables die1 and die2 here are local to this function.
    """
    die1: int = random.randint(1, NUM_SIDES)  # Roll first die
    die2: int = random.randint(1, NUM_SIDES)  # Roll second die
    total: int = die1 + die2  # Add both dice
    print("Total of two dice:", total)  # Print result

def main():
    # This die1 is local to main() function and has nothing to do with die1 in roll_dice()
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))  # Show that die1 starts at 10

    # Roll dice three times
    roll_dice()
    roll_dice()
    roll_dice()

    # After rolling dice, die1 in main() is still 10 because it was never changed
    print("die1 in main() is: " + str(die1))

# Required to call the main() function
if __name__ == '__main__':
    main()
