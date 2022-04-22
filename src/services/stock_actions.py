import yfinance as yf
from repositories.user_repository import (
    user_repository as default_user_repository)
from repositories.stock_repository import (
    stock_repository as default_stock_repository)

class SymbolNotFoundError(Exception):
    pass



class StockActions:
    """Sovelluslogiikasta vastaava luokka"""

    def __init__(self,  user_repository=default_user_repository,
                 stock_repository=default_stock_repository,
                 ):
        """Konstruktori, joka luo sovelluslogiikan palvelun.
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
        try:
            share = yf.Ticker(stock)
            dataframe = share.history(period="1d", interval="1d")
            return float(f"{dataframe.iat[0, 3]:.2f}")
        except SymbolNotFoundError:
            print("Symbol not found")
            

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
            stock:
        """
        try:
            share = yf.Ticker(stock)
            data = share.info
            if data:
                print(len(share.info))
        except SymbolNotFoundError:
            print("Symbol not found")

    def logged_user(self, username):
        """Kirjaa käyttäjän sisään sovellukseen.

        Args:
            username:

        """
        self._logged_user = username

stock_actions = StockActions()