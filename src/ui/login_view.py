from tkinter import StringVar, ttk, constants
from services.stock_actions import StockActions, stock_actions as actions
from services.user_services import user_services, InvalidCredentialsError
from services.portfolio_services import portfolio_services as portofolio


class LoginView:

    def __init__(self, root, handle_create_user, handle_action):
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
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_services.login(username, password,
                                self.stock_actions, self.portfolio_services)
            self._handle_action(self.stock_actions, self.portfolio_services)

        except InvalidCredentialsError:
            self._show_error("Invalid username or password")

        

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Hello")

        # Error_label
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        # Username
        username_label = ttk.Label(master=self._frame, text="Username:")
        self._username_entry = ttk.Entry(master=self._frame)

        # Password
        password_label = ttk.Label(master=self._frame, text="Password:")
        self._password_entry = ttk.Entry(master=self._frame)

        # Buttons
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

        # Build Frame grid
        heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        create_user_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self._error_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self._frame.grid_columnconfigure(0, weight=1, minsize=150)

        self._hide_error()
