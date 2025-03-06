import random
import string

def generate_password(length, use_digits, use_special):
    """Generates a random password."""
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    
    if use_special:
        characters += string.punctuation
    
    return "".join(random.choice(characters) for _ in range(length))

def main():
    """Main function to generate and display the password."""
    print("Password Generator")
    print("-" * 20)

    try:
        length = int(input("Enter password length (minimum 6): "))
        if length < 6:
            print("Password length must be at least 6.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_digits, use_special)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()