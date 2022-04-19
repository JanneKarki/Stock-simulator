import yfinance as yf
from user import User
from repositories.user_repository import (user_repository as default_user_repository)
from repositories.stock_repository import (stock_repository as default_stock_repository)
#from services.user_services import user_services

class InvalidCredentialsError(Exception):
    pass



class Actions:

    '''Sovelluslogiikasta vastaava luokka''' 

    def __init__(self,  user_repository=default_user_repository,
                 stock_repository=default_stock_repository,
                 ):
        """Konstruktori, joka luo sovelluslogiikan palvelun
        
        
        Args:
            stock_repository:

                Olio, jolla on StockRepository-luokkaa vastaavat metodit.
            user_repository:
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        
        self._logged_user = None
        self._stock_repository = stock_repository
        self._user_repository = user_repository

    def get_latest_price(self, stock):
        """Palauttaa haettavan osakkeen sen hetkisen hinnan
        
        Args:
            stock: Merkkijono joka kertoo osakkeen symbolin.
        
        Returns:
            Paluttaa osakkeen hinnan yfinance moduulista 
            kahden desimaalin tarkkuudella
        
        """
        share = yf.Ticker(stock)
        dataframe = share.history(period="1d", interval="1d")
        return float("%.2f" % dataframe.iat[0, 3])

    def buy_stock(self, stock, amount):

        """Ostaa osaketta annetun määrän ja lisää ne käyttäjän 
        portfolioon, sekä vähentää niiden hinnan käyttäjän pääomasta
        
        Args:
            stock:
            amount:
        
        Returns
        """

        buy_price = self.get_latest_price(stock)
        self._user_repository.adjust_capital(
            self._logged_user, -abs(buy_price*amount))
        self._stock_repository.add_to_portfolio(
            self._logged_user, stock, buy_price, amount)
        return buy_price

    def sell_stock(self, stock, amount):

        """Myy osaketta annetun määrän ja vähentää ne käyttäjän, 
        sekä lisää niiden hinnan käyttäjän pääomaan
        
        Args:
            stock:
            amount: 
            
        Returns:
        """
        sell_price = self.get_latest_price(stock)
        self._user_repository.adjust_capital(
            self._logged_user, sell_price*amount)
        self._stock_repository.remove_stock_from_portfolio(
            self._logged_user, stock, amount)
        return sell_price

    def get_stock_info(self, stock):
        """Hakee ja tulostaa osakkeen yritystiedot yfinance moduulista
        
        Args:
            stock:"""
        share = yf.Ticker(stock)
        print(share.info['longBusinessSummary'])


    """ def create_user(self, username, password, capital):
        """"""Luo uuden käyttäjän
        
        Args:
            username:
            password:
            capital:
            
        Returns:
        
        """"""
        user = self._user_repository.new_user(
            User(username, password, capital))
        self._logged_user = username
        return user
    """
 
  #  def get_logged_user(self):
   #     return self._logged_user

 
    def login(self, username):
        """Kirjaa käyttäjän sisään sovellukseen
        
        Args:
            username:
            password:

        
        """
        self._logged_user = username
        return self._logged_user

    def logout(self):
        """Kirjaa käyttäjän ulos sovelluksesta"""
        self._logged_user = None