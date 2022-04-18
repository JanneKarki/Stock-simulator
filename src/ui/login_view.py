from tkinter import ttk, constants


class LoginView:

    def __init__(self,root, handle_good_bye, handle_action):
        self._root = root
        self._handle_good_bye = handle_good_bye
        self._frame = None
        self._handle_action = handle_action

        self._username_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        heading_label = ttk.Label(master=self._root, text = "Login")
        #heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Login")
        
        login_button = ttk.Button(
            master=self._frame,
            text="Login User",
            command=self._handle_action
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create User",
            command=self._handle_good_bye
        )

        label.grid(row=0, column=0)
        login_button.grid(row=1, column=0)
        create_user_button.grid(row=2, column=0)

