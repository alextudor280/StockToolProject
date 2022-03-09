import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from datetime import date
import matplotlib.pyplot as plt
import Portfolio
import Index
import investpy
import requests
from bs4 import BeautifulSoup

class Stock:

    today = date.today()
    def __init__(self, symbol):
    #define variables
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
        self.nr_of_shares = int
    #set variables ------------------------------> this would need constant refreshment in a database or web app since the prices are changing
        self.symbol = symbol
        self.set_data()
        self.set_simple_return()
        self.set_log_returns()
        self.set_annual_return()                  # Decided to use log returns for annual return of individual stocks and simple return for portfolio
        self.set_stdev()
        self.price = self.get_price()
        self.set_stdev()
        self.set_variance()
        self.set_nr_of_shares()
    #calculate data
        self.capitalization = self.price * self.nr_of_shares

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

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_data(self):
        self.data['Adj Close'] = investpy.get_stock_historical_data(stock=self.symbol, country=('Romania'), from_date='01/01/2015', to_date=date.today().strftime('%d/%m/%Y'))['Close']
        #self.data['Adj Close'] = wb.DataReader(self.get_symbol(), data_source='yahoo', start='2015-1-1')['Adj Close']
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

    def set_nr_of_shares(self):
        symbol = self.symbol
        if symbol[:2] == 'RO':
            symbol = symbol[2:]
        html_text = requests.get('https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=' + symbol).text
        soup = BeautifulSoup(html_text, 'lxml')
        nr_of_shares = int(soup.find(id='ctl00_body_ctl02_IssueInfoControl_dvInfo').find_all('td')[1].text.replace(',', ''))
        self.nr_of_shares = nr_of_shares

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.log_returns, color = 'green')
        plt.title(self.symbol + ' Return')
        return plt.show()

    def get_beta(self, index):
        stocks = [self, index]
        portfolio = Portfolio.Portfolio(stocks)
        cov_with_market = portfolio.get_covariance().iloc[0,1]
        market_var = index.get_variance()
        self.beta = cov_with_market/market_var
        return self.beta

    def expected_return(self, risk_free, index):
        expected_return = risk_free + self.get_beta(index)*(index.get_annual_return()-risk_free)
        #print("The expected return of " + self.symbol + " according to CAPM formula is : " + str(round(expected_return*100, 2)) + ' %')
        return expected_return

    def sharpe_ratio(self, risk_free, index):
        sharpe = (self.expected_return(risk_free, index) - risk_free)/self.get_stdev()
        return sharpe






