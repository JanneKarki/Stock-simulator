from asyncio import constants
from tkinter import Button, Radiobutton, Tk, ttk, constants


class UI:
    def __init__(self,root):
        self.__root = root

    def start (self):
        heading_label = ttk.Label(master=self.__root, text = "Login")
        
        username_label = ttk.Label(master=self.__root, text="Username")
        username_entry = ttk.Entry(master=self.__root)

        password_label = ttk.Label(master=self.__root, text="Password")
        password_entry = ttk.Entry(master=self.__root)

        button = ttk.Button(master=self.__root, text="Submit")
        
        heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        username_label.grid(row=1, column=0, padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=2, column=0, padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button.grid(row=3,column=0,columnspan=2, padx=5, pady=5)

        self.__root.grid_columnconfigure(1, weight=1, minsize=250)

window = Tk()

window.title("TkInter example")

ui = UI(window)

ui.start()

window.mainloop()
