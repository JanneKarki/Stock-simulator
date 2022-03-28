import yfinance as yf

class Investor:
    
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital
        self.portfolio = {}
            
    
    def buy_stock(self, stock, amount):
        buy_price = self.get_latest_price(stock)
        self.adjust_capital(-abs(buy_price*amount)) # vähennä pääomaa sijoituksen verran
        self.add_portfolio(stock, buy_price, amount) # lisää osakkeet portfolioon
        
        # amount, price
                   
                
    def add_portfolio(self, stock, price, amount): # lisää osakkeen portfolioon
        if stock not in self.portfolio: # jos osaketta ei ole vielä, lisää portfolioon sellaisenaan
            self.portfolio[stock] = (amount, price)
            
        else: #jos osaketta on jo ostettuna, päivitä määrä ja osakkeille keskimääräinen hinta
            x = self.portfolio[stock]
            new_amount = amount + x[0]
            avgprice = ((price*amount)+(x[0]*x[1]))/new_amount
            self.portfolio[stock] = (new_amount,avgprice)   
    
    
    def sell_stock(self, stock, sell_price, amount):
        
        if stock in self.portfolio:
            x = self.portfolio[stock] #osake portfoliosta
            avg_price = x[1]        # osakkeen keskimääräinen hankinta hinta
            net = sell_price-avg_price # sijoituksen netto tuotto/tappio
            
            if amount <= x[0]:  # jos myyntimäärä oikein, päivitä pääoma ja portfolio
                self.adjust_capital(net)
                self.remove_stock(stock,amount, x)
                
            
            else:
                print("Too large sell order. You own", x[0], "shares" )
              
    
    def remove_stock(self, stock, amount, holding ):
        if holding[0] == amount:    # Jos myyty kaikki osakkeet, poistetaan osake kokonaan portfoliosta
            self.portfolio.pop(stock)
        else:                       # Jos myyty osa, päivitetään uusi määrä
            new_amount = holding[0]-amount
            self.portfolio[stock] = (new_amount, holding[1])
         
    def adjust_capital(self, amount):
        self.capital += amount
        
    
    def show_portfolio(self):
        print(self.portfolio)
        
    def show_capital(self):
        print(self.capital)
        
    def get_stock_info(self, stock):
        share = yf.Ticker(stock)
        print(share.info['longBusinessSummary'])
        
    def get_latest_price(self, stock):
        share = yf.Ticker(stock)
        df = share.history(period="1d", interval= "1d")
        return df.iat[0,1]
        
        
    
seppo = Investor("Seppo", 10000)
seppo.add_portfolio("MSFT", 12,20)
seppo.show_portfolio()
seppo.add_portfolio("MSFT", 11, 20)
seppo.show_portfolio()
seppo.sell_stock('MSFT', 200, 10)
seppo.show_capital()
seppo.show_portfolio()

print(seppo.get_latest_price('MSFT'))
