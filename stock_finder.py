from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QVBoxLayout, QHBoxLayout,QGridLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QFrame, QStackedWidget

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


class StockFinder(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        #creating labels for Stock Finder widget
        main_title = QLabel("Stock Finder", self)
        secondary_label = QLabel("Welcome to the Stock Finder - this is where you can choose stock to buy and sell!", self)
        font2(self, secondary_label, main_title)  # setting font for main title and secondary label

        self.AMZNButton = QPushButton("AMZN", self) #creating stock buttons
        self.TSLAButton = QPushButton("TSLA", self)
        self.AAPLButton = QPushButton("AAPL",self)

        self.AMZNButton.setStyleSheet("background-color : cyan") #setting button colours
        self.AAPLButton.setStyleSheet("background-color : cyan")
        self.TSLAButton.setStyleSheet("background-color : cyan")

        AMZNLabel = QLabel("Amazon.com, Inc.", self) #creating labels
        AAPLLabel = QLabel("Apple Inc.", self)
        TSLALabel = QLabel("Tesla, Inc.", self)

        main_title.setGeometry(320,20,231, 51) #setting position and size of buttons and labels
        secondary_label.setGeometry(10, 70, 800, 81)

        self.AMZNButton.setGeometry(20, 190, 93, 28)
        self.AAPLButton.setGeometry(20, 250, 93, 28)
        self.TSLAButton.setGeometry(20, 310, 93, 28)
        AMZNLabel.setGeometry(140, 200, 161, 16)
        AAPLLabel.setGeometry(140, 260, 281, 16)
        TSLALabel.setGeometry(140, 315, 281, 16)