import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Stock

class Portfolio:

    def __init__(self, stocks):
        self.data = pd.DataFrame()
        self.stocks = []
        self.log_return = pd.DataFrame()
        self.simple_return = pd.DataFrame()
        self.annual_return = pd.Series()
        self.covariance = pd.DataFrame()
        self.correlation = pd.DataFrame()
        self.nstocks = int
        self.weights = []
        self.portfolio_returns = []
        self.portfolio_volatilities = []
        self.log_return = self.get_log_return()
        self.simple_return = self.get_simple_return()
        self.annual_return = self.get_annual_return()
        self.covariance = self.get_covariance()
        self.correlation = self.get_correlation()
        self.stocks = stocks
        self.nstocks = len(stocks)
        self.data = self.get_data()

    def get_nstocks(self):
        return self.nstocks

    def get_covariance(self):
        self.update_covariance()
        return self.covariance

    def get_correlation(self):
        self.update_correlation()
        return self.correlation

    def get_simple_return(self):
        self.update_simple_return()
        return self.simple_return

    def get_log_return(self):
        self.update_log_return()
        return self.log_return

    def get_annual_return(self):
        self.update_annual_return()
        return self.annual_return

    def get_stocks(self):
        return self.stocks

    def get_data(self):
        self.update_data()
        return self.data

    def add_stock(self,  stock):
        self.stocks.append(stock)

    def update_data(self):
        for s in self.stocks:
            self.data[s.get_symbol()] = s.get_data()['Adj Close']

    def update_log_return(self):
        self.log_return = np.log(self.data / self.data.shift(1))

    def update_simple_return(self):
        self.simple_return = ((self.data / self.data.shift(1)) - 1)

    def update_annual_return(self):
        if (len(self.stocks) <= 2):
            self.annual_return = self.log_return.mean() * 250
        else:
            self.simple_return.mean() * 250

    def update_covariance(self):
        self.covariance = self.log_return.cov() * 250

    def update_correlation(self):
        self.correlation = self.log_return.corr()

    def plot_evo(self):
        (self.data / self.data.iloc[0] * 100).plot(figsize=(10, 5))
        return plt.show()

    def best_distribution(self):
        max_ratio = 0
        max_ratio_weights = []
        self.get_log_return()
        self.get_covariance()
        self.get_simple_return()

        for x in range(10000):
            self.weights = np.random.random(self.nstocks)
            self.weights /= np.sum(self.weights)
            if self.nstocks > 2:
                self.portfolio_returns.append(np.sum(self.weights * self.simple_return.mean()) * 250)
            else:
                self.portfolio_returns.append(np.sum(self.weights * self.log_return.mean()) * 250)
            self.portfolio_volatilities.append(np.sqrt(np.dot(self.weights.T, np.dot(self.covariance, self.weights))))
            ratio = self.portfolio_returns[x]/self.portfolio_volatilities[x]
            max_ratio_weights

            if ratio > max_ratio:
                max_ratio = ratio
                max_ratio_weights = self.weights
                best_return = self.portfolio_returns[x]
                best_volatility = self.portfolio_volatilities[x]

        self.portfolio_returns = np.array(self.portfolio_returns)
        self.portfolio_volatilities = np.array(self.portfolio_volatilities)

        print('The best and safest return is: ' + str(round(best_return * 100, 2)) + ' %. The risk is emphasized with a volatility of: ' + str(round(best_volatility * 100, 2)) + ' %.')
        print('These are obtained with the following returns: ')
        for i in range(self.nstocks):
            print(self.stocks[i].get_symbol() + ' ' + str(round(max_ratio_weights[i] * 100, 2)) + ' %')


    def plot_returns(self):
        self.best_distribution()
        portfolios = pd.DataFrame({'Return': self.portfolio_returns, 'Volatility': self.portfolio_volatilities})
        portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6))
        plt.xlabel('Expected Volatility')
        plt.ylabel('Expected Return')
        plt.show()




