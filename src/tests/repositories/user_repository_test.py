import unittest
from entities.user import User
from repositories.user_repository import user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        
        self.user_repository = user_repository
        self.testaaja = User("Testaaja", "1234", 10000)
        user_repository.new_user(self.testaaja)

    def test_user_is_found_from_database(self):
        user = user_repository.find_user(self.testaaja.username)
        self.assertEqual(self.testaaja.username, user[0])
        self.assertEqual(self.testaaja.password, user[1])
        self.assertEqual(self.testaaja.capital, user[2])

    def test_get_user_capital_is_correct(self):
        capital = user_repository.get_user_capital(self.testaaja.username)
        self.assertEqual(capital, self.testaaja.capital)

    def test_adjust_capital_changes_capital_correctly(self):
        self.user_repository.adjust_capital(self.testaaja.username, -233)
        self.user_repository.adjust_capital(self.testaaja.username, 450)
        self.assertEqual(self.user_repository.get_user_capital(self.testaaja.username), 10217)

    def test_delete_user_not_found(self):
        user_repository.delete_all()
        user = user_repository.find_user(self.testaaja.username)
        self.assertEqual(user, None)