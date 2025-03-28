
# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

def main() -> None:
    # Asking the user to type a number (can be decimal)
    num: float = float(input("Type a number to see its square: "))

    # Calculate the square by multiplying the number with itself or using ** 2
    square: float = num ** 2

    # Printing the result, convert both numbers to string while printing
    print(str(num) + " squared is " + str(square))


# This part makes sure main() runs when this file is executed
if __name__ == '__main__':
    main()
