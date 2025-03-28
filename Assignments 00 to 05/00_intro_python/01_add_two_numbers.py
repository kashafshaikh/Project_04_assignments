
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# 1. Prompt the user to enter the first number.

# 2. Read the input and convert it to an integer.

# 3. Prompt the user to enter the second number.

# 4. Read the input and convert it to an integer.

# 5. Calculate the sum of the two numbers.

# 6. Print the total sum with an appropriate message.

def main() -> None:
    print("This program adds two numbers.")

    # Take first number input as string, convert to int
    num1: int = int(input("Enter first number: "))

    # Take second number input as string, convert to int
    num2: int = int(input("Enter second number: "))

    # Add both numbers
    total: int = num1 + num2

    # Print the result
    print("The total is " + str(total) + ".")


# This ensures main() runs only when this script is executed directly
if __name__ == '__main__':
    main()
