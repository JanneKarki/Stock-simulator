from tkinter import StringVar, ttk, constants
from turtle import bgcolor
from services.stock_actions import stock_actions as actions
from services.user_services import user_services, InvalidCredentialsError
from services.portfolio_services import portfolio_services as portofolio


class LoginView:
    """Käyttöliittymäluokka, joka vastaa sisäänkirjautumisnäkymästä.
    """
    def __init__(self, root, handle_create_user, handle_action):
        """_summary_

        Args:
            root (tkinter.TK): Graafisen käyttöliittymän moduuli.
            handle_create_user (method): Metodi, joka siirtää CreateUser-näkymään.
            handle_action (method): Metodi, joka siirtää StockActions-näkymään.
        """
        self._root = root
        self._handle_create_user = handle_create_user
        self._frame = None
        self._handle_action = handle_action
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None
        self.stock_actions = actions
        self.portfolio_services = portofolio

        self._initialize()

    def pack(self):
        """Määrittää ikkunan geometrian.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Sulkee nykyisen näkymän.
        """
        self._frame.destroy()

    def _login_handler(self):
        """Tapahtumankäsittelijä joka kirjaa käyttäjän sisään.
        """
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_services.login(username, password,
                                self.stock_actions, self.portfolio_services)
            self._handle_action(self.stock_actions, self.portfolio_services)

        except InvalidCredentialsError:
            self._show_error("Invalid username or password")

    def _show_error(self, message):
        """Asettaa virheviestin näkyville.

        Args:
            message (str): Näytettävä virheviesti.
        """
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Piilottaa näytetyn virheviestin.
        """
        self._error_label.grid_remove()

    def _initialize(self):
        """Alustaa StockActions-näkymän.
        """

        self._frame = ttk.Frame(master=self._root)
        s = ttk.Style()
        s.configure("TFrame", background='skyblue')
        s.configure("TButton", background="lightblue")
        s.configure("TLabel", background="skyblue")
        s.configure("TListbox", background="blue")
        self._set_buttons()
        self._set_entries()
        self._set_labels()

        self._frame.grid_columnconfigure(0, weight=1, minsize=150)

    def _set_labels(self):
        """Määrittelee ja asettaa näkymän teksti-labelit.
        """
        heading_label = ttk.Label(master=self._frame, text="Hello")
        username_label = ttk.Label(master=self._frame, text="Username:")
        password_label = ttk.Label(master=self._frame, text="Password:")

        # Error_label
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        #Label positions
        heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._error_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        
    
    def _set_buttons(self):
        """Määrittelee ja asettaa näkymään button-painikkeet.
        """

        login_button = ttk.Button(
            master=self._frame,
            text="Login User",
            command=self._login_handler
        )
        create_user_button = ttk.Button(
            master=self._frame,
            text="New User",
            command=self._handle_create_user
        )
        #Button positions
        login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        create_user_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)       


    def _set_entries(self):
        """Määrittelee ja asettaa näkymään "username"- ja "password"-syötteiden entry-kentät.
        """
        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame)

        # Entries positions
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
