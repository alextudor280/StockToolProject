import pandas as pd
import numpy as np
from pandas_datareader import data as wb
from scipy.stats import norm

#We are defining the Black Scholes Formula

#S - stock price
#K - strike price
#rf -  risk-free rate
#stdev - standard deviation
#t - time until maturity in years

def d1(s, k, rf, stdev, t):
    return(np.log(s / k) + (rf + stdev ** 2 / 2) * t) / (stdev * np.sqrt(t))

def d2(s, k, rf, stdev, t):
    return (np.log(s / k) + (rf - stdev ** 2 / 2) * t) / (stdev * np.sqrt(t))

def BS_call(s, k, rf, stdev, t):
    return(s * norm.cdf(d1(s, k, rf, stdev, t))) - (k * np.exp(-rf * t) * norm.cdf(d2(s, k, rf, stdev, t)))

def BS_put(s, k, rf, stdev, t):
    return(k * np.exp(-rf * t) * norm.cdf(-d2(s, k, rf, stdev, t)) - s * norm.cdf(-d1(s, k, rf, stdev, t)))



#Using BSM Formula on stocks

rf = 0.025         #research
k = 300           #should be asked for
t = 1               #also asked for

symbol = 'FB'
data = pd.DataFrame()
data[symbol] = wb.DataReader(symbol, data_source = 'yahoo', start = '2015-1-1')['Adj Close']

s = data.iloc[-1]

log_returns = np.log(1 + data.pct_change())
stdev = log_returns.std() * 250 ** 0.5

print(log_returns.mean() * 250)


print('The ' + symbol + ' call option is estimated to cost: ' + str(BS_put(s, k, rf, stdev, t)) + ' $')
