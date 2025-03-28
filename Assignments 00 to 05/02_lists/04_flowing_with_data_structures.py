# This function takes a list and a string, and appends that string three times to the list
def add_three_copies(my_list: list, data: str) -> None:
    for i in range(3):
        my_list.append(data)

# Main function to get user input and display before/after results
def main() -> None:
    message: str = input("Enter a message to copy: ")  # Ask user for message
    my_list: list = []  # Create an empty list
    print("List before:", my_list)  # Show empty list
    add_three_copies(my_list, message)  # Call function to add three copies of message
    print("List after:", my_list)  # Show updated list

# Entry point of the program
if __name__ == "__main__":
    main()

