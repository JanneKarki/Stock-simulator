import unittest
from investor import Investor


class TestInvestor(unittest.TestCase):
    def setUp(self):
        self.investor = Investor("ABC", 10000)
    

    def test_investor_name_and_capital_correct_at_start(self):
        self.assertEqual(self.investor.capital, 10000)