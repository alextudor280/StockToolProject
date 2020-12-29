import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

#GATHERING DATA

indexes = ['^GSPC', '^IXIC', '^GDAXI', '^RUT']

ind_data = pd.DataFrame()
for i in indexes:
    ind_data[i] = wb.DataReader(i, data_source='yahoo', start='2010-1-1')['Adj Close']

#NORMALISING DATA AND CREATING CHART

((ind_data / ind_data.iloc[0]) * 100).plot(figsize=(15, 6))
plt.show()

#CALCULATING THE SIMPLE RETURNS

ind_returns = (ind_data / ind_data.shift(1)) - 1

ind_daily_returns = ind_returns.mean()*100

ind_annual_returns = ind_daily_returns * 250
print(ind_annual_returns)