import random

def check_guess(guess, secret_word):
    # Step 2: Convert the guess to lowercase
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(secret_word):
    # Step 1: Define a function called ask_for_input
    while True:
        # Step 2: Move the code to check if the input is a valid guess into this function block
        guess = input("Guess a letter: ")

        # Step 3: Call the check_guess function to check if the guess is in the word
        check_guess(guess, secret_word)

        # Step 4: Break out of the loop if needed or continue as necessary
        break  # For testing purposes, you might want to remove this break statement in a real game loop

# Test the code
word_list = ["apple", "banana", "orange", "grape", "kiwi"]
secret_word = random.choice(word_list)

# Call the ask_for_input function to test the code
ask_for_input(secret_word)