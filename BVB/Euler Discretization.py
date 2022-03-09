import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb
from scipy.stats import norm

rf = 0.025
t = 1.0
t_intervals = 250
delta_t = t / t_intervals
iterations = 10000

symbol = 'FB'
data = pd.DataFrame()
data[symbol] = wb.DataReader(symbol, data_source = 'yahoo', start = '2007-1-1')['Adj Close']



log_returns = np.log(1 + data.pct_change())
stdev = log_returns.std() * 250 ** 0.5
stdev = stdev.values

z = np.random.standard_normal((t_intervals + 1, iterations))
s = np.zeros_like(z)
P0 = data.iloc[-1]
s[0] = P0

for i in range(1, t_intervals + 1):
    s[i] = s[i-1] * np.exp((rf - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * z[i])

plt.figure(figsize=(10, 6))
plt.plot(s[:, :10])
plt.show()

#Using the Monte Carlo simulation into call option pricing
k = 205             #strike price

p = np.maximum(s[-1] - k, 0)

call = np.exp(-rf * t) * np.sum(p) / iterations
print('The call option price is: ' + str(call) + ' $')

