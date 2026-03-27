"""
Author: Anselm Munango

Purpose: Practice writing programs that compare strings and numbers.

"""
#Prompt the user to enter the following information
first = int(input("What is the first number? "))
second = int(input("What is the second number? "))

#First > Second
if first > second:
  print("The first number is greater")
else:
  print("The first number is not greater")

#Check if the numbers are equal
if first == second:
  print("The numbers are equal")
else:
  print("The numbers are not equal")

#First > Second
  if first > second:
    print("The second number is greater.")
  else:
    print("The second number is not greater.")

#Hardcoded value
favorite = input("What is your favorite animal? ")
favourite_animal = "teddy bear"
if favorite.lower() == favourite_animal:
  print("That is my favorite animal too!")
else:
  print("That is not my favorite animal.")
