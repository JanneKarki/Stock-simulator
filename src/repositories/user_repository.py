from database_connection import get_database_connection


class UserRepostory:
    """Käyttäjien tietokannan hallinnasta vastaava luokka.
    """
    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection (object): Tietokantayhteyden connection-olio.
        """
        self.connection = connection


    def new_user(self, user):
        """Tallentaa uuden käyttäjän tietokantaan.

        Args:
            user (object): User-olio joka tallennetaan tietokantaan

        Returns:
            _object_: Tallennettu user-olio.
        """
        cursor = self.connection.cursor()

        cursor.execute(
            """INSERT INTO
                Users(
                    username,
                    password,
                    capital
                )
                values (?,?,?)""",
                (user.username, user.password, user.capital)
            )

        self.connection.commit()
        
        return user


    def print_all_users(self):
        """Tulostaa kaikki tietokantaan tallennetut käyttäjänimet.
        """
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM Users")

        rows = cursor.fetchall()

        for row in rows:
            username = row[0]
            print(username)


    def find_user(self, user):
        """Palauttaa tietokannasta käyttäjän.

        Args:
            user (_str_): Käyttäjä joka tietokannasta palautetaan.

        Returns:
            _tuple_: Palauttaa käyttäjän käyttäjänimen, salasana ja pääoman. Jos
                    käyttäjää ei ole, palauttaa None.
        """
        cursor = self.connection.cursor()

        cursor.execute(
            """SELECT *
                FROM Users
                WHERE username = ?""",
                [user]
            )

        row = cursor.fetchone()

        if not row:
            return None

        username = row[0]
        password = row[1]
        capital = row[2]

        return (username,password,capital)


    def get_user_capital(self, user):
        """Palauttaa tietokannasta käyttäjän pääoman.

        Args:
            user (_str_): Käyttäjä jonka pääoma tietokannasta palautetaan.

        Returns:
            _float_: Palauttaa käyttäjän pääoman. Jos käyttäjää ei ole,
                    palauttaa None.
        """
        capital = None

        cursor = self.connection.cursor()


        cursor.execute(
            """SELECT *
                FROM Users
                WHERE username = ?
                """,
                [user]
            )

        row = cursor.fetchone()

        if row:
            capital = float(f"{row[2]:.2f}")

        return capital


    def adjust_capital(self, user, amount):
        """Päivittää käyttäjän pääoman summan.

        Args:
            user (_str_): Käyttäjä jonka pääoma päivitetään.
            amount (_float_): Määrä joka lisätään pääomaan. 
        """
        old_capital = self.get_user_capital(user)
        new_capital = old_capital + amount

        cursor = self.connection.cursor()

        cursor.execute(
            """UPDATE Users
                SET capital = ?
                WHERE username = ?
                """,
                [new_capital, user]
            )


    def delete_all(self):
        """Poistaa tietokannasta kaikki käyttäjät.
        """
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM Users")
        
        self.connection.commit()


user_repository = UserRepostory(get_database_connection())
