#Main Program
#importing modules
import sqlite3
import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

##################User Interface Creation ##############


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
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.main_title = QtWidgets.QLabel(self.centralwidget)
        self.main_title.setGeometry(QtCore.QRect(60, 40, 671, 81))
        self.main_title.setText("Trading Simulator For Beginners 101")
        self.secondary_label = QtWidgets.QLabel(self.centralwidget)
        self.secondary_label.setGeometry(QtCore.QRect(270, 100, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.secondary_label.setFont(font)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(26)
        self.main_title.setFont(font)
        self.LogButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogButton.setGeometry(QtCore.QRect(310, 200, 131, 51))
        self.LogButton.setText("Log-in")
        self.SignButton = QtWidgets.QPushButton(self.centralwidget)
        self.SignButton.setGeometry(QtCore.QRect(310, 300, 131, 51))
        self.SignButton.setText("Sign-up")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(310, 400, 131, 51))
        self.ExitButton.setText("Exit")
        #makes the buttons blue
        self.LogButton.setStyleSheet("background-color : cyan")
        self.SignButton.setStyleSheet("background-color : cyan")
        self.ExitButton.setStyleSheet("background-color : cyan")
        #what happens when buttons clicked
        self.ExitButton.clicked.connect(self.close) # closes the program
        self.LogButton.clicked.connect(lambda: self.individual_stock())
        self.SignButton.clicked.connect(lambda: self.sign_up())
        self.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self)

    def Dashboard(self):
        self.pass_label.hide()
        self.user_label.hide()
        self.username_textbox.hide()
        self.pass_textbox.hide()
        self.submit_button.hide()
        self.pass_label_2.hide()
        self.user_label_2.hide()
        self.username_textbox_2.hide()
        self.pass_textbox_2.hide()
        self.submit_button_2.hide()
        self.main_title.setText("Dashboard")
        self.main_title.adjustSize()
        self.secondary_label.setGeometry(QtCore.QRect(270, 100, 191, 51))
        self.secondary_label.setText("Welcome to TSB101!")
        self.update_secondary()
        #image set up
        self.stock_finder_image = QtWidgets.QLabel(self.centralwidget)
        self.stock_finder_image.setGeometry(QtCore.QRect(50, 180, 211, 231))
        self.stock_finder_image.setPixmap(QtGui.QPixmap("images/stock_finder.png"))
        self.stock_finder_image.setScaledContents(True)
        self.portfolio_image = QtWidgets.QLabel(self.centralwidget)
        self.portfolio_image.setGeometry(QtCore.QRect(320, 180, 181, 231))
        self.portfolio_image.setPixmap(QtGui.QPixmap("images/portfolio.png"))
        self.portfolio_image.setScaledContents(True)
        self.learning_centre_image = QtWidgets.QLabel(self.centralwidget)
        self.learning_centre_image.setGeometry(QtCore.QRect(560, 180, 181, 231))
        self.learning_centre_image.setPixmap(QtGui.QPixmap("images/learning_centre.png"))
        self.learning_centre_image.setScaledContents(True)
        #creating buttons and changing colours
        self.StockFinderButton = QtWidgets.QPushButton(self.centralwidget)
        self.StockFinderButton.setGeometry(QtCore.QRect(80, 440, 131, 41))
        self.StockFinderButton.setText("Stock Finder")
        self.PortfolioButton = QtWidgets.QPushButton(self.centralwidget)
        self.PortfolioButton.setGeometry(QtCore.QRect(340, 440, 131, 41))
        self.PortfolioButton.setText("Portfolio")
        self.LearningCentreButton = QtWidgets.QPushButton(self.centralwidget)
        self.LearningCentreButton.setGeometry(QtCore.QRect(590, 440, 131, 41))
        self.LearningCentreButton.setText("Learning Centre")
        self.stock_finder_image.show()
        self.learning_centre_image.show()
        self.portfolio_image.show()
        self.LearningCentreButton.show()
        self.StockFinderButton.show()
        self.PortfolioButton.show()
        #what happens when buttons clicked
        # lambda function (sometimes called a mini function)
        # lambda allows us to take multiple arguments on the same line

        self.StockFinderButton.clicked.connect(lambda: self.stock_finder())
        self.PortfolioButton.clicked.connect(lambda: self.portfolio())

        # makes the buttons blue
        self.StockFinderButton.setStyleSheet("background-color : cyan")
        self.LearningCentreButton.setStyleSheet("background-color : cyan")
        self.PortfolioButton.setStyleSheet("background-color : cyan")

    def update_secondary(self):
        self.secondary_label.adjustSize()
        # adjusts the width of the label to fit text

    def sign_up(self):
        #sign-up section
        self.LogButton.hide()
        self.SignButton.hide()
        self.ExitButton.hide()
        self.main_title.setGeometry(QtCore.QRect(330, 20, 111, 51))
        self.main_title.setText("Sign up")
        self.main_title.adjustSize()
        self.secondary_label.setGeometry(QtCore.QRect(170, 110, 441, 31))
        self.secondary_label.setText("Welcome to TSB101's Sign-Up - Create an account!")
        self.update_secondary()
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(190, 220, 91, 21))
        self.user_label.setText("Username")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(190, 290, 91, 21))
        self.pass_label.setText("Password")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.user_label.setFont(font)
        self.pass_label.setFont(font)
        self.user_label.adjustSize()
        self.pass_label.adjustSize()
        #textbox is where the user enters in their information
        self.username_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.username_textbox.setGeometry(QtCore.QRect(310, 220, 201, 20))
        self.pass_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_textbox.setGeometry(QtCore.QRect(310, 290, 201, 20))
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(330, 380, 131, 41))
        self.submit_button.setText("Submit")
        self.submit_button.setStyleSheet("background-color : cyan")
        self.pass_label.show()
        self.user_label.show()
        self.username_textbox.show()
        self.pass_textbox.show()
        self.submit_button.show()

    def log_in(self):
        #log-in section
        self.LogButton.hide()
        self.SignButton.hide()
        self.ExitButton.hide()
        self.main_title.setGeometry(QtCore.QRect(330, 20, 111, 51))
        self.main_title.setText("Log In")
        self.main_title.adjustSize()
        self.secondary_label.setGeometry(QtCore.QRect(120, 110, 441, 31))
        self.secondary_label.setText("Welcome to TSB101's Log-In - Sign Back Into Your Account")
        self.update_secondary()
        self.user_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.user_label_2.setGeometry(QtCore.QRect(190, 220, 91, 21))
        self.user_label_2.setText("Username")
        self.pass_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.pass_label_2.setGeometry(QtCore.QRect(190, 290, 91, 21))
        self.pass_label_2.setText("Password")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.user_label_2.setFont(font)
        self.pass_label_2.setFont(font)
        self.user_label_2.adjustSize()
        self.pass_label_2.adjustSize()
        #textbox is where the user enters in their information
        self.username_textbox_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.username_textbox_2.setGeometry(QtCore.QRect(310, 220, 201, 20))
        self.pass_textbox_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_textbox_2.setGeometry(QtCore.QRect(310, 290, 201, 20))
        self.submit_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button_2.setGeometry(QtCore.QRect(330, 380, 131, 41))
        self.submit_button_2.setText("Submit")
        self.submit_button_2.setStyleSheet("background-color : cyan")
        self.pass_label_2.show()
        self.user_label_2.show()
        self.username_textbox_2.show()
        self.pass_textbox_2.show()
        self.submit_button_2.show()

    def individual_stock(self):
        self.GOOGButton.hide()
        self.AMLButton.hide()
        self.TSLAButton.hide()
        self.stock_finder_image.hide()
        self.portfolio_image.hide()
        self.learning_centre_image.hide()

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to 'plot' method
        self.button = QtWidgets.QPushButton(self.centralwidget)

        # adding action to the button
        self.button.clicked.connect(self.plot)

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        layout.addWidget(self.button)

        # setting layout to the main window
        self.setLayout(layout)

        # action called by thte push button

    def plot(self):
        # random data
        data = [random.random() for i in range(10)]

        # clearing old figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

    def stock_finder(self):
        self.PortfolioButton.hide()
        self.StockFinderButton.hide()
        self.LearningCentreButton.hide()
        self.main_title.setText("Stock Finder")
        self.main_title.adjustSize()
        self.secondary_label.setText("Welcome to the Stock Finder - this is where you can choose stock to buy and sell!")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.secondary_label.setFont(font)
        self.update_secondary()
        self.secondary_label.setGeometry(QtCore.QRect(80, 70, 541, 81))
        self.GOOGButton = QtWidgets.QPushButton(self.centralwidget)
        self.GOOGButton.setGeometry(QtCore.QRect(20, 190, 93, 28))
        self.GOOGButton.setText("GOOG")
        self.AMLButton = QtWidgets.QPushButton(self.centralwidget)
        self.AMLButton.setGeometry(QtCore.QRect(20, 250, 93, 28))
        self.AMLButton.setText("AML.L")
        self.TSLAButton = QtWidgets.QPushButton(self.centralwidget)
        self.TSLAButton.setGeometry(QtCore.QRect(20, 310, 93, 28))
        self.TSLAButton.setText("TSLA")
        self.stock_finder_image.setText("Alphabet Inc. (Google)")
        self.stock_finder_image.setGeometry(QtCore.QRect(150, 200, 161, 16))
        self.portfolio_image.setText("Aston Martin Lagonda Global Holdings plc")
        self.portfolio_image.setGeometry(QtCore.QRect(140, 260, 281, 16))
        self.learning_centre_image.setText("Tesla, Inc")
        self.learning_centre_image.setGeometry(QtCore.QRect(140, 315, 281, 16))

        # makes the buttons blue
        self.GOOGButton.setStyleSheet("background-color : cyan")
        self.AMLButton.setStyleSheet("background-color : cyan")
        self.TSLAButton.setStyleSheet("background-color : cyan")

        self.GOOGButton.show()
        self.AMLButton.show()
        self.TSLAButton.show()

    def portfolio(self):
        self.PortfolioButton.hide()
        self.StockFinderButton.hide()
        self.LearningCentreButton.hide()
        self.main_title.setText("Portfolio")
        self.main_title.setGeometry(QtCore.QRect(350, 10, 191, 41))
        self.main_title.adjustSize()
        self.secondary_label.setGeometry(QtCore.QRect(40, 65, 111, 21))
        self.secondary_label.setText("Account value:")
        self.update_secondary()
        self.stock_finder_image.setGeometry(QtCore.QRect(160, 70, 91, 21))
        self.stock_finder_image.setText("£20,000")
        self.portfolio_image.setGeometry(QtCore.QRect(420, 70, 101, 21))
        self.portfolio_image.setText("Free funds:")
        self.learning_centre_image.setGeometry(QtCore.QRect(330, 70, 61, 21))
        self.learning_centre_image.setText("£10,000")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 70, 71, 21))
        self.label_4.setText("Invested:")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 70, 61, 21))
        self.label_7.setText("£5,000")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(590, 70, 71, 21))
        self.label_8.setText( "Return:")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 70, 81, 21))
        self.label.setText("+£10,000:")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(730, 70, 61, 21))
        self.label_2.setText("(50%)")
        self.secondary_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.secondary_label_2.setGeometry(QtCore.QRect(20, 120, 771, 21))
        self.secondary_label_2.setText("Stock     |      Quantity     |     Purchase Price     |    Current Price   |   Total Value   |   Today\'s Change     |     Total Gain /Loss  ")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 170, 47, 13))
        self.label_9.setText("GOOG")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 220, 47, 13))
        self.label_10.setText("AML.L")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 270, 47, 13))
        self.label_11.setText("TSLA")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(100, 170, 661, 16))
        self.label_12.setText("         10                    £3.50                      £4.00                     £40.00                   +0.1")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(80, 220, 661, 16))
        self.label_13.setText("             10                      £3.50                   £4.00                    £40.00                   +0.1")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(100, 270, 651, 16))
        self.label_14.setText("         10                     £3.50                    £4.00                   £40.00                    +0.1")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 90, 791, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 60, 791, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.secondary_label.setFont(font)
        self.secondary_label_2.setFont(font)
        self.label.setFont(font)
        self.label_4.setFont(font)
        self.label_7.setFont(font)
        self.label_8.setFont(font)
        self.label_2.setFont(font)
        self.label_14.setFont(font)
        self.label_13.setFont(font)
        self.label_12.setFont(font)
        self.secondary_label_2.setFont(font)
        self.learning_centre_image.setFont(font)
        self.portfolio_image.setFont(font)
        self.stock_finder_image.setFont(font)
        self.label_9.setFont(font)
        self.label_10.setFont(font)
        self.label_11.setFont(font)
        self.label.show()
        self.label_4.show()
        self.label_7.show()
        self.label_8.show()
        self.label_2.show()
        self.label_9.show()
        self.label_14.show()
        self.label_13.show()
        self.label_11.show()
        self.label_12.show()
        self.label_10.show()
        self.secondary_label_2.show()
        self.line.show()
        self.line_2.show()

def window():
    #driver code
    app = QApplication(sys.argv)
    #setting up application
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
    #clean exit - closing application after Q has been close

window()