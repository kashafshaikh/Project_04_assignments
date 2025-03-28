# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

def main() -> None:
    numbers: list[int] = [1, 2, 3, 4]  # List of numbers
    doubled_numbers: list[int] = [num * 2 for num in numbers]  # Double each element using list comprehension
    print("Doubled list is:", doubled_numbers)  # Print the doubled list

if __name__ == '__main__':
    main()

