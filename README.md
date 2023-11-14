# Hangman

## Table of Contents
- [Project Title](#project-title)
- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

This project is a simple guessing game where the user tries to guess a letter in a randomly chosen word.

## Installation
Clone the repository and run the Python script.

## Usage
The game prompts the user to guess a letter in the randomly chosen word. The ask_for_input function handles user input, and the check_guess function verifies if the guessed letter is in the word.

# Test the code
word_list = ["apple", "banana", "orange", "grape", "kiwi"]
secret_word = random.choice(word_list)

# Call the ask_for_input function to test the code
ask_for_input(secret_word)

## File Structure
guessing_game.py: Main script containing the game logic.
README.md: Documentation for the project.

## License
This project is licensed under the MIT License.

