import unittest
from user import User
from actions import Actions
from user_repository import user_repository
from stock_repository import stock_repository


class TestActions(unittest.TestCase):

    def setUp(self):
        stock_repository.delete_all()
        user_repository.delete_all()

        self.actions = Actions()
        self.user_erkki = self.actions.create_user("Erkki", "1234", 10000)
        self.actions.login(self.user_erkki.username, self.user_erkki.password)

    def test_get_logged_user(self):
        user = self.actions.get_user()
        self.assertEqual(user[0], self.user_erkki.username)

    def test_get_correct_capital(self):
        capital = self.actions.get_capital()
        self.assertEqual(capital, 10000)

    def test_buy_stock_goes_in_portfolio_and_amount_is_correct(self):
        self.actions.buy_stock("AAPL", 1)
        stock_from_portolio = self.actions.find_stock_from_portfolio("AAPL")
        self.assertEqual(stock_from_portolio[1], "AAPL")
        self.assertEqual(stock_from_portolio[3], 1)

    def test_sell_all_stock_removes_the_stock_from_portfolio(self):
        self.actions.buy_stock("AAPL",1)
        self.actions.sell_stock("AAPL",1)
        stock_from_portfolio = self.actions.find_stock_from_portfolio("AAPL")
        self.assertEqual(stock_from_portfolio, None)

    def test_buy_more_stock_updates_stock_amount_correctly(self):
        self.actions.buy_stock("AAPL", 1)
        self.actions.buy_stock("AAPL", 2)
        stock_from_portfolio = self.actions.find_stock_from_portfolio("AAPL")
        self.assertEqual(stock_from_portfolio[3], 3)
    
    def test_sell_stock_updates_stock_amount_correctly(self):
        self.actions.buy_stock("AAPL", 3)
        self.actions.sell_stock("AAPL", 2)
        stock_from_portfolio = self.actions.find_stock_from_portfolio("AAPL")
        self.assertEqual(stock_from_portfolio[3], 1)

    def test_buy_stock_capital_decreases_correctly(self):
        capital_before = self.actions.get_capital()
        price = self.actions.buy_stock("AAPL", 1)
        capital_after = self.actions.get_capital()
        self.assertEqual(float("{0:.2f}".format(capital_before-capital_after)), price)

    def test_sell_stock_capital_decreases_correctly(self):
        capital_before = self.actions.get_capital()
        price = self.actions.sell_stock("AAPL", 1)
        capital_after = self.actions.get_capital()
        self.assertEqual(float("{0:.2f}".format(capital_after-capital_before)), price)

    #def test_sell_stock_capital_increases_correctly(self):
     #   self.actions.buy_stock("AAPL", 4)
      #  capital_before = self.actions.get_capital()
       # price = self.actions.sell_stock("AAPL",1)
       # capital_after = self.actions.get_capital
       # self.assertEqual(float("{0:.2f}".format(capital_before-capital_after)), 5)

