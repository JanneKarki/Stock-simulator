from tkinter import Tk, ttk


class UI:
    def __init__(self,root):
        self.__root = root

    def start (self):
        label = ttk.Label(master=self.__root, text = "Hello world!")

        label.pack()

window = Tk()

window.title("TkInter example")

ui = UI(window)

ui.start()

window.mainloop()
