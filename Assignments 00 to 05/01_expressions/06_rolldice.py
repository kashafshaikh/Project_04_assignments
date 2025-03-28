
# Simulate rolling two dice, and prints results of each roll as well as the total.


# Import random library to generate random numbers (simulate dice rolls)
import random

# This constant defines how many sides each die has (usually 6)
NUM_SIDES: int = 6

def main():
    # (Optional) You can use random.seed(1) here for predictable rolls when testing

    # Roll the first die — random number between 1 and 6
    die1: int = random.randint(1, NUM_SIDES)

    # Roll the second die — random number between 1 and 6
    die2: int = random.randint(1, NUM_SIDES)

    # Add both dice results to get total
    total: int = die1 + die2

    # Print the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# This part runs the main() function when the program is executed
if __name__ == '__main__':
    main()
