import yfinance as yf
from user import User
from user_repository import (user_repository as default_user_repository)
from stock_repository import (stock_repository as default_stock_repository)


'''Sovelluslogiikasta vastaava luokka''' # pylint: disable=pointless-string-statement


class Actions:

    def __init__(self, user_repository=default_user_repository,
                 stock_repository=default_stock_repository):
        self.__user = None
        self.__stock_repository = stock_repository
        self.__user_repository = user_repository

    def get_latest_price(self, stock):
        share = yf.Ticker(stock)
        dataframe = share.history(period="1d", interval="1d")
        return float("%.2f" % dataframe.iat[0, 3])

    def buy_stock(self, stock, amount):
        buy_price = self.get_latest_price(stock)
        # vähennä pääomaa sijoituksen verran
        self.__user_repository.adjust_capital(
            self.__user, -abs(buy_price*amount))
        self.__stock_repository.add_to_portfolio(
            self.__user, stock, buy_price, amount)  # lisää osakkeet portfolioon

    def sell_stock(self, stock, amount):
        sell_price = self.get_latest_price(stock)
        self.__user_repository.adjust_capital(
            self.__user, sell_price*amount)  # lisää pääomaa myynnin verran
        self.__stock_repository.remove_stock_from_portfolio(
            self.__user, stock, amount)  # vähennä osakkeita

    def get_stock_info(self, stock):
        share = yf.Ticker(stock)
        print(share.info['longBusinessSummary'])

    def get_capital(self):
        return self.__user_repository.get_user_capital(self.__user)

    def create_user(self, username, password, capital):
        user = self.__user_repository.new_user(
            User(username, password, capital))
        return user

    def get_portfolio(self):
        return self.__stock_repository.get_portfolio_from_database(self.__user)

    def get_all_users(self):
        return self.__user_repository.print_all_users()

    def get_user(self):
        return self.__user

    def login(self, user):
        self.__user = user

    def rank_investments(self):
        rank_list = []
        portfolio = self.get_portfolio()
        for item in portfolio:
            latest_price = self.get_latest_price(item[0])
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
            latest_price = self.get_latest_price(item[0])
            entry_price = item[1]*item[2]
            end_price = latest_price*item[2]
            profit = end_price-entry_price
            total += profit
        return total

    def total_capital(self):
        net_capital = self.get_capital()
        return net_capital+self.total_win_loss()

    def print_total_win_loss(self):
        total = self.total_win_loss()
        print("Net profit " "%.3f" % total)
