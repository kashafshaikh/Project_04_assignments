import random

def generate_password():
    # Defining character sets
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!@#$%^&*()"
    all_chars = uppercase_letters + lowercase_letters + digits + symbols

    # Input validation for amount
    while True:
        try:
            amount = int(input("Amount of passwords to generate: ").strip())
            if amount > 0:
                break
            else:
                print("⛔ Please enter a positive number!")
        except ValueError:
            print("❌ Invalid input! Enter a valid number.")

    # Input validation for length
    while True:
        try:
            length = int(input("Length of password: ").strip())
            if length >= 4:  # Ensuring minimum length for strong passwords
                break
            else:
                print("⛔ Password length should be at least 4!")
        except ValueError:
            print("❌ Invalid input! Enter a valid number.")

    print("\nHere are your passwords:")

    for _ in range(amount):
        # Ensuring password contains at least one from each category
        password = (
            random.choice(uppercase_letters) +
            random.choice(lowercase_letters) +
            random.choice(digits) +
            random.choice(symbols)
        )
        # Filling remaining characters randomly
        password += "".join(random.choice(all_chars) for _ in range(length - 4))
        
        # Shuffling to avoid predictable patterns
        password = ''.join(random.sample(password, len(password)))
        print(password)

generate_password()
