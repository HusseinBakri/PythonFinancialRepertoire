#!/usr/bin/python3
import pandas as pd

# Example code

# Read from CSV via Pandas
XYZ = pd.read_csv('XYZ.csv', index_col = 'Date')

# To read back from Excel via Pandas
XYY = pd.read_excel('XYZ.xlsx')
print(XYY.head())

# To read from Excel a specific sheet (like Sheet1)
pd.read_excel('XYZ.xlsx',sheetname='Sheet1')

# To Write to Excel a specific sheet (like Sheet 1) - NB: df is a Pandas dataframe
df.to_excel('XYZ.xlsx',sheet_name='Sheet1')

# To write to CSV (df being a dataframe)
df.to_csv('Test.csv', index=False)

