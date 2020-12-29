import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb


assets = ['FB', '^GSPC']
portfolio = pd.DataFrame()

for a in assets:
    portfolio[a] = wb.DataReader(a, data_source='yahoo', start = '2015-1-1' )['Adj Close']

(portfolio / portfolio.iloc[0] * 100).plot(figsize=(10,5))
plt.show()

log_return = np.log(portfolio / portfolio.shift(1))
assets_annual_return = log_return.mean() * 252
print(type(log_return))

portfolio_cov = log_return.cov() * 252
print(type(portfolio_cov))
portfolio_corr = log_return.corr()

print(type(portfolio_corr))

print('Assets annual return is:\n' + str(assets_annual_return * 100))
print('Assets covariance is:\n' + str(portfolio_cov))
print('Assets correlation is:\n' + str(portfolio_corr))

num_assets = len(assets)

#ASSIGN WEIGHTS TO YOUR PORTFOLIO MANUALLY OR RANDOMLY (in this case we do it randomly)

weights = np.random.random(num_assets)
weights /= np.sum(weights)

# print(weights)

np.sum(weights * log_return.mean()) * 252  # the portfolio return based on the given weights

np.dot(weights.T, np.dot(portfolio_cov, weights)) # portfolio variance based on the given weights
np.sqrt(np.dot(weights.T, np.dot(portfolio_cov, weights))) # portfolio volatility based on the given weights

portfolio_returns = []
portfolio_volatilities = []
max_ratio = 0
max_ratio_weights = []

for x in range(1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    portfolio_returns.append(np.sum(weights * log_return.mean()) * 252)
    portfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(portfolio_cov, weights))))
    ratio = portfolio_returns[x]/portfolio_volatilities[x]

    if ratio > max_ratio:
        max_ratio = ratio
        max_ratio_weights = weights
        max_return = portfolio_returns[x]
        max_volatility = portfolio_volatilities[x]
portfolio_returns = np.array(portfolio_returns)
portfolio_volatilities = np.array(portfolio_volatilities)

print(max_ratio)
print('Max return/volatility ratio is: \n Return:' + str(round(max_return*100, 2)) + ' %' + '\n Volatility: ' + str(round(max_volatility*100, 2)) +' %')
print(max_ratio_weights)

#Now we create all the possible portfolios based on the return 1000 return rates and volatilities which
# are calculated for different weights of the asstes in the portfolio

portfolios = pd.DataFrame({'Return': portfolio_returns, 'Volatility': portfolio_volatilities})

portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10,6))
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.show()

#CALCULATING BETA OF A STOCK ( IN VARIABLE 'ASSETS' PUT THE STOCK YOU WANT THE BETA AND THE S&P500 INDEX )
#WE NEED PORTFOLIO COVARIANCE AS CALCULATED BEFORE

cov_with_market = portfolio_cov.iloc[0,1]

market_var = log_return['^GSPC'].var() *252       # THIS IS THE MARKET VARIANCE
FB_beta = cov_with_market/market_var

print('FB beta is: ' + str(FB_beta))

#CALCULATING THE EXPECTED RETURN USING CAPM FORMULA

risk_free = 0.025    #risk free asset value can be changed
marker_return = 0.08     # market return can be changed

FB_er = risk_free + FB_beta*(marker_return-risk_free)
print('The expected return of Facebook according to CAPM formula is : ' + str(round(FB_er*100, 2)) + ' %')

#CALCULATING SHARPE RATIO FOR COMPARING STOCKS OR PORTFOLIOS (HIGHER SHARPE MEANS BETTER)

sharpe = (FB_er - risk_free)/(log_return['FB'].std() * 252 ** 0.5)

print('The sharpe ratio of Facebook is: ' + str(sharpe))