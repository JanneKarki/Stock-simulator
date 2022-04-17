from asyncio import constants
from tkinter import Button, Radiobutton, Tk, ttk, constants


class UI:
    def __init__(self,root):
        self.__root = root

    def start (self):
        label = ttk.Label(master=self.__root, text = "Hello world!")
        button = ttk.Label(master=self.__root, text="Button")
        entry = ttk.Entry(master=self.__root)
        checkbutton = ttk.Checkbutton(master=self.__root, text="Check button")
        radiobutton = ttk.Radiobutton(master=self.__root, text="Radio button")

        label.pack(side=constants.LEFT)
        button.pack(side=constants.LEFT)
        entry.pack()
        checkbutton.pack()
        radiobutton.pack()

window = Tk()

window.title("TkInter example")

ui = UI(window)

ui.start()

window.mainloop()
