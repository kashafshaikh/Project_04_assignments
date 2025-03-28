
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C

# **03_fahrenheit_to_celsius.md**

def main() -> None:
    # Prompt user for temperature in Fahrenheit
    fahrenheit_temp: float = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius using the given formula
    celsius_temp: float = (fahrenheit_temp - 32) * 5.0 / 9.0

    # Print the result with proper formatting
    print("Temperature: " + str(fahrenheit_temp) + "F = " + str(celsius_temp) + "C")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
