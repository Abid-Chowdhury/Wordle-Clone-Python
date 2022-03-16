from main import *
from webbrowser import open

class UIFunctions(MainWindow):
    
    def close_window(self):
        self.close()
        
    def minimize_window(self):
        self.showMinimized()
        
    def credit_button(self):
        open('https://github.com/Abid-Chowdhury/Wordle-Clone-Python')
    