import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect("stocks.db")
connection.isolation_level = None



def get_database_connection():
    return connection
