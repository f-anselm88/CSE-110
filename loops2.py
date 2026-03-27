payment = float(input("What is the payment amount?"))

penalty = 0

while payment < 0:
    penalty = 1.50

    print("Sorry, the payment cannot be negative.")
payment = float(input("What is the payment amount?"))

print(f"The amount is $ {payment:.2f}. The penalty is {penalty:.2f}")
