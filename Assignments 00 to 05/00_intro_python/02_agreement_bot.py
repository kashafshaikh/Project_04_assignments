
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!

def main() -> None:
    # Ask the user about their favorite animal
    favorite_animal: str = input("What's your favorite animal? ")

    # Respond with the same animal
    print(f"My favorite animal is also {favorite_animal}!")


# This ensures the main() function runs only when the file is executed directly
if __name__ == '__main__':
    main()
