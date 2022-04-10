from database_connection import get_database_connection
import sqlite3
from user import User

class UserRepostory:
    def __init__(self, connection):
        self.connection = sqlite3.connect("stocks.db")
        self.connection.isolation_level = None


    def new_user(self, user):

        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO Users (username, password, capital) values (?,?,?)", (user.username, user.password, user.capital))

        self.connection.commit()

        return user

    def find_user(self, user):

        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM Users WHERE username = ?", (user,) )

user_repository = UserRepostory(get_database_connection)