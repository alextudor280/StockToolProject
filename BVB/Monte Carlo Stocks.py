import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb
from scipy.stats import norm

symbol = 'HBT'
data = pd.DataFrame()
data[symbol] = wb.DataReader(symbol, data_source = 'yahoo', start = '2007-1-1')['Adj Close']

log_returns = np.log(1 + data.pct_change())

data.plot(figsize=(10, 6))
plt.title(symbol + ' Price')
plt.show()

log_returns.plot(figsize=(10, 6))
plt.title(symbol + ' Returns')
plt.show()

#We will approximate the daily return using the Brownian motion formula:
# r = drift + stdev * e^r
#Where drift = mean - 1/2*var

mean = log_returns.mean()
var = log_returns.var()

drift = mean - (0.5 * var)
stdev = log_returns.std()

#we also need to change the newly created variables into np arrays

np.array(drift)
np.array(stdev)

#norm.ppf(0.95)  #tool for creating the distance from mean to the event expressed in stdev
                #so if the event as 0.95 probability of happening, it will be norm.ppf(0.95)*stdev away from the mean

#x = np.random.rand(10, 2) This creates random numbers for the probability, also arranged in a 10 by 2 array

t_intervals = 1000      #forecasting the stock price for 1000 days
iterations = 50         #the number of predictions per day

z = norm.ppf(np.random.rand(t_intervals, iterations))


daily_returns = np.exp(drift.values + stdev.values * z)


P0 = data.iloc[-1]          #the last price in our data from yahoo, also known as the starting price for our simulation

prices = np.zeros_like(daily_returns)
prices[0] = P0              #assigning the first row of 10 prices the present stock price

#Generating prices

for i in range(1, t_intervals):
    prices[i] = prices[i-1] * daily_returns[i]


plt.figure(figsize=(10,6))
plt.title('Possible ' + symbol + ' Prices')
plt.plot(prices)
plt.show()
