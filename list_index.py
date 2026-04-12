# index = 0   1   2   3
from turtle import color


colors = ["red", "blue", "green", "yellow"]

# print(colors[1])

colors.insert(2, "purple") #This will insert "purple" at index 2, and move the rest of the list to the right.
for color in colors:
    print(color)
for i in range(len(colors)):
    color = colors[i]
    human_count = i + 1
    print(f"{human_count}: {color}")
