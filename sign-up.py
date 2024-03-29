# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign-up.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_title = QtWidgets.QLabel(self.centralwidget)
        self.main_title.setGeometry(QtCore.QRect(330, 20, 111, 51))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(26)
        self.main_title.setFont(font)
        self.main_title.setObjectName("main_title")
        self.secondary_label = QtWidgets.QLabel(self.centralwidget)
        self.secondary_label.setGeometry(QtCore.QRect(170, 110, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.secondary_label.setFont(font)
        self.secondary_label.setObjectName("secondary_label")
        self.stock_finder_image = QtWidgets.QLabel(self.centralwidget)
        self.stock_finder_image.setGeometry(QtCore.QRect(190, 220, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stock_finder_image.setFont(font)
        self.stock_finder_image.setObjectName("stock_finder_image")
        self.portfolio_image = QtWidgets.QLabel(self.centralwidget)
        self.portfolio_image.setGeometry(QtCore.QRect(190, 290, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.portfolio_image.setFont(font)
        self.portfolio_image.setObjectName("portfolio_image")
        self.username_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.username_textbox.setGeometry(QtCore.QRect(310, 220, 201, 20))
        self.username_textbox.setObjectName("username_textbox")
        self.pass_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_textbox.setGeometry(QtCore.QRect(310, 290, 201, 20))
        self.pass_textbox.setObjectName("pass_textbox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 380, 131, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_title.setText(_translate("MainWindow", "Sign up"))
        self.secondary_label.setText(_translate("MainWindow", "Welcome to TSB101\'s Sign-Up - Create an account!"))
        self.stock_finder_image.setText(_translate("MainWindow", "Username"))
        self.portfolio_image.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
