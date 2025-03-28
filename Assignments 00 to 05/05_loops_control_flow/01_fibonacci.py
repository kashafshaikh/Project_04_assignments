# Title: Print Fibonacci numbers up to 10,000
# Description: This program prints all terms in the Fibonacci sequence up to 10,000.

MAX_TERM_VALUE: int = 10000  # Maximum value till which we will print Fibonacci numbers

def main():
    curr_term = 0  # Starting from Fib(0)
    next_term = 1  # Starting next number Fib(1)

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)  # Print the current Fibonacci number
        
        # Calculate the next Fibonacci number by adding current and next terms
        term_after_next = curr_term + next_term
        
        # Update values: move forward in the sequence
        curr_term = next_term
        next_term = term_after_next


# Call the main function when this file is run
if __name__ == '__main__':
    main()
