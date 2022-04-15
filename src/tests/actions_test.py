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
