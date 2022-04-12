from unicodedata import name
from database_connection import get_database_connection
import sqlite3


def drop_tables(parameter):

    cursor = parameter.cursor()
    print(parameter)
    cursor.execute("DROP TABLE IF EXISTS Stocks")
    cursor.execute("DROP TABLE IF EXISTS Users")

    parameter.commit()

def create_tables(connection):

    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE Stocks(
                    user text, 
                    content text, 
                    avg_price float(24), 
                    amount integer)""")

    cursor.execute("""CREATE TABLE Users(
                    username text primary key, 
                    password text, 
                    capital float(24))""")
    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()

