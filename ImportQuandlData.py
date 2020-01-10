#!/usr/bin/python3

'''
Description:
------------
A script that retrieves financial data from Quantl (https://www.quandl.com/)

Requirements:
------------
First install the Quantl module via pip per example: "pip install quandl"
Pandas should also be installed.

There is no need for an API key (at the time of writing of this script).
Follow the method here to retrieve financial data via Quandl.

Usage: 
-----
python ImportQuandlData.py

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

import pandas as pd
import quandl

FRED_GDP = quandl.get("FRED/GDP")
print(FRED_GDP.head())
print(FRED_GDP.tail())

############ Saving Data ##################
############ Saving as CSV ################
FRED_GDP.to_csv('FRED_GDP.csv')

############ Saving as Excel #############
FRED_GDP.to_excel('FRED_GDP.xlsx')

