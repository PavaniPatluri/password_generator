"""
Password Generator using Python
-------------------------------
Generates strong, secure, and customizable random passwords.

Features:
- User-defined password length
- Option to include/exclude uppercase, digits, and symbols
- Option to exclude similar characters for clarity
- Clipboard copy support (if pyperclip installed)
"""

import string
import secrets

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True, exclude_similar=False):
    """Generate a random password based on selected options."""
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{};:,.<>?/"

    if exclude_similar:
        for ch in "Il1O0":
            characters = characters.replace(ch, "")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Password Generator")
    print("----------------------")

    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        exclude_similar = input("Exclude similar characters (Il1O0)? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_digits, use_symbols, exclude_similar)
        print("\n✅ Generated Password:", password)

        # Try to copy to clipboard (optional)
        try:
            import pyperclip
            pyperclip.copy(password)
            print("(Copied to clipboard!)")
        except ImportError:
            print("(Install pyperclip to enable clipboard copy)")

    except ValueError:
        print("❌ Please enter a valid number for length.")


if __name__ == "__main__":
    main()
