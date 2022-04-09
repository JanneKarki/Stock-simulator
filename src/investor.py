#import yfinance as yf
from stock_repository import stock_repository


class Investor:

    def __init__(self,name, capital, stock_repository=stock_repository):
        self.name = name
        self.capital = capital
        self.portfolio = {}
        self.repository = stock_repository
        

    def add_portfolio(self, stock, price, amount): # lisää osakkeen portfolioon
        self.repository.add_to_portfolio(stock,price,amount) # TIETOKANTAOPERAATIO!
        

    def remove_stock(self, stock, amount ):
        self.repository.remove_stock_from_portfolio(stock,amount) #TIETOKANTAOPERAATIO!
      
    def adjust_capital(self, amount):
        self.capital += amount

    def get_portfolio(self):  
              
        return self.portfolio

    def get_portfolio_from_db(self): #TIETOKANTA!       
        return self.repository.get_portfolio_from_database() 

    def get_database_portfolio(self):
        return self.repository.get_portfolio

        
    def get_capital(self):
        return "Buying power "+str(self.capital)+ " USD"