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
    
    random_word = get_random_word().upper()
    
    def check_if_letters_in_word(self,guess):       
        letters_in_word = []
        
        for letter in guess:
            if letter in UIFunctions.random_word:
               letters_in_word.append(letter)
        
        print(letters_in_word)
        print(UIFunctions.random_word)
        
    def get_guess(self):
        guess = self.ui.entry_guess.text().upper()
        self.ui.label_previous_guess.setText(guess)
        
        self.ui.label_previous_guess.setText(f'<html><head/><body><p><span style="color: red">{guess}</span></p></body></html>')
        
        UIFunctions.check_if_letters_in_word(self,guess)
        
    