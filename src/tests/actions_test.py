import unittest
from investor import Investor
from actions import Actions

class TestActions(unittest.TestCase):
    def setUp(self):
        self.investor = Investor("ABC", 10000)
        self.actions = Actions(self.investor)

    def test_buy_stock_capital_decreases(self):
        self.actions.buy_stock('NOK', 1)
        self.assertLess(self.investor.capital, 10000)

    def test_bought_stock_is_in_portfolio(self):
        self.actions.buy_stock('NOK', 1)
        found = 'NOK' in self.investor.portfolio
        self.assertEqual(found, True)

    def test_stock_amount_is_correct_in_portfolio(self):
        self.actions.buy_stock('NOK',1)
        amount = self.investor.portfolio['NOK'][0]
        self.assertEqual(amount,1)