#!/usr/bin/python3

'''
Description:
------------
A script that retrieves financial data from Quantl (https://www.quandl.com/)

Requirements:
------------
First install the Quantl module via pip per example: "pip install quandl"
Pandas should also be installed.

There is no need for an API key in order to retrive just basic information from free datasets.
You can of course request an API by creating a free account. 
There are different types of licences that you can have. You can also buy a premium licence.

I will show you in this script both methods of using Quandl with an API and without it.

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

'''
There are many Quandl Databases IDs
Please search for what you need (ttps://www.quandl.com/search)
You need to be signed in. You can retrieve all datasets and Databases codes from the website
Choose the table tab,  there is under "Export Data", an option for the Python language (Libraries -> Python)
You will get a popup showing you the Python command that you need to use with the code of the dataset and extra parameters such as dates

Some Quandl Databases Codes
--------------------------
U.S. Energy Information Administration Data             EIA 
CFTC Commitment of Traders Data                         CFTC
Core US Stock Fundamentals                              SF1
Federal Reserve Economic Data                           FRED
etc..

Under each database there is usually a big number of datasets. You can use the free ones.

Example under CFTC, there is:
* Commitment of traders for wheat (CFTC/W_F_ALL)
* etc..
'''

import pandas as pd
import quandl

# With an API KEY or Token - get your API Key from quandl website
API_KEY = "XXXXXXXXXXXXXXXXX"
Commitment_of_Traders_Data = quandl.get("CFTC/06641H_FO_L_CHG", authtoken=API_KEY)
print(Commitment_of_Traders_Data.head())
print(Commitment_of_Traders_Data.tail())

########### Saving Data ##################
########### Saving as CSV ################
Commitment_of_Traders_Data.to_csv('Commitment_of_Traders_Data.csv')

########### Saving as Excel #############
Commitment_of_Traders_Data.to_excel('Commitment_of_Traders_Data.xlsx')

#############  Without API Key or token ################
# Federal Reserve GDP
FRED_GDP = quandl.get("FRED/GDP")
# quandl.get("EIA/PET_RWTC_D")
print(FRED_GDP.head())
print(FRED_GDP.tail())

########### Saving Data ##################
########### Saving as CSV ################
FRED_GDP.to_csv('FRED_GDP.csv')

########### Saving as Excel #############
FRED_GDP.to_excel('FRED_GDP.xlsx')

####### Specifying a start date and an end date for data
EIA_GAS = quandl.get("EIA/AEO_2016_REF_NO_CPP_PRCE_NA_COMM_NA_NG_NA_SATL_Y13DLRPMCF_A", start_date="2015-12-31", end_date="2016-12-31")
print(EIA_GAS.head())

########### Saving Data ##################
########### Saving as CSV ################
EIA_GAS.to_csv('EIA_GAS.csv')

########### Saving as Excel #############
EIA_GAS.to_excel('EIA_GAS.xlsx')

####################### To get stock Prices with Quandl #############
print("\nRetrieving Stock Prices with Quandl ----")
start_date = pd.to_datetime('2015-01-01')
end_date = pd.to_datetime('2018-01-01')

# .11 means get me only the Adjusted Close prices, if you remove it you get Open, Volume etc...
print("\nApple stocks ----")
Apple_Quandl_Stocks = quandl.get("WIKI/AAPL.11", start_date=start_date, end_date=end_date)
print(Apple_Quandl_Stocks.head())
Apple_Quandl_Stocks.to_excel('Apple_Quandl_Stocks.xlsx')

print("\nCISCO stocks ----")
Cisco_Quandl_Stocks = quandl.get("WIKI/CSCO", start_date=start_date, end_date=end_date)
print(Cisco_Quandl_Stocks.head())
Cisco_Quandl_Stocks.to_excel('Cisco_Quandl_Stocks.xlsx')

print("\nIBM stocks ----")
IBM_Quandl_Stocks = quandl.get("WIKI/IBM.11", start_date=start_date, end_date=end_date)
print(IBM_Quandl_Stocks.head())
IBM_Quandl_Stocks.to_excel('IBM_Quandl_Stocks.xlsx')

print("\nAmazon stocks ----")
Amazon_Quandl_Stocks = quandl.get("WIKI/AMZN.11", start_date=start_date, end_date=end_date)
print(Amazon_Quandl_Stocks.head())
Amazon_Quandl_Stocks.to_excel('Amazon_Quandl_Stocks.xlsx')
