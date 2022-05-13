import unittest

from numpy import empty
from entities.user import User
from services.stock_actions import StockActions
from services.user_services import UserServices
from repositories.user_repository import NotEnoughMoneyError, user_repository
from repositories.stock_repository import stock_repository
from services.portfolio_services import PortfolioServices


class TestActions(unittest.TestCase):

    def setUp(self):
        stock_repository.delete_all()
        user_repository.delete_all()

        self.actions = StockActions()
        self.user_actions = UserServices()
        self.portfolio_services = PortfolioServices()
        self.user_erkki = self.user_actions.create_user(
            "Erkki", "1234", "10000")
        self.user_actions.login(
            self.user_erkki.username,
            self.user_erkki.password,
            self.actions,
            self.portfolio_services
        )

    def test_find_created_user(self):
        user = self.user_actions.find_user(self.user_erkki.username)
        self.assertEqual(user, True)

    def test_get_correct_capital(self):
        capital = self.user_actions.get_capital()
        self.assertEqual(capital, 10000)

    def test_buy_stock_goes_in_portfolio_and_amount_is_correct(self):
        self.actions.buy_stock("AAPL", "1")
        stock_from_portolio = self.portfolio_services.find_stock_from_portfolio(
            "AAPL")
        isempty = []
        self.assertNotEqual(stock_from_portolio, isempty )
        self.assertEqual(stock_from_portolio[0][1], 1)

    def test_sell_all_stock_removes_the_stock_from_portfolio(self):
        self.actions.buy_stock("AAPL", "1")
        self.actions.sell_stock("AAPL", "1")
        stock_from_portfolio = self.portfolio_services.find_stock_from_portfolio(
            "AAPL")
        isempty = []
        self.assertEqual(stock_from_portfolio, isempty)

    def test_buy_more_stock_updates_stock_amount_correctly(self):
        self.actions.buy_stock("AAPL", "1")
        self.actions.buy_stock("AAPL", "2")
        stock_from_portfolio = self.portfolio_services.find_stock_from_portfolio(
            "AAPL")
        self.assertEqual(stock_from_portfolio[0][1], 3)

    def test_sell_stock_updates_stock_amount_correctly(self):
        self.actions.buy_stock("AAPL", "3")
        self.actions.sell_stock("AAPL", "2")
        stock_from_portfolio = self.portfolio_services.find_stock_from_portfolio(
            "AAPL")
        self.assertEqual(stock_from_portfolio[0][1], 1)

    def test_buy_stock_capital_decreases_correctly(self):
        capital_before = self.user_actions.get_capital()
        price = self.actions.buy_stock("AAPL", "1")
        capital_after = self.user_actions.get_capital()
        self.assertEqual(float("{0:.2f}".format(
            capital_before-capital_after)), price)

    def test_sell_stock_capital_increases_correctly(self):
        self.actions.buy_stock('AAPL', "1")
        capital_before = self.user_actions.get_capital()
        price = self.actions.sell_stock("AAPL", "1")
        capital_after = self.user_actions.get_capital()
        self.assertEqual(float("{0:.2f}".format(
            capital_after-capital_before)), price)


    def test_if_not_enough_money_stock_not_bought(self):
        with self.assertRaises(NotEnoughMoneyError) as cm:

        
            self.actions.buy_stock("TSLA", "10000000")
        the_exception = cm.exception
        self.assertEqual(the_exception, NotEnoughMoneyError('Not enough money'))