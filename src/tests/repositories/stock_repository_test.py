import unittest
from repositories.stock_repository import stock_repository


class TestStockRepository(unittest.TestCase):
    def setUp(self):
        stock_repository.delete_all()
        self.stock_repository = stock_repository
        stock_repository.add_to_portfolio("Testaaja", "AAPL", 100, 10)   

    def test_stock_is_found_and_amount_and_price_are_correct(self):
        stock_data = self.stock_repository.get_stock_from_portfolio("Testaaja", "AAPL")
        amount = stock_data[0][1]
        price = stock_data[0][0]
        self.assertEqual(amount, 10)
        self.assertEqual(int(price),100)

    def test_remove_stock_decreases_amount_correctly(self):
        self.stock_repository.remove_stock_from_portfolio("Testaaja", "AAPL", 5)
        stock_data = self.stock_repository.get_stock_from_portfolio("Testaaja", "AAPL")
        amount = stock_data[0][1]
        self.assertEqual(int(amount), 5)

    def test_portfolio_length_is_correct(self):
        self.stock_repository.add_to_portfolio("Testaaja", "NOK", 100, 10)
        porfolio = stock_repository.get_portfolio_from_database("Testaaja")
        self.assertEqual(len(porfolio), 2)

    def test_delete_stocks_is_empty(self):
        stock_repository.delete_all()
        found = self.stock_repository.get_portfolio_from_database("Testaaja")
        isempty = []
        self.assertEqual(found, isempty)

    def test_removing_whole_amount_of_stocks_deletes_the_stock_from_database(self):
        self.stock_repository.remove_stock_from_portfolio("Testaaja", "AAPL", 10)
        porfolio = stock_repository.get_portfolio_from_database("Testaaja")
        self.assertEqual(len(porfolio), 0)