# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

# The first even number is 0:

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

def main():
    for i in range(20):  # i will go from 0 to 19
        print(i * 2)     # multiply each i by 2 and print it

if __name__ == "__main__":
    main()
