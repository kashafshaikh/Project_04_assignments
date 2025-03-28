# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

def get_first_element(lst: list) -> None:

    print(lst[0])  # Print the first element


def get_lst() -> list:
 
    lst: list = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")  # take first element
    while elem != "":  # loop until user presses enter
        lst.append(elem)  # add entered element to list
        elem = input("Please enter an element of the list or press enter to stop. ")  # ask for next element
    return lst  # return the full list


def main() -> None:
    
    lst = get_lst()  # Get list from user
    get_first_element(lst)  # Print first element of the list


# This part runs the main function when the program is executed
if __name__ == '__main__':
    main()
























