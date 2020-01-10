#!/usr/bin/python3
'''
Description:
------------
A script that calculates the rate of return of certain stock Market Indices
It plots the graphs so we can understand better the concept.

API Used: Yahoo Finance
S&P500, NASDAQ, DAX30, Dowjones
Market_Indices_tickers = ['^GSPC','^IXIC', '^GDAXI', '^DJI']

Requirements:
------------
Make sure that Pandas, pandas_datareader, numpy, matplotlib and xlrd are installed
no need for anything else

Usage: 
-----
python Calculate_Historical_Rate_of_Return_Marketindex.py

Dr. Hussein Bakri
Enjoy!
'''

'''
Some famous Market indices to work with
------------------------------------------------
Standard & Poor's 500 (S&P500)                  ^GSPC       Scope:USA
Dowjones                                        ^DJI        Scope:USA
NASDAQ                                          ^IXIC       Scope:USA mainly IT companies               
DAX30                                           ^GDAXI      Scope: Germany
Nikkei 225                                                  Scope: Japan
Financial Times Stock Exchange (FTSE100)        ^FTSE       Scope: London/UK
SSE Composite Index                                         Scope: China
'''

import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import datetime

# We will be calculating the historical rate of return of S&P500, NASDAQ, German DAX30, FTSE100 & DowJones, 
# from 1st of January 2000 until today
# For some reason Yahoo Finance is not fetching anymore '^FTSE' so we will discard it
Market_Indices_tickers = ['^GSPC','^IXIC', '^GDAXI', '^DJI']

start_date = "2000-1-1"
end_date = datetime.now()

MarketIndices_Data = pd.DataFrame()

for ticker in Market_Indices_tickers:
    MarketIndices_Data[ticker] = web.DataReader(ticker, data_source='yahoo', start=start_date)['Adj Close']

print(MarketIndices_Data.head())
print(MarketIndices_Data.tail())


############ Calculating Rate of return of the Market Indices #############
# Formula of calculating simple rate is very simple: (P1-P0)/P0 or (P1/P0) - 1
# Single Rate of Return: (Price on Day1 - Price on Day0)/Price on Day0
# For the whole table of Market Indices it will be:
Returns_forMarketIndices = (MarketIndices_Data / MarketIndices_Data.shift(1)) - 1
print("\nReturns for all Market Indices -----")
print(Returns_forMarketIndices.head())

#### The average annual single rate of returns  of all Markets ####
# It is important to know the number of trading days till now from
# The NYSE and NASDAQ average about 253 trading days a year. 
# This is from 365.25 (days on average per year) * 5/7 (proportion work days per week) - 6 (weekday holidays) - 3*5/7 (fixed date holidays) = 252.75 ≈ 253.
Average_Simple_Annual_Returns_AllMarkets = Returns_forMarketIndices.mean() * 253
print("\nThe 4 Markets Average Simple Annual Returns ------ ")
print(Average_Simple_Annual_Returns_AllMarkets.head())

############ Now Plotting graphs ###############
MarketIndices_Data.plot(figsize=(15,6))

# Plot Title
plt.title('Market Indices - Not Normalised')

# X-Axis Label 
# plt.xlabel('Dates', fontsize=12)
plt.xlabel('Dates')

# Y-Axis Label 
plt.ylabel('Market Indices Adjusted Closing Prices')

# Saving the plot - specifying high DPI
plt.savefig('MarketIndices_NotNormalised.png')
plt.savefig('MarketIndices_NotNormalised300DPI.png', dpi=300)

# Uncomment the following if you want to see the plot during execution of the script
# plt.show()

############### Ploting normalised graph ######
### Normalisation: first row/first row * 100 = 100
# this means that all the graphs will start from 100 (one point of comparision)

(MarketIndices_Data / MarketIndices_Data.iloc[0] * 100).plot(figsize = (15, 6))
# Plot Title
plt.title('Market Indices - Normalised to 100')

# X-Axis Label 
# plt.xlabel('Dates', fontsize=12)
plt.xlabel('Dates')

# Y-Axis Label 
plt.ylabel('Market Indices Adjusted Closing Prices')

# Saving the plot - specifying high DPI
plt.savefig('MarketIndices_Normalised.png')
plt.savefig('MarketIndices_Normalised300DPI.png', dpi=300)

# Uncomment the following if you want to see the plot during execution of the script
# plt.show()

############ Saving Data ##################
############ Saving as CSV ################
MarketIndices_Data.to_csv('MarketIndices_Data.csv')

############ Saving as Excel #############
MarketIndices_Data.to_excel('MarketIndices_Data.xlsx')