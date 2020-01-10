#!/usr/bin/python3
'''
Description:
------------
A script that retrieves financial data via the API of Alpha Vantage

Requirements:
------------
Install the alpha-vantage module via pip: "pip install alpha-vantage"
Make sure also that Pandas, pandas_datareader, numpy and xlrd are installed

You have to claim a free API key from https://www.alphavantage.co/documentation/

Usage: 
-----
python ImportAlphaVantageAPI.py

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

API_KEY = "YOUR_API_KEY_HERE"
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key = API_KEY, output_format='pandas')

# get_daily_adjusted() method obtains the adjusted closing prices for the designated stock.
PG_data, PG_metadata = ts.get_daily_adjusted('PG', outputsize='full')
# print(PG_data)

# Apple company stocks ticker is 'AAPL'
AAPL_data, AAPL_metadata = ts.get_daily_adjusted('AAPL', outputsize='full')
# print(AAPL_data)

# Apart from US stocks, you can retrieve data about foreign stocks (e.g. Beiersdorf, ticker: 'BEI.DE'), 
# or market indices (e.g. Standard & Poor's, ticker: '^GSPC', or Dow Jones, ticker: '^DJI').
GSPC_data, GSPC_metadata = ts.get_daily_adjusted('^GSPC', outputsize='full')
# print(GSPC_data)
GSPC_data.info()

print(GSPC_data.head(15))

# To combine specific columns from various stocks, one would need to concatenate the columns of interest by using the .concat() function to specify which columns you want to extract.
portfolio = pd.concat([PG_data['5. adjusted close'], GSPC_data['5. adjusted close']], axis = 1)
portfolio.columns = ['PG Adjusted Close', 'GSPC Adjusted Close']
# print(portfolio)

############ Saving Apple Data ###########
############ Saving as CSV ################
AAPL_data.to_csv('AAPL_data.csv')

############ Saving as Excel #############
AAPL_data.to_excel('AAPL_data.xlsx')

# To read back from CSV
AAPL_data_CSV = pd.read_csv('AAPL_data.csv')
# print(AAPL_data_CSV.head())

# To read back from Excel
AAPL_data_EXCEL = pd.read_excel('AAPL_data.xlsx')
# print(AAPL_data_EXCEL.head())