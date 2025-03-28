def main():
    # Ask the user to enter a year
    year = int(input('Please input a year: '))

    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If divisible by 4, check if it is divisible by 100
        if year % 100 == 0:
            # If divisible by 100, check if it is also divisible by 400
            if year % 400 == 0:
                print("That's a leap year!")  # If divisible by 400, it’s a leap year
            else:
                print("That's not a leap year.")  # Divisible by 100 but not by 400 means not a leap year
        else:
            print("That's a leap year!")  # Divisible by 4 but not by 100 means leap year
    else:
        print("That's not a leap year.")  # Not divisible by 4 means not a leap year

# Call the main function when the file is run
if __name__ == '__main__':
    main()


