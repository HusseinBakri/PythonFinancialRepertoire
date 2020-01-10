#!/usr/bin/python3

'''
Description:
------------
A script that retrieves financial data via the API of Yahoo! Finance

Requirements:
------------
Make sure also that Pandas, pandas_datareader, numpy and xlrd are installed

no need for anything else

Usage: 
-----
python ImportYahooFinanceDataAPI.py

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

Apple_Data_Yahoo = web.DataReader('AAPL', data_source='yahoo', start='2019-1-1')

print(Apple_Data_Yahoo.head())
print(Apple_Data_Yahoo.tail())

############ Saving Data ##################
############ Saving as CSV ################
Apple_Data_Yahoo.to_csv('Apple_Data_Yahoo.csv')

############ Saving as Excel #############
Apple_Data_Yahoo.to_excel('Apple_Data_Yahoo.xlsx')

# To read back from CSV
Apple_Data_Yahoo_CSV = pd.read_csv('Apple_Data_Yahoo.csv')
# print(Apple_Data_Yahoo_CSV.head())

# To read back from Excel
Apple_Data_Yahoo_EXCEL = pd.read_excel('Apple_Data_Yahoo.xlsx')
# print(Apple_Data_Yahoo_EXCEL.head())