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

class Portfolio(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # creating main title for Portfolio widget
        main_title = QLabel("Portfolio", self)

        real_return_value1 = QLabel(self)
        real_return_value2 = QLabel(self)
        header = QLabel("Stock     |      Quantity     |     Purchase Price     |    Current Price   |   Total Value   |   Today\'s Change     |     Total Gain /Loss  ",self)
        header.adjustSize()
        stock1 = QLabel("AAPL", self)
        stock2 = QLabel("AMZN", self)
        stock3 = QLabel("TSLA", self)
        self.stock1_result = QLabel(self)
        self.stock2_result = QLabel(self)
        self.stock3_result = QLabel(self)

        self.return_button = QPushButton("Return", self)
        self.refresh_button = QPushButton("Refresh", self)

        line1 = QFrame(self)  # creating lines for dividing sections
        line2 = QFrame(self)

        font1(self, main_title)  # setting fonts

        font = QtGui.QFont()
        font.setPointSize(10)

        header.setFont(font)
        stock1.setFont(font)
        stock2.setFont(font)
        stock3.setFont(font)
        self.stock1_result.setFont(font)
        self.stock2_result.setFont(font)
        self.stock3_result.setFont(font)

        main_title.setGeometry(350, 10, 191, 41)#setting Geometry
        header.setGeometry(20, 120, 741, 21)
        stock1.setGeometry(20, 170, 47, 13)
        stock2.setGeometry(20, 220, 47, 13)
        stock3.setGeometry(20, 270, 47, 13)
        self.stock1_result.setGeometry(70, 125, 661, 100)
        self.stock2_result.setGeometry(70, 165, 661, 100)
        self.stock3_result.setGeometry(70, 230, 651, 100)

        line1.setGeometry(20, 90, 791, 20)
        line2.setGeometry(20, 60, 791, 16)

        self.return_button.setGeometry(10,500,90,50)
        self.refresh_button.setGeometry(590,500,90,50)

        self.return_button.setStyleSheet("background-color : cyan")
        self.refresh_button.setStyleSheet("background-color : cyan")