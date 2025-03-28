# Constant affirmation string that user has to type exactly
AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    # Display the message asking the user to type the affirmation
    print("Please type the following affirmation: " + AFFIRMATION)

    # Take user input and remove extra spaces from start and end
    user_feedback = input().strip()  

    # Loop continues until user types the affirmation exactly
    while user_feedback != AFFIRMATION:
        # Inform user they typed incorrectly
        print("That was not the affirmation.")
        
        # Prompt user again to type the affirmation
        print("Please type the following affirmation: " + AFFIRMATION)
        
        # Take new input and strip spaces
        user_feedback = input().strip()  

    # If user types it correctly, show success message
    print("That's right! :)")

# Calls the main function when the file is run
if __name__ == '__main__':
    main()