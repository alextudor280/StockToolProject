import numpy as np
import pandas as pd
import Stock
import Portfolio
import Index
import Option
from datetime import date
import investpy
from bs4 import BeautifulSoup
import lxml
import requests




#FB = Stock.Stock('FB')
#TSLA = Stock.Stock('TSLA')
#PG = Stock.Stock('PG')
#SP = Index.Index('^GSPC')
#GME = Stock.Stock('GME')
#GME_option = Option.Option(GME, 10, 50)
#FB_option = Option.Option(FB, 300, 365)


#stocks = [FB, TSLA, PG]

#Portfolio = Portfolio.Portfolio(stocks)

#print(sum(weights))
#print(FB_option.BS_call())

#print(Portfolio.best_distribution())

#Portfolio.plot_evolution()
#print(round(TSLA.expected_return(0.025, SP),4)*100)

#print(GME_option.BS_call())
#print(Portfolio.plot_returns())
#df = investpy.get_stock_historical_data(stock=FB.get_symbol(), country='United States', from_date='01/01/2015', to_date='24/05/2021')
BET = Index.Index('BET')
BETBK = Index.Index('BET-BK')
BETPLUS = Index.Index('Bucharest Plus')


SNP = Stock.Stock('ROSNP')
TLV = Stock.Stock('ROTLV')
TRP = Stock.Stock('ROTRP')
SNN = Stock.Stock('ROSNN')
BNET = Stock.Stock('BNET')
BRK = Stock.Stock('ROBRK')
BRD = Stock.Stock('ROBRD')
DIGI = Stock.Stock('DIGI')
M = Stock.Stock('ROM')
HUNT = Stock.Stock('ROHUNT')

#stocks = [TLV, TRP, SNN, BNET, BRK, BRD]
#Port = Portfolio.Portfolio(stocks)

#print(M.nr_of_shares)
#DIGICALL = Option.Option(DIGI, 37, 30)

#print(investpy.get_stock_company_profile("ROSNP", "romania", "en"))
#print(investpy.technical_indicators("DIGI","romania", product_type='stock', interval='daily'))
#print(str(DIGI.data))
#print(DIGICALL.BS_put())


#data = investpy.get_stock_historical_data(stock='ROBRK', country=('Romania'), from_date='01/01/2015', to_date=date.today().strftime('%d/%m/%Y'))
#print(data)

#print(investpy.get_stocks_list('Romania'))
#print(Port.plot_evolution())
#print(Port.plot_returns())

#data = pd.DataFrame
#data = investpy.get_stock_information("ROTLV", country='romania')
#pd.set_option("display.max_columns", None)
#print(data)
print(M.data)
print(HUNT.data)
#print(investpy.get_currency_crosses_list())

#print(investpy.get_stock_financial_summary(stock='ROTLV', country='Romania', summary_type='income_statement', period='annual'))
#print(investpy.get_stock_dividends(stock='ROSNN', country='Romania'))

#---------------------------------------------------------------------------------------------------------------------------------------------------
# Retrieving data from a website (bvb) xD
#print(DIGI.nr_of_shares)
