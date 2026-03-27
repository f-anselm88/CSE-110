"""
Author: Anselm Munango

Purpose: Practice using mathematical expressions
"""
#Ask user for age
age = int(input("How old are you? "))
next_age = age + 1

print()

#Age calculation
print(f"On your next birthday, you will be {next_age}. ")

print()

#Egg cartons calculation
cartons = int(input("How many egg cartons do you have? "))
eggs = cartons * 12
print(f"You have {eggs} eggs")

print()

#Cookies distribution
cookies = int(input("/nHow many cookies do you have? "))
people = int(input("How many people are there? "))

cookies_per_person = cookies / people 
print(f"Each person may have {cookies_per_person} cookies")