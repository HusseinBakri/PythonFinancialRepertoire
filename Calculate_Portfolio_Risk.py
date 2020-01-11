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

# Calculating Variance and Covariance of securities
Ford_Variance = Returns['F'].var()
print("\nFord Variance: " + str(Ford_Variance)) 

Apple_Variance = Returns['AAPL'].var()
print("\nApple Variance: " + str(Ford_Variance))

# Calculating Annual Variance and Covariance
# It is important to know the number of trading days till now from
# "The NYSE and NASDAQ average about 253 trading days a year."" 
# "This is from 365.25 (days on average per year) * 5/7 (proportion work days per week) - 6 (weekday holidays) - 3*5/7 (fixed date holidays) = 252.75 ≈ 253."
Ford_Variance_Annual = Returns['F'].var() * 253
print("\nAnnual Ford Variance: " + str(Ford_Variance_Annual)) 

Apple_Variance_Annual = Returns['AAPL'].var() * 253
print("\nApple Variance: " + str(Apple_Variance_Annual)) 

print("\nCovariance Matrix between securities ----")
Covariance_Matrix = Returns.cov()
print(Covariance_Matrix)

print("\nAnnual Covariance Matrix between securities ----")
Covariance_Matrix_Annual = Returns.cov() * 253
print(Covariance_Matrix_Annual)

print("\nCorrelation Matrix between securities ----")
Correlation_Matrix = Returns.corr()
print(Correlation_Matrix)

print("\n########### Portfolio Risk ###############")
## Suppose I have a portfolio containing Apple and Ford with equal weights
# In other words, we invested 50% in Apple and 50% in Ford
Portfolio_Weights = np.array([0.50, 0.50])

# T is for the numpy Transpose notation
Portfolio_Variance = np.dot(Portfolio_Weights.T, np.dot(Returns.cov() * 253, Portfolio_Weights))
print("\nPortfolio Variance ---- ")
print(Portfolio_Variance)

# To calculate the Volatility
print("\nPortfolio Volatility ---- ")
Portfolio_Volatility = (np.dot(Portfolio_Weights.T, np.dot(Returns.cov() * 253, Portfolio_Weights))) ** 0.5
print("Portfolio Volatility: " + str(round(Portfolio_Volatility,3)*100) + " %")

print("\n#### Diversifiable and Non-Diversifiable Risk of a Portfolio ####")
print("\nDiversifiable Risk ---- ")
# Formula for Diversifiable Risk = portfolio variance - weighted annual variance
Diversifiable_Risk = Portfolio_Variance - (Portfolio_Weights[0] ** 2 * Apple_Variance_Annual) - (Portfolio_Weights[1] ** 2 * Ford_Variance_Annual)
print("\nDiversifiable Risk: " + str(round(Diversifiable_Risk,2)*100) + " %")

print("\nNon-Diversifiable Risk ---- ")
print("First Method of Calculation-- ")
NonDiversifiable_Risk = Portfolio_Variance - Diversifiable_Risk
print("Non Diversifiable Risk via method 1: " + str(round(NonDiversifiable_Risk,2)*100) + " %")

print("\nSecond Method of Calculation-- ")
NonDiversifiable_Risk2= (Portfolio_Weights[0] ** 2 * Apple_Variance_Annual) + (Portfolio_Weights[1] ** 2 * Ford_Variance_Annual)
print("Non Diversifiable Risk: " + str(round(NonDiversifiable_Risk2,2)*100) + " %")
