from logging import raiseExceptions
from random import choices
from actions import Actions, InvalidCredentialsError

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
actions = Actions()
actions.get_all_users()



while True:
    
    print(kirjaudu)
    valinta = input(": ")
    if valinta == "1":
       
        print("Käyttäjätunnus")
        username = input(": ")
        if username == "":
            continue
            
        print("Salasana")
        password = input (": ")

        try:
            actions.login(username, password)
        except InvalidCredentialsError:
            print("Väärä käyttäjätunnus tai salasana")
            continue
            

    if valinta == "2":
        while True:
            print("Valitse käyttäjätunnus")
            username = input(": ")
            if username == "":
                continue
            if actions.find_user(username):
                print("Käytössä")
                continue
            else:
                print("tunnus natsaa")
                break
        print("Valitse salasana")
        password = input(":") 
        print("Valitse pääoman määrä")
        capital = input(": ")
        user = actions.create_user(username, password, capital)
       
    if valinta == "3":
        break


    while True:
        print(actions.find_user(username))
        logged_user = actions.get_logged_user()
        print("Kirjautunut:" , logged_user)
        print("Free capital", actions.get_capital(), "$")
         
        print("Portfolio worth", actions.total_portfolio_worth())
        actions.print_total_win_loss()
        print( "Total capital", actions.total_capital())
        print( "Rank list", actions.rank_investments())
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
            print(actions.get_portfolio(), "tämä on käyttäjän", logged_user, "portfolio")

        if valinta == "5":
            actions.logout()
            break
