import random
import string


def generate_password():

    # Get password length
    while True:
        try:
            length = int(input("\nEnter password length (minimum 8): "))

            if length >= 8:
                break
            else:
                print("Password length must be at least 8!")

        except ValueError:
            print("Please enter a valid number!")

    # Ask for character types
    print("\nChoose character types (yes/no):")

    uppercase = input("Include uppercase letters? ").lower()
    lowercase = input("Include lowercase letters? ").lower()
    numbers = input("Include numbers? ").lower()
    symbols = input("Include symbols? ").lower()

    # Store selected character types
    characters = []
    required_characters = []

    if uppercase == "yes":
        characters += string.ascii_uppercase
        required_characters.append(random.choice(string.ascii_uppercase))

    if lowercase == "yes":
        characters += string.ascii_lowercase
        required_characters.append(random.choice(string.ascii_lowercase))

    if numbers == "yes":
        characters += string.digits
        required_characters.append(random.choice(string.digits))

    if symbols == "yes":
        characters += string.punctuation
        required_characters.append(random.choice(string.punctuation))

    # Validate character selection
    if len(required_characters) < 2:
        print("\nPlease select at least two character types!")
        return

    # Generate remaining characters
    password = required_characters.copy()

    for i in range(length - len(password)):
        password.append(random.choice(characters))

    # Shuffle password
    random.shuffle(password)

    # Display password
    final_password = ''.join(password)

    print("\n================================")
    print("Your Generated Password:", final_password)
    print("================================")


# Main program
print("================================")
print("     RANDOM PASSWORD GENERATOR")
print("================================")

while True:

    generate_password()

    choice = input("\nGenerate another password? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using Password Generator!")
        break
    