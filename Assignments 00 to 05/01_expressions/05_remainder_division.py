
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

def main():
    # Ask user for the number to be divided (dividend)
    dividend: int = int(input("Please enter an integer to be divided: "))

    # Ask user for the number to divide by (divisor)
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Calculate the quotient (result of integer division)
    quotient: int = dividend // divisor

    # Calculate the remainder of the division
    remainder: int = dividend % divisor

    # Print the result in a readable way
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# Call main() function (this part runs the program)
if __name__ == '__main__':
    main()
