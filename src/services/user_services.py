from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository)


class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class EmptyInputError(Exception):
    pass

class CapitalInputError(Exception):
    pass

class UserServices:
    """Käyttäjään liittyvistä toiminnoista vastaava luokka.
    """

    def __init__(self, user_repository=default_user_repository):
        """Luokan konstruktori.

        Args:
            user_repository (object, optional):
        """
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, capital):
        """Luo uuden käyttäjän.

        Args:
            username (str): Käyttäjän valitsema käyttäjänimi.
            password (str): Käyttäjän valitsema salasana.
            capital (int): Käyttäjän valitsema alkupääoma.

        Returns:
            object: User-luokan olio.

        Raises:
            EmptyInputError:
                Virhe joka tapahtuu jos jokin syöte on tyhjä.
            CapitalInputError:
                Virhe joka tapahtuu jos pääoman syöte ei ole numeerinen.
            UsernameExistsError:
                Virhe joka tapahtuu jos käyttäjänimi on jo käytössä.

        """

        if username == "" or password == "" or capital == "":
            raise EmptyInputError('Inputs cannot be empty')

        if not capital.isnumeric():
            raise CapitalInputError('Capital entry must be only numeric')

        existing_user = self._user_repository.find_user(username)

        if existing_user:
            raise UsernameExistsError('Username', username, 'already exists')

        user = self._user_repository.new_user(
            User(username, password, capital))
        return user

    def find_user(self, username):
        """Etsii käyttäjän tietokannasta kutsumalla UserRepository-luokan metodia.

        Args:
            username (str): Etsittävä käyttäjätunnus.

        Returns:
            boolean: True jos käyttäjä löytyy tietokannasta, muussa tapauksessa False.
        """
        user = self._user_repository.find_user(username)

        if user:
            return True
        return False

    def get_capital(self):
        """Hakee kirjautuneen käyttäjän pääoman kutsumalla UserRepository-luokan metodia.
        
        Returns:
            float: Palauttaa käyttäjän pääoman.
        """
        return self._user_repository.get_user_capital(self._user)


    def login(self, username, password, stock_actions, portfolio_services):
        """Kirjaa käyttäjän sisään sovellukseen.

        Args:
            username (str): Kirjautuvan käyttäjän käyttäjätunnus.
            password (str): Kirjautuvan käyttäjän salasana.
            stock_actions (class): Osakkeiden toiminnoista vastaava luokka.
            portfolio_services (class): Portfolion toiminnoista vastaava luokka.

        Raises:
            InvalidCredentialsError:
                Virhe joka nousee, jos käyttäjätunnus tai salasana on väärin.

        """
        result = None, None

        user = self._user_repository.find_user(username)
        
        if user:
            result = user
        user_password = result[1]
        user_username = result[0]

        if user_password != password:
            raise InvalidCredentialsError('Väärä käyttäjätunnus tai salasana')
        
        #Login
        self._user = user_username
        stock_actions.set_logged_user(self._user)
        portfolio_services.set_logged_user(self._user)

        


    def get_logged_user(self):
        """Palauttaa kirjautuneen käyttäjän.

        Returns:
            str: Palauttaa kirjautuneen käyttäjän käyttäjänimen.
        """
        return self._user


    def logout(self):
        """Kirjaa käyttäjän ulos sovelluksesta.
        """
        self._user = None


user_services = UserServices()
