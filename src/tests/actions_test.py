import unittest
from user import User
from actions import Actions
from user_repository import (user_repository as default_user_repository)
from stock_repository import (stock_repository as default_stock_repository)


class TestActions(unittest.TestCase):
    def setUp(self):
        self.actions = Actions()
        self.user = User("Erkki", "1234", 10000)

    def test_buy_stock_capital_decreases(self):
        self.actions.buy_stock('NOK', 1)
        self.assertLess(self.actions.show_capital, 10000)

    def test_bought_stock_is_in_portfolio(self):
        self.actions.buy_stock('NOK', 1)
        found = 'NOK' in self.actions.get_portfolio()
        self.assertEqual(found, True)

    def test_stock_amount_is_correct_in_portfolio(self):
        self.actions.buy_stock('NOK',1)
        amount = self.actions.get_portfolio['NOK'][0]
        self.assertEqual(amount,1)