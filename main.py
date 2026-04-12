"""
Password Generator
#Author: Anselm Munango
#Purpose: This program generates a random password based on user-defined length and strength.
Users can choose between weak, medium, and strong passwords, and have the option to save generated passwords to a file.

"""


import random
import string

def generate_password(length, strength):
    if strength == "weak":
        characters = string.ascii_letters
    elif strength == "medium":
        characters = string.ascii_letters + string.digits
    elif strength == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return None

    return ''.join(random.choice(characters) for _ in range(length))


def get_valid_length():
    while True:
        try:
            length = int(input("Enter password length (6–32 recommended): "))
            if length < 1:
                print("Length must be greater than 0.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")


def get_strength():
    while True:
        print("\nChoose password strength:")
        print("1 - Weak (letters only)")
        print("2 - Medium (letters + numbers)")
        print("3 - Strong (letters + numbers + symbols)")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            return "weak"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "strong"
        else:
            print("Invalid choice. Try again.")


def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")


# MAIN PROGRAM
print("Welcome to the Password Generator")

while True:
    length = get_valid_length()
    strength = get_strength()

    password = generate_password(length, strength)

    print("\n==============================")
    print("Your Password:", password)
    print("==============================\n")

    save_choice = input("Save password to file? (y/n): ")
    if save_choice.lower() == "y":
        save_password(password)
        print("Password saved!")

    again = input("\nGenerate another password? (y/n): ")
    if again.lower() != "y":
        print("Goodbye! Stay secure.")
        break