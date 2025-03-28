from hashlib import sha256  # We import sha256 to hash passwords

# Function to hash a password using sha256
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Function to check if login is successful
def login(email, stored_logins, password_to_check):
    """
    This function will:
    - Take the email and the password the user is trying to log in with
    - Hash that password
    - Compare it with the stored hash for that email
    - Return True if it matches, otherwise False
    """
    if email in stored_logins:  # Check if email exists in stored logins
        # Compare stored hash with the hash of given password
        return stored_logins[email] == hash_password(password_to_check)
    else:
        # Email not found
        return False

# Main function to run some test cases
def main():
    # Dictionary storing emails and their hashed passwords
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # karel
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # 123!456?789
    }
    
    # Test cases:
    print(login("example@gmail.com", stored_logins, "password"))  # Should print True
    print(login("example@gmail.com", stored_logins, "wrongpassword"))  # Should print False
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # Should print True
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # Should print False (case sensitive)
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # Should print True
    print(login("student@stanford.edu", stored_logins, "alpha"))  # Should print False

# This will call the main function when running the file
if __name__ == '__main__':
    main()
