from tkinter import ttk, constants


class HelloView:

    def __init__(self,root, handle_good_bye):
        self._root = root
        self._handle_good_bye = handle_good_bye
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Hello!")
        
        button = ttk.Button(
            master=self._frame,
            text="Say good bye",
            command=self._handle_good_bye
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)