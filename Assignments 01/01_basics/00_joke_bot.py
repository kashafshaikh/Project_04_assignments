# Type: Python Script
# Description: A simple joke bot that tells a joke when asked for one


# Constants to store prompt, joke, and sorry message
PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY = "Sorry, I only tell jokes."

def main():
    try:
        # Get input from the user, remove extra spaces, and convert to lowercase
        user_input = input(PROMPT).strip().lower()

        # If the input is empty (user pressed enter without typing)
        if user_input == "":
            print("You didn't type anything! Please try again.")
        
        # If the input contains the word 'joke'
        elif "joke" in user_input:
            print(JOKE)

        # For any other input, show the sorry message
        else:
            print(SORRY)
    
    # Catch and display any unexpected errors
    except Exception as e:
        print(f"Oops! Something went wrong. Error: {e}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
