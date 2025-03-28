# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

Minimum_height: int = 5  # Setting the minimum height required

def main():
    while True:  # Start an infinite loop to keep asking the user
        height_input = input("How tall are you in feet? (press enter to stop): ")  # Ask for user height

        if height_input == "":  # If the user presses enter without typing anything
            print("Program stopped. Bye!")  
            break  # Exit the loop and stop the program

        height = float(height_input)  # Convert the input string to a float number

        # Check conditions for height:
        if height >= Minimum_height and height <= 8:
            print("You're tall enough to ride!")  # If height is between 5 and 8 (inclusive), allowed to ride
        elif height > 8:
            print("Don't lie, buddy!!!")  # If height is more than 8, show a funny message
        else:
            print("You're not tall enough to ride, but maybe next year!")  # If height is less than 5, not allowed

if __name__ == '__main__':
    main()  # Call the main function
