import unittest
from repositories.user_repository import user_repository
from user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_erkki = User("Erkki", "1234", 10000)

    def test_new_user(self):
        user_repository.new_user(self.user_erkki)
        user = user_repository.find_user(self.user_erkki.username)

        self.assertEqual(user[0], self.user_erkki.username)
        self.assertEqual(user[2], 10000)
