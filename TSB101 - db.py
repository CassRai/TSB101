#importing all the necessary modules
import sqlite3
import csv
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


conn = sqlite3.connect("TSB101.db")
c = conn.cursor()
#connects to the database and creates a cursor to interact with db
c.execute("""CREATE TABLE IF NOT EXISTS username_password( 
                username NOT NULL PRIMARY KEY,
                password CHAR(8)
                CONSTRAINT CheckPassword CHECK(LENGTH(password) = 8)
                CONSTRAINT CheckUsername CHECK(LENGTH(username) <= 10 and LENGTH(username) >=5)
                )""")
#creates username_password table with two attributes username and password

c.execute("""CREATE TABLE IF NOT EXISTS portfolio(
             username CHAR, 
             stock_symbol VARCHAR(4),
             company_name TEXT,
             stock_qty INT,
             purchase_price FLOAT,
             current_price FLOAT,
             total_value FLOAT,
             free_funds FLOAT,
             allocated_funds FLOAT,
             change_today FLOAT,
             total_gain_loss FLOAT,
             FOREIGN KEY (username) REFERENCES username_password(username),
             FOREIGN KEY (stock_symbol) REFERENCES individual_stock(stock_symbol)
            )""")
#creates portfolio table with 11 different attributes and establishes the username attribute as a foreign key
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS individual_stock(
             stock_symbol NOT NULL PRIMARY KEY,
             company_name TEXT,
             price FLOAT
            )""")

#creates fundamental_data table with many key stastics attributes as well as using two foreign keys
#stock_symbol and company_name are attributes from the portfolio table that need to be referenced
c.execute("""CREATE TABLE IF NOT EXISTS fundamental_data(
             stock_symbol NOT NULL PRIMARY KEY,
             company_name TEXT,
             P_E_ratio FLOAT,
             PEGY_ratio FLOAT,
             shares_outstanding FLOAT,
             price_book_ratio FLOAT,
             price_sales_ratio FLOAT,
             one_year_return FLOAT,
             thirty_day_avg_volume FLOAT,
             EPS FLOAT, 
             FOREIGN KEY (stock_symbol) REFERENCES individual_stock(stock_symbol),
             FOREIGN KEY(company_name) REFERENCES individual_stock(company_name)
            )""")

conn.commit()

#4 testing modules
def insert(a,b):
    c.execute("INSERT or IGNORE INTO username_password VALUES(?,?)", (a,b))
#ignore - is so the code wont crash if there are duplicating values
def insert2(a,b,d):
    c.execute("INSERT or IGNORE INTO individual_stock VALUES(?,?,?)", (a,b,d))
#ignore - is so the code wont crash if there are duplicating values
def insert3(a,b,d,e,f,g,h,i,j,k,l):
    c.execute("INSERT or IGNORE INTO portfolio VALUES(?,?,?,?,?,?,?,?,?,?,?)", (a,b,d,e,f,g,h,i,j,k,l))
#ignore - is so the code wont crash if there are duplicating values
def insert4(a,b,d,e,f,g,h,i,j,k):
    c.execute("INSERT or IGNORE INTO fundamental_data VALUES(?,?,?,?,?,?,?,?,?,?)", (a,b,d,e,f,g,h,i,j,k))

#testing data for username_password table, should only allow 4 entries based on constraints
#insert("cass1234","pass1234")
#insert("cass1234","password")
#insert("james","password1234")
#insert("henry","12345678")
#insert("sam123","catsdogs")
#insert("downton","jackjill")
#insert("BorisJohnson","password")
#insert("","898")
#insert("a","")
#conn.commit()


#testing data for individual_stock table
#insert2("AMZN","Amazon",3048.41)
#insert2("APPL","Apple",110.44)
#insert2("UBER","Uber Technologies, Inc. ",35.77)
#insert2("A","A",40.3)
#insert2("","BC",40.9)

#testing data for portfolio table
insert3("Cass1234","AMZN","Amazon",39.41,59.60,30.4,0.94,0.18,0.93, -0.08, -0.58)
insert3("Cass1234","AMZN","Amazon",39.444441,59.550,30.4,1.94,0.18,0.93, +0.28, +1.4)
insert3("sam123", "APPL","Apple","0.04","0.008",81.29,30.4,1.94,0.93,-0.008,-0.98)
insert3("Henry","A","A",39.41,59.60,81.29,30.4,0.94,0.18,10.9828, +0.114)
insert3("downton", "UBER","Uber Technologies, Inc. ",35.77, 59.60,81.29,30.4,0.18,0.93,+0.00001,+0.1)
insert3("BorisJohnson", "YHOO","Yahoo!","0.04","0.008",81.29,30.4,1.94,0.93,-0.008,-0.98)
conn.commit()


#testing data for fundamental_data table
#insert4("AMZN","Amazon",39.41,59.60,81.29,30.4,0.94,0.18,0.93,10.9828)
#insert4("AMZN","Amazon",39.444441,59.550,81.29,30.4,1.94,0.18,0.93,10.9828)
#insert4("APPL","Apple","a","b",81.29,30.4,1.94,0.18,0.93,10.9828)
#insert4("A","A",39.41,59.60,81.29,30.4,0.94,0.18,0.93,10.9828)
#insert4("UBER","Uber Technologies, Inc. ",35.77, 59.60,81.29,30.4,0.94,0.18,0.93,10.9828)
#conn.commit()

def window():
    app = QApplication(sys.argv)
    #setting up application
    window = QMainWindow()
    window.setGeometry(200,200,300,300)
    #4 arguments - (x position, y position, width,height)
    window.setWindowTitle("TSB101")

    window.show()
    sys.exit(app.exec())
    #clean exit - closing application after Q has been closed



def get_historical_data(name, number_of_days):
    #yahoo stock function - gets the historical data from the stock of your choice
    datafile = open(name + ".csv","r")
    #will open different stock depending on the stock entered as argument
    datareader = csv.reader(datafile, delimiter=";")
    data = []
    #gets the data from the amazon csv file
    print(name)
    print(number_of_days)
    for each_row in datareader:
            data.append(each_row)
        #puts each row in csv file into 2d array
    return data[:number_of_days]

#Test
for i in get_historical_data('AAPL', 5):
   print(i)

c.execute("SELECT * FROM Portfolio WHERE purchase_price=?",(59.6,))
conn.commit()
x = c.fetchall()


