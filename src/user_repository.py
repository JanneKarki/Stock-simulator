import sqlite3
from database_connection import get_database_connection


class UserRepostory:
    def __init__(self, connection):
        self.connection = connection
        #self.connection.isolation_level = None

    def new_user(self, user):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Users (username, password, capital) values (?,?,?)",
                       (user.username, user.password, user.capital))
        self.connection.commit()
        return user

    def print_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])

    def find_user(self, user):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ?", [user])
        row = cursor.fetchone()
        if not row:
            return None
        return row[0],row[1],row[2]

    def get_user_capital(self, user):
        capital = None,None,None
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ? ", [user])
        row = cursor.fetchone()
        if row:
            capital = float("{0:.2f}".format(row[2]))
        return  capital


    def adjust_capital(self, user, amount):
        cursor = self.connection.cursor()
        capital = self.get_user_capital(user)
        new_capital = capital+amount
        cursor.execute("UPDATE Users SET capital = ? WHERE username = ?", [
                       new_capital, user])

    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Users")
        self.connection.commit()


user_repository = UserRepostory(get_database_connection())
