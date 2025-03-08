import sys
print(sys.path)
import random
import string

def generate_password(length, num_letters, num_digits, num_specials):
    """
    Generates a secure password based on user-defined criteria.

    :param length: Total length of the password (min 8)
    :param num_letters: Number of letters in the password
    :param num_digits: Number of digits in the password
    :param num_specials: Number of special characters in the password
    :return: A randomly generated secure password as a string
    """

    # Validate input
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    if num_letters < 0 or num_digits < 0 or num_specials < 0:
        raise ValueError("Number of letters, digits, and special characters cannot be negative.")
    if num_letters + num_digits + num_specials > length:
        raise ValueError("Sum of letters, digits, and special characters exceeds total password length.")

    # Generate character pools
    letters = random.choices(string.ascii_letters, k=num_letters)
    digits = random.choices(string.digits, k=num_digits)
    specials = random.choices(string.punctuation, k=num_specials)

    # Fill remaining characters randomly
    remaining_chars = length - (num_letters + num_digits + num_specials)
    all_chars = string.ascii_letters + string.digits + string.punctuation
    extra_chars = random.choices(all_chars, k=remaining_chars)

    # Combine all characters
    password_chars = letters + digits + specials + extra_chars
    random.shuffle(password_chars)  # Shuffle for randomness

    return "".join(password_chars)

def get_user_input():
    """Collects user input for password parameters and returns them."""
    try:
        length = int(input("Enter total password length (min 8): "))
        num_letters = int(input("Enter number of letters: "))
        num_digits = int(input("Enter number of digits: "))
        num_specials = int(input("Enter number of special characters: "))

        return length, num_letters, num_digits, num_specials
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return get_user_input()

def main():
    """Main function to run the password generator."""
    print("🔐 Secure Password Generator 🔐")
    length, num_letters, num_digits, num_specials = get_user_input()

    try:
        password = generate_password(length, num_letters, num_digits, num_specials)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
