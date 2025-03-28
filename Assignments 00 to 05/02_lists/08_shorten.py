# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

MAX_LENGTH : int = 3

def shorten(lst):
    # Keep removing items from the end of the list
    # until the list length is equal to or less than MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last element from the list
        print("Removed:", removed_item)  # Print the removed element

def get_lst():
    # Function to get user input and build a list
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)  # Add each entered element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst  # Return the final list

def main():
    user_list = get_lst()  # Get the list from user input
    print("Original list:", user_list)  # Print the original list

    shorten(user_list)  # Call shorten to remove extra elements

    print("Modified list:", user_list)  # Print the shortened list

if __name__ == "__main__":
    main()

