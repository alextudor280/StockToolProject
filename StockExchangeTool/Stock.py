import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import Portfolio
import Index

class Stock:

    def __init__(self, symbol):
        self.weight = 1
        self.symbol = str
        self.price = float
        self.weight = float
        self.stdev = float
        self.annual_return = float
        self.variance = float
        self.beta = float
        self.data = pd.DataFrame()
        self.simple_returns = pd.DataFrame()
        self.log_returns = pd.DataFrame()
        self.symbol = symbol
        self.set_data()
        self.set_simple_return()
        self.set_log_returns
        self.set_annual_return                  # Decided to use log returns for annual return of individual stocks and simple return for portfolio
        self.set_stdev()
        #self.set_beta()
        self.price = self.get_price()
        self.stdev = self.get_stdev()
        self.variance = self.get_variance()




    def get_symbol(self):
        return self.symbol

    def get_price(self):
        return self.data['Adj Close'].iloc[-1]

    def get_simple_returns(self):
        return self.data['Simple Return']

    def get_log_returns(self):
        return self.data['Log Return']

    def get_data(self):
        return self.data

    def get_annual_return(self):
        return self.annual_return

    def get_stdev(self):
        return self.stdev

    def get_variance(self):
        return self.variance

    def get_beta(self):
        return self.beta

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_data(self):
        self.data['Adj Close'] = wb.DataReader(self.get_symbol(), data_source='yahoo', start='2015-1-1')['Adj Close']
        self.data['Simple Return'] = ((self.data['Adj Close'] / self.data['Adj Close'].shift(1)) - 1)
        self.data['Log Return'] = np.log(self.data['Adj Close'] / self.data['Adj Close'].shift(1))

    def set_simple_return(self):
        self.simple_returns = self.data['Simple Return']

    def set_log_returns(self):
        self.log_returns = self.data['Log Return']

    def set_annual_return(self):
        self.annual_return = self.data['Log Return'].mean() * 250

    def set_price(self, price):
        self.price = price

    def set_stdev(self):
        self.stdev = self.log_returns.std() * 250 ** 0.5

    def set_variance(self):
        self.variance = self.log_returns.var() * 250

    def set_weight(self, weight):
        self.weight = weight

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.log_returns, color = 'green')
        plt.title(self.symbol + ' Return')
        return plt.show()

    def set_beta(self):
        SP = Index.Index('^GSPC')
        stocks = [self, SP]
        portfolio = Portfolio.Portfolio(stocks)
        portfolio.get_covariance()
        cov_with_market = portfolio.get_covariance().iloc[0,1]
        market_var = SP.get_variance()
        self.beta = cov_with_market/market_var







