temperature = float(input("What is the temperature outside? "))

if temperature < 5:
    print("Ask other quetions...")
elif temperature < -15:
    print("It is too cold. Don't go!")
else:
    print("Enjoy your run.")