# Activity 1: Functions
def display_regular(message):
    """Purpose: Display a regular message."""
    print(message)

def display_uppercase(message):
    """Purpose: Display a message in uppercase."""
    new_message = message.upper()
    print(new_message)

def display_lowercase(message):
    """Purpose: Display a message in lowercase."""
    new_message = message.lower()
    print(new_message)

# Get a message from the user.
user_message = input("Enter a message: ")

# Call the functions to display the message in different ways.
display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message) 