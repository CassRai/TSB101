#Main Program
#importing modules
import sqlite3
import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QVBoxLayout, QHBoxLayout,QGridLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QFrame, QStackedWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

##################User Interface Creation ##############

def font1(self, a):
    font = QtGui.QFont()  # setting fonts for main-title only
    font.setFamily("MS UI Gothic")
    font.setPointSize(26)
    a.setFont(font)

def font2(self, a, b):
    font = QtGui.QFont()  # setting fonts for main-title and secondary label
    font.setFamily("Nirmala UI")
    font.setPointSize(13)
    a.setFont(font)
    font = QtGui.QFont()
    font.setFamily("MS UI Gothic")
    font.setPointSize(26)
    b.setFont(font)

class Main_Menu(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        main_title = QLabel("Trading Simulator For Beginners 101",self)
        main_title.setGeometry(60, 40, 671, 81)
        secondary_label = QLabel("",self)
        secondary_label.setGeometry(270, 100, 191, 51)
        font2(self, secondary_label, main_title)
        LogButton = QPushButton("Log-in", self)
        LogButton.setGeometry(310, 200, 131, 51)
        SignButton = QPushButton("Sign-up", self)
        SignButton.setGeometry(310, 200, 131, 51)
        ExitButton = QPushButton("Exit", self)
        ExitButton.setGeometry(310, 400, 131, 51)
        LogButton.setStyleSheet("background-color : cyan")
        SignButton.setStyleSheet("background-color : cyan")
        ExitButton.setStyleSheet("background-color : cyan")

class Sign_Up(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        #creating labels for sign-up widget
        main_title = QLabel("Sign up", self)
        main_title.adjustSize()
        secondary_label = QLabel("Welcome to TSB101's Sign-Up - Create an account!", self)
        username_label = QLabel("Username", self)
        password_label = QLabel("Password", self)

        font = QtGui.QFont() #setting font for password and username labels
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        username_label.setFont(font)
        password_label.setFont(font)

        font2(self,secondary_label,main_title)

        #textbox is where the user will enter their information
        username_textbox = QLineEdit(self)
        password_textbox = QLineEdit(self)
        submit_button = QPushButton("Submit", self)

        #fixing the position and size of labels, buttons and textboxes
        main_title.setGeometry(QtCore.QRect(330, 20, 111, 51))
        secondary_label.setGeometry(QtCore.QRect(170, 110, 441, 31))
        username_label.setGeometry(QtCore.QRect(190, 220, 91, 21))
        password_label.setGeometry(QtCore.QRect(190, 290, 91, 21))
        username_textbox.setGeometry(QtCore.QRect(310, 220, 201, 20))
        password_textbox.setGeometry(QtCore.QRect(310, 290, 201, 20))
        submit_button.setGeometry(QtCore.QRect(330, 380, 131, 41))

        #setting submit button to blue
        submit_button.setStyleSheet("background-color : cyan")

class Log_In(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        #creating labels for sign-up widget
        main_title = QLabel("Login", self)
        main_title.adjustSize()
        secondary_label = QLabel("Welcome to TSB101's Login - Login Into Your Account!", self)
        secondary_label.adjustSize() #contents of label are too large for the standard size of label - need to resize

        username_label = QLabel("Username", self)
        password_label = QLabel("Password", self)

        font = QtGui.QFont() #setting font for password and username labels
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        username_label.setFont(font)
        password_label.setFont(font)

        font2(self,secondary_label,main_title)

        #textbox is where the user will enter their information
        username_textbox = QLineEdit(self)
        password_textbox = QLineEdit(self)
        submit_button = QPushButton("Submit", self)

        #fixing the position and size of labels, buttons and textboxes
        main_title.setGeometry(QtCore.QRect(330, 20, 111, 51))
        secondary_label.setGeometry(QtCore.QRect(168, 110, 441, 31))
        username_label.setGeometry(QtCore.QRect(190, 220, 91, 21))
        password_label.setGeometry(QtCore.QRect(190, 290, 91, 21))
        username_textbox.setGeometry(QtCore.QRect(310, 220, 201, 20))
        password_textbox.setGeometry(QtCore.QRect(310, 290, 201, 20))
        submit_button.setGeometry(QtCore.QRect(330, 380, 131, 41))

        #setting submit button to blue
        submit_button.setStyleSheet("background-color : cyan")


class Portfolio(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # creating main title for Portfolio widget
        main_title = QLabel("Portfolio", self)

        account_val = QLabel("Account value:", self)  # creating all other labels
        account_val_value = QLabel(self)
        free_funds = QLabel("Free funds:", self)
        free_funds_value = QLabel(self)
        invested = QLabel("Invested:", self)
        invested_value = QLabel(self)
        real_return = QLabel("Return:", self)
        real_return_value1 = QLabel(self)
        real_return_value2 = QLabel(self)
        header = QLabel("Stock     |      Quantity     |     Purchase Price     |    Current Price   |   Total Value   |   Today\'s Change     |     Total Gain /Loss  ",self)
        stock1 = QLabel("GOOG", self)
        stock2 = QLabel("AML.L", self)
        stock3 = QLabel("TSLA", self)
        stock1_result = QLabel(self)
        stock2_result = QLabel(self)
        stock3_result = QLabel(self)

        line1 = QFrame(self)  # creating lines for dividing sections
        line2 = QFrame(self)

        font1(self, main_title)  # setting fonts

        font = QtGui.QFont()
        font.setPointSize(10)
        account_val.setFont(font)
        account_val_value.setFont(font)
        free_funds.setFont(font)
        free_funds_value.setFont(font)
        invested.setFont(font)
        invested_value.setFont(font)
        real_return.setFont(font)
        real_return_value1.setFont(font)
        real_return_value2.setFont(font)
        header.setFont(font)
        stock1.setFont(font)
        stock2.setFont(font)
        stock3.setFont(font)
        stock1_result.setFont(font)
        stock2_result.setFont(font)
        stock3_result.setFont(font)

        main_title.setGeometry(350, 10, 191, 41)#setting Geometry
        header.setGeometry(730, 70, 61, 21)
        stock1.setGeometry(20, 170, 47, 13)
        stock2.setGeometry(20, 220, 47, 13)
        stock3.setGeometry(20, 270, 47, 13)
        stock1_result.setGeometry(100, 170, 661, 16)
        stock2_result.setGeometry(80, 220, 661, 16)
        stock3_result.setGeometry(100, 270, 651, 16)

        line1.setGeometry(20, 90, 791, 20)
        line2.setGeometry(20, 60, 791, 16)

        account_val.setGeometry(40, 65, 111, 21)
        account_val_value.setGeometry(160, 70, 91, 21)
        free_funds.setGeometry(420, 70, 101, 21)
        free_funds_value.setGeometry(330, 70, 61, 21)
        invested.setGeometry(250, 70, 71, 21)
        invested_value.setGeometry(510, 70, 61, 21)
        real_return.setGeometry(590, 70, 71, 21)
        real_return_value1.setGeometry(650, 70, 81, 21)
        real_return_value2.setGeometry(730, 70, 61, 21)


class Dashboard(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        #creating labels for Dashboard widget
        main_title = QLabel("Dashboard", self)
        secondary_label = QLabel("Welcome to TSB101!", self)

        font2(self,secondary_label,main_title)#setting font for main title and secondary label

        stock_finder_image = QLabel(self) #creating image labels
        portfolio_image = QLabel(self)
        learning_centre_image = QLabel(self)

        stock_finder_image.setPixmap(QtGui.QPixmap("images/stock_finder.png")) #setting the images to image labels
        stock_finder_image.setScaledContents(True)

        portfolio_image.setPixmap(QtGui.QPixmap("images/portfolio.png"))
        portfolio_image.setScaledContents(True)

        learning_centre_image.setPixmap(QtGui.QPixmap("images/learning_centre.png"))
        learning_centre_image.setScaledContents(True)

        StockFinderButton = QPushButton("Stock Finder", self) #creating buttons
        PortfolioButton = QPushButton("Portfolio", self)
        LearningCentreButton =  QPushButton("Learning Centre", self)

        main_title.setGeometry(320,20,231, 51) #setting the positons and sizes for all the labels and buttons
        secondary_label.setGeometry(320, 100, 191, 51)
        stock_finder_image.setGeometry(50, 180, 211, 231)
        portfolio_image.setGeometry(320, 180, 181, 231)
        learning_centre_image.setGeometry(560, 180, 181, 231)
        StockFinderButton.setGeometry(80, 440, 131, 41)
        PortfolioButton.setGeometry(340, 440, 131, 41)
        LearningCentreButton.setGeometry(590, 440, 131, 41)

        StockFinderButton.setStyleSheet("background-color : cyan") #setting the colours for the buttons
        LearningCentreButton.setStyleSheet("background-color : cyan")
        PortfolioButton.setStyleSheet("background-color : cyan")

    class MyWindow(QMainWindow):
        # inherits all of properties from QMainWindow
        def __init__(self):
            super(MyWindow, self).__init__()
            # will run whenever an instance of MyWindow is created
            self.setGeometry(100, 100, 800, 600)
            # 4 arguments - (x position, y position, width,height)
            self.setWindowTitle("TSB101")
            self.initializeUi()

        def initializeUi(self):
            #sets up the user interface and creates buttons
            layout = QVBoxLayout()
            main_title = QLabel("Trading Simulator For Beginners 101", self)
            secondary_label = QLabel("", self)

            font2(self, secondary_label, main_title) # setting fonts for main-title and secondary label

            LogButton = QPushButton("Log-in", self)  # creating Log-in,Sign-up and Exit Buttons
            SignButton = QPushButton("Sign-up", self)
            ExitButton = QPushButton("Exit", self)

            LogButton.setStyleSheet("background-color : cyan")  # making Log-in,Sign-up and Exit Buttons blue
            SignButton.setStyleSheet("background-color : cyan")
            ExitButton.setStyleSheet("background-color : cyan")

            LogButton.setFixedSize(131, 51) #setting size of buttons
            SignButton.setFixedSize(131, 51)
            ExitButton.setFixedSize(131, 51)

            #what happens when buttons clicked
            ExitButton.clicked.connect(self.close) # closes the program

            # what happens when buttons clicked
            # lambda function (sometimes called a mini function)
            # lambda allows us to take multiple arguments on the same line
            LogInObject = Log_In(self) #creating Log_In object
            LogButton.clicked.connect(lambda: self.setCentralWidget(stackedwidget)) #connecting Log_In Object to Sign-Up Button

            SignUpObject = Sign_Up(self) #creating Sign_Up object
            SignButton.clicked.connect(lambda: self.setCentralWidget(SignUpObject)) #connecting SignUp Object to Sign-Up Button

            layout.addWidget(main_title)
            layout.addWidget(secondary_label)
            layout.addStretch()
            layout.addWidget(LogButton)
            layout.addWidget(SignButton)
            layout.addWidget(ExitButton)
            layout.addStretch()

            main = QWidget()
            main.setLayout(layout)
            self.setCentralWidget(main)

            stackedwidget = QStackedWidget(self)
            DashboardWidget = Dashboard(self)
            PortfolioWidget = Portfolio(self)

            stackedwidget.addWidget(DashboardWidget)
            stackedwidget.addWidget(PortfolioWidget)

            stackedwidget.setCurrentIndex(0)
            stackedwidget.setCurrentWidget(DashboardWidget)