import Stock
import Portfolio
import Index
import Option

FB = Stock.Stock('FB')
TSLA = Stock.Stock('TSLA')
PG = Stock.Stock('PG')
SP = Index.Index('^GSPC')
FB_option = Option.Option(FB, 300, 365)

stocks = [FB, TSLA]

Portfolio = Portfolio.Portfolio(stocks)

print(FB_option.BS_call())

#print(Portfolio.plot_returns())


#print(FB.beta())

#print(Portfolio.plot_returns())

