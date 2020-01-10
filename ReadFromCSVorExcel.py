#!/usr/bin/python3
import pandas as pd

# Examples
# Read from CSV via Pandas
XYZ = pd.read_csv('XYZ.csv', index_col = 'Date')


# To read back from Excel via Pandas
XYY = pd.read_excel('XYZ.xlsx')
print(XYY.head())