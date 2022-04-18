from tkinter import ttk, constants

class CreateUserView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):

    
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Create User")

        button = ttk.Button(
            master=self._frame,
            text="New User",
            command=self._handle_login
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
