#!/usr/bin/python3
'''
Background Reading to understand this tool ----
Paper: Portfolio Selection - Harry Markowitz 1952 URL:
https://www.math.ust.hk/~maykwok/courses/ma362/07F/markowitz_JF.pdf
https://www.investopedia.com/terms/e/efficientfrontier.asp
https://en.wikipedia.org/wiki/Efficient_frontier
https://en.wikipedia.org/wiki/Markowitz_model

The idea is that there is an efficent set of portfolio containing different securities
with different weights of investments and for each amount of risk investor is willing to indure.
This set of efficient portfolios can be calculated and discovered. This script helps us understand how!
Enjoy!
'''
'''
Description:
------------
This Python script calculates Markowitz Efficient Frontier
API Used: Yahoo Finance

I am studying the efficiency (Markowitz-wise) of 500 portfolios containing only
stocks of Apple & Ford with many random weights for each portfolio
Duration: Data from 2010-1-1 till now

Requirements:
------------
Make sure that Pandas, pandas_datareader, numpy, matplotlib and xlrd are installed
no need for anything else

Usage: 
-----
python Calculate_Markowitz_Efficient_Frontier.py

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
import matplotlib.pyplot as plt

# Ford is F and Apple is AAPL
Stock_tickers = ['F', 'AAPL']

ComparisionofEfficiency = pd.DataFrame()

# Duration: 2010-1-1 till now from Yahoo Finance
for ticker in Stock_tickers:
    ComparisionofEfficiency[ticker] = web.DataReader(ticker, data_source='yahoo', start='2010-1-1')['Adj Close']

# Normalising to 100 and ploting the data of both stock
(ComparisionofEfficiency / ComparisionofEfficiency.iloc[0] * 100).plot(figsize=(10, 5))
# Plot Title
plt.title('Comparing Apple with Ford - Normalised to 100')

# X-Axis Label 
# plt.xlabel('Dates', fontsize=12)
plt.xlabel('Dates')

# Y-Axis Label 
plt.ylabel('Adjusted Closing Prices')

# Saving the plot - specifying high DPI
plt.savefig('Comparision_Normalised.png')
plt.savefig('Comparision_Normalised300DPI.png', dpi=300)

# Uncomment the following if you want to see the plot during the execution of the script
# plt.show()

# Calculating their logarithmic rate of returns
Logarithmic_Returns = np.log(ComparisionofEfficiency / ComparisionofEfficiency.shift(1))
# print(Logarithmic_Returns.head())

print("\nAnnual Logarithmic Averages of Returns")
# It is important to know the number of trading days in a year
# "The NYSE and NASDAQ average about 253 trading days a year."" 
# "This is from 365.25 (days on average per year) * 5/7 (proportion work days per week) - 6 (weekday holidays) - 3*5/7 (fixed date holidays) = 252.75 ≈ 253."
print(Logarithmic_Returns.mean() * 253)

Logarithmic_Returns_Variance_Annual = Logarithmic_Returns.var() * 253
print("\nAnnual Logarithmic Returns Variance") 
print(Logarithmic_Returns_Variance_Annual)

print("\nAnnual Logarithmic Covariance Matrix between securities ----")
Covariance_Matrix_Covariance_Annual = Logarithmic_Returns.cov() * 253
print(Covariance_Matrix_Covariance_Annual)

print("\nChecking the correlation between securities (Logarithmic)")
Correlation_Matrix = Logarithmic_Returns.corr()
print(Correlation_Matrix)

## Suppose I have a portfolio containing Apple and Ford with different weights
# In other words, we have invested 45% worth of stocks in Ford and 65% in Apple
Portfolio_Weights = np.array([0.45, 0.65])

print("\nExpected Annual Portfolio Return ----")
Expected_Portfolio_Return_Annually = np.sum(Portfolio_Weights * Logarithmic_Returns.mean())*253
print(Expected_Portfolio_Return_Annually)

print("\nExpected Annual Portfolio Variance ----")
Expected_Portfolio_Variance_Annually = np.dot(Portfolio_Weights.T, np.dot(Logarithmic_Returns.cov() * 253, Portfolio_Weights))
print(Expected_Portfolio_Variance_Annually)

print("\nExpected Annual Portfolio Volatility ----")
Expected_Portfolio_Volatility_Annually = (np.dot(Portfolio_Weights.T, np.dot(Logarithmic_Returns.cov() * 253, Portfolio_Weights))) ** 0.5
print(Expected_Portfolio_Volatility_Annually)

#### Markowitz Efficient Frontier Calculation for 500 portfolios of random weights' combinations ####
# Per example: Portfolio 1 could be 1% investment in Ford, 99% investment in Apple
# Portfolio 2: could be 34% in Ford, 66% in Apple
# etc..

Portfolio_Returns = []
Portfolio_Volatilities = []

for instance in range (500):
    # The following two lines create two random numbers that sums to 1 ie 100%
    Current_Portfolio_Random_Weights = np.random.random(len(Stock_tickers))
    Current_Portfolio_Random_Weights = Current_Portfolio_Random_Weights/np.sum(Current_Portfolio_Random_Weights)
    # Logarithmic_Returns for the two stocks is calculated before in the script
    # Calculating each return & appending it to the corresponding list
    Portfolio_Returns.append(np.sum(Current_Portfolio_Random_Weights * Logarithmic_Returns.mean()) * 253)
    # Calculating each Volatility & appending it to the corresponding list
    Portfolio_Volatilities.append(np.sqrt(np.dot(Current_Portfolio_Random_Weights.T, np.dot(Logarithmic_Returns.cov() * 253, Current_Portfolio_Random_Weights))))

# Transforming Python lists to numpy arrays  
Portfolio_Returns = np.array(Portfolio_Returns)
Portfolio_Volatilities = np.array(Portfolio_Volatilities)

AllPortfolios = pd.DataFrame({'Portfolio Return': Portfolio_Returns, 'Portfolio Volatility': Portfolio_Volatilities})
# print(AllPortfolios.head())
# print(AllPortfolios.tail())

############# Plotting ###############
AllPortfolios.plot(x='Portfolio Volatility', y='Portfolio Return', kind='scatter', figsize=(10, 6))

# Plot Title
plt.title('Markowitz Efficient Frontier')

# X-Axis Label 
plt.xlabel('Expected Portfolio Volatility')

# Y-Axis Label 
plt.ylabel('Expected Portfolio Return')

# Saving the plot - specifying high DPI
plt.savefig('Markowitz.png')
plt.savefig('Markowitz300DPI.png', dpi=300)

# Uncomment the following if you want to see the plot during execution of the script
plt.show()