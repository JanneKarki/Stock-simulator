from tkinter import ttk, constants
from services.user_services import user_services, InvalidCredentialsError

class CreateUserView:
    def __init__(self, root, handle_return):
        self._root = root
        self._handle_return = handle_return
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        capital = self._capital_entry.get()
    
        try:
            print(username)
            print(password)
            user_services.create_user(username, password, capital)
            self._handle_return
           
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")

    def _show_error(self,message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Create new user")


         # Username
        username_label = ttk.Label(master=self._frame, text="Username:")
        self._username_entry = ttk.Entry(master=self._frame)

        # Password
        password_label = ttk.Label(master=self._frame, text="Password:")
        self._password_entry = ttk.Entry(master=self._frame)

        # Capital
        capital_label = ttk.Label(master=self._frame, text="Capital:")
        self._capital_entry = ttk.Entry(master=self._frame)




        create_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._create_user_handler
        )


        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_return
        )

        heading_label.grid(row=0, column=0)

        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        capital_label.grid(row=3, column=0, padx=5, pady=5)
        self._capital_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        create_button.grid(row=4, column=0, padx=5, pady=25)
        back_button.grid(row=4, column=1, padx=5, pady=25)