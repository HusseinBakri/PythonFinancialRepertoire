#!/usr/bin/python3
'''
Description:
------------
A script that calculates the rate of return of a certain portfolio of securities.
It plots also graphs so we can understand better the concept.

API Used: Yahoo Finance
Portfolio 1 Used: Apple, GE, Ford and Microsoft
Portfolio1 Weights are equal i.e. each company stocks has 25% weight

Requirements:
------------
Make sure that Pandas, pandas_datareader, numpy, matplotlib and xlrd are installed
no need for anything else

Usage: 
-----
python Calculate_Rate_of_Return_Portfolio.py

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

# Portfolio 1 - Apple, GE, Ford and Microsoft - historical data from 2005-2019
# Portfolio1 Weights are equal i.e. each company stocks has 25% weight
# I will construct the data that I need i.e. the adjusted closing price of these 4 during these years

# You can also specify to DataReader only the start day with the end date being today
start_date = "2010-1-1"
end_date ="2020-1-07"

tickers = ['AAPL','GE','F','GOOGL']
Apple_Data_Yahoo = web.DataReader('AAPL', data_source='yahoo', start=start_date, end=end_date)
GE_Data_Yahoo = web.DataReader('GE', data_source='yahoo', start=start_date, end=end_date)
Ford_Data_Yahoo = web.DataReader('F', data_source='yahoo', start=start_date, end=end_date)
Google_Data_Yahoo = web.DataReader('GOOGL', data_source='yahoo', start=start_date, end=end_date)
Portfolio1_Data_List = [Apple_Data_Yahoo['Adj Close'], GE_Data_Yahoo['Adj Close'], Ford_Data_Yahoo['Adj Close'], Google_Data_Yahoo['Adj Close']]

Portfolio1_Data = pd.concat(Portfolio1_Data_List, axis = 1)
Portfolio1_Data.columns = ['Apple', 'GE','Ford','Google']
print(Portfolio1_Data.tail())

# Print first row
print("\nFirst Row: ")
print(Portfolio1_Data.iloc[0])

# Print row of certain date
print("\nSpecific row: ")
print(Portfolio1_Data.loc['2020-01-03'])

############ Calculating Rate of return of the portfolio #############
# Since the 4 companies security weights are equal (each one 25%)
Portfolio1_Weights = np.array([0.25, 0.25, 0.25, 0.25])

# Formula of calculating simple rate is very simple: (P1-P0)/P0 or (P1/P0) - 1
# Single Rate of Return: (Price on Day1 - Price on Day0)/Price on Day0
# For the whole portfolio it will be:
Returns_forPortfolio = (Portfolio1_Data / Portfolio1_Data.shift(1)) - 1
print(Returns_forPortfolio.head())

# Another way of calculating rate of change is using the Pandas pct_change()
# Returns_forPortfolio = Portfolio1_Data.pct_change(1)
# print(Returns_forPortfolio.head())

# The average annual single rate of return  of portfolio
# It is important to know the number of trading days till now from
# "The NYSE and NASDAQ average about 253 trading days a year."" 
# "This is from 365.25 (days on average per year) * 5/7 (proportion work days per week) - 6 (weekday holidays) - 3*5/7 (fixed date holidays) = 252.75 ≈ 253."
Average_Simple_Annual_Return_Portfolio = Returns_forPortfolio.mean() * 253
print("\nPortfolio Average Simple Annual Return ------ ")
print(Average_Simple_Annual_Return_Portfolio)

#It remains to calculate the final number while taking into consideration the weights in the portfolio
Portfolio_Rate_of_Return = str(round(np.dot(Average_Simple_Annual_Return_Portfolio, Portfolio1_Weights), 3)*100) + " %"
print("\nFinal Portfolio Rate of Return------ ")
print(Portfolio_Rate_of_Return)

############ Now Plotting graphs ###############
Portfolio1_Data.plot(figsize=(15,6))

# Plot Title
plt.title('Portfolio 1 - Not Normalised')

# X-Axis Label 
# plt.xlabel('Dates', fontsize=12)
plt.xlabel('Dates')

# Y-Axis Label 
plt.ylabel('Stock Adjusted Closing Price')

# Saving the plot - specifying a DPI
plt.savefig('Portforlio1_NotNormalised.png')
plt.savefig('Portforlio1_NotNormalised300DPI.png', dpi=300)

# Uncomment the following if you want to see the plot during execution of the script
# plt.show()

############### Ploting normalised graph ######
### Normalisation: first row/first row * 100 = 100
# this means all graphs will start from 100 (one point of comparision)

(Portfolio1_Data / Portfolio1_Data.iloc[0] * 100).plot(figsize = (15, 6))
# Plot Title
plt.title('Portfolio 1 - Normalised to 100')

# X-Axis Label 
# plt.xlabel('Dates', fontsize=12)
plt.xlabel('Dates')

# Y-Axis Label 
plt.ylabel('Stock Adjusted Closing Price')

# Saving the plot - specifying high DPI
plt.savefig('Portforlio1_Normalised.png')
plt.savefig('Portforlio1_Normalised300DPI.png', dpi=300)

# Uncomment the following if you want to see the plot during execution of the script
# plt.show()

############ Saving Data ##################
############ Saving as CSV ################
Portfolio1_Data.to_csv('Portfolio1_Data.csv')

############ Saving as Excel #############
Portfolio1_Data.to_excel('Portfolio1_Data.xlsx')
