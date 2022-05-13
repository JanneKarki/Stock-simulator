import yfinance as yf
from repositories.user_repository import (
    NotEnoughMoneyError,
    user_repository as default_user_repository)
from repositories.stock_repository import (
    StockNotInPortfolioError,
    TooLargeSellOrderError,
    stock_repository as default_stock_repository)


class SymbolNotFoundError(Exception):
    pass


class EmptyInputError(Exception):
    pass


class InvalidAmountError(Exception):
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

        Returns:
            float: Palauttaa osakkeen ostolle toteutuneen hinnan.

        Raises:
            SymbolNotFoundError:
                Virhe joka tapahtuu jos symbolia ei löydy.
            NotEnoughMoneyError:
                Virhe joka tapahtuu jos käyttäjällä ei ole tarpeeksi rahaa.
            EmptyInputError:
                Virhe joka tapahtuu jos syötteet ovat tyhjiä.
            IvalidAmountError:
                Virhe joka tapahtuu jos ostettavien osakkeiden määrän syöte ei ole numeerinen.

        """
        if not amount or not stock:
            raise EmptyInputError()

        if not amount.isnumeric():
            raise InvalidAmountError('Invalid amount')
        try:
            buy_price = self.get_latest_price(stock)
        except SymbolNotFoundError:
            raise SymbolNotFoundError('Symbol not found')

        try:
            self._user_repository.adjust_capital(
                self._logged_user, -abs(buy_price*int(amount)))
        except NotEnoughMoneyError:
            raise NotEnoughMoneyError("Not enough money")

        self._stock_repository.add_to_portfolio(
            self._logged_user, stock, buy_price, int(amount))
        return buy_price

    def sell_stock(self, stock, amount):
        """Myy osaketta annetun määrän ja poistaa ne käyttäjän portfoliosta,
            sekä lisää niiden myynnistä saadun hinnan käyttäjän pääomaan.

        Args:
            stock (str): Myytävän osakkeen symboli.
            amount (int): Myytävän osakkeen määrä.

        Returns
            float: Palauttaa osakkeen myynnille toteutuneen hinnan.

        Raises:
            SymbolNotFoundError:
                Virhe joka tapahtuu jos symbolia ei löydy.
            StockNotInPortfolioError:
                Virhe joka tapahtuu jos osaketta ei ole portfoliossa.
            TooLargeSellOrderError:
                Virhe joka tapahtuu jos myyntitoimeksianto on suurempi kuin
                osakkeiden määrä portfoliossa.
            InvalidAmountError:
                Virhe joka tapahtuu jos osakkeiden määrän syöte ei ole numeerinen.
            EmptyInpurError:
                Virhe joka tapahtuu jos syötteet ovat tyhjiä.
        """
        if not amount or not stock:
            raise EmptyInputError

        if not amount.isnumeric():
            raise InvalidAmountError('Invalid amount')

        try:
            sell_price = self.get_latest_price(stock)
        except SymbolNotFoundError:
            raise SymbolNotFoundError('Symbol not found')

        try:
            self._stock_repository.remove_stock_from_portfolio(
                self._logged_user, stock, int(amount))
        except StockNotInPortfolioError:
            raise StockNotInPortfolioError("Incorrect amount")

        except TooLargeSellOrderError:
            raise TooLargeSellOrderError('Too large sell order')

        self._user_repository.adjust_capital(
            self._logged_user, sell_price*int(amount))

        return sell_price

    def get_stock_info(self, stock):
        """Hakee ja palauttaa osakkeen yritystiedot yfinance-moduulista

        Args:
            stock(str): Haettavan yrityksen osakkeen symboli.

        Returns:
            str: Palauttaa yrityksen info-tekstin.
        """

        share = yf.Ticker(stock)
        get_data = share.history(period="1d", interval="1d")

        if get_data.empty:
            raise SymbolNotFoundError('Symbol not found')

        info_data = share.info

        return info_data["longBusinessSummary"]

    def get_stock_name(self, symbol):
        """Hakee ja palauttaa yhtiön nimen osakkeen symbolin perusteella.

        Args:
            symbol (str): Osakkeen symboli.

        Returns:
            str: Yhtiön nimi.

        """
        share = yf.Ticker(symbol)
        get_data = share.history(period="1d", interval="1d")

        if get_data.empty:
            raise SymbolNotFoundError('Symbol not found')

        data = share.info
        company_name = data['longName']

        return company_name

    def set_logged_user(self, username):
        """Kertoo luokalle sisään kirjautuneen käyttäjän.

        Args:
            username(str): Sisäänkirjautunut käyttäjä.

        """
        self._logged_user = username


stock_actions = StockActions()
