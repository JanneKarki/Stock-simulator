from repositories.user_repository import (user_repository as default_user_repository)
from repositories.stock_repository import (stock_repository as default_stock_repository)
from services.actions import Actions


class PortfolioServices:

    def __init__(
        self,
        user_repository=default_user_repository, 
        stock_repository=default_stock_repository
        ):

        self._logged_user = None
        self._stock_repository = stock_repository
        self._user_repository = user_repository
        self.actions = Actions()

    def login(self, username):
        """Kirjaa käyttäjän sisään sovellukseen.
        
        Args:
            username:
            password:

        """
        self._logged_user = username
        return self._logged_user

    def get_capital(self):
        """Palauttaa kirjautuneen käyttäjän pääoman"""
        return self._user_repository.get_user_capital(self._logged_user)

   # def find_stock_from_portfolio(self,stock):
    #        return self._stock_repository.get_stock_from_portfolio(self._logged_user,stock)

    def get_portfolio(self):
        """Palauttaa kirjautuneen käyttäjän portfolion"""
        return self._stock_repository.get_portfolio_from_database(self._logged_user)

    def rank_investments(self):
            """Lasekee ja järjestää sijoitukset listaan tuoton/tappion perusteella"""
            rank_list = []
            portfolio = self.get_portfolio()
            for item in portfolio:
                latest_price = self.actions.get_latest_price(item[0])
                entry_price = item[1]*item[2]
                end_price = latest_price*item[2]
                profit = end_price-entry_price
                rank_list.append((item[0], "%.3f" % profit))
            rank_list.sort(key=lambda y: y[1])
            return rank_list

    def total_win_loss(self):
        total = 0
        portfolio = self.get_portfolio()
        for item in portfolio:
            latest_price =  self.actions.get_latest_price(item[0])
            entry_price = item[1]*item[2]
            end_price = latest_price*item[2]
            profit = end_price-entry_price
            total += profit
        return total

    def total_portfolio_worth(self):
        portfolio = self._stock_repository.get_portfolio_from_database(self._logged_user)
        total_worth = 0
        for i in portfolio:
            stock_amount = i[2]
            present_price = self.actions.get_latest_price(i[0]) 
            total_worth += (stock_amount*present_price)
        return total_worth

    def total_capital(self):
        if self._logged_user:
            net_capital = self.get_capital()
            return net_capital+self.total_portfolio_worth()
        return None

    def print_total_win_loss(self):
        total = self.total_win_loss()
        print("Net profit " "%.3f" % total)
    
    def logout(self):
        """Kirjaa käyttäjän ulos sovelluksesta"""
        self._logged_user = None