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
    
    # check if a letter is in the word
    def check_if_letters_in_word(self, guess):       
        global letters_in_word
        letters_in_word = []
        
        for letter in guess:
            if letter in UIFunctions.random_word:
               letters_in_word.append(letter)
        
        print(letters_in_word)
        print(UIFunctions.random_word)
       
    # set the previous guess label 
    def set_previous_guess(self, guess):
        self.ui.label_previous_guess_1.setText(guess[0])
        self.ui.label_previous_guess_2.setText(guess[1])
        self.ui.label_previous_guess_3.setText(guess[2])
        self.ui.label_previous_guess_4.setText(guess[3])
        self.ui.label_previous_guess_5.setText(guess[4])
    
    def set_yellow(self, label):
        label.setStyleSheet("""
                             QLabel {
                                 color: rgb(255, 255, 0);
                                 font: 40px "Adam Bold";
                                 background-color: rgba(0, 0, 0,0);
                             }
                             
                             """)        
    
    def check_if_yellow(self, guess, letters_in_word):
        if guess[0] in letters_in_word:
            UIFunctions.set_yellow(self, self.ui.label_previous_guess_1)
        if guess[1] in letters_in_word:
            UIFunctions.set_yellow(self, self.ui.label_previous_guess_2)
        if guess[2] in letters_in_word:
            UIFunctions.set_yellow(self, self.ui.label_previous_guess_3)
        if guess[3] in letters_in_word:
            UIFunctions.set_yellow(self, self.ui.label_previous_guess_4)
        if guess[4] in letters_in_word:
            UIFunctions.set_yellow(self, self.ui.label_previous_guess_5)
        
    # get the guess
    def get_guess(self):
        global letters_in_word
        guess = self.ui.entry_guess.text().upper()

        UIFunctions.check_if_letters_in_word(self, guess)
        UIFunctions.set_previous_guess(self, guess)
        UIFunctions.check_if_yellow(self, guess, letters_in_word)