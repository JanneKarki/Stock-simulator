from investor import Investor 
import yfinance as yf

class Portfolio:

    def __init__(self, investor : Investor):
        self.investor = investor
        
    def get_latest_price(self, stock):
        share = yf.Ticker(stock)
        df = share.history(period="1d", interval= "1d")
        return df.iat[0,3]

    def total_win_loss(self):
        total = 0
        portfolio = self.investor.get_portfolio()
        for stock,value in portfolio.items():
            latest_price = self.get_latest_price(stock)
            entry_price = value[0]*value[1]
            end_price = latest_price*value[0]
            profit = end_price-entry_price
            total += profit
        print(total)


    def rank_investments(self):
        list = []
        portfolio = self.investor.get_portfolio()
        for stock,value in portfolio.items():
            latest_price = self.get_latest_price(stock)
            entry_price = value[0]*value[1]
            end_price = latest_price*value[0]
            profit = end_price-entry_price
            list.append((stock,profit))
        list.sort(key=lambda y: y[1])
        print(list)