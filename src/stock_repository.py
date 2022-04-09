from database_connection import get_database_connection
import sqlite3


class StockRepository:


    def __init__(self, connection):

        self.__connection = connection
        self.connection = sqlite3.connect("stocks.db")
        self.connection.isolation_level = None

    def add_to_portfolio(self,stock,price,amount):
        stocks_database = self.connection.cursor()
        #Tähän if lause jos osake ei ole tietokannassa
        stocks_database.execute("SELECT avg_price,amount FROM Stocks WHERE content=?", [stock])
        data=stocks_database.fetchall()
        print(data)
        if len(data) == 0: # jos 0 niin ei ole tietokannassa
            stocks_database.execute("INSERT INTO Stocks (content,avg_price,amount) values (?,?,?)", [stock,price,amount])
        else:
            print("on")
            new_amount= data[0][1]+amount
            new_avg_price = ((data[0][0]*data[0][1])+(amount*price))/new_amount
            stocks_database.execute("UPDATE Stocks SET avg_price = ? where content = ?", [new_avg_price, stock])
            stocks_database.execute("UPDATE Stocks SET amount = ? where content = ?", [new_amount, stock])
        #tähän UPDATE toiminto
        

    def remove_stock_from_portfolio(self,stock,amount):
        stocks_database = self.connection.cursor()
        stocks_database.execute("SELECT avg_price,amount FROM Stocks WHERE content=?", [stock])
        data=stocks_database.fetchall()
        if len(data) > 0:            
            old_amount = data[0][1]
            if amount == old_amount:
                stocks_database.execute("DELETE FROM Stocks (content) values (?)", [stock])
            if amount < old_amount:
                new_amount= data[0][1]-amount
                stocks_database.execute("UPDATE Stocks SET amount = ? where content = ?", [new_amount, stock])
        else:
             print("not in portfolio") # jos 0 niin ei ole tietokannassa
        

    def get_portfolio_from_database(self):
        stocks_database = self.connection.cursor()
        stocks_database.execute("SELECT * from Stocks")
        results = stocks_database.fetchall()
        return results

    
stock_repository = StockRepository(get_database_connection)