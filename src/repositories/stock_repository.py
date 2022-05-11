from database_connection import get_database_connection


class StockNotInPortfolioError(Exception):
    pass


class TooLargeSellOrderError(Exception):
    pass


class StockRepository:
    """Osakkeiden tietokannan hallinnasta vastaava luokka.

    Attributes:
        connection: Tietokantayhteys.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection (object): Tietokantayhteyden connection-olio.
        """
        self.connection = connection

    def add_to_portfolio(self, user, stock, price, amount):
        """Lisää osakkeen tietokantaan. Tarkistaa ensin löytyykö osake jo käyttäjän
        tietokannasta. Jos osake löytyy, hinta päivitetään uuden ja vanhan hinnan
        keskiarvoon per osake, sekä osakkeiden määrään lisätään uudet osakkeet.

        Args:
            user (str): Käyttäjän tunnus, jolle osakkeet lisätään.
            stock (str): Lisättävän osakkeen symboli.
            price (float): Lisättävän osakkeen hinta.
            amount (int): Lisättävien osakkeiden määrä.

        """
        stocks_database = self.connection.cursor()

        stocks_database.execute(
            """SELECT avg_price,
            amount FROM Stocks WHERE user = ? and content = ?""",
            [user, stock]
        )

        data = stocks_database.fetchall()

        if len(data) == 0:  # Osake ei löytynyt tietokannasta
            stocks_database.execute(
                """INSERT INTO Stocks (
                    user,
                    content,
                    avg_price,
                    amount)
                    values (?,?,?,?)""",
                [user, stock, price, amount]
            )
        else:  # Osake löytyi tietokannasta
            old_amount = data[0][1]
            new_amount = old_amount+amount
            old_total_value = data[0][0]*data[0][1]
            new_total_value = amount*price
            new_avg_price = (old_total_value+new_total_value)/new_amount

            stocks_database.execute(
                """UPDATE Stocks
                    SET avg_price = ?, amount = ?
                    WHERE user = ?
                    AND content = ?""",
                [float(f"{new_avg_price:.2f}"), new_amount, user, stock]
            )

    def remove_stock_from_portfolio(self, user, stock, amount):
        """Poistaa osakkeen tietokannasta, joko kokonaan, tai vähentää sitä
            annetun määrän verran.

        Args:
            user (str): Käyttäjän tunnus, jolta osakkeet poistetaan.
            stock (str): Osakkeen symboli, joka poistetaan.
            amount (int): Poistettavien osakkeiden määrä.

        Raises:
            TooLargeSellOrderError:
                Virhe joka tapahtuu jos myyntimäärä on suurempi kuin portofliossa olevien osakkeiden määrä.
            StockNotInPortfolioError:
                Virhe joka tapahtuu jos myytävää osaketta ei ole portfoliossa.
        """
        data = self.get_stock_from_portfolio(user, stock)
        stocks_database = self.connection.cursor()

        if len(data) > 0:  # osake löytyi tietokannasta
            old_amount = data[0][1]
            if amount > old_amount:
                raise TooLargeSellOrderError("Too large sell order")
            if amount == old_amount:

                stocks_database.execute(
                    """DELETE FROM
                        Stocks WHERE
                        user = ?
                        AND content = ?""",
                    [user, stock]
                )

            if amount < old_amount:
                new_amount = old_amount - amount
                stocks_database.execute(
                    """UPDATE Stocks
                        SET amount = ?
                        WHERE user = ?
                        AND content = ?""",
                    [new_amount, user, stock]
                )
        else:
            raise StockNotInPortfolioError("Stock not owned")

    def get_portfolio_from_database(self, user):
        """ Hakee ja palauttaa tietokannasta käyttäjän portfolion.

        Args:
            user (str): Käyttäjän tunnus, jonka portfolio palautetaan.

        Returns:
            list: Palauttaa listan käytäjän osakkeista, niiden määrän ja
            keskimääräisen hankintahinnan.
        """
        stocks_database = self.connection.cursor()

        stocks_database.execute(
            """SELECT content,
                avg_price,
                amount
                FROM Stocks
                WHERE user = ?""",
            [user]
        )

        results = stocks_database.fetchall()
        print(results)
        return results

    def get_stock_from_portfolio(self, user, stock):
        """ Hakee osakkeen tietokannasta.

        Args:
            user (str): Käyttäjän tunnus, jonka portfoliosta osake palautetaan.
            stock (str): Palautettavan osakkeen symboli.

        Returns:
            list: Palauttaa osakkeen, sen määrän ja keskimääräisen
            hankintahinnan.
        """
        stock_database = self.connection.cursor()

        stock_database.execute(
            """SELECT avg_price,
                amount
                FROM Stocks
                WHERE user = ?
                AND content=?""",
            [user, stock]
        )

        result = stock_database.fetchall()

        return result

    def delete_all(self):
        """ Poistaa tietokannasta kaikki osakkeet.
        """
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM Stocks")

        self.connection.commit()


stock_repository = StockRepository(get_database_connection())
