from operator import le
from words import words
from random import choice
import colorama

# game loop
def wordle():
    # pick a random word from the list
    word = choice(words)

    # get player guess
    guess = input("Guess the word: ")
    
    # keep track of correct guesses
    letters_in_word = []
    letters_in_correct_place = []

    # check if a letter is in the correct position
    for i in range(5):
        if guess[i] == word[i]:
            letters_in_correct_place.append(guess[i])

    # check if a letter is in the word
    for letter in guess:
        if letter in word:
            letters_in_word.append(letter)

    print(f'Word: {word}\nGuess: {guess}\nLetters in word: {letters_in_word}\nLetters in correct place: {letters_in_correct_place}')

wordle()

# import webbrowser
# webbrowser.open('https://github.com/Abid-Chowdhury')