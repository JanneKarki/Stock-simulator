from logging import raiseExceptions
from random import choices
from services.portfolio_services import PortfolioServices
from services.user_services import UserServices, InvalidCredentialsError, UsernameExistsError
from services.stock_actions import StockActions, SymbolNotFoundError
from initialize_database import initialize_database

kirjaudu_valikko = """
1 - Kirjaudu sisään
2 - Luo käyttäjä
3 - Exit
"""


valinnat_valikko = """Toiminnot:
    1 - Osta osaketta
    2 - Myy osaketta
    3 - Hae yrityksen esittely
    4 - Näytä portfolio
    5 - Kirjaudu ulos
Enter - Päivitä hinnat

"""


user_actions = UserServices()
actions = StockActions()
portfolio = PortfolioServices()
user_actions.get_all_users()


def print_numbers():
    print("Free capital", user_actions.get_capital(), "$")
    print("Portfolio worth", portfolio.total_portfolio_worth())
    portfolio.print_total_win_loss()
    print("Total capital", portfolio.total_capital())
    print("Rank list", portfolio.rank_investments())

while True:
    
    print(kirjaudu_valikko)
    valinta = input(": ")
    if valinta == "1":

        print("Käyttäjätunnus")
        username = input(": ")
        if username == "":
            continue

        print("Salasana")
        password = input(": ")

        try:
            user_actions.login(username, password, actions, portfolio)

        except InvalidCredentialsError:
            print("Väärä käyttäjätunnus tai salasana")
            continue

    if valinta == "2":
        while True:
            print("Valitse käyttäjätunnus")
            username = input(": ")
            if username == "":
                continue
            
            print("Valitse salasana")
            password = input(":")
            print("Valitse pääoman määrä")
            capital = input(": ")

            try: 
                user = user_actions.create_user(username, password, capital)
                
            except UsernameExistsError:
                print("Käyttäjätunnus on jo käytössä")
            

            user_actions.login(user.username, user.password, actions, portfolio)
            break

    if valinta == "3":
        break

    while True:
        logged_user = user_actions.get_logged_user()
        print("Kirjautunut:", logged_user)
        print()
        print_numbers()
        print(valinnat_valikko)
        print("Valinta")
        valinta = input(": ")
        print(valinta)
        if valinta == "1":
            while True:
                print("Anna symboli (Esim. AAPL)")
                symbol = input(": ")
                try:
                    price = actions.get_latest_price(symbol)
                    if price:
                        break
                except SymbolNotFoundError:
                    continue
                

            print(symbol, "share price", price)
            print("Anna määrä")
            while True:
                amount = input(": ")
                if not amount:
                    print("amount cant be empty")
                    continue
                if all(not num.isdigit() for num in amount):
                    print("Amount must be number.")
                    continue
                break
            total_price = price*int(amount)
            print(symbol, amount, "shares", "USD" + str("%.2f" % total_price))
            print("Hyväksy osto? y/n")
            choice = input(": ")
            if choice == "y":
                actions.buy_stock(symbol, int(amount))

        if valinta == "2":

            print("Anna symboli")
            symbol = input(": ")
            price = actions.get_latest_price(symbol)
            print(symbol, "share price", "USD"+str(price))
            print("Anna määrä")
            amount = int(input(": "))
            total_price = price*amount
            print(symbol, amount, "shares", "USD" + str("%.2f" % total_price))
            print("Hyväksy myynti? y/n")
            choice = input(": ")
            if choice == "y":
                actions.sell_stock(symbol, amount)

        if valinta == "3":
            print("Anna symboli")
            symbol = input(": ")
            
            try:
                data = actions.get_stock_info(symbol)
            except SymbolNotFoundError:
                print("Symbol not found")
            

        if valinta == "4":
            print(portfolio.get_portfolio(),
                  "tämä on käyttäjän", logged_user, "portfolio")

        if valinta == "5":
            user_actions.logout()
            actions.logged_user(None)
            portfolio.logged_user(None)
            break

