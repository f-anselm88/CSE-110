# I added extra user inputs (color, animal2, place, food)
# to extend the story and create a funny, creative ending.

print("Please enter the following:")

adjective = input("adjective: ")
animal = input("animal: ")
verb = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb2: ")
verb3 = input("verb3: ")

# Extra words for creative ending
color = input("color: ")
animal2 = input("animal2: ")
place = input("place: ")
food = input("food: ")

story = f"""
The other day, I was really in trouble. It all started when I saw a very {adjective} {animal}
{verb} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2}
over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right
in front of my family. 

Then suddenly a {color} {animal2} jumped out of the {place} while 
eating a giant {food}!
"""
print(story)





