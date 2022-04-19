from logging import raiseExceptions
from random import choices

from services.portfolio_services import PortfolioServices
from services.user_services import UserServices
from services.actions import Actions
from services.actions import Actions, InvalidCredentialsError
from initialize_database import initialize_database

kirjaudu = """
1 - Kirjaudu sisään
2 - Luo käyttäjä
3 - Exit
"""


valinnat = """Toiminnot:
    1 - Osta osaketta
    2 - Myy osaketta
    3 - Hae yrityksen esittely
    4 - Näytä portfolio
    5 - Kirjaudu ulos
Enter - Päivitä hinnat

"""


user_actions = UserServices()
actions = Actions()
portfolio = PortfolioServices()
user_actions.get_all_users()
while True:

    print(kirjaudu)
    valinta = input(": ")
    if valinta == "1":

        print("Käyttäjätunnus")
        username = input(": ")
        if username == "":
            continue

        print("Salasana")
        password = input(": ")

        try:
           # portfolio.login(actions.login(user_actions.login(username, password)))
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
            if user_actions.find_user(username):
                print("Käytössä")
                continue
            else:
                print("tunnus natsaa")
                break
        print("Valitse salasana")
        password = input(":")
        print("Valitse pääoman määrä")
        capital = input(": ")
        user = user_actions.create_user(username, password, capital)
        user_actions.login(user.username, user.password, actions, portfolio)

        #portfolio = PortfolioServices(user)

    if valinta == "3":
        break

    while True:
        logged_user = user_actions.get_logged_user()
        print("Kirjautunut:", logged_user)
        print("Free capital", user_actions.get_capital(), "$")

        print("Portfolio worth", portfolio.total_portfolio_worth())
        portfolio.print_total_win_loss()
        print("Total capital", portfolio.total_capital())
        print("Rank list", portfolio.rank_investments())
        print()
        print(valinnat)
        print("Valinta")
        valinta = input(": ")
        print(valinta)
        if valinta == "1":
            print("Anna symboli (Esim. AAPL)")
            symbol = input(": ")
            price = actions.get_latest_price(symbol)
            print(symbol, "share price", price)
            print("Anna määrä")
            amount = int(input(": "))
            total_price = price*amount
            print(symbol, amount, "shares", "USD" + str("%.2f" % total_price))
            print("Hyväksy osto? y/n")
            choice = input(": ")
            if choice == "y":
                actions.buy_stock(symbol, amount)

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
            actions.get_stock_info(symbol)

        if valinta == "4":
            print(portfolio.get_portfolio(),
                  "tämä on käyttäjän", logged_user, "portfolio")

        if valinta == "5":
            user_actions.logout()
            actions.logout()
            portfolio.logout()
            break
