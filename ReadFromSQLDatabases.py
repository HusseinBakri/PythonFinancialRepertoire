#!/usr/bin/python3

'''
Description:
------------
This Python script retrieves stock data from Yahoo finance and store them in different SQL databses.
It teaches you how to do that in SQLite.

Requirements:
------------
Make sure that Pandas  is installed

Depending on what SQL RDMS you are using whether sqlite, postgreeSQl or MySQL.
You can install a general purpose library called SQLAlchemy via pip
pip install SQLAlchemy.

For SQLite
----------
We will store the data in .db file. You can also use the .sqlite extension

Usage: 
-----
python ReadFromSQLDatabases.py

Dr. Hussein Bakri
Enjoy!
'''

from sqlalchemy import create_engine

import pandas as pd
from pandas_datareader import data as web

StockAndMarket_tickers = ['SBUX', '^IXIC']
start_date = "2015-1-1"

ComparitionofStockToMarket = pd.DataFrame()
for ticker in StockAndMarket_tickers:
    ComparitionofStockToMarket[ticker] = web.DataReader(ticker, data_source='yahoo', start=start_date)['Adj Close']   

#### Printing Data gathered from Yahoo Finance ##########
print("\nData from Yahoo Finance ---")
print(ComparitionofStockToMarket.head())

############ For SQLite ################
print("\n Writing to SQLite DB ---")

# To keep the database in memory (RAM)
# SQLite_Engine = create_engine('sqlite:///:memory:', echo=True)
# SQLite_Engine = create_engine('sqlite:///:memory:')

print("Storing a Pandas dataframe in a SQLite Database...")

# To store database in a .db file. PS: you can use the extension .sqlite also
# You can use a famous tool called DB Browser for SQLite to view your .db database
# https://sqlitebrowser.org/
SQLite_Engine_onFile = create_engine("sqlite:///database.db")

ComparitionofStockToMarket.to_sql('ComparisionOfStocksTable', SQLite_Engine_onFile)

############## Reading from SQLite Database ############
print("\n Reading from SQLite DB ---")
SQL_Dataframe = pd.read_sql('ComparisionOfStocksTable', con=SQLite_Engine_onFile)
print(SQL_Dataframe.head())

############## For MySQL #############
# Will be added later