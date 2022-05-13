import unittest
from entities.user import User
from services.stock_actions import StockActions
from services.user_services import InvalidCredentialsError, UserServices
from repositories.user_repository import user_repository
from repositories.stock_repository import stock_repository
from services.portfolio_services import PortfolioServices


class TestUserServices(unittest.TestCase):

    def setUp(self):
        stock_repository.delete_all()
        user_repository.delete_all()

        self.actions = StockActions()
        self.user_services = UserServices()
        self.portfolio_services = PortfolioServices()
        self.user_erkki = self.user_services.create_user(
            "Erkki", "1234", "1000000")
        self.user_services.login(
            self.user_erkki.username,
            self.user_erkki.password,
            self.actions,
            self.portfolio_services
        )

    def test_delete_user_not_found(self):
        user_repository.delete_all()
        found = self.user_services.find_user("Erkki")
        self.assertEqual(found, False)

    def test_login_with_invalid_username_and_password(self):
        with self.assertRaises(InvalidCredentialsError):
            self.user_services.login("Seppo", "1_Ulla", self.actions, self.portfolio_services)

    def test_after_logout_get_user_is_none(self):
        self.user_services.logout()
        user = self.user_services.get_logged_user()
        self.assertEqual(user,None)

    def test_succesful_login(self):
        self.user_services.logout()
        self.actions.set_logged_user(None)
        self.portfolio_services.set_logged_user(None)
        self.user_services.login(
            self.user_erkki.username,
            self.user_erkki.password,
            self.actions,
            self.portfolio_services
        )
        self.assertEqual(self.user_services.get_logged_user(), "Erkki")
        self.assertEqual(self.actions.get_logged_user(), "Erkki")
        self.assertEqual(self.portfolio_services.get_logged_user(),"Erkki")
