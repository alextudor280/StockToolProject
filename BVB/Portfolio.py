import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

symbols = ['AAPL', 'F', 'MSFT', 'JPM']
mydata = pd.DataFrame()
for s in symbols:
    mydata[s] = wb.DataReader(s, data_source='yahoo', start='2010-1-1')['Adj Close']

# IMPORTANT !!! THIS FORMULA IS CALLED NORMALISATION TO 100
# The graph resulting from this is better because all data start from the same point (100)

(mydata / mydata.iloc[0] * 100).plot(figsize=(15,6))
plt.show()

#Calculating the returns of the portofolio
weights = np.array([0.25, 0.25, 0.25, 0.25])
returns = ((mydata / mydata.shift(1)) - 1) * 100

annual_returns = returns.mean() * 250
portfolio_return = np.dot(annual_returns, weights)

print(type(annual_returns))
print(portfolio_return)
print(type(portfolio_return))