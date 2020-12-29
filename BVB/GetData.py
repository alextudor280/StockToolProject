import pandas as pd
from pandas_datareader import data as wb

# Getting data from online sources like yahoo.

AAPL = wb.DataReader('AAPl', data_source='yahoo', start='2015-1-1')

symbol = ['AAPl', 'F', 'TSLA', 'MSFT', 'GE']
important_company_price = pd.DataFrame()
for s in symbol:
    important_company_price[s] = wb.DataReader(s, data_source='yahoo', start='2015-1-1')['Adj Close']

# print(AAPL)

# print(important_company_price)

# Getting data from offline sources like a .csv file

import quandl

#mydata = quandl.get("FRED/GDP")  # for US/GDP price

#mydata.to_csv(r"C:\Users\alex_\Desktop\New.csv") #This fills the file "New.csv" with the data in mydata variable

#mydata2 = pd.read_csv(r"C:\Users\alex_\Desktop\Phynance course\57 Importing Data - Part III\CSV\Python 3 CSV\Data_03.xlsx") #For reading from a file in the pc

