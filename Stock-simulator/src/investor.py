#import yfinance as yf

class Investor:

    def __init__(self,nimi, capital):
        self.nimi = nimi
        self.capital = capital
        self.portfolio = {}
        

    def add_portfolio(self, stock, price, amount): # lisää osakkeen portfolioon
        if stock not in self.portfolio: # jos osaketta ei ole vielä, lisää portfolioon sellaisenaan
            self.portfolio[stock] = (amount, price)
            
        else: #jos osaketta on jo ostettuna, päivitä määrä ja osakkeille keskimääräinen hinta
            x = self.portfolio[stock]
            new_amount = amount + x[0]
            avgprice = ((price*amount)+(x[0]*x[1]))/new_amount
            self.portfolio[stock] = (new_amount,avgprice)  

    def remove_stock(self, stock, amount ):
        holding = self.portfolio[stock]
        if holding[0] == amount:    # Jos myyty kaikki osakkeet, poistetaan osake kokonaan portfoliosta
            self.portfolio.pop(stock)
        else:                       # Jos myyty osa, päivitetään uusi määrä
            new_amount = holding[0]-amount
            self.portfolio[stock] = (new_amount, holding[1])

    def adjust_capital(self, amount):
        self.capital += amount

    def get_portfolio(self):
        return self.portfolio
        
    def get_capital(self):
        return self.capital