#!/usr/bin/python3

'''
Description:
------------
A script that calculates the natural logarithm of single rate of return.
It plots graphs so we can understand better the concept.

API Used: Yahoo Finance

Requirements:
------------
Make sure that Pandas, pandas_datareader, numpy, matplotlib and xlrd are installed
no need for anything else

Usage: 
-----
python Calculate_Logarithmic_Single_Rate_of_Return.py

Dr. Hussein Bakri
Enjoy!
'''

'''
Some famous companies stocks tikers to work with
------------------------------------------------
Apple                               AAPL
Procter & Gamble Co                 PG
Microsoft Corporation               MSFT
Exxon Mobil Corporation             XOM
BP plc                              BP
AT&T Inc.                           T
Ford Motor Company                  F
General Electric Company            GE
Alphabet Inc Class A (Google)       GOOGL
'''

import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

# Retrieving Apple prices from start of year 2019 till the end of it
# You can also specify to DataReader only the start date with the end date being by default today
start_date = "2019-1-1"
end_date = "2019-12-31"
Apple_Data_Yahoo = web.DataReader('AAPL', data_source='yahoo', start=start_date, end=end_date)

# Formula is very simple: ln(P1/P0) or ln(P1)-ln(P0)
# Natural logarith of Single Rate of Return: Logarithm(Price on Day1/Price on Day0)
# Price is always the adjusted closing price

# To calculate natural logarithm of simple daily return for Apple
Apple_Data_Yahoo['Logarithm Simple Daily Return'] = np.log(Apple_Data_Yahoo['Adj Close'] / Apple_Data_Yahoo['Adj Close'].shift(1))
# In the first row, you will see a NaN (Not a Number) which is normal since 
# we are dividing ln of Current day over previous day which in the case of first row absent. 
print (Apple_Data_Yahoo['Logarithm Simple Daily Return'])

############ Saving Data ##################
############ Saving as CSV ################
Apple_Data_Yahoo.to_csv('Apple_Data_Log_Yahoo.csv')

############ Saving as Excel #############
Apple_Data_Yahoo.to_excel('Apple_Data_Log_Yahoo.xlsx')

# The logarithmic average daily single rate of return is good to know
Average_Log_Simple_Daily_Return_Apple = Apple_Data_Yahoo['Logarithm Simple Daily Return'].mean()
print("\nApple Logarithmic Average Simple Daily Return for 2019 is: " + str(Average_Log_Simple_Daily_Return_Apple*100) + " %")

# The logarithmic average annual single rate of return is also good to know
# It is important to know the number of trading days till now from
# "The NYSE and NASDAQ average about 253 trading days a year." 
# "This is from 365.25 (days on average per year) * 5/7 (proportion work days per week) - 6 (weekday holidays) - 3*5/7 (fixed date holidays) = 252.75 ≈ 253."
Average_Log_Simple_Annual_Return_Apple = Apple_Data_Yahoo['Logarithm Simple Daily Return'].mean() * 253
print("\nApple Logarithmic Average Simple Annual Return for 2019 is: " + str(round(Average_Log_Simple_Annual_Return_Apple,3)*100) +" %")

# Plotting the natural logarithm of Simple Daily Return over 1 year (2019)
Apple_Data_Yahoo['Logarithm Simple Daily Return'].plot(figsize=(8, 5))
plt.show()
