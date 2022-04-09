import yfinance as yf
from investor import Investor 
from portfolio import Portfolio


class Actions:

    def __init__(self, investor : Investor):
        self.investor = investor
        
    def get_latest_price(self, stock):
        share = yf.Ticker(stock)
        df = share.history(period="1d", interval= "1d")
        return float("%.2f" % df.iat[0,3])

    def buy_stock(self, stock, amount):       
        buy_price = self.get_latest_price(stock)
        self.investor.adjust_capital(-abs(buy_price*amount)) # vähennä pääomaa sijoituksen verran
        self.investor.add_portfolio(stock, buy_price, amount) # lisää osakkeet portfolioon

    def sell_stock(self, stock, amount):
        sell_price = self.get_latest_price(stock)
        self.investor.remove_stock(stock,amount)
        #if stock in self.investor.portfolio:
         #   x = self.investor.portfolio[stock] # haetaan osake portfoliosta
          #  avg_price = x[1]        # osakkeen keskimääräinen hankinta hinta
           # net = sell_price-avg_price # sijoituksen netto tuotto/tappio
            
           # if amount <= x[0]:  # jos myyntimäärä oikein, päivitä pääoma ja portfolio
           #     self.investor.adjust_capital(net)
           #     self.investor.remove_stock(stock,amount)
           # else:
           #     print("Too large sell order. You own", x[0], "shares" )
        #else:
        #    print("Ei osaketta salkussa")

    def get_stock_info(self, stock):
        share = yf.Ticker(stock)
        print(share.info['longBusinessSummary'])


    

    


