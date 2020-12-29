import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

symbols = ['TWTR', 'FB']

data = pd.DataFrame()
for s in symbols:
    data[s] = wb.DataReader(s, data_source='yahoo', start='2014-1-1')['Adj Close']

data_returns = np.log(data / data.shift(1))

#Mean of one year
data_returns['TWTR'].mean() * 250

#Standard deviation for on year
data_returns['TWTR'].std() * 250 ** 0.5

#Mean of one year
data_returns['FB'].mean() * 250

#Standard deviation for on year
data_returns['FB'].std() * 250 ** 0.5

#OR FOR BOTH
data_returns[['TWTR', 'FB']].mean() * 250
print(data_returns[['TWTR', 'FB']].std() * 250 ** 0.5)

#Now we are going to calculate the covariance and the correlation between stocks

TWTR_var = data_returns['TWTR'].var()
FB_var = data_returns['FB'].var()
TWTR_var_a = data_returns['TWTR'].var() * 250
FB_var_a = data_returns['FB'].var() * 250

#Calculating covariance

cov_matrix = data_returns.cov()
cov_matrix_a = data_returns.cov() * 250
print(cov_matrix)

#Calculating correlation

corr_matrix = data_returns.corr()
print(corr_matrix)

#CALCULATING PORTFOLIO RISK

weights = np.array([0.5, 0.5])

#Portfolio variance
portfolio_var = np.dot(weights.T, np.dot(data_returns.cov() * 250, weights))
print(portfolio_var)

#Portfolio volatility (standard deviation)
portfolio_vol = np.dot(weights.T, np.dot(data_returns.cov() * 250, weights)) ** 0.5
print(str(portfolio_vol * 100) + ' %')

#Calculating the unsystematic risk (the one we can eliminate with diversification)

div_risk = portfolio_var - (weights[0] ** 2 * FB_var_a) - (weights[1] ** 2 * TWTR_var_a)
print('The diversifiable risk of the portfolio is: ' + str(round(div_risk * 100, 3)) + ' %')

#Calculating the systematic risk (the one we can't eliminate by diversification)

n_div_risk = (weights[0] ** 2 * FB_var_a) + (weights[1] ** 2 * TWTR_var_a)            #also n_div_risk = portfolio_var = div_risk
print('The undiversifiable risk of the portfolio is: ' + str(round(n_div_risk * 100, 3)) + ' %')


