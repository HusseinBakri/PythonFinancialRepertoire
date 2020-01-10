#!/usr/bin/python3
'''
Description:
------------
A script that retrieves financial data via the API of IEX

Requirements:
------------
Pandas & pandas_datareader should be installed

Register a User https://iexcloud.io/cloud-login#/register 
choose the free plan (if you want), and then verify your email (on the same browser) to get the API Key. 

Then you can check your API KEYS, URLS and Usage on this web site https://iexcloud.io/console/

NB: Your allotted quota on the free plan is very very very limited. 
Don't test out requests - I advice you to use other providers than IEX.
If you run this script, you would consume all your monthly quota :-)

Follow the method here to retrieve financial data from IEX

Usage: 
-----
python ImportIEXData.py

Dr. Hussein Bakri
Enjoy!
'''

'''
Some famous companies stocks tikers to work with
-----------------------------------------------
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

from datetime import datetime
import pandas as pd
import pandas_datareader.data as web
import os

# API Keys of IEX starts with pk
IEX_API_Token = "pk_APIKEY"
os.environ["IEX_API_KEY"] = IEX_API_Token

start_date = datetime(2018, 1, 1)
end_date = datetime(2019, 1, 1)

Apple_Data = web.DataReader('AAPL', data_source='iex', start='2019-1-1')

# Fetch data between two dates
Facebook_Data = web.DataReader('F', 'iex', start_date, end_date)
# print(Facebook_Data.loc['2018-08-31'])

#### View data #####
print(Apple_Data)
print(Apple_Data.info())
print(Apple_Data.head())
print(Apple_Data.head(50))
print(Apple_Data.tail())
print(Apple_Data.tail(20))

Stock_tickers_Group1 = ['PG', 'MSFT', 'T', 'F', 'GE']
Stock_tickers_Group2 = ['AAPL', 'MSFT', 'XOM', 'BP']

# Loop through a bunch of stock tickers
# Create a empty Pandas data frame
Ticker_Data_Group1 = pd.DataFrame()
for ticker in Stock_tickers_Group1:
    # Store the "close" from 1-1-2019
    Ticker_Data_Group1[ticker] = web.DataReader(ticker, data_source='iex', start='2019-1-1')['close']

print(Ticker_Data_Group1.tail())
print(Ticker_Data_Group1.head())

############ Saving Data ##################
############ Saving as CSV ################
Ticker_Data_Group1.to_csv('Ticker_Data_Group1.csv')

############ Saving as Excel #############
Ticker_Data_Group1.to_excel('Ticker_Data_Group1.xlsx')

# To read back from CSV
Ticker_Data_Group1_CSV = pd.read_csv('Ticker_Data_Group1.csv')
# print(Ticker_Data_Group1.head())

# To read back from Excel
Ticker_Data_Group1_EXCEL = pd.read_excel('Ticker_Data_Group1.xlsx')
# print(Ticker_Data_Group1_EXCEL.head())
