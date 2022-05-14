import unittest
from entities.user import User
from services.stock_actions import StockActions
from services.user_services import UserServices
from repositories.user_repository import user_repository
from repositories.stock_repository import stock_repository
from services.portfolio_services import PortfolioServices


class TestPortfolioServices(unittest.TestCase):

    def setUp(self):
        stock_repository.delete_all()
        user_repository.delete_all()

        self.actions = StockActions()
        self.user_actions = UserServices()
        self.portfolio_services = PortfolioServices()
        self.user_erkki = self.user_actions.create_user(
            "Erkki", "1234", "1000000")
        self.user_actions.login(
            self.user_erkki.username,
            self.user_erkki.password,
            self.actions,
            self.portfolio_services
        )

    def test_stock_goes_in_portfolio_and_amount_is_correct(self):
        stock_repository.add_to_portfolio("Erkki", "AAPL", 1, 1)
        stock_from_portolio = self.portfolio_services.find_stock_from_portfolio(
            "AAPL")
        isempty = []
        self.assertNotEqual(stock_from_portolio, isempty)
        self.assertEqual(stock_from_portolio[0][1], 1)


    def test_portfolio_rank_is_in_correct_order(self):
        stock_repository.add_to_portfolio("Erkki", "TSLA", -2000, 1)
        stock_repository.add_to_portfolio("Erkki", "NOK", -100, 1)
        stock_repository.add_to_portfolio("Erkki", "AAPL", -1000, 1)

        rank_list = self.portfolio_services.rank_investments()
        self.assertEqual(rank_list[0][0], "NOK")
        self.assertEqual(rank_list[1][0], "AAPL")
        self.assertEqual(rank_list[2][0], "TSLA")

    def test_portfolio_worth_is_correct(self):
        price_a = self.actions.buy_stock("ABEV", "10")
        price_b = self.actions.buy_stock("TLRY", "10")
        price_c = self.actions.buy_stock("ZOM", "10")
        total_cost = (price_a*10)+(price_b*10)+(price_c*10)
        portfolio_worth = self.portfolio_services.total_portfolio_worth()
        self.assertEqual(int(portfolio_worth), int(total_cost))

    def test_total_win_loss_is_correct(self):
        stock_repository.add_to_portfolio("Erkki", "ABEV", -2000, 1)
        stock_repository.add_to_portfolio("Erkki", "TLRY", 100, 1)
        stock_repository.add_to_portfolio("Erkki", "ZOM", -1000, 1)

        profit_a = self.actions.get_latest_price("ABEV")+2000
        profit_b = self.actions.get_latest_price("TLRY")-100
        profit_c = self.actions.get_latest_price("ZOM")+1000
        total_profit = profit_a+profit_b+profit_c

        total_win_loss = self.portfolio_services.total_win_loss()
        self.assertEqual(int(total_win_loss),int(total_profit))
    
    def test_total_capital_is_correct(self):
        price = self.actions.buy_stock("ABEV", "1")
        capital = self.user_actions.get_capital()
        total_capital = (price)+capital
        self.assertEqual(total_capital, self.portfolio_services.total_capital())

    def test_not_logged_user_total_capital_returns_none(self):
        self.portfolio_services.set_logged_user(None)
        capital = self.portfolio_services.total_capital()
        self.assertEqual(capital,None)