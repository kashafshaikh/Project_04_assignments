
# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_many_numbers(numbers: list[int]) -> int:
    # Initialize a variable to keep track of the total sum
    total: int = 0
    # Loop through each number in the list and add it to the total
    for num in numbers:
        total = total + num
    # Return the final total
    return total

def main() -> None:
    # Create a simple list of numbers
    numbers: list[int] = [1, 2, 3, 4, 5]
    # Call the function to calculate the sum of numbers
    result: int = add_many_numbers(numbers)
    # Print the result
    print("The total sum of numbers is:", result)

if __name__ == '__main__':
    main()
