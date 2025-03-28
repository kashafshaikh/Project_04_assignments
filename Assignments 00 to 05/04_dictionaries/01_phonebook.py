# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_numbers():
    """
    Ask the user for names and phone numbers with validation.
    Store valid entries in a dictionary.
    """
    phonebook = {}

    while True:
        name = input("Enter name (leave blank to finish): ").strip()
        if name == "":
            break

        # Name validation using try-except
        try:
            if not name.isalpha():
                raise ValueError("Name must contain only alphabets.")
        except ValueError as e:
            print(f"Error: {e}")
            continue

        number = input("Enter number: ").strip()

        # Number validation using try-except
        try:
            if not number.isdigit() or len(number) != 11:
                raise ValueError("Number must be exactly 11 digits.")
        except ValueError as e:
            print(f"Error: {e}")
            continue

        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Print all names and numbers in the phonebook.
    """
    print("\n--- Phonebook Entries ---")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers by name.
    """
    print("\n--- Lookup Numbers ---")
    while True:
        name = input("Enter name to lookup (leave blank to stop): ").strip()
        if name == "":
            break

        try:
            if name not in phonebook:
                raise KeyError(f"{name} not found in the phonebook.")
            else:
                print(f"{name}'s number: {phonebook[name]}")
        except KeyError as e:
            print(f"Error: {e}")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


if __name__ == '__main__':
    main()
