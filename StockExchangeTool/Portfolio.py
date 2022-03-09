import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import investpy


class Portfolio:

    def __init__(self, stocks, *weights):
        self.data = pd.DataFrame()
        self.stocks = []
        self.log_return = pd.DataFrame()
        self.simple_return = pd.DataFrame()
        self.annual_return = pd.Series()
        self.covariance = pd.DataFrame()
        self.correlation = pd.DataFrame()
        self.weights = []
        self.variance = float
        self.stdev = float
        self.portfolio_returns = []
        self.portfolio_volatilities = []
        self.stocks = stocks
        self.nstocks = len(self.stocks)
        for s in self.stocks:
            self.data[s.get_symbol()] = s.get_data()['Adj Close']
        self.log_return = np.log(self.data / self.data.shift(1))
        self.simple_return = ((self.data / self.data.shift(1)) - 1)
        if self.nstocks <= 2:
            self.annual_return = self.log_return.mean() * 250
        else:
            self.annual_return = self.simple_return.mean() * 250
        self.covariance = self.log_return.cov() * 250
        self.correlation = self.log_return.corr()
        #if np.sum(weights) == 1.0:
           # self.weights = np.array(weights)
           # self.variance = np.dot(self.weights.T, np.dot(self.covariance, self.weights))
           # self.stdev = np.dot(self.weights.T, np.dot(self.covariance, self.weights)) ** 0.5

    def add_stock(self, stock):
        self.stocks.append(stock)
        self.update_data()
        self.update_covariance()
        self.update_correlation()
        self.update_simple_return()
        self.update_log_return()
        self.update_annual_return()

    def get_nstocks(self):
        return self.nstocks

    def get_covariance(self):
        return self.covariance

    def get_correlation(self):
        return self.correlation

    def get_simple_return(self):
        return self.simple_return

    def get_log_return(self):
        return self.log_return

    def get_annual_return(self):
        return self.annual_return

    def get_stocks(self):
        return self.stocks

    def get_data(self):
        return self.data

    def get_variance(self):
        return self.variance

    def get_stdev(self):
        return self.stdev

    def get_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights.clear()
        if (np.sum(weights) == 1.0):
            self.weights = np.array(weights)
            self.update_variance()
            self.update_stdev()
        else:
            print("The total weights should sum up to 1!")

    def update_data(self):
        for s in self.stocks:
            self.data[s.get_symbol()] = s.get_data()['Adj Close']

    def update_log_return(self):
        self.log_return = np.log(self.data / self.data.shift(1))

    def update_simple_return(self):
        self.simple_return = ((self.data / self.data.shift(1)) - 1)

    def update_annual_return(self):
        if self.nstocks <= 2:
            self.annual_return = self.log_return.mean() * 250
        else:
            self.annual_return = self.simple_return.mean() * 250

    def update_covariance(self):
        self.covariance = self.log_return.cov() * 250

    def update_correlation(self):
        self.correlation = self.log_return.corr()

    def update_variance(self):
        self.variance = np.dot(self.weights.T, np.dot(self.covariance, self.weights))

    def update_stdev(self):
        self.stdev = np.dot(self.weights.T, np.dot(self.covariance, self.weights)) ** 0.5

    def plot_evolution(self):
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
            ratio = self.portfolio_returns[x] / self.portfolio_volatilities[x]
            max_ratio_weights

            if ratio > max_ratio:
                max_ratio = ratio
                max_ratio_weights = self.weights
                best_return = self.portfolio_returns[x]
                best_volatility = self.portfolio_volatilities[x]

        self.portfolio_returns = np.array(self.portfolio_returns)
        self.portfolio_volatilities = np.array(self.portfolio_volatilities)

        print('The best and safest return is: ' + str(
            round(best_return * 100, 2)) + ' %. The portfolio has a volatility of: ' + str(
            round(best_volatility * 100, 2)) + ' %.')
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
