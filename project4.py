#Word Puzzle Game with Hints
#Author: Anselm Munango
#Creativity: I added a limit to the number of guesses
#to make the game more challenging.

#Step 1: Store the secret word
secret_word = "snake"
number_of_guesses = 0
max_attempts = 6

print("Welcome to the word guessing game!")
print("Try to guess the secret word!")

#Show blanks for the secret word
blank = "_ " * len(secret_word)
print(f"The secret word is: {blank.strip()}")

#Step 2: Loop until the user guesses correctly
guess = ""

while number_of_guesses < max_attempts:
    guess = input("Enter your guess: ").lower()

    #Length check
    if len(guess) != len(secret_word):
        print((f"Please enter a {len(secret_word)} - letter word."))
        continue
    
    number_of_guesses += 1

    #Check if correct
    if guess == secret_word:
        print(f"Congatulations! You guessed the word {secret_word} correctly.")
        print(f"It took you {number_of_guesses} guesses.")
        break

    #Generate hint
    hint = ""

    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper() + " "
        elif guess[i] in secret_word:
            hint += guess[i].lower() + " "
        else:
            hint += "_ "

    print(f"Hint: {hint.strip()}")
    print("Incorrect, try again.")

#Final result if user fails
if guess != secret_word:
    print(f"You ran out of attempts. The word was {secret_word}.")
    print(f"You used {number_of_guesses} guesses.")

    


