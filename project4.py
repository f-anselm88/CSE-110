#Word Puzzle 

#Program: Word puzzle game
#Author: Anselm Munango

#Step 1: Store the secret word
secret_word = "snake"

#Step 2: Initialize guesses counter
number_of_guesses = 0

print("Welcome to the word guessing game!")
print("Try to guess the secret word!")

#Step 3: Loop until the user guesses correctly
guess = ""

while guess != secret_word:
    guess = input("Enter your guess: ").lower()
    number_of_guesses += 1

    if guess != secret_word:
        print("Incorrect, try again.")

#Display result
print(f"Congatulations! You guessed the word {secret_word} correctly.")
print(F"It took you {number_of_guesses} guesses.")

    


