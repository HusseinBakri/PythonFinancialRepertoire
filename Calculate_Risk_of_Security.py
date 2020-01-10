#!/usr/bin/python3
'''
Description:
------------
This Python script calculates the risk of securities.
It plots also graphs so we can understand better the concept.

API Used: Yahoo Finance

I am comparing the risk of Apple vs Ford
Duration: 2010-1-1 till now

Requirements:
------------
Make sure that Pandas, pandas_datareader, numpy, matplotlib and xlrd are installed
no need for anything else

Usage: 
-----
python Calculate_Risk_of_Security.py

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