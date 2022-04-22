from user import User
from repositories.user_repository import (
    user_repository as default_user_repository)


class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass


class UserServices:
    """Käyttäjän toiminnoista vastaava luokka."""

    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, capital):
        """Luo uuden käyttäjän.

        Args:
            username:
            password:
            capital:

        Returns:

        """
        existing_user = self._user_repository.find_user(username)
        
        if existing_user:
            raise UsernameExistsError('Username', username, 'already exists')
        
        user = self._user_repository.new_user(
            User(username, password, capital))
        return user

    def find_user(self, username):
        row = self._user_repository.find_user(username)
        if row:
            return True
        return False

    def login(self, username, password, stock_actions, portfolio_services):
        """Kirjaa käyttäjän sisään sovellukseen.

        Args:
            username:
            password:


        """
        user = self._user_repository.find_user(username)
        result = None, None
        if user:
            result = user
        if result[1] != password:
            raise InvalidCredentialsError('Väärä käyttäjätunnus tai salasana')
        self._user = result[0]
        stock_actions.logged_user(self._user)
        portfolio_services.logged_user(self._user)
        return user[0]

    def get_logged_user(self):
        """Palauttaa kirjautuneen käyttäjän.

        Returns:
            Kirjautuneen käyttäjän.
        """
        return self._user

    def logout(self):
        """Kirjaa käyttäjän ulos sovelluksesta."""
        self._user = None

    def get_all_users(self):
        """Palauttaa tulosteena kaikki luodut käyttäjät."""
        return self._user_repository.print_all_users()

    def get_capital(self):
        """Palauttaa kirjautuneen käyttäjän pääoman"""

        return self._user_repository.get_user_capital(self._user)


user_services = UserServices()
