#!/usr/bin/python3
'''
Description:
------------
This Python script calculates the risk of a portfolio of securities

API Used: Yahoo Finance

I am comparing the risk of a portfolio containing  stocks of Apple & Ford with an equal weight investment
Duration: 2010-1-1 till now

Requirements:
------------
Make sure that Pandas, pandas_datareader, numpy and xlrd are installed
no need for anything else

Usage: 
-----
python Calculate_Portfolio_Risk.py

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

Stock_tickers = ['F', 'AAPL']

ComparisionofRisk = pd.DataFrame()

for ticker in Stock_tickers:
    ComparisionofRisk[ticker] = web.DataReader(ticker, data_source='yahoo', start='2010-1-1')['Adj Close']

Returns = np.log(ComparisionofRisk / ComparisionofRisk.shift(1))

print("\n---- Ford Risk Calculations----")
dash = '-' * 100
print(dash)   
print('{:<25s}{:<25s}{:<25s}{:<25s}'.format('Daily Average Return','Annual Return', 'Standard Deviation','Annual Standard Deviation'))
print(dash)   
print('{:<25s}{:<25s}{:<25s}{:<25s}'.format(str(Returns['F'].mean()), str(Returns['F'].mean() * 253), str(Returns['F'].std()), str(Returns['F'].std() * 250 ** 0.5)))

print("\n---- Apple Risk Calculations----")
dash = '-' * 100
print(dash)   
print('{:<25s}{:<25s}{:<25s}{:<25s}'.format('Daily Average Return','Annual Return', 'Standard Deviation','Annual Standard Deviation'))
print(dash)   
print('{:<25s}{:<25s}{:<25s}{:<25s}'.format(str(Returns['AAPL'].mean()), str(Returns['AAPL'].mean() * 253), str(Returns['AAPL'].std()), str(Returns['AAPL'].std() * 250 ** 0.5)))

print("\nAnnual Average Returns")
print(Returns[['F', 'AAPL']].mean() * 253)
print("\nAnnual Standard Deviations")
print(Returns[['F', 'AAPL']].std() * 253 ** 0.5)

print("\n########### Portfolio Risk ###############")
## Suppose I have a portfolio containing Facebook and Ford with equal weights
# In other words, we invested 50% in Facebook and 50% in Ford
Portfolio_Weights = np.array([0.50, 0.50])

# T is for the numpy Transpose notation
Portfolio_Variance = np.dot(Portfolio_Weights.T, np.dot(Returns.cov() * 250, Portfolio_Weights))
print("\nPortfolio Variance ---- ")
print(Portfolio_Variance)

# To calculate the Volatility
print("\nPortfolio Volatility ---- ")
Portfolio_Volatility = (np.dot(Portfolio_Weights.T, np.dot(Returns.cov() * 250, Portfolio_Weights))) ** 0.5
print("Portfolio Volatility: " + str(round(Portfolio_Volatility,3)*100) + " %")