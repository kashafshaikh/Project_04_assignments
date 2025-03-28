def main():
    # Dictionary containing fruit names and their prices
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0  # Initialize total cost
    
    # Loop through each fruit in the dictionary
    for fruit_name in fruits:
        price = fruits[fruit_name]  # Get the price of each fruit
        
        while True:  # Keep asking until a valid number is entered
            try:
                # Ask user how many they want to buy
                amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: ").strip())
                
                if amount_bought < 0:
                    print("Please enter a non-negative number.")
                    continue
                
                total_cost += (price * amount_bought)  # Add to total cost
                break  # Break out of loop if input is valid
            
            except ValueError:
                # If user input is not a valid integer, show error and ask again
                print("Invalid input! Please enter a valid number.")
    
    # Print the total cost
    print("Your total is $" + str(total_cost))


# Standard Python boilerplate to run the main function
if __name__ == '__main__':
    main()

