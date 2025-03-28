def get_user_numbers():
    """
    Get numbers from the user until they press enter without typing anything.
    Store all valid numbers (integers or decimals) in a list and return that list.
    If the user enters invalid input, show a message and ask again.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        if user_input == "":
            break  # Stop if user presses enter without typing anything
        
        try:
            # Try to convert input to float (yeh decimal bhi allow karega)
            num = float(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Invalid input! Please enter a valid number only.")
    
    return user_numbers

def count_nums(num_lst):
    """
    Count how many times each number appears in the list.
    Store the counts in a dictionary.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict

def print_counts(num_dict):
    """
    Print each number and how many times it appeared.
    """
    for num in num_dict:
        count = num_dict[num]
        print(f"{num} appears {count} time{'s' if count > 1 else ''}.")

def main():
    """
    Call the functions to get user input, count the numbers, and print results.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()

