from unicodedata import name
from database_connection import get_database_connection
import sqlite3


def drop_tables(parameter):

    cursor = parameter.cursor()
    print(parameter)
    cursor.execute("DROP TABLE IF EXISTS Stocks")

    parameter.commit()

def create_tables(connection):

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE Stocks(ID integer primary key, content text, avg_price float(24), amount integer)")

    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()

