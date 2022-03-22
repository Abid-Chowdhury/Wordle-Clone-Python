# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIxhFWCp.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

GLOBAL_STATE = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 390)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 500, 390))
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(25,25,25);\n"
"	border-radius: 15px;\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 0, 500, 70))
        font = QFont()
        font.setFamily(u"Adam Bold")
        font.setBold(False)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	font: 40px  \"Adam Bold\";\n"
"	background: none\n"
"}")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.entry_guess = QLineEdit(self.frame)
        self.entry_guess.setObjectName(u"entry_guess")
        self.entry_guess.setGeometry(QRect(100, 160, 300, 80))
        self.entry_guess.setFont(font)
        self.entry_guess.setCursor(QCursor(Qt.IBeamCursor))
        self.entry_guess.setFocusPolicy(Qt.StrongFocus)
        self.entry_guess.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgba(0,0,0,0);\n"
"	border: 2px solid rgba(255,255,255,255);\n"
"	border-radius: 15px;\n"
"	font: 50px \"Adam Bold\";\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"")
        self.entry_guess.setMaxLength(5)
        self.entry_guess.setFrame(True)
        self.entry_guess.setEchoMode(QLineEdit.Normal)
        self.entry_guess.setAlignment(Qt.AlignCenter)
        self.entry_guess.setDragEnabled(False)
        self.entry_guess.setReadOnly(False)
        self.entry_guess.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.entry_guess.setClearButtonEnabled(False)
        
        
        self.button_guess = QPushButton(self.frame)
        self.button_guess.setObjectName(u"button_guess")
        self.button_guess.setGeometry(QRect(150, 260, 200, 60))
        self.button_guess.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color: rgb(225,225,225);\n"
"	font: 40px \"Adam Bold\";\n"
"	border-radius: 15px;\n"
"       padding-top: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"        background-color: rgb(255,255,255);\n}"
"")
        
        
        self.button_minimize = QPushButton(self.frame)
        self.button_minimize.setObjectName(u"button_minimize")
        self.button_minimize.setGeometry(QRect(440, 15, 15, 15))
        self.button_minimize.setStyleSheet(u"QPushButton {\n"
"	background-color: #ff0;\n"
"	border-radius: 7px;\n"
"}\n"
"")
        self.button_close = QPushButton(self.frame)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(470, 15, 15, 15))
        self.button_close.setStyleSheet(u"QPushButton {\n"
"	background-color: #ff0000;\n"
"	border-radius: 7px\n"
"}")
        self.button_credit = QPushButton(self.frame)
        self.button_credit.setObjectName(u"button_credit")
        self.button_credit.setGeometry(QRect(0, 360, 500, 30))
        self.button_credit.setStyleSheet(u"QPushButton {\n"
"	color: rgb(225,225,225);\n"
"	font: 20px \"Adam Bold\";\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: rgb(255,255,255)"
"}")
        self.label_previous_guess_1 = QLabel(self.frame)
        self.label_previous_guess_1.setObjectName(u"label_previous_guess_1")
        self.label_previous_guess_1.setGeometry(QRect(70, 90, 70, 70))
        self.label_previous_guess_1.setStyleSheet(u"QLabel {\n"
"	color: rgb(150,150,150);\n"
"	font: 40px \"Adam Bold\";\n"
"	background-color: rgba(0,0,0,0);\n"
"\n"
"}")
        self.label_previous_guess_1.setAlignment(Qt.AlignCenter)
        self.label_previous_guess_3 = QLabel(self.frame)
        self.label_previous_guess_3.setObjectName(u"label_previous_guess_3")
        self.label_previous_guess_3.setGeometry(QRect(210, 90, 70, 70))
        self.label_previous_guess_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(150,150,150);\n"
"	font: 40px \"Adam Bold\";\n"
"	background-color: rgba(0,0,0,0);\n"
"	\n"
"}")
        self.label_previous_guess_3.setAlignment(Qt.AlignCenter)
        self.label_previous_guess_4 = QLabel(self.frame)
        self.label_previous_guess_4.setObjectName(u"label_previous_guess_4")
        self.label_previous_guess_4.setGeometry(QRect(280, 90, 70, 70))
        self.label_previous_guess_4.setStyleSheet(u"QLabel {\n"
"	color: rgb(150,150,150);\n"
"	font: 40px \"Adam Bold\";\n"
"	background-color: rgba(0,0,0,0);\n"
"\n"
"}")
        self.label_previous_guess_4.setAlignment(Qt.AlignCenter)
        self.label_previous_guess_5 = QLabel(self.frame)
        self.label_previous_guess_5.setObjectName(u"label_previous_guess_5")
        self.label_previous_guess_5.setGeometry(QRect(350, 90, 70, 70))
        self.label_previous_guess_5.setStyleSheet(u"QLabel {\n"
"	color: rgb(150,150,150);\n"
"	font: 40px \"Adam Bold\";\n"
"	background-color: rgba(0,0,0,0);\n"
"\n"
"}")
        self.label_previous_guess_5.setAlignment(Qt.AlignCenter)
        self.label_previous_guess_2 = QLabel(self.frame)
        self.label_previous_guess_2.setObjectName(u"label_previous_guess_2")
        self.label_previous_guess_2.setGeometry(QRect(140, 90, 70, 70))
        self.label_previous_guess_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(150,150,150);\n"
"	font: 40px \"Adam Bold\";\n"
"	background-color: rgba(0,0,0,0);\n"
"\n"
"}")
        self.label_previous_guess_2.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wordle", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"WORDLE", None))
        self.button_guess.setText(QCoreApplication.translate("MainWindow", u"GUESS", None))
        self.button_minimize.setText("")
        self.button_close.setText("")
        self.button_credit.setText(QCoreApplication.translate("MainWindow", u"Github.com/Abid-Chowdhury", None))
        self.label_previous_guess_1.setText("")
        self.label_previous_guess_3.setText("")
        self.label_previous_guess_4.setText("")
        self.label_previous_guess_5.setText("")
        self.label_previous_guess_2.setText("")
    # retranslateUi

    def return_status():
        return GLOBAL_STATE