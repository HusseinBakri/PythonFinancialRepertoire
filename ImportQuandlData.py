#!/usr/bin/python3

'''
Description:
------------
A script that retrieves financial data from Quantl (https://www.quandl.com/)

Requirements:
------------
First install the Quantl module via pip per example: "pip install quandl"
Pandas should also be installed.

There is no need for an API key in order to retrive just basic information.
You can of course request an API by creating a free account. 
There are different types of licences that you can buy.

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
You can when you sign in retrieve all datasets and Databases on the website
There is under export Data, Libraries -> Python

Some Quandl Databases IDs
--------------------------
U.S. Energy Information Administration Data             EIA 
CFTC Commitment of Traders Data                         CFTC
Core US Stock Fundamentals                              SF1
Federal Reserve Economic Data                           FRED
etc..

Under each database there is usually a big number of datasets

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
EIA_GAS = quandl.get("EIA/AEO_2016_REF_NO_CPP_PRCE_NA_COMM_NA_NG_NA_SATL_Y13DLRPMCF_A", start_date="2010-12-31", end_date="2012-1-1")
print(EIA_GAS.head())

########### Saving Data ##################
########### Saving as CSV ################
EIA_GAS.to_csv('EIA_GAS.csv')

########### Saving as Excel #############
EIA_GAS.to_excel('EIA_GAS.xlsx')




