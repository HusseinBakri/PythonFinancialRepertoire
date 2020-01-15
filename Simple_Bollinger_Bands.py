#!/usr/bin/python3
'''
Background reading: https://www.investopedia.com/terms/b/bollingerbands.asp
'''

'''
Description:
------------
This Python script draws the Bollinger Bands plot of Apple stocks.
It uses a manual traditional widely used way.

API Used: Yahoo Finance

Duration: Data from 2012-1-1 till now

Requirements:
------------
Make sure that Pandas, pandas_datareader, numpy, matplotlib are installed

Usage: 
-----
python Simple_Bollinger_Bands.py

Dr. Hussein Bakri
Enjoy!
'''

import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

# Retrieving Apple prices from 2012 till now
# You can also specify to DataReader only the start day with the end date being today
start_date = "2012-1-1"

Apple_Stocks_Data = web.DataReader('AAPL', data_source='yahoo', start=start_date)
print(Apple_Stocks_Data.head())

# Check index of data should be the Date column - Date colum should be Datetime
print(Apple_Stocks_Data.index)

#if not
# Use the following to transfomr Date into Datetime - uncomment if needed
# Apple_Stocks_Data['Date'] = Apple_Stocks_Data['Date'].apply(pd.to_datetime)

# Setting Date as index
# Apple_Stocks_Data.set_index('Date', inplace=True)

############ Plotting Bollinger Bands for Apple stocks ##############
#### The Simple method #####
# Adjusted Closed price 20 days moving average (A)
Apple_Stocks_Data['Close 20 Days Mean'] = Apple_Stocks_Data['Close'].rolling(20).mean()

# Upper band = A + 2* std(A)
Apple_Stocks_Data['Upper Band'] = Apple_Stocks_Data['Close 20 Days Mean'] + 2 * (Apple_Stocks_Data['Close'].rolling(20).std())

# Lower band = A - 2* Std(A)
Apple_Stocks_Data['Lower Band'] = Apple_Stocks_Data['Close 20 Days Mean'] - 2 * (Apple_Stocks_Data['Close'].rolling(20).std())

(Apple_Stocks_Data[['Close','Close 20 Days Mean','Upper Band','Lower Band']]).plot(figsize = (15, 6))
# Plot Title
plt.title('Apple Stocks - Simple Bollinger Bands plot')

# X-Axis Label 
# plt.xlabel('Dates', fontsize=12)
plt.xlabel('Dates')

# Y-Axis Label 
plt.ylabel('Adjusted Closing Prices')

# Saving the plot - specifying a DPI
plt.savefig('Apple_Simple_Bollinger_Bands.png')
plt.savefig('Apple_Simple_Bollinger_Bands_300DPI.png', dpi=300)

# Uncomment the following if you want to see the plot during execution of the script
plt.show()


