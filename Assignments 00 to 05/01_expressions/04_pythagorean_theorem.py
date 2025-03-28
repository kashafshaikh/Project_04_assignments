
# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

import math  # Import the math library to use the sqrt (square root) function

def main():
    # Ask the user to enter the length of side AB and convert input into float
    ab: float = float(input("Enter the length of AB: "))

    # Ask the user to enter the length of side AC and convert input into float
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse (BC) using the Pythagorean theorem formula:
    # BC = square root of (AB^2 + AC^2)
    bc: float = math.sqrt(ab**2 + ac**2)

    # Display the length of the hypotenuse
    print("The length of BC (the hypotenuse) is: " + str(bc))

# This line ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
