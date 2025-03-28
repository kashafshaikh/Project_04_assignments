# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

def main():
    lst = []  # Create an empty list to store values

    val = input("Enter a value: ")  # Ask the user to enter the first value

    # Keep asking for values until the user presses Enter without typing anything
    while val:
        lst.append(val)  # Add the entered value to the list
        val = input("Enter a value: ")  # Ask for the next value

    # Once the user presses Enter without typing, print the entire list
    print("Here's the list:", lst)


# This part makes sure the main function runs when the file is executed
if __name__ == '__main__':
    main()
