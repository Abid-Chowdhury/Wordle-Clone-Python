# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backup0MaHwSb.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
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
        font.setWeight(50)
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
        self.label_previous_guess = QLabel(self.frame)
        self.label_previous_guess.setObjectName(u"label_previous_guess")
        self.label_previous_guess.setGeometry(QRect(0, 90, 500, 70))
        self.label_previous_guess.setStyleSheet(u"QLabel {\n"
"	color: rgb(150,150,150);\n"
"	font: 40px \"Adam Bold\";\n"
"	background-color: rgba(0,0,0,0)\n"
"}")
        self.label_previous_guess.setAlignment(Qt.AlignCenter)
        self.button_guess = QPushButton(self.frame)
        self.button_guess.setObjectName(u"button_guess")
        self.button_guess.setGeometry(QRect(150, 260, 200, 60))
        self.button_guess.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color: white;\n"
"	font: 40px \"Adam Bold\";\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	font: 42px \"Adam Bold\"\n"
"}\n"
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
"	color: white;\n"
"	font: 20px \"Adam Medium\";\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	font: 22px \"Adam Bold\"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"WORDLE", None))
        self.label_previous_guess.setText("")
        self.button_guess.setText(QCoreApplication.translate("MainWindow", u"GUESS", None))
        self.button_minimize.setText("")
        self.button_close.setText("")
        self.button_credit.setText(QCoreApplication.translate("MainWindow", u"Github.com/Abid-Chowdhury", None))
    # retranslateUi

