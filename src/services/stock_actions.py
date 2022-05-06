import yfinance as yf
from repositories.user_repository import (
    NotEnoughMoneyError,
    user_repository as default_user_repository)
from repositories.stock_repository import (
    StockNotInPortfolioError,
    stock_repository as default_stock_repository)


class SymbolNotFoundError(Exception):
    pass


class StockActions:
    """Osakkeisiin liittyvästä sovelluslogiikasta vastaava luokka.
    """

    def __init__(self,  user_repository=default_user_repository,
                 stock_repository=default_stock_repository,
                 ):
        """Luokan konstruktori, joka luo sovelluslogiikasta vastaavan palvelun.

        Args:
            user_repository (object, optional):
                UserRepository-olio jolla on UserRepository-luokkaa vastaavat metodit.

            stock_repository (object, optional):
                StockRepository-olio jolla on StockRepository-luokkaa vastaavat metodit.
        """
        self._logged_user = None
        self._stock_repository = stock_repository
        self._user_repository = user_repository

    def get_latest_price(self, stock):
        """Hakee ja palauttaa yfinance-palvelusta osakkeen sen hetkisen hinnan.

        Args:
            stock (str): Merkkijono joka kertoo osakkeen symbolin.

        Returns:
            float: Paluttaa osakkeen hinnan kahden desimaalin tarkkuudella.

        Raises:
            SymbolNotFoundError:
                Virhe joka tapahtuu jos symbolia ei löydy.

        """

        share = yf.Ticker(stock)
        dataframe = share.history(period="1d", interval="1d")
        if dataframe.empty:
            raise SymbolNotFoundError("Symbol not found")
        return float(f"{dataframe.iat[0, 3]:.2f}")


    def buy_stock(self, stock, amount):
        """Ostaa osaketta annetun määrän ja lisää ne käyttäjän portfolioon,
            sekä vähentää niiden hinnan käyttäjän pääomasta.

        Args:
            stock (str): Ostettavan osakkeen symboli.
            amount (int): Ostettavan osakkeen määrä.

        Returns
            float: Palauttaa osakkeen ostolle toteutuneen hinnan.
        """
        try:
            buy_price = self.get_latest_price(stock)
        except:
            SymbolNotFoundError('Symbol not found')
            raise SymbolNotFoundError('Symbol not found')

        try:
            self._user_repository.adjust_capital(
            self._logged_user, -abs(buy_price*amount))
        except:
            NotEnoughMoneyError("Not enough money")
            raise NotEnoughMoneyError("Not enough money")

        self._stock_repository.add_to_portfolio(
            self._logged_user, stock, buy_price, amount)
        return buy_price

    def sell_stock(self, stock, amount):
        """Myy osaketta annetun määrän ja poistaa ne käyttäjän portfoliosta,
            sekä lisää niiden hinnan käyttäjän pääomaan.

        Args:
            stock (str): Myytävän osakkeen symboli.
            amount (int): Myytävän osakkeen määrä.

        Returns
            float: Palauttaa osakkeen myynnille toteutuneen hinnan.
        """
        try:
            sell_price = self.get_latest_price(stock)
        except:
            SymbolNotFoundError('Symbol not found')
            raise SymbolNotFoundError('Symbol not found')

        self._user_repository.adjust_capital(
            self._logged_user, sell_price*amount)
        try:
            self._stock_repository.remove_stock_from_portfolio(
                self._logged_user, stock, amount)
        except:
            StockNotInPortfolioError("Incorrect amount")
            raise StockNotInPortfolioError("Incorrect amount")

        return sell_price

    def get_stock_info(self, stock):
        """Hakee ja palauttaa osakkeen yritystiedot yfinance moduulista

        Args:
            stock:
        """
        share = yf.Ticker(stock)
        data = share.info

        if len(data) < 50:
            print("Symbol not found")
            raise SymbolNotFoundError('Symbol not found')
        return data["longBusinessSummary"]



    def logged_user(self, username):
        """Kertoo luokalle sisään kirjautuneen käyttäjän.

        Args:
            username(str): Sisäänkirjautunut käyttäjä.

        """
        self._logged_user = username

    def get_stock_name(self, symbol):
        """_summary_

        Args:
            symbol (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.info
            if len(data) > 50:
                long_name = data['longName']
        except SymbolNotFoundError:
            print("Symbol not found")

        return long_name


stock_actions = StockActions()
