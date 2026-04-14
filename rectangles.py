def get_positive_value(prompt_text):
    """Purpose: Get a positive value from the user."""

    # Prompt the user for a value and ensure it is positive.
    value = float(input(prompt_text))
    while value <= 0:

    # If the value is not positive, display an error message and prompt again.
        print("Value must be a positive number. Please try again.")
        value = float(input(prompt_text))

    # return the valid positive value.
    return value

length = get_positive_value("Enter the length of the rectangle: ")
width = get_positive_value("Enter the width of the rectangle: ") 

area = length * width

print(f"The area of the rectangle is: {area}")