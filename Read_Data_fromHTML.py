#!/usr/bin/python3

'''
Description:
------------
This Python script retrieves data from an HTML(web) page using Beautifulsoup and Pandas

Requirements:
------------
Make sure that Pandas and BeautifulSoup4 are installed
no need for anything else

Usage: 
-----
python Read_Data_fromHTML.py

Dr. Hussein Bakri
Enjoy!
'''

from bs4 import BeautifulSoup
import pandas as pd

Web_URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
# Pandas will store all the tables in the web page into a list
Data_as_list = pd.read_html(Web_URL)
Dataframe_fromList =  pd.DataFrame(Data_as_list[0]) 
print(Dataframe_fromList)
