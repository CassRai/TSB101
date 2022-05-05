Main Program
#importing modules
import sqlite3
import csv
import datetime
import sys
import time

import numpy as np
import pandas as pd

from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QVBoxLayout, QHBoxLayout,QGridLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QFrame, QStackedWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

from LearningCentre import Ui_LearningCentre
from Portfolio import Portfolio
from stock_finder import StockFinder
from dashboard import Dashboard

conn = sqlite3.connect("TSB101.db")
c = conn.cursor()

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        c.execute("INSERT or IGNORE INTO username_password VALUES(?,?)", (self.username, self.password))
        # if you try to create a user with a name already in the DB the db will ignore this request
        # good so the program wont crash
        conn.commit()

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
        secondary_label = QLabel("Welcome to TSB101's Sign-Up - Password = 8 characters and Username =  5 to 10 characters", self)
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
        self.username_textbox = QLineEdit(self)
        self.password_textbox = QLineEdit(self)
        self.submit_button = QPushButton("Submit", self)

        #fixing the position and size of labels, buttons and textboxes
        main_title.setGeometry(QtCore.QRect(330, 20, 111, 51))
        secondary_label.setGeometry(QtCore.QRect(170, 110, 741, 131))
        username_label.setGeometry(QtCore.QRect(190, 220, 91, 21))
        password_label.setGeometry(QtCore.QRect(190, 290, 91, 21))
        self.username_textbox.setGeometry(QtCore.QRect(310, 220, 201, 20))
        self.password_textbox.setGeometry(QtCore.QRect(310, 290, 201, 20))
        self.submit_button.setGeometry(QtCore.QRect(330, 380, 131, 41))

        #setting submit button to blue
        self.submit_button.setStyleSheet("background-color : cyan")

class Log_In(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        #creating labels for sign-up widget
        main_title = QLabel("Login", self)
        main_title.adjustSize()
        self.secondary_label = QLabel("Welcome to TSB101's Login - Login Into Your Account!", self)
        self.secondary_label.adjustSize() #contents of label are too large for the standard size of label - need to resize

        username_label = QLabel("Username", self)
        password_label = QLabel("Password", self)

        font = QtGui.QFont() #setting font for password and username labels
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        username_label.setFont(font)
        password_label.setFont(font)

        font2(self,self.secondary_label,main_title)

        #textbox is where the user will enter their information
        self.username_textbox = QLineEdit(self)
        self.password_textbox = QLineEdit(self)
        self.submit_button = QPushButton("Submit", self)

        #fixing the position and size of labels, buttons and textboxes
        main_title.setGeometry(QtCore.QRect(330, 20, 111, 51))
        self.secondary_label.setGeometry(QtCore.QRect(168, 110, 441, 31))
        username_label.setGeometry(QtCore.QRect(190, 220, 91, 21))
        password_label.setGeometry(QtCore.QRect(190, 290, 91, 21))
        self.username_textbox.setGeometry(QtCore.QRect(310, 220, 201, 20))
        self.password_textbox.setGeometry(QtCore.QRect(310, 290, 201, 20))
        self.submit_button.setGeometry(QtCore.QRect(330, 380, 131, 41))

        #setting submit button to blue
        self.submit_button.setStyleSheet("background-color : cyan")


class Graph(QWidget):
    def __init__(self, parent, stock):
        super(Graph, self).__init__(parent)
        self.stock = stock
        self.setLayout(QVBoxLayout())
        self.canvas = PlotCanvas(self, self.stock, width=10, height=8)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout().addWidget(self.toolbar)
        self.layout().addWidget(self.canvas)

class PlotCanvas(FigureCanvas):
    def __init__(self,stock, parent=None, width=13, height=9, dpi=105):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.stock = stock
        FigureCanvas.__init__(self, fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot(self.stock)

    def plot(self,stock):

        stockFile = stock.stock + ".csv"


        ax1 = self.figure.add_subplot()
        ax2 = ax1.twinx()

        data = pd.read_csv(stockFile, parse_dates=['Date'])
        data["Diff"] = data.Close.subtract(data.Open)

        ax1.plot(data.Date, data.Close)
        ax2.bar(data.Date, data.Diff, alpha=0.5)

        ax1.set_ylabel("Value of Close", color='b')
        ax2.set_ylabel("Close - Open", color='r')

        ax1.set_title(stock.stock)

        self.show()

class Individual_Stock(QWidget):
    def __init__(self, parent, stock):
        super(Individual_Stock, self).__init__(parent)
        self.setStyleSheet("background-color: white")
        self.stock = stock

        self.buy_button = QPushButton('Buy', self)
        self.return_button = QPushButton("Return", self)
        self.sell_button = QPushButton('Sell', self)

        self.buy_button.setStyleSheet("background-color : green")
        self.return_button.setStyleSheet("background-color : cyan")
        self.sell_button.setStyleSheet("background-color : red")

        self.buy_button.setFixedSize(90, 50)
        self.return_button.setFixedSize(90, 50)
        self.sell_button.setFixedSize(90, 50)

        StockChart = Graph(self,self.stock)
        layout = QGridLayout()
        layout.addWidget(StockChart, 2, 2)
        layout.addWidget(self.buy_button, 4, 1)
        layout.addWidget(self.return_button, 1, 1)
        layout.addWidget(self.sell_button, 4, 3)
        self.widget = QWidget(self)
        self.widget.setLayout(layout)


class MyWindow(QMainWindow):
    # inherits all of properties from QMainWindow
    def __init__(self):
        super(MyWindow, self).__init__()
        # will run whenever an instance of MyWindow is created
        self.setGeometry(100, 100, 1100, 700)
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
        LogButton.clicked.connect(lambda: self.setCentralWidget(LogInObject)) #connecting Log_In Object to Sign-Up Button
        LogInObject.submit_button.clicked.connect(lambda: Log_in_check())

        SignUpObject = Sign_Up(self) #creating Sign_Up object
        SignButton.clicked.connect(lambda: self.setCentralWidget(SignUpObject)) #connecting SignUp Object to Sign-Up Button
        SignUpObject.submit_button.clicked.connect(lambda: Sign_up_check())

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

        stackedwidget = QStackedWidget(self) #creating the stacked widget object
        DashboardWidget = Dashboard(self) #creating the objects of each class that is a section of our program
        PortfolioWidget = Portfolio()
        StockFinderWidget = StockFinder()
        LearningCentreWidget = Ui_LearningCentre()
        AAPL_IndividualStockWidget = Individual_Stock(self,"AAPL")
        AMZN_IndividualStockWidget = Individual_Stock(self, "AMZN")
        TSLA_IndividualStockWidget = Individual_Stock(self, "TSLA")

        AAPL_IndividualStockWidget.buy_button.clicked.connect(lambda: Individual_stock_buy("APPL"))
        AMZN_IndividualStockWidget.buy_button.clicked.connect(lambda: Individual_stock_buy("AMZN"))
        TSLA_IndividualStockWidget.buy_button.clicked.connect(lambda: Individual_stock_buy("TSLA"))

        AAPL_IndividualStockWidget.sell_button.clicked.connect(lambda: Individual_stock_sell("APPL"))
        AMZN_IndividualStockWidget.sell_button.clicked.connect(lambda: Individual_stock_sell("AMZN"))
        TSLA_IndividualStockWidget.sell_button.clicked.connect(lambda: Individual_stock_sell("TSLA"))

        PortfolioWidget.refresh_button.clicked.connect(lambda: PortolioRefresh())

        stackedwidget.addWidget(DashboardWidget) #adding the Dashboard, Porfolio and Stock Finder to the stackedwidget
        stackedwidget.addWidget(PortfolioWidget)#index 1
        stackedwidget.addWidget(StockFinderWidget) #index 2
        stackedwidget.addWidget(LearningCentreWidget) #index3
        stackedwidget.addWidget(AAPL_IndividualStockWidget.widget) #index4
        stackedwidget.addWidget(AMZN_IndividualStockWidget.widget) #index5
        stackedwidget.addWidget(TSLA_IndividualStockWidget.widget) #index6

        stackedwidget.setCurrentIndex(0) #this basically means that the Dashboard widget will be index 0
        stackedwidget.setCurrentWidget(DashboardWidget)

        DashboardWidget.PortfolioButton.clicked.connect(lambda: stackedwidget.setCurrentIndex(1))
        DashboardWidget.StockFinderButton.clicked.connect(lambda: stackedwidget.setCurrentIndex(2))
        DashboardWidget.LearningCentreButton.clicked.connect(lambda: stackedwidget.setCurrentIndex(3))

        StockFinderWidget.AAPLButton.clicked.connect(lambda: stackedwidget.setCurrentIndex(4))
        StockFinderWidget.AMZNButton.clicked.connect(lambda: stackedwidget.setCurrentIndex(5))
        StockFinderWidget.TSLAButton.clicked.connect(lambda: stackedwidget.setCurrentIndex(6))

        AAPL_IndividualStockWidget.return_button.clicked.connect(lambda: stackedwidget.setCurrentIndex(0))
        AMZN_IndividualStockWidget.return_button.clicked.connect(lambda: stackedwidget.setCurrentIndex(0))
        TSLA_IndividualStockWidget.return_button.clicked.connect(lambda: stackedwidget.setCurrentIndex(0))

        PortfolioWidget.return_button.clicked.connect(lambda: stackedwidget.setCurrentIndex(0))
        LearningCentreWidget.return_button.clicked.connect(lambda: stackedwidget.setCurrentIndex(0))

        def Log_in_check(): #LogIn Check
            global current_user
            username = LogInObject.username_textbox.text() #users input from username and password textbox
            password = LogInObject.password_textbox.text()

            check = c.execute("SELECT * FROM username_password WHERE username = ? AND password = ?",(username, password)) #checking to see if user exists in table
            conn.commit()
            check2 = c.fetchone() #fetches one result from database
            if check2 == None: #if nothing is fetched - user does not exist
                time.sleep(2)
                current_user = User(username,password)
                self.setCentralWidget(SignUpObject) #swtiches to Signup page

            else:
                current_user = User(username, password)
                self.setCentralWidget(stackedwidget) #user must exist - takes user to dashboard

        def Sign_up_check(): #Sign_up Check
            global current_user
            username = SignUpObject.username_textbox.text() #users input from username and password textbox
            password = SignUpObject.password_textbox.text()

            check = c.execute("SELECT * FROM username_password WHERE username = ? AND password = ?",(username, password)) #checking to see if user exists in table
            conn.commit()
            check2 = c.fetchone() #fetches one result from database
            if check2 == None : #if nothing is fetched - user does not exist
                if len(password) == 8 and len(username) >= 5 and len(username) <= 10:
                    current_user = User(username,password)
                    self.setCentralWidget(stackedwidget)
            else: #user exists
                time.sleep(2)
                current_user = User(username, password)
                self.setCentralWidget(LogInObject)  # swtiches to Signup page

        def Individual_stock_buy(stock):
            stock_num = 0
            check = c.execute("SELECT stock_qty FROM portfolio WHERE username = ? AND stock_symbol = ?",(current_user.username, stock))
            conn.commit()
            check2 = c.fetchall()
            print(check2)
            if check2 == []:
                stock_num += 1
            else:
                length = len(check2) - 1
                tuple = check2
                stock_num = tuple[length][0]
                stock_num += 1

            total_value = stock_num * 121.44
            print(stock_num)
            c.execute("INSERT into portfolio VALUES(?,?,?,?,?,?,?,?,?,?,?)",(current_user.username,stock,stock,stock_num,121.44,121.44, total_value, 0, 0, 0, 0))
            conn.commit()

        def Individual_stock_sell(stock):
            stock_num = 0
            check = c.execute("SELECT stock_qty FROM portfolio WHERE username = ? AND stock_symbol = ?",(current_user.username, stock))
            conn.commit()
            check2 = c.fetchall()
            if check2 != []:
                length = len(check2) - 1
                tuple = check2
                stock_num = tuple[length][0]
                stock_num -= 1

                total_value = stock_num * 121.44
                c.execute("INSERT into portfolio VALUES(?,?,?,?,?,?,?,?,?,?,?)",(current_user.username, stock, stock, stock_num, 121.44, 121.44, total_value, 0, 0, 0, 0))
                conn.commit()

        def PortolioRefresh():
            check_APPL_list = []
            check_TSLA_list = []
            check_AMZN_list = []

            check_APPL = c.execute("""SELECT stock_qty,purchase_price,current_price,total_value,change_today,total_gain_loss
                                FROM portfolio WHERE username = ? AND stock_symbol = ?""",(current_user.username, "APPL"))

            conn.commit()
            check_APPL_result = c.fetchall()
            if check_APPL_result != []:
                length = len(check_APPL_result) - 1
                for i in range(6):
                    check_APPL_list.append(check_APPL_result[length][i])

            check_AMZN = c.execute("""SELECT stock_qty,purchase_price,current_price,total_value,change_today,total_gain_loss
                                            FROM portfolio WHERE username = ? AND stock_symbol = ?""",
                                   (current_user.username, "AMZN"))

            conn.commit()
            check_AMZN_result = c.fetchall()
            if check_AMZN_result != []:
                length = len(check_AMZN_result) - 1
                for i in range(6):
                    check_AMZN_list.append(check_AMZN_result[length][i])

            check_TSLA = c.execute("""SELECT stock_qty,purchase_price,current_price,total_value,change_today,total_gain_loss
                                            FROM portfolio WHERE username = ? AND stock_symbol = ?""",
                                   (current_user.username, "TSLA"))

            conn.commit()

            check_TSLA_result = c.fetchall()
            if check_TSLA_result != []:
                length = len(check_TSLA_result) - 1
                for i in range(6):
                    check_TSLA_list.append(check_TSLA_result[length][i])

            remove_content = ["'", "[", "]"]  # Content you want to be removed from `str`

            check_APPL_string = repr(check_APPL_list)  # convert list to `str`
            check_TSLA_string = repr(check_TSLA_list)
            check_AMZN_string = repr(check_AMZN_list)


            for content in remove_content:
                check_APPL_string = check_APPL_string.replace(content, '')
                check_TSLA_string = check_TSLA_string.replace(content, '')
                check_AMZN_string = check_AMZN_string.replace(content, '')


            PortfolioWidget.stock1_result.setText(check_APPL_string)
            PortfolioWidget.stock2_result.setText(check_AMZN_string)
            PortfolioWidget.stock3_result.setText(check_TSLA_string)



def window():
    #driver code
    app = QApplication(sys.argv)
    #setting up application
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
    #clean exit - closing application after Q has been close

window()
