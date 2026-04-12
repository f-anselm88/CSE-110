"""
Title: Number Fun
Author: Anselm Munango

Purpose: Practice using numbers in lists.
Instructions:
"""

#Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.

nums = []
num = -1

while num != 0:
    num = int(input("Enter a number please: "))
    if num != 0:
        nums.append(num)

print(nums)

#Once you have the list, have your program do the following:

#Compute the sum, or total of the numbers in the list.
sum = 0

for num in nums:   
    sum += num #This is the same as sum = sum + num

print(f"The sum of the numbers in your list is: {sum}")

#Compute the average of the numbers in the list.
count = len(nums)
average = sum / len(nums)

print(f"The average of the numbers in your list is: {average}")

#Find the largest number in the list.
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num

print(f"The largest number in your list is: {largest}")

#Enhancement: Find the smallest number in the list.
smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num
        
print(f"The smallest number in your list is: {smallest}")