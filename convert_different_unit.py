"""
Author: Anselm Munango

Purpose: Convert from Fahrenheit to Celsius

"""

#Prompt the user to enter the temprature in Fahrenheit
fahrenheit = float(input("What is the temperature in fahrenheit: "))
input()

#Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9

#Display the result with one decimal place
print(f"The temperature in celsius is {celsius:.1f} ")