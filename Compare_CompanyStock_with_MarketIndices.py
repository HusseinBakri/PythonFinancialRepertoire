#!/usr/bin/python3
'''
Description:
------------
This Python script compares certain stock prices with rates of returns of certain stock Market Indices
It plots also graph so we can understand better the concept.

API Used: Yahoo Finance

I am comparing Apple with the performance of the markets: S&P500, Dowjones
Market_Indices_tickers = ['^GSPC','^DJI']
Duration: 2010-1-1 till now

Requirements:
------------
Make sure that Pandas, pandas_datareader, numpy, matplotlib and xlrd are installed
no need for anything else

Usage: 
-----
python Compare_CompanyStock_with_MarketIndices.py

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
from datetime import datetime

# I am comparing Apple with performance of the markets: S&P500, Dowjones
# Market_Indices_tickers = ['^GSPC','^DJI']
# Duration: 2010-1-1 till now
MarketAndAppleStock_tickers = ['AAPL','^GSPC','^DJI']
start_date = "2010-1-1"
end_date = datetime.now()

Comparision_Data = pd.DataFrame()

for ticker in MarketAndAppleStock_tickers:
    Comparision_Data[ticker] = web.DataReader(ticker, data_source='yahoo', start=start_date)['Adj Close'] 

print(Comparision_Data.head())
print(Comparision_Data.tail())

############ Now Plotting graphs ###############
############### Ploting normalised graph ######
### Normalisation is done by dividing onto the first row & with first row/first row * 100 = 100
# This means all graphs will start from 100 i.e one point of comparision

(Comparision_Data / Comparision_Data.iloc[0] * 100).plot(figsize = (15, 6))
# Plot Title
plt.title('Comparing Apple with S&P500 & Dowjones - Normalised to 100')

# X-Axis Label 
# plt.xlabel('Dates', fontsize=12)
plt.xlabel('Dates')

# Y-Axis Label 
plt.ylabel('Adjusted Closing Prices')

# Saving the plot - specifying high DPI
plt.savefig('Comparision_Normalised.png')
plt.savefig('Comparision_Normalised300DPI.png', dpi=300)

# Uncomment the following if you want to see the plot during execution of the script
plt.show()