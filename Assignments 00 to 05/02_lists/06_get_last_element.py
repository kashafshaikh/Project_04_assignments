# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst: list) -> None:

    # Print the last element using index
    print(lst[-1])  


def get_lst() -> list:
    
    lst: list = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)  # Add the entered element to the list
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst  # Return the complete list


def main() -> None:
   
    lst = get_lst()  # Get the list from user input
    get_last_element(lst)  # Print the last element from the list


# Run the main function when the program is executed
if __name__ == '__main__':
    main()

