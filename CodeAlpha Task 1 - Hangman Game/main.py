"""
This script implements a simple Hangman game using Python. The player attempts to guess a randomly selected word by inputting single letters.
The game provides feedback on whether the guesses are correct or incorrect, tracks the number of incorrect guesses, and reveals the word
progressively. The game ends when the player either successfully guesses the word or exceeds the maximum number of incorrect guesses.
"""

import random


def get_random_word():
    words = ["python", "hangman", "programming", "random", "word", "game", "example"]
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return displayed_word


def hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print("Incorrect!")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame Over! The word was: {word}")


if __name__ == "__main__":
    hangman()

