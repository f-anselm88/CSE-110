#I added a feature that allows the user to include drinks in a meal.
# The program calculates the drink total and adds it to the subtotal.

print("Please provide the following information.\n")

#Ask for the price of meals (floating point numbers)
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of adult's meal? "))

#Ask for the number of people (integers)
number_of_children = int(input("How many Children are there? "))
number_of_adults = int(input("How many adults are there? "))

#Ask for drink information
drink_price = float(input("What is the price of a drink? "))
drink_count = int(input("How many drinks were ordered? "))

#Calculate the cost for children and adults
children_total = child_price * number_of_children
adults_total = adult_price * number_of_adults

#calculate drink total
drink_total = drink_price * drink_count

#Calculate the subtotal including drinks
subtotal = children_total + adults_total
subtotal = subtotal + drink_total

#Display the subtotal
print()
print(f"subtotal: ${subtotal:.2f}")

#Ask the user for the sales tax rate
tax_rate = float(input("What is the sales tax rate? "))

#Compute the sales tax
sales_tax = subtotal * (tax_rate / 100)

#Display the sales tax
print(f"Sales Tax: ${sales_tax:.2f}")

#Compute the total
total = subtotal + sales_tax

#Display the total
print(f"Total: ${total:.2f}")

#Ask for the payment amount 
payment_amount = float(input("What is the payment amount? "))

#Compute the change
change = payment_amount - total

#Display the change
print(f"Change: ${change:.2f}")
print()
print("\nThank you for dining with us!")
