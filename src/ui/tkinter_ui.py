from asyncio import constants
from tkinter import Button, Radiobutton, Tk, ttk, constants
from tkinter_helloview import HelloView



class UI:
    def __init__(self,root):
        self._root = root
        self._entry = None
        self._username_entry = None

    def start (self):
        self._show_hello_view()
    """ heading_label = ttk.Label(master=self._root, text = "Login")
        
        username_label = ttk.Label(master=self._root, text="Username")
        self._username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Password")
        password_entry = ttk.Entry(master=self._root)


        button = ttk.Button(
          master=self._root,
          text="Submit",
          command=self._handle_button_click()
        )
        
        heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=2, column=0, padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button.grid(row=3,column=0,columnspan=2, padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=250)
    """
    def _handle_button_click(self):
        
        print("asdflknfdslkjlkj")
    
    def _handle_good_bye(self):
        print("Good bye")

    def _show_hello_view(self):
        self._current_view = HelloView(
            self._root,
            self._handle_good_bye
        )

        self._current_view.pack()


window = Tk()

window.title("TkInter example")

ui = UI(window)

ui.start()

window.mainloop()
