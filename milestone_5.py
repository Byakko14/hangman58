import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Initialize attributes
        self.word_list = word_list
        self.word = random.choice(word_list)  # Corrected usage
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        # Step 1: Convert the guessed letter to lower case
        guess = guess.lower()

         # Step 2: Check if the guess is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            # Step 3: Replace underscores in word_guessed with the guessed letter
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

            # Step 4: Reduce the variable num_letters by 1
            self.num_letters -= 1

         # Step 5: If the guess is not in the word
        else:
            # Reduce num_lives by 1
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

        # Continue with the logic of the check_guess method in the next task

    def ask_for_input(self):
        while True:
            # Ask the user to guess a letter
            guess = input("Guess a letter: ")

            # Check if the guess is NOT a single alphabetical character
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            # Check if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            
            else:
                # Call the check_guess method
                self.check_guess(guess)

                # Append the guess to the list_of_guesses
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    # Step 1: Initialize variables and create an instance of the Hangman class
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        # Check if the game has ended (no lives remaining)
        if game.num_lives == 0:
            print('You lost!')
            break
        
        # Check if there are still letters to guess
        elif game.num_letters > 0:
            # Continue the game by calling the ask_for_input method
            game.ask_for_input()

        # Check if the user has won the game
        else:
            print('Congratulations. You won the game!')
            break

# Step 2: Call the play_game function
word_list = ["apple", "banana", "orange", "grape", "kiwi"]
play_game(word_list)