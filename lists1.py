"""
Author: Anselm Munango

Purpose: Practice using lists, by adding the names of friends.
"""
#Ask the user to enter the names of their friends, and append each one to a list. Stop when they enter "end".
friends = []

#Hint: You can use a while loop to keep asking for names until the user types "end".
friend = ""

while friend != "end":
    friend = input("Enter the name of a friend (or 'end' to stop): ")
    if friend != "end":
        friends.append(friend)

#Once you have the list, print out the names of your friends.
print("Your friends are:")
for friend in friends:
    print(friend)
