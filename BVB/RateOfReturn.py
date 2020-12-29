from pandas_datareader import data as wb
import numpy as np
import matplotlib.pyplot as plt

# Getting data from online sources like yahoo.

AAPL = wb.DataReader('AAPl', data_source='yahoo', start='2015-1-1')

#Calculating daily return based on the simple return formula (new-old/old)

AAPL['simple_return'] = ((AAPL['Adj Close'] / AAPL['Adj Close'].shift(1)) - 1)*100

AAPL['simple_return'].plot(figsize=(8,5))
print('The plot represents daily returns of AAPL stock.\n')
plt.show()

avg_return_day = AAPL['simple_return'].mean()
print('Average daily simple return of AAPL stock for the past 5 years: ' + str(avg_return_day) + ' %\n')

avg_return_year = AAPL['simple_return'].mean()*250
print('Average annual simple return of AAPl stock for the past 5 years: ' + str(avg_return_year) + ' %\n')

#Calculating daily return based on the log formula

AAPL['log_return'] = np.log(AAPL['Adj Close'] / AAPL['Adj Close'].shift(1)) *100

AAPL['log_return'].plot(figsize=(8, 5))
plt.show()

log_return_day = AAPL['log_return'].mean()
print('Average daily log return of AAPL stock for the past 5 years: ' + str(log_return_day) + ' %\n')

log_return_year = AAPL['log_return'].mean()*250
print('Average annual log return of AAPL stock for the past 5 years ' + str(log_return_year) + ' %\n')




