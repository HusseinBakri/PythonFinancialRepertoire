#!/usr/bin/python3
'''
Description:
------------
This Python script creates a candle stick plot for Apple stocks in November 2019.
It used mplfinance module which is a matplotlib utilities for the visualization, and
visual analysis, of financial data.

matplotlib.finance is deprecated now

API Used: Yahoo Finance

Requirements:
------------
Make sure that Pandas, pandas_datareader, numpy, matplotlib, Pillow are installed

mplfinance should be installed:
pip install mplfinance

Usage: 
-----
python OneMonth_Candle_Stick_Plot.py

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
General Motors                      GM
General Electric Company            GE
Alphabet Inc Class A (Google)       GOOGL
Tesla                               TSLA
'''

import numpy as np
import pandas as pd
from pandas_datareader import data as web
from datetime import datetime
import matplotlib.pyplot as plt

# For matplotlib Financial plots
import mplfinance as mpf

# Retrieving Apple stock prices
start_date = datetime(2019, 11, 1) 
end_date =  datetime(2019, 11, 30) 

Apple_Stocks_Nov2019 = web.DataReader('AAPL', data_source='yahoo', start=start_date, end=end_date)
print(Apple_Stocks_Nov2019.head())

# Always Check index of data should be the Date column - Date colum should be Datetime
print(Apple_Stocks_Nov2019.index)

# if this is not the case
# Use the following to transform Date Colum into Datetime - uncomment if needed
# Apple_Stocks_Data['Date'] = Apple_Stocks_Data['Date'].apply(pd.to_datetime)

# Setting Date as index
# Apple_Stocks_Data.set_index('Date', inplace=True)

# Type Candle
# mpf.plot(Apple_Stocks_Nov2019, type='candlestick')
mpf.plot(Apple_Stocks_Nov2019, type='candle')

# Type ohlc which is the default
mpf.plot(Apple_Stocks_Nov2019)

# Saving the Candle Stick figure
mpf.plot(Apple_Stocks_Nov2019, type='candle', savefig='OneMonthAppleCandleStick.png')

# Saving the Candle Stick figure as PNG specifying a DPI
mpf.plot(Apple_Stocks_Nov2019, type='candlestick', savefig=dict(fname='OneMonthAppleCandleStick.png', dpi=300, pad_inches=0.25))

