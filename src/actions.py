import yfinance as yf

#from portfolio import Portfolio
from user import User
from user_repository import (user_repository as default_user_repository)
from stock_repository import (stock_repository as default_stock_repository)


"""Sovelluslogiikasta vastaava luokka"""
class Actions:

    def __init__(self, user_repository=default_user_repository, stock_repository=default_stock_repository ):
       # self.investor = investor
        self.__user = "erkki"
        self.__stock_repository = stock_repository
        self.__user_repository = user_repository
        
     
    def get_latest_price(self, stock):
        share = yf.Ticker(stock)
        df = share.history(period="1d", interval= "1d")
        return float("%.2f" % df.iat[0,3])

    def buy_stock(self, stock, amount):       
        buy_price = self.get_latest_price(stock)
        self.__user_repository.adjust_capital(self.__user, -abs(buy_price*amount)) # vähennä pääomaa sijoituksen verran
        self.__stock_repository.add_to_portfolio(self.__user,stock, buy_price, amount) # lisää osakkeet portfolioon

    def sell_stock(self, stock, amount):
        sell_price = self.get_latest_price(stock)
        self.__user_repository.adjust_capital(self.__user, sell_price*amount) # lisää pääomaa myynnin verran
        self.__stock_repository.remove_stock_from_portfolio(self.__user, stock, sell_price, amount) # vähennä osakkeita
       

    def get_stock_info(self, stock):
        share = yf.Ticker(stock)
        print(share.info['longBusinessSummary'])

    def show_capital(self):
        return self.__user_repository.get_capital(self.__user)

    def create_user(self, username, password, capital):
        user = self.__user_repository.new_user(User(username, password,capital))
        return user

    def get_portfolio(self):
        return self.__stock_repository.get_portfolio_from_database(self.__user)

    def get_users(self):
        return self.__user_repository.print_all_users()

    def login(self, username, password):
        
        self.__user = username
        self.__password = password
       