from repositories.user_repository import (
    user_repository as default_user_repository)
from repositories.stock_repository import (
    stock_repository as default_stock_repository)
from services.stock_actions import StockActions


class PortfolioServices:
    """Käyttäjän portfolioon liittyvistä toiminnoista vastaava luokka.
    """

    def __init__(
        self,
        user_repository=default_user_repository,
        stock_repository=default_stock_repository
    ):
        """Luokan konstruktori joka luo portfolion toiminnasta vastaavan palvelun.

        Args:
            user_repository (object, optional):
                UserRepository-olio jolla on UserRepository-luokkaa vastaavat metodit.

            stock_repository (object, optional):
                StockRepository-olio jolla on StockRepository-luokkaa vastaavat metodit.
        """
        self._logged_user = None
        self._stock_repository = stock_repository
        self._user_repository = user_repository
        self.actions = StockActions()

    def get_capital(self):
        """Palauttaa kirjautuneen käyttäjän pääoman, kutsumalla UserRepository-luokan metodia.

        Returns:
            float : Palauttaa kirjautuneen käyttäjän pääoman float muodossa.
        """
        capital = self._user_repository.get_user_capital(self._logged_user)

        return capital

    def get_starting_capital(self):
        """Palauttaa kirjautuneen käyttäjän aloituspääoman,
            kutsumalla UserRepository-luokan metodia.

        Returns:
            float : Palauttaa kirjautuneen käyttäjän aloituspääoman float muodossa.
        """
        starting_capital = self._user_repository.get_user_starting_capital(self._logged_user)

        return starting_capital

    def get_net_result(self):
        """Palauttaa kirjautuneen käyttäjän nettotuloksen.

        Returns:
            float : Palauttaa kirjautuneen käyttäjän nettotuloksen.
        """
        starting_capital = self._user_repository.get_user_starting_capital(self._logged_user)
        total_capital = self.total_capital()
        net_result = total_capital-starting_capital

        return float(f"{net_result:.2f}")

    def get_portfolio(self):
        """Palauttaa kirjautuneen käyttäjän portfolion kutsumalla UserRepository-luokan metodia.

        Returns:
            list: Palauttaa listan käytäjän osakkeista, niiden määrän ja
            keskimääräisen hankintahinnan. Jos niitä ei ole palauttaa tyhjän listan.

        """
        return self._stock_repository.get_portfolio_from_database(self._logged_user)

    def find_stock_from_portfolio(self, stock):
        """Hakee ja palauttaa osakkeen, sen määrän ja hankintahinnan käyttäjän portfoliosta
            kutsumalla StockRepository-luokan metodia.

        Args:
            stock (str): Haettavan osakkeen merkkijonoesitys.

        Returns:
            list: Palauttaa osakkeen, niiden määrän ja
            keskimääräisen hankintahinnan. Jos osaketta ei löydy palauttaa
            tyhjän listan.
        """

        return self._stock_repository.get_stock_from_portfolio(self._logged_user, stock)

    def rank_investments(self):
        """Laskee ja järjestää käyttäjän sijoitukset listaan tuoton/tappion perusteella.

        Returns:
            list: Palauttaa listan jossa on  osake ja sen tuotto, tuoton mukaisessa suuruus
                järjestyksessä.
        """
        rank_list = []

        portfolio = self.get_portfolio()

        for item in portfolio:
            latest_price = self.actions.get_latest_price(item[0])
            entry_price = item[1]*item[2]
            end_price = latest_price*item[2]
            profit = end_price-entry_price
            rank_list.append((item[0], float(f"{profit:.2f}")))
        rank_list.sort(key=lambda y: y[1], reverse=True)

        return rank_list

    def total_win_loss(self):
        """Laskee käyttäjän portfolissa olevien osakkeiden kokonaistuoton.

        Returns:
            float: Palauttaa käyttäjän portfoliossa olevien osakkeiden kokonaistuoton,
                kahden desimaalin tarkkuudella.
        """
        total = 0
        portfolio = self.get_portfolio()
        for item in portfolio:
            latest_price = self.actions.get_latest_price(item[0])
            entry_price = item[1]*item[2]
            end_price = latest_price*item[2]
            profit = end_price-entry_price
            total += profit
        return float(f"{total:.2f}")

    def total_portfolio_worth(self):
        """Laskee käyttäjän portfoliossa olevien osakkeiden kokonaisarvon.

        Returns:
            float: Palauttaa käyttäjän osakkeiden kokonaisarvon kahden desimaalin tarkkuudella.
        """
        portfolio = self._stock_repository.get_portfolio_from_database(
            self._logged_user)
        total_worth = 0
        for i in portfolio:
            stock_amount = i[2]
            present_price = self.actions.get_latest_price(i[0])
            total_worth += (stock_amount*present_price)
        return float(f"{total_worth:.2f}")

    def total_capital(self):
        """Laskee ja palauttaa käyttäjän kokonaispääoman.

        Returns:
            float: Palauttaa käyttäjän kokonaispääoman kahden desimaalin tarkkuudella.
        """
        if self._logged_user:
            capital = self.get_capital()
            total_capital = self.total_portfolio_worth()+capital
            return float(f"{total_capital:.2f}")

        return None

    def set_logged_user(self, username):
        """Asettaa kirjautuneen käyttäjän palveluun.

        Args:
            username (str): Sisäänkirjautuvan käyttäjän käyttäjätunnus

        """
        self._logged_user = username

    def get_logged_user(self):
        """Palauttaa kirjautuneen käyttäjän.

        Returns:
            str: Palauttaa kirjautuneen käyttäjän käyttäjänimen
        """
        return self._logged_user


portfolio_services = PortfolioServices()
