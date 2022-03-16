import platform
import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QEvent,
                            QMetaObject, QObject, QPoint, QPropertyAnimation,
                            QRect, QSize, Qt, QTime, QUrl)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# import functions
from functions import *
# GUI file
from UI import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
        
        # makes the window rounded and keeps it on top
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)   
        
        # move window
        def move_window(event):
            # restore before moving
            if Ui_MainWindow.return_status() == 1:
                Ui_MainWindow.maximize_restore(self)

            # if left click, move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        
        self.ui.frame.mouseMoveEvent = move_window  
        
        # functions
        self.ui.button_close.clicked.connect(lambda: UIFunctions.close_window(self))
        self.ui.button_minimize.clicked.connect(lambda: UIFunctions.minimize_window(self))
        self.ui.button_credit.clicked.connect(lambda: UIFunctions.credit_button())
        self.ui.button_guess.clicked.connect(lambda: UIFunctions.get_guess(self))
        
        # show the window
        self.show()
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
