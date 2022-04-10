import yfinance as yf
from investor import Investor 
from portfolio import Portfolio
from user import User
from user_repository import (user_repository as default_user_repository)
from stock_repository import (stock_repository as default_stock_repository)


"""Sovelluslogiikasta vastaava luokka"""
class Actions:

    def __init__(self, investor : Investor, user_repository=default_user_repository, stock_repository=default_stock_repository ):
        self.investor = investor
        self.__user = "Erkki"
        self.__stock_repository = stock_repository
        self.__user_repository = user_repository


        
    def get_latest_price(self, stock):
        share = yf.Ticker(stock)
        df = share.history(period="1d", interval= "1d")
        return float("%.2f" % df.iat[0,3])

    def buy_stock(self, stock, amount):       
        buy_price = self.get_latest_price(stock)
        self.investor.adjust_capital(-abs(buy_price*amount)) # vähennä pääomaa sijoituksen verran

        #self.investor.add_portfolio(stock, buy_price, amount) # lisää osakkeet portfolioon
        self.__stock_repository.add_to_portfolio(self.__user,stock, buy_price, amount) # lisää osakkeet portfolioon

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


    
    def create_user(self, username, password, capital):
        user = self.__user_repository.new_user(User(username, password,capital))
    
        return user


    def login(self, username, password):

        user = self.__user_repository.find_user(username)

        self.__user = user

        return user