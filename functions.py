from main import *
from UI import *
from words import words
from webbrowser import open
from random import choice, random

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
    print(random_word)
    
    # set the previous guess label 
    def set_previous_guess(self, guess):
        self.ui.label_previous_guess_1.setText(guess[0])
        self.ui.label_previous_guess_2.setText(guess[1])
        self.ui.label_previous_guess_3.setText(guess[2])
        self.ui.label_previous_guess_4.setText(guess[3])
        self.ui.label_previous_guess_5.setText(guess[4])
    
    # set label to yellow
    def set_yellow(self, label):
        label.setStyleSheet("""
                             QLabel {
                                 color: rgb(255, 255, 0);
                                 font: 40px "Adam Bold";
                                 background-color: rgba(0, 0, 0,0);
                             }
                             """)        
    
    def check_if_yellow(self, guess, word):
        if guess[0] in word:
            UIFunctions.set_yellow(self, self.ui.label_previous_guess_1)
        if guess[1] in word:
            UIFunctions.set_yellow(self, self.ui.label_previous_guess_2)
        if guess[2] in word:
            UIFunctions.set_yellow(self, self.ui.label_previous_guess_3)
        if guess[3] in word:
            UIFunctions.set_yellow(self, self.ui.label_previous_guess_4)
        if guess[4] in word:
            UIFunctions.set_yellow(self, self.ui.label_previous_guess_5)

    def set_tries_label(self, tries):
        self.ui.label_tries.setText(f'Tries\n{str(tries)}')

    # win function
    def win(self):
        UIFunctions.set_tries_label(self, UIFunctions.tries)
        
        self.ui.label_tries.setVisible(True)
        UIFunctions.set_previous_guess(self, '     ')
        self.ui.entry_guess.setStyleSheet("""
                                          QLineEdit {
                                              color: rgb(0, 255, 0);
                                              background-color: rgba(0, 0, 0,0);
                                              border: 2px solid rgb(0, 255, 0);
                                              border-radius: 15px;
                                              font: 50px "Adam Bold";
                                              text-transform: uppercase;
                                              }
                                          
                                          """)
        self.ui.entry_guess.setReadOnly(True)
        self.ui.button_guess.setVisible(False)
        self.ui.button_restart.setVisible(True)
        
    # set label to green
    def set_green(self, label):
        label.setStyleSheet("""
                             QLabel {
                                 color: rgb(0, 255, 0);
                                 font: 40px "Adam Bold";
                                 background-color: rgba(0, 0, 0,0);
                             }
                             """)           
    
    def check_if_green(self, guess, word):
        score = 0
        
        if guess[0] == word[0]:
            UIFunctions.set_green(self, self.ui.label_previous_guess_1)
            score += 1
        if guess[1] == word[1]:
            UIFunctions.set_green(self, self.ui.label_previous_guess_2)
            score += 1
        if guess[2] == word[2]:
            UIFunctions.set_green(self, self.ui.label_previous_guess_3)
            score += 1
        if guess[3] == word[3]:
            UIFunctions.set_green(self, self.ui.label_previous_guess_4)
            score += 1
        if guess[4] == word[4]:
            UIFunctions.set_green(self, self.ui.label_previous_guess_5)
            score += 1
        
        if score == 5:
            UIFunctions.win(self)
            
    # reset colors before each guess
    def set_gray(self, label):
        label.setStyleSheet("""
                             QLabel {
                                 color: rgb(150, 150, 150);
                                 font: 40px "Adam Bold";
                                 background-color: rgba(0, 0, 0,0);
                             }
                             """)
    
    def reset_colors(self):
        UIFunctions.set_gray(self, self.ui.label_previous_guess_1)
        UIFunctions.set_gray(self, self.ui.label_previous_guess_2)
        UIFunctions.set_gray(self, self.ui.label_previous_guess_3)
        UIFunctions.set_gray(self, self.ui.label_previous_guess_4)
        UIFunctions.set_gray(self, self.ui.label_previous_guess_5)
    
    # keep track of tries
    tries = 0
    
    # reset game
    def reset_game(self):
        self.ui.entry_guess.setStyleSheet("""
                                          QLineEdit {
                                              color: rgb(255, 255, 255);
                                              background-color: rgba(0, 0, 0,0);
                                              border: 2px solid rgb(255, 255, 255);
                                              border-radius: 15px;
                                              font: 50px "Adam Bold";
                                              text-transform: uppercase;
                                              }
                                          
                                          """)
        self.ui.entry_guess.setReadOnly(False)
        self.ui.label_tries.setVisible(False)
        self.ui.entry_guess.setText('')
        UIFunctions.random_word = UIFunctions.get_random_word().upper()
        print(UIFunctions.random_word)
        UIFunctions.tries = 0
        UIFunctions.reset_colors(self)
        UIFunctions.set_previous_guess(self, '     ')
        self.ui.button_guess.setVisible(True)
        self.ui.button_restart.setVisible(False)
        
    # get the guess
    def get_guess(self):
        try:  
            guess = self.ui.entry_guess.text().upper()

            UIFunctions.tries += 1
            print(UIFunctions.tries)
            
            UIFunctions.reset_colors(self)
            UIFunctions.set_previous_guess(self, guess)
            UIFunctions.check_if_yellow(self, guess, UIFunctions.random_word)
            UIFunctions.check_if_green(self, guess, UIFunctions.random_word)
        except IndexError:
            pass
            