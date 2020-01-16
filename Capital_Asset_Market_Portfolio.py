#!/usr/bin/python3
'''
Essential Background Reading to understand this tool ----
Paper: Portfolio Selection - Harry Markowitz 1952 URL:
https://www.math.ust.hk/~maykwok/courses/ma362/07F/markowitz_JF.pdf
https://en.wikipedia.org/wiki/Capital_asset_pricing_model
https://www.investopedia.com/terms/c/capm.asp
https://en.wikipedia.org/wiki/Efficient_frontier
https://en.wikipedia.org/wiki/Markowitz_model

Beta
---
https://www.investopedia.com/terms/b/beta.asp
https://www.investopedia.com/investing/beta-know-risk/
https://en.wikipedia.org/wiki/Beta_(finance)

https://www.investopedia.com/terms/l/libor.asp

We will
1) ===== Calculate the BETA of a stock vis-a vis the market ======
We will start by calculating Beta which is a measurement that shows us how risky an individual security
in comparision with the rest of the market. In other words, it quantifies or measures the relationship
between a particular security per example a particular stock and the overall market portfolio.
Precisely it is an indication of the amount of risk that a security bears regarding the market portfolio.

Beta is calculated as: (covariance between the stock and the market)/variance of the market.
The higher the Beta, the riskier the stock (ie more bound to lose in bad economic conditions)
--IF--
A stock of Beta= zero, this means the stock has no relationship regarding the market.
A stock of Beta<1 called defensive stock because if the market does poorly the stock is bound to lose but to lesser extent.
A stock of Beta=1 of one will perform in the same way as the market performs (positively or negatively).
A stock of Beta>1 do way worse than the market when things are not good (economic recession or depression),
in similar do way better than the market when things are good.

Essential Companies of Food and medicine usually (not always) have betas that are 
near zero ex 0.05, 0.1, 0.2 since people will keep buying them in economic crisis.

The market portfolio is defined as all securities in the market meaning all securities with low expected
return and low risk and all the securities with high expected return and high risk.
a stock with high level of volatility => performs bad in times of crisis (economic recession etc...)

2) Calculating the expected return of a stock using CAPM
ER = Rf + βi(ERm−Rf)
​ER: expected return of investment 
Rf: Risk-free asset
βi: Beta of the investment or stock
(ERm-RF): market risk premium

Thre is no risk free asset in real life but economists usually consider this as
a 10 years or 5 years governmental bonds which are the safest investment.
Some consider puting money in a bank saving account as a risk free investment or the London InterBank Offered Rate (LIBOR)
Economists consider 5% as an accepted market risk premium

We can get governmental bonds numbers from Bloomberg Website:
https://www.bloomberg.com/markets/rates-bonds/government-bonds/uk
The UK 10 year governmental bond: 0.77%
The USA 10 year governmental bond: 1.82%

3) Calculating the Sharpe Ratio
Background reading: William Sharpe
https://www.investopedia.com/terms/s/sharperatio.asp
https://www.investopedia.com/articles/07/sharpe_ratio.asp
Sharpe Ratio = (Rp - Rf)/σp
​Rf: Risk-free asset
Rp: Return of portfolio
σp: Standard deviation of the portfolio's excess return​	 
​	
'''
'''
Description:
------------
This Python script do many calculations that pertains to Capital Asset Pricing Model (CAPM)
1) Beta calculation: Calculate the BETA of a stock vis-a vis the market
2) Calculate the expected return of a stock using CAPM
3) Calculate the Sharpe Ratio

API Used: Yahoo Finance

Duration: Data from 2015-1-1 till now

Requirements:
------------
Make sure that Pandas, pandas_datareader, numpy, matplotlib and xlrd are installed
no need for anything else

Usage: 
-----
python Capital_Asset_Market_Portfolio.py

Dr. Hussein Bakri
Enjoy!
'''

'''
Since we will be also working with Markets
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
I included some that deals with medicine, food and beverages
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
Alphabet Inc Class C (Google)       GOOG
eBay Inc.                           EBAY
Netflix                             NFLX
Cisco Systems                       CSCO
Starbucks Corporation               SBUX
Alexion Pharmaceuticals             ALXN
Walgreen Boots Alliance, Inc        WBA
'''

import numpy as np
import pandas as pd
from pandas_datareader import data as web

# Please compare a stock to the market in which it is most relevant (Google the stock)
# Below comparing Starbucks to NASDAQ
# 5 years data is taken into consideration
StockAndMarket_tickers = ['SBUX', '^IXIC']
start_date = "2015-1-1"

ComparitionofStockToMarket = pd.DataFrame()
for ticker in StockAndMarket_tickers:
    ComparitionofStockToMarket[ticker] = web.DataReader(ticker, data_source='yahoo', start=start_date)['Adj Close']   

StocksAndMarket_Logarithmic_Returns = np.log( ComparitionofStockToMarket / ComparitionofStockToMarket.shift(1) )
print(StocksAndMarket_Logarithmic_Returns.head())
# It is important to know the number of trading days in a year
# "The NYSE and NASDAQ average about 253 trading days a year."" 
# "This is from 365.25 (days on average per year) * 5/7 (proportion work days per week) - 6 (weekday holidays) - 3*5/7 (fixed date holidays) = 252.75 ≈ 253."
StockAndMarket_Logarithmic_Returns_Covariance = StocksAndMarket_Logarithmic_Returns.cov() * 253
print(StockAndMarket_Logarithmic_Returns_Covariance.head())

# Get only the covariance between stock & the market from the table
Covariance_between_StockAndMarket = StockAndMarket_Logarithmic_Returns_Covariance.iloc[0,1]
print("CoVariance between stock and market: "+ str(Covariance_between_StockAndMarket))

Market_Variance = StocksAndMarket_Logarithmic_Returns['^IXIC'].var() * 253
print("NASDAQ Market Variance: "+ str(Market_Variance))

############# Beta Calculation #############
print("Calculating Beta of Starbucks compared to the NASDAQ Market ----")
Starbucks_Beta = Covariance_between_StockAndMarket / Market_Variance
print(Starbucks_Beta)

# Calculating the expected return of Starbucks using CAPM
print("\nExpected Return of Starbuks using CAPM in US market ----")
# From Bloomberg Website:
# https://www.bloomberg.com/markets/rates-bonds/government-bonds/uk
# The UK 10 year governmental bond: 0.77%
# The USA 10 year governmental bond: 1.82%
# Economists consider 5% as an accepted market risk premium
Governmental_10Year_Bond_UK = 0.007
Governmental_10Year_Bond_US = 0.0182
# ER = Rf + βi(ERm−Rf)
Expected_Return_Starbukcs_CAPM = Governmental_10Year_Bond_US + Starbucks_Beta * 0.05
print(str(round(Expected_Return_Starbukcs_CAPM,4)*100)+ " %")

# Calculating the Sharpe ratio of Starbucks using CAPM
print("\nSharpe ratio of Starbucks using CAPM ----")
# Sharpe Ratio = (Rp - Rf)/σp
# ​Rf: Risk-free asset such as a governmental bond
# Rp: Return of portfolio
# σp: Standard deviation of the portfolio's excess return​
Sharpe_Ratio_Starbukcs = (Expected_Return_Starbukcs_CAPM - Governmental_10Year_Bond_US) / (StocksAndMarket_Logarithmic_Returns['SBUX'].std() * 253 ** 0.5)
print(Sharpe_Ratio_Starbukcs)
