import random

word_list = ["banana", "durian", "orange", "rambutan", "lychee"]

word = random.choice(word_list)

guess = input("Please enter a single letter: ")

if len(guess) == 1 & word.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

print(word_list)
print(word)