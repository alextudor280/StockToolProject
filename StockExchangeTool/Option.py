import pandas as pd
import numpy as np
from scipy.stats import norm
import Stock
import investpy

class Option:

    rf = 0.035

    def __init__(self, stock, strike, maturity):
        self.price = float
        self.stdev = pd.DataFrame()
        self.stock_price = stock.get_price()
        self.strike = strike
        self.stock_log = np.log(1 + stock.get_data()['Adj Close'].pct_change())
        self.stdev = self.stock_log.std() * 250 ** 0.5
        self.maturity = maturity/365            #from time in days into years

    def d1(self):
        return (np.log(self.stock_price / self.strike) + (self.rf + self.stdev ** 2 / 2) * self.maturity) / (self.stdev * np.sqrt(self.maturity))

    def d2(self):
        return (np.log(self.stock_price / self.strike) + (self.rf - self.stdev ** 2 / 2) * self.maturity) / (self.stdev * np.sqrt(self.maturity))

    def BS_call(self):
        return (self.stock_price * norm.cdf(self.d1())) - (self.strike * np.exp(-self.rf * self.maturity) * norm.cdf(self.d2()))

    def BS_put(self):
        return (self.strike * np.exp(-self.rf * self.maturity) * norm.cdf(-self.d2()) - self.stock_price * norm.cdf(-self.d1()))