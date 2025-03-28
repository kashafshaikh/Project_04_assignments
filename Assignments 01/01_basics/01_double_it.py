# Title: Double It
# Description: This program takes a number from the user and doubles it until the number is greater than or equal to 100.

def main():
    while True:  # Keep asking until a valid number is given
        try:
            # Take input from user and convert to integer
            curr_value = int(input("Enter a number: "))
            print()  # Print a newline for better readability
            break  # If successful, break out of the loop
        except ValueError:
            # If input is not a number, show message and ask again
            print("Please enter a valid number!\n")

    # Print the starting number as well
    print(f"Starting from: {curr_value}\n")

    # Continue doubling until curr_value is less than 100
    while curr_value < 100:
        new_value = curr_value * 2   # Double the current value
        print(f"{curr_value} doubled is {new_value}\n")  # Print the result with newline
        curr_value = new_value       # Update curr_value

if __name__ == '__main__':
    main()