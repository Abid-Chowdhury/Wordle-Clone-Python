from main import *
from UI import *
from words import words
from webbrowser import open
from random import choice

class UIFunctions(MainWindow):
    
    def close_window(self):
        self.close()
        
    def minimize_window(self):
        self.showMinimized()
        
    def credit_button():
        open('https://github.com/Abid-Chowdhury/Wordle-Clone-Python')
    
    # main game functions
    def get_random_word():
        word = choice(words)
        return word
    
    random_word = get_random_word()
    
    def check_if_letters_in_word(self):
        guess = self.ui.entry_guess.text().upper()
        print(UIFunctions.random_word)
        
    def get_guess(self):
        guess = self.ui.entry_guess.text().upper()
        self.ui.label_previous_guess.setText(guess)
        
        letters_in_word = []
        for letter in guess:
            if letter in UIFunctions.random_word:
                letters_in_word.append(letter)
        print(UIFunctions.random_word)
        
        UIFunctions.check_if_letters_in_word(self)