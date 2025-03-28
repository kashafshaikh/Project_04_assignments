import random  # Import the random module

N_NUMBERS: int = 10  # How many random numbers to generate
MIN_VALUE: int = 1   # Minimum value for random number
MAX_VALUE: int = 100 # Maximum value for random number

def main():
    # Loop 10 times to print 10 random numbers
    for i in range(1, N_NUMBERS + 1):  
        value = random.randint(MIN_VALUE, MAX_VALUE)  # Generate random number
        print(f"Random number {i} = {value}")  # Print with numbering

if __name__ == '__main__':
    main()