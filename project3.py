#Text Adventure Game - Two Levels
#I added two levels of choices to make the story of the game more interactive and creative.
#The player makes the first choice and an item, and the second choice decides what to do next.

print("Welcome to the Temple Adventure!")

print("Stand at the entrance of the temple.")
print("You will see three items: a TORCH, a ROPE, and a MAP.")

choice1 = input("Which one do you pick? (TORCH / ROPE / MAP): ").lower()

#Level 1
if choice1 == "torch":
    print("\nYou light the torch. The temple entrance becomes visible and less scary when you walk.")
    print("Walk into the dark hallway and hear strange noises.")

choice2 = input("Will you FOLLOW the SOUND or IGNORE SOUND? ").lower()

#Level 2
if choice2 == "follow the sound":
    print("/nFollow the sound and find a hidden room with treasure. You win!.")
elif choice2 == "ignore sound":
    print("You keep walking and fall into a trap. Game over!")
else:
    print("Invalid choice. Game over!")
  
if choice1 == "rope":
    print("You take the rope. It might help you to climb and escape danger eventually.")
choice2 = input("Do you CLIMB down or WALK away? (climb / walk): ").lower()

if choice2 == "climb":
    print("You safely reach the bottom and find treasure.")
elif choice2 == "walk":
    print("You avoid the hole but get lost. Game over!")
else:
    print("Invalid choice. Game over!")

if choice1 == "map":
    print("Study the map. It shows hidden paths inside the temple: LEFT or RIGHT.")
choice2 = input("Which path do you take? (left / right): ").lower()

if choice2 == "left":
  print("You find treasure safely!")
elif choice2 == "right":
     print("You walk into danger. Game over!")
else:
    print("That is not a valid choice. Please restart and choose TORCH, ROPE, or MAP. ")