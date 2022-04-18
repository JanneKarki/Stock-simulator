from tkinter import ttk, constants

class PortfolioView:
    def __init__(self, root, handle_action):
        self._root = root
        self._handle_action = handle_action
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Portfolio is here")
                
        back_to_action_button= ttk.Button(
            master=self._frame,
            text="Back_to_action",
            command=self._handle_action
        )

        label.grid(row=0, column=0)
        back_to_action_button.grid(row=2, column=0)
        