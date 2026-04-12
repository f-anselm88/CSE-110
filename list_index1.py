"""
Author: Anselm Munango

Purpose: Practice using lists and list indexes.
"""
print("Please enter the items of the shopping list (type: quit to finish): ")

shopping_list = []
item = ""

while item != "quit":
    item = input("Enter an item: ")

    if item != "quit":
        shopping_list.append(item)

#Once you have the list, print out the items with their corresponding numbers (starting from 1).
print("\nThe shopping list is:")
for i in range(len(shopping_list)):
    print(f"{i + 1}. {shopping_list[i]}")

print()
index = int(input("Which item would you like to change?: "))
new_item = input("What is the new item?: ")
shopping_list[index - 1] = new_item

print("\nThe updated shopping list with indexes is:")
for i in range(len(shopping_list)):
    print(f"{i + 1}. {shopping_list[i]}")