import sqlite3

connection = sqlite3.connect("stocks.db")
connection.isolation_level = None

def get_database_connection():
    return connection

    