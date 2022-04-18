from argparse import Action
from asyncio import constants
from tkinter import Button, Radiobutton, Tk, ttk, constants
from login_view import LoginView
from create_user_view import CreateUserView
from action_view import ActionView
from portfolio_view import PortfolioView

class UI:
    def __init__(self,root):
        self._root = root
        self._entry = None
        self._current_view = None

    def start (self):
        self._show_hello_view()
   
    def _handle_button_click(self):
        print("asdflknfdslkjlkj")
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_action(self):
        self._show_action_view()

    def _handle_portfolio(self):
        self._show_portfolio_view()
    
    def _handle_hello(self):
        self._show_hello_view()

    def _handle_good_bye(self):
        self._show_good_bye_view()

    def _show_hello_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_good_bye,
            self._handle_action
        )
        self._current_view.pack()

    def _show_good_bye_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._handle_hello
        )
        self._current_view.pack()

    def _show_action_view(self):
        self._hide_current_view()

        self._current_view = ActionView(
            self._root,
            self._handle_hello,
            self._handle_portfolio
        )
        self._current_view.pack()

    def _show_portfolio_view(self):
        self._hide_current_view()

        self._current_view = PortfolioView(
            self._root,
            self._handle_action
        )
        self._current_view.pack()
window = Tk()

window.title("TkInter example")

ui = UI(window)

ui.start()

window.mainloop()
