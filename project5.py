"""
Author: Anselm Munango
Date: April 4, 2026
Purpose: Practice using lists and list indexes by creating a shopping cart program.

Features:
- Stores both item names and prices
- Validates user input for item removal to prevent errors
- Computes total cost of items in the cart
- Displays items in the cart with their prices and numbers for easy reference
- Provides a user-friendly menu for interaction
- Allows users to quit the program gracefully
- Handles empty cart scenarios for viewing and removing items
- Computes total cost using a generator expression for efficiency

Extra Creativity:
- The program uses a tuple to store both the item name and price together in the cart list, making it easier to manage and display items.
- Ready for customization with different currencies or additional features like saving the cart to a file or applying discounts in the future.

"""
cart = [] # List to store items in the cart
cart_prices = [] # List to store prices of items in the cart
currency = "$" # Currency symbol for displaying prices

print("Welcome to the shopping cart program!")

# Use a while loop to continuously ask 
# the user for items until they type "quit".
while True:
    print("\nPlease select one of the following:")
    print("1. Add an item")
    print("2. View Cart")
    print("3. Remove an item")
    print("4. Compute total")
    print("5. Quit")

    choice = input("Please enter an action: ")

#Add an item to the cart if the user selects option 1.
    if choice == "1":
        name = input("What item would you like to add to your cart? ")
        price = float(input("What is the price of the item? "))

        cart.append((name, price))
        cart_prices.append(price)

        print(f"{name} has been added to your cart.")

    # View the items in the cart if the user selects option 2.
    elif choice == "2":
        if not cart:
            print("Your cart is empty.")
        else:
            print("Here are the items in your cart:")
            for item, price in cart:
                print(f"- {item}: ${price:.2f}")

    # Remove an item from the cart if the user selects option 3.
    elif choice == "3":
        if not cart:
            print("Your cart is empty. No items to remove.")
        else:
            print("Here are the items in your cart:")

            # Display the items in the cart with their corresponding numbers
            for i, (item, price) in enumerate(cart):
                print(f"{i + 1}. {item}: ${price:.2f}")
            item_index = int(input("What item would you like to remove? ")) - 1

            if 0 <= item_index < len(cart):
                removed_item = cart.pop(item_index)
                print(f"{removed_item[0]} has been removed from your cart.")
            else:
                print("Invalid item number. Please try again.")

    # If the user selects option 3, display the items in the cart with their prices.
    elif choice == "3":
        print("Your shopping cart contains the following items:")
        for item, price in cart:
            print(f"- {item}: ${price:.2f}")

    # If the user selects option 4, compute and display the total cost of the items in the cart.
    elif choice == "4":
        total = sum(price for _, price in cart)
        print(f"The total cost of the items in your cart is: ${total:.2f}")

    # If the user selects option 5, exit the program.
    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the shopping cart program!")
