
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Constant variable for conversion
INCHES_IN_FOOT: int = 12  # There are 12 inches in 1 foot

def main():
    # Ask the user to enter number of feet
    feet: float = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches: float = feet * INCHES_IN_FOOT

    # Display the result
    print("That is", inches, "inches!")

# This line ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
