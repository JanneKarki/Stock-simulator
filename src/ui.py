from random import choices
from actions import Actions
#from portfolio import Portfolio
from initialize_database import initialize_database
from portfolio import Portfolio
from user import User


valinnat = """Toiminnot
1 - Osta osaketta
2 - Myy osaketta
3 - Hae yrityksen esittely
4 - Näytä portfolio
5 - Exit
"""

print("Anna nimesi")
nimi = input(": ")
print("Valitse pääoman suuruus")
capital = int(input(": "))

actions = Actions()


user = actions.create_user(nimi,"1234",capital)
actions.get_all_users()
actions.login(nimi)




while True:
    actions.print_total_win_loss()
    print(actions.get_capital(), "capital tietokannasta")
    print(actions.rank_investments(), "rank list")
    print(actions.get_portfolio, "tämä on käyttäjän portfolio")

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
        print(symbol, amount, "shares", "USD"+ str("%.2f" % total_price))
        print("Hyväksy osto? y/n")
        choice = input(": ")
        if choice == "y":
            actions.buy_stock(symbol,amount)

    if valinta == "2":
        
        print("Anna symboli")
        symbol = input(": ")
        price = actions.get_latest_price(symbol) 
        print(symbol, "share price","USD"+str(price))
        print("Anna määrä")
        amount = int(input(": "))
        total_price = price*amount
        print(symbol, amount, "shares", "USD"+ str("%.2f" % total_price))
        print("Hyväksy myynti? y/n")
        choice = input(": ")
        if choice == "y":
            actions.sell_stock(symbol,amount)


    if valinta == "3":
        print("Anna symboli")
        symbol = input(": ")
        actions.get_stock_info(symbol)

    if valinta == "4":
        
        print(actions.get_portfolio())
       # print(investor.get_portfolio_from_db(user))

    if valinta == "5":
        break
    

    