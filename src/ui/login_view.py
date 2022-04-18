from tkinter import ttk, constants
from services.actions import Actions

class LoginView:

    def __init__(self,root, handle_create_user, handle_action):
        self._root = root
        self._handle_create_user = handle_create_user
        self._frame = None
        self._handle_action = handle_action
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):

        
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Hello")
        
        #Username
        username_label = ttk.Label(master=self._frame, text="Username:")
        self._username_entry = ttk.Entry(master=self._frame)

        #Password
        password_label = ttk.Label(master=self._frame, text="Password:")
        self._password_entry = ttk.Entry(master=self._frame)
        
        #Buttons
        login_button = ttk.Button(
            master=self._frame,
            text="Login User",
            command=self._handle_action
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="New User",
            command=self._handle_create_user
        )

        #Build Frame grid
        heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)      
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        create_user_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=250)