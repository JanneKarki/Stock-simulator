import yfinance as yf
from investor import Investor 
from portfolio import Portfolio


class Actions:

    def __init__(self, investor : Investor):
        self.investor = investor
        
    def get_latest_price(self, stock):
        share = yf.Ticker(stock)
        df = share.history(period="1d", interval= "1d")
        return df.iat[0,3]

    def buy_stock(self, stock, amount):       
        buy_price = self.get_latest_price(stock)
        self.investor.adjust_capital(-abs(buy_price*amount)) # vähennä pääomaa sijoituksen verran
        self.investor.add_portfolio(stock, buy_price, amount) # lisää osakkeet portfolioon

    def sell_stock(self, stock, sell_price, amount):
        if stock in self.portfolio:
            x = self.investor.portfolio[stock] #haetaan osake portfoliosta
            avg_price = x[1]        # osakkeen keskimääräinen hankinta hinta
            net = sell_price-avg_price # sijoituksen netto tuotto/tappio
            
            if amount <= x[0]:  # jos myyntimäärä oikein, päivitä pääoma ja portfolio
                self.adjust_capital(net)
                self.remove_stock(stock,amount, x)
            else:
                print("Too large sell order. You own", x[0], "shares" )

    def get_stock_info(self, stock):
        share = yf.Ticker(stock)
        print(share.info['longBusinessSummary'])


    

    


seppo = Investor("seppo", 10000)
actions = Actions(seppo)
portfolio = Portfolio(seppo)
print(seppo.capital)
actions.buy_stock("MSFT", 100)
print(seppo.capital)
print(seppo.portfolio)
portfolio.total_win_loss()
portfolio.rank_investments()