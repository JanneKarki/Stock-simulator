from importlib import import_module
import unittest
from user import User
from services.stock_actions import StockActions
from repositories.user_repository import (
    user_repository as default_user_repository)
from repositories.stock_repository import (
    stock_repository as default_stock_repository)


class TestStockRepository(unittest.TestCase):
    def setUp(self):
        self.actions = Actions()
        self.user_erkki = User('arkki', "1234", 10000)
