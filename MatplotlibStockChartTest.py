import csv
import time
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib



matplotlib.rc('figure', figsize=(8, 5))

def graphData(stock):
    stockFile = stock + ".csv"


    # Subplots are like multiple plots or graphs on the same graph. We use this to get the two y axises of both graphs
    # ax1 is the y-axis for the actual line, and ax2 is the y-axis for the bars
    # we use _ because its just some random variable we dont care about but that is the figure itself for future reference
    _, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # We read the actual csv and store it in the data DataFrame, parse_dates is some built in thing for reading dates
    data = pd.read_csv(stockFile, parse_dates=['Date'])

    # Create a new column for Close - Open using the subtract method to subtract two columns from each other
    data["Diff"] = data.Close.subtract(data.Open)


    # Plot all the close values against the dates
    # and also all the Diffs against the date too with a transparency of 0.5
    ax1.plot(data.Date, data.Close)
    ax2.bar(data.Date, data.Diff, alpha=0.5)

    # Create two labels for each y axis etc etc
    ax1.set_ylabel("Value of Close", color='b')
    ax2.set_ylabel("Close - Open", color='r')


    plt.show()


graphData("AMZN")
